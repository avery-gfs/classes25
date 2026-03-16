import polars as pl
import altair as alt

cities = pl.read_csv("data/cities.csv")  # Load dataframe from CSV

pctChange = (
    cities.with_columns(
        (pl.col("pop2024") / pl.col("pop2020") * 100 - 100).alias("pctChange")
    )
    .sort("pctChange", descending=True)
    .head(10)
)

chart = (
    alt.Chart(pctChange).mark_bar().encode(alt.X("pctChange"), alt.Y("city", sort="-x"))
)
chart.save("pct-change.png", scale_factor=1.5)
