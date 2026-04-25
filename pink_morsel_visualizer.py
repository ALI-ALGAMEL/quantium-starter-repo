import pandas
from dash import Dash, html, dcc, callback, Output, Input
from plotly.express import line

DATA_PATH = "./formatted_data.csv"

data = pandas.read_csv(DATA_PATH)
data = data.sort_values(by="date")

dash_app = Dash(__name__)

header = html.H1(
    "Pink Morsel Visualizer",
    id="header",
    style={
        "textAlign": "center",
        "color": "#fff",
        "backgroundColor": "#e91e8c",
        "padding": "20px",
        "margin": "0",
        "fontFamily": "Arial, sans-serif",
        "letterSpacing": "2px",
    }
)

region_picker = dcc.RadioItems(
    id="region-filter",
    options=[
        {"label": "All", "value": "all"},
        {"label": "North", "value": "north"},
        {"label": "East", "value": "east"},
        {"label": "South", "value": "south"},
        {"label": "West", "value": "west"},
    ],
    value="all",
    inline=True,
    style={
        "textAlign": "center",
        "padding": "16px",
        "fontSize": "16px",
        "fontFamily": "Arial, sans-serif",
        "backgroundColor": "#f9f9f9",
        "gap": "20px",
    }
)

visualization = dcc.Graph(id="visualization")

dash_app.layout = html.Div(
    [
        header,
        region_picker,
        visualization,
    ],
    style={"backgroundColor": "#f0f0f0", "minHeight": "100vh"}
)


@callback(
    Output("visualization", "figure"),
    Input("region-filter", "value"),
)
def update_chart(selected_region):
    filtered = data if selected_region == "all" else data[data["region"] == selected_region]
    fig = line(
        filtered,
        x="date",
        y="sales",
        title=f"Pink Morsel Sales — {selected_region.capitalize()}",
        labels={"date": "Date", "sales": "Total Sales ($)"},
    )
    fig.update_layout(
        plot_bgcolor="#fff",
        paper_bgcolor="#f0f0f0",
        font={"family": "Arial, sans-serif"},
        title_font_size=20,
    )
    return fig


if __name__ == '__main__':
    dash_app.run(debug=True)
