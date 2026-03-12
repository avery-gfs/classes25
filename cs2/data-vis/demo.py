import polars as pl

cities = pl.read_csv("cities.csv")  # Load dataframe from CSV

withPopDensity = cities.with_columns((pl.col("pop2024") / pl.col("area")))

print(withPopDensity)
