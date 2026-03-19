import polars as pl
import altair as alt

cities = pl.read_csv("data/cities.csv")  # Load dataframe from CSV

print(
    cities.select(
        pl.col("city"),
        pl.col("state"),
        (pl.col("pop2024") - pl.col("pop2020")).alias("popChange"),
    )
    .sort("popChange", descending=True)
    .head(10)
    .with_row_index(name="rank", offset=1)
)
