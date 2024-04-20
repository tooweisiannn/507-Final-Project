import dash
from dash import dcc
from dash import html
import plotly.express as px
import pandas as pd

app = dash.Dash(__name__)
server = app.server

# see https://plotly.com/python/px-arguments/ for more options
df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})

fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")

app.css.append_css({
    "external_url": "https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap"
})

df2 = pd.read_csv('https://gist.githubusercontent.com/chriddyp/5d1ea79569ed194d432e56108a04d188/raw/a9f9e8076b837d541398e999dcbac2b2826a81f8/gdp-life-exp-2007.csv')

fig2 = px.scatter(df2, x="gdp per capita", y="life expectancy",
                 size="population", color="continent", hover_name="country",
                 log_x=True, size_max=60)

fig.update_layout(
    plot_bgcolor='rgba(0,0,0,0)', 
    paper_bgcolor='rgba(0,0,0,0)',
    margin={"r":0,"t":0,"l":0,"b":0}
)
fig2.update_layout(
    plot_bgcolor='rgba(0,0,0,0)',
    paper_bgcolor='rgba(0,0,0,0)',
    margin={"r":0,"t":0,"l":0,"b":0}
)

# Create a Dash app
app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1('Hello Dash', style={'textAlign': 'center', 'color': '#007BFF'}),

    html.Div('''
        Dash: A web application framework for your data.
    ''', style={'textAlign': 'center', 'margin': '10px', 'color': '#007BFF'}),

    dcc.Graph(
        id='example-graph',
        figure=fig,
        style={'borderRadius': '15px', 'boxShadow': '2px 2px 2px lightgrey'}
    ),

    html.Div('''
        Dash: Another example for chart
    ''', style={'textAlign': 'center', 'margin': '10px', 'color': '#007BFF'}),

    dcc.Graph(
        id='example-graph2',
        figure=fig2,
        style={'borderRadius': '15px', 'boxShadow': '2px 2px 2px lightgrey'}
    )
], style={'backgroundColor': '#FFFFFF', 'padding': '20px', 'borderRadius': '15px'})

if __name__ == '__main__':
    app.run_server(debug=True, port=8080)
