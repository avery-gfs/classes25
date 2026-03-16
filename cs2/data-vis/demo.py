import polars as pl

cities = pl.read_csv("data/cities.csv")  # Load dataframe from CSV

print((cities.group_by("state").count().sort("count", descending=True)))
