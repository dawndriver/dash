import dash
from dash import html
from dash import dcc
import plotly.express as px
import pandas as pd

data = pd.read_csv("precious_metals_prices_2018_2021.csv", usecols=["DateTime", "Gold"])
fig = px.line(data, x="DateTime", y="Gold", title="Precious Metal Prices 2018-2021")

app = dash.Dash(__name__)

app.layout = html.P("Hello Dash!")

if __name__ == "__main__":
    app.run_server(debug=True)
