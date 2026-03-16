import polars as pl
import altair as alt

cities = pl.read_csv("data/cities.csv")  # Load dataframe from CSV

topCities = cities.head(20)

chart = (
    alt.Chart(topCities)
    .mark_bar()
    .encode(
        alt.X("pop2024"),
        alt.Y("city", sort="-x"),
    )
)

chart.save("pop-bars.png", scale_factor=1.5)


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


## Chart: Population Growth


pctChange = (
    cities.with_columns(
        (pl.col("pop2024") / pl.col("pop2020") * 100 - 100).alias("pctChange")
    )
    .sort("pctChange", descending=True)
    .head(10)
)

chart = (
    alt.Chart(pctChange)
    .mark_bar()
    .encode(
        alt.X("pctChange"),
        alt.Y("city", sort="-x"),
    )
)

chart.save("pct-change.png", scale_factor=1.5)


## Scatter Plot

top10 = cities.head(10)

chart = (
    alt.Chart(top10)
    .mark_circle(size=40)
    .encode(
        alt.X("area"),
        alt.Y("pop2024"),
        alt.Color("city"),
    )
)

chart.save("pop-scatter.png", scale_factor=1.5)
