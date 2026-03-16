import polars as pl
import altair as alt

cities = pl.read_csv("data/cities.csv")  # Load dataframe from CSV


topCities = cities.head(20)
chart = (
    alt.Chart(topCities).mark_bar().encode(alt.X("pop2024"), alt.Y("city", sort="-x"))
)
chart.save("pop-bars.png", scale_factor=1.5)


cityCounts = cities.group_by("state").count()

chart = (
    alt.Chart(cityCounts).mark_bar().encode(alt.X("state", sort="-y"), alt.Y("count"))
)
chart.save("city-counts.png", scale_factor=1.5)


## Scatter Plot

top25 = cities.head(25)

chart = (
    alt.Chart(top25)
    .mark_circle(size=40)
    .encode(
        alt.X("area"),
        alt.Y("pop2024"),
        alt.Color("state"),
    )
)

chart.save("pop-area-scatter.png", scale_factor=1.5)
