#!/usr/bin/env python3
"""Transform NFL play-by-play CSV into a classroom-friendly play dataset.

Usage:
  python3 transform_pbp.py input.csv output.csv
"""

import argparse
import csv
from pathlib import Path


OUTPUT_FIELDS = [
    "home_team",
    "away_team",
    "possession",
    "field_position",
    "down",
    "distance",
    "quarter",
    "minutes",
    "seconds",
    "home_score",
    "away_score",
    "play_type",
    "yards_gained",
    "points_scored",
    "score_type",
    "penalty_type",
    "penalty_yards",
    "penalized_team",
    "td_attempt_type",
    "td_attempt_result",
    "outcome",
]


def to_int(value):
    try:
        if value is None or value == "":
            return 0
        return int(float(value))
    except Exception:
        return 0


def parse_field_position(value):
    try:
        if value is None or str(value).strip() == "":
            return ""
        number = int(round(float(value)))
        if number < 0:
            number = 0
        if number > 100:
            number = 100
        return number
    except Exception:
        return ""


def extract_time_parts(time_raw):
    time_raw = (time_raw or "").strip()
    if ":" in time_raw:
        minutes, seconds = time_raw.split(":", 1)
        return minutes, seconds
    return "", ""


def build_outcome(row):
    if row.get("touchdown") == "1":
        return "td"
    if (
        row.get("first_down") == "1"
        or row.get("first_down_rush") == "1"
        or row.get("first_down_pass") == "1"
        or row.get("first_down_penalty") == "1"
    ):
        return "1st_down"
    if row.get("field_goal_attempt") == "1" and row.get("field_goal_result") == "made":
        return "fg_made"
    if row.get("field_goal_attempt") == "1" and row.get("field_goal_result") in {
        "missed",
        "blocked",
    }:
        return "fg_no_good"
    if row.get("interception") == "1":
        return "turnover_interception"
    if row.get("fumble_lost") == "1":
        return "turnover_fumble"
    if row.get("fourth_down_failed") == "1":
        return "turnover_on_downs"
    if row.get("safety") == "1":
        return "safety"
    if row.get("punt_attempt") == "1":
        return "punt"
    if row.get("penalty") == "1":
        return "penalty"
    return ""


def build_score_type(outcome, points_scored):
    if outcome == "td":
        return "td"
    if outcome == "fg_made":
        return "fg"
    if outcome == "safety":
        return "safety"
    if points_scored > 0:
        return "other_score"
    return ""


def build_penalized_team(row):
    penalty_team = (row.get("penalty_team") or "").strip()
    if penalty_team and penalty_team == row.get("home_team"):
        return "home"
    if penalty_team and penalty_team == row.get("away_team"):
        return "away"
    return ""


def transform_rows(rows):
    out_rows = []
    current_game = None
    pending_td_index = None
    pending_td_drive = None

    for row in rows:
        game_id = row.get("game_id")
        if game_id != current_game:
            current_game = game_id
            pending_td_index = None
            pending_td_drive = None

        # Attach PAT/2PT result to previous TD row.
        if pending_td_index is not None:
            if row.get("extra_point_attempt") == "1":
                result = row.get("extra_point_result", "")
                out_rows[pending_td_index]["td_attempt_type"] = "xp"
                out_rows[pending_td_index]["td_attempt_result"] = result
                if result == "good":
                    out_rows[pending_td_index]["points_scored"] += 1
                    out_rows[pending_td_index]["score_type"] = "td_xp_good"
                else:
                    out_rows[pending_td_index]["score_type"] = "td_try_failed"
                pending_td_index = None
                pending_td_drive = None
            elif row.get("two_point_attempt") == "1":
                result = row.get("two_point_conv_result", "")
                out_rows[pending_td_index]["td_attempt_type"] = "2pt"
                out_rows[pending_td_index]["td_attempt_result"] = result
                if result == "success":
                    out_rows[pending_td_index]["points_scored"] += 2
                    out_rows[pending_td_index]["score_type"] = "td_2pt_good"
                else:
                    out_rows[pending_td_index]["score_type"] = "td_try_failed"
                pending_td_index = None
                pending_td_drive = None
            elif row.get("kickoff_attempt") == "1" or (
                pending_td_drive
                and row.get("drive")
                and row.get("drive") != pending_td_drive
            ):
                pending_td_index = None
                pending_td_drive = None

        if row.get("season_type") != "REG":
            continue
        if not row.get("posteam"):
            continue

        # Exclude procedural plays.
        if row.get("kickoff_attempt") == "1":
            continue
        if row.get("extra_point_attempt") == "1":
            continue
        if row.get("two_point_attempt") == "1":
            continue

        play_type = row.get("play_type", "")
        penalty_yards = to_int(row.get("penalty_yards"))

        # Keep no_play only when it reflects an enforced field-position change.
        if play_type == "no_play" and penalty_yards == 0:
            continue
        # Skip administrative rows such as timeout/end game with blank play_type.
        if play_type == "":
            continue

        home_score = to_int(row.get("total_home_score"))
        away_score = to_int(row.get("total_away_score"))
        minutes, seconds = extract_time_parts(row.get("time"))

        points_scored = (
            to_int(row.get("posteam_score_post"))
            + to_int(row.get("defteam_score_post"))
            - to_int(row.get("posteam_score"))
            - to_int(row.get("defteam_score"))
        )

        outcome = build_outcome(row)
        score_type = build_score_type(outcome, points_scored)

        out_row = {
            "home_team": row.get("home_team", ""),
            "away_team": row.get("away_team", ""),
            "possession": row.get("posteam", ""),
            "field_position": parse_field_position(row.get("yardline_100")),
            "down": row.get("down", ""),
            "distance": row.get("ydstogo", ""),
            "quarter": row.get("qtr", ""),
            "minutes": minutes,
            "seconds": seconds,
            "home_score": home_score,
            "away_score": away_score,
            "play_type": play_type,
            "yards_gained": row.get("yards_gained", ""),
            "points_scored": points_scored,
            "score_type": score_type,
            "penalty_type": row.get("penalty_type", ""),
            "penalty_yards": penalty_yards,
            "penalized_team": build_penalized_team(row),
            "td_attempt_type": "",
            "td_attempt_result": "",
            "outcome": outcome,
        }
        out_rows.append(out_row)

        if row.get("touchdown") == "1":
            pending_td_index = len(out_rows) - 1
            pending_td_drive = row.get("drive")

    return out_rows


def run(input_path, output_path):
    with input_path.open(newline="", encoding="utf-8") as f_in:
        rows = list(csv.DictReader(f_in))

    out_rows = transform_rows(rows)

    with output_path.open("w", newline="", encoding="utf-8") as f_out:
        writer = csv.DictWriter(f_out, fieldnames=OUTPUT_FIELDS)
        writer.writeheader()
        writer.writerows(out_rows)

    print(f"Wrote {len(out_rows)} rows to {output_path}")


def main():
    parser = argparse.ArgumentParser(
        description="Transform NFL PBP CSV to filtered teaching dataset."
    )
    parser.add_argument("input_csv", type=Path, help="Path to raw PBP CSV")
    parser.add_argument("output_csv", type=Path, help="Path for transformed output CSV")
    args = parser.parse_args()

    run(args.input_csv, args.output_csv)


if __name__ == "__main__":
    main()
