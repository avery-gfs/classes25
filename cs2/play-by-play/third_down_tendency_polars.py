#!/usr/bin/env python3
"""Summarize 3rd-down run/pass tendencies by yards-to-gain bucket using Polars.

Usage:
  python3 third_down_tendency_polars.py input_filtered.csv output_summary.csv
"""

import argparse
from pathlib import Path

import polars as pl


def build_summary(input_csv: Path) -> pl.DataFrame:
    df = pl.read_csv(input_csv)

    prepared = df.with_columns(
        [
            pl.col("down").cast(pl.Int64, strict=False).alias("down_i"),
            pl.col("distance").cast(pl.Int64, strict=False).alias("distance_i"),
            pl.col("yards_gained")
            .cast(pl.Float64, strict=False)
            .alias("yards_gained_f"),
            pl.col("play_type").cast(pl.Utf8).str.to_lowercase().alias("play_type_l"),
        ]
    ).filter(
        (pl.col("down_i") == 3)
        & (pl.col("distance_i").is_not_null())
        & (pl.col("play_type_l").is_in(["run", "pass"]))
    )

    bucketed = prepared.with_columns(
        [
            pl.when(pl.col("distance_i") <= 1)
            .then(pl.lit("1"))
            .when(pl.col("distance_i") == 2)
            .then(pl.lit("2"))
            .when(pl.col("distance_i") == 3)
            .then(pl.lit("3"))
            .when(pl.col("distance_i") == 4)
            .then(pl.lit("4"))
            .when(pl.col("distance_i") == 5)
            .then(pl.lit("5"))
            .when(pl.col("distance_i") == 6)
            .then(pl.lit("6"))
            .when(pl.col("distance_i") == 7)
            .then(pl.lit("7"))
            .when(pl.col("distance_i") == 8)
            .then(pl.lit("8"))
            .when(pl.col("distance_i") == 9)
            .then(pl.lit("9"))
            .when(pl.col("distance_i") == 10)
            .then(pl.lit("10"))
            .otherwise(pl.lit("11+"))
            .alias("ytg_bucket"),
            pl.when(pl.col("distance_i") <= 1)
            .then(pl.lit(1))
            .when(pl.col("distance_i") == 2)
            .then(pl.lit(2))
            .when(pl.col("distance_i") == 3)
            .then(pl.lit(3))
            .when(pl.col("distance_i") == 4)
            .then(pl.lit(4))
            .when(pl.col("distance_i") == 5)
            .then(pl.lit(5))
            .when(pl.col("distance_i") == 6)
            .then(pl.lit(6))
            .when(pl.col("distance_i") == 7)
            .then(pl.lit(7))
            .when(pl.col("distance_i") == 8)
            .then(pl.lit(8))
            .when(pl.col("distance_i") == 9)
            .then(pl.lit(9))
            .when(pl.col("distance_i") == 10)
            .then(pl.lit(10))
            .otherwise(pl.lit(11))
            .alias("bucket_order"),
        ]
    )

    per_type = bucketed.group_by(["bucket_order", "ytg_bucket", "play_type_l"]).agg(
        [
            pl.len().alias("play_count"),
            pl.col("yards_gained_f").mean().alias("avg_yards_gained"),
        ]
    )

    count_pivot = (
        per_type.pivot(
            values="play_count",
            index=["bucket_order", "ytg_bucket"],
            on="play_type_l",
            aggregate_function="first",
        )
        .rename({"run": "run_count", "pass": "pass_count"})
        .with_columns(
            [
                pl.col("run_count").fill_null(0).cast(pl.Int64),
                pl.col("pass_count").fill_null(0).cast(pl.Int64),
            ]
        )
    )

    avg_pivot = per_type.pivot(
        values="avg_yards_gained",
        index=["bucket_order", "ytg_bucket"],
        on="play_type_l",
        aggregate_function="first",
    ).rename({"run": "run_avg_yards_gained", "pass": "pass_avg_yards_gained"})

    summary = (
        count_pivot.join(avg_pivot, on=["bucket_order", "ytg_bucket"], how="left")
        .with_columns((pl.col("run_count") + pl.col("pass_count")).alias("total_plays"))
        .with_columns(
            [
                pl.when(pl.col("total_plays") > 0)
                .then((pl.col("run_count") * 100.0) / pl.col("total_plays"))
                .otherwise(None)
                .alias("run_pct"),
                pl.when(pl.col("total_plays") > 0)
                .then((pl.col("pass_count") * 100.0) / pl.col("total_plays"))
                .otherwise(None)
                .alias("pass_pct"),
            ]
        )
        .sort("bucket_order")
        .select(
            [
                "ytg_bucket",
                "total_plays",
                "run_count",
                "pass_count",
                "run_pct",
                "pass_pct",
                "run_avg_yards_gained",
                "pass_avg_yards_gained",
            ]
        )
    )

    return summary


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Summarize 3rd-down run/pass tendencies by yards-to-gain bucket."
    )
    parser.add_argument(
        "input_csv",
        nargs="?",
        default="play_by_play_2025_regular_filtered.csv",
        type=Path,
        help="Path to transformed filtered PBP CSV.",
    )
    parser.add_argument(
        "output_csv",
        nargs="?",
        default="third_down_tendency_summary.csv",
        type=Path,
        help="Path for summary CSV output.",
    )
    args = parser.parse_args()

    summary = build_summary(args.input_csv)
    summary.write_csv(args.output_csv)
    print(f"Wrote {summary.height} rows to {args.output_csv}")


if __name__ == "__main__":
    main()
