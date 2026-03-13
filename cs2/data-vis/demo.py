import polars as pl

cities = pl.read_csv("data/cities.csv")  # Load dataframe from CSV

withPopChange = cities.with_columns(
    (pl.col("pop2024") - pl.col("pop2020")).alias("change")
)


print(
    cities.group_by("state")
    .agg(
        pl.sum("pop2024"),
        pl.sum("area"),
    )
    .sort("pop2024", descending=True)
)
