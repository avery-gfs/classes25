import polars as pl
import altair as alt

cities = pl.read_csv("cities.csv")  # Load dataframe from CSV

cityCounts = cities.group_by("state").count()

chart = (
    alt.Chart(cityCounts)
    .mark_bar()
    .encode(
        alt.X("state", sort="-y"),
        alt.Y("count"),
    )
)

chart.save("city-counts.png", scale_factor=1.5)
