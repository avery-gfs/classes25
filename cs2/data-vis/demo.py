import polars as pl
import altair as alt

cities = pl.read_csv("data/cities.csv")  # Load dataframe from CSV
