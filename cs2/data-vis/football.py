import polars as pl

# Increase table display size

pl.Config(tbl_cols=10)

# Read CSV data as a dataframe

games = pl.read_csv("data/games.csv")
print(games)

# Get the win / loss and scoring results for the home and away teams in each game

homeResults = games.select(
    pl.col("home_team").alias("team"),
    (pl.col("home_score") > pl.col("away_score")).alias("isWin"),
    pl.col("home_score").alias("scored"),
    pl.col("away_score").alias("allowed"),
)

awayResults = games.select(
    pl.col("away_team").alias("team"),
    (pl.col("away_score") > pl.col("home_score")).alias("isWin"),
    pl.col("away_score").alias("scored"),
    pl.col("home_score").alias("allowed"),
)

print(homeResults)
print(awayResults)

# Combine the home and away win loss results

combined = pl.concat([homeResults, awayResults])

print(combined)

# Group the stats from each team game into a single row

summary = combined.group_by("team").agg(
    pl.len().alias("numGames"),
    pl.sum("isWin").alias("wins"),
    (~pl.col("isWin")).sum().alias("losses"),
    pl.sum("scored").alias("scored"),
    pl.sum("allowed").alias("allowed"),
)

print(summary)

# Calculate the per-game stats for each team
# Sort the team data by win percentage, highest to lowest

finalStats = summary.with_columns(
    (pl.col("wins") / pl.col("numGames")).round(3).alias("winPct"),
    (pl.col("scored") / pl.col("numGames")).round(1).alias("scoredPerGame"),
    (pl.col("allowed") / pl.col("numGames")).round(1).alias("allowedPerGame"),
).sort("winPct", descending=True)

# Increase table display size

pl.Config(tbl_rows=32)

print(finalStats)
