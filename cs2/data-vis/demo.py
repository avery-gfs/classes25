import polars as pl
import altair as alt

cities = pl.read_csv("cities.csv")  # Load dataframe from CSV

cityCounts = (
    cities.group_by("state")
    .agg(pl.len().alias("cities"))
    .sort("cities", descending=True)
)

print(cityCounts)

chart = (
    alt.Chart(cityCounts).mark_bar().encode(alt.X("state", sort="-y"), alt.Y("cities"))
)
chart.save("city-counts.png", scale_factor=2)
