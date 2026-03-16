import polars as pl

cities = pl.read_csv("data/cities.csv")  # Load dataframe from CSV

print(cities.sort("pop2020").with_row_index(name="rank", offset=1))
