# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.


from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import pandas as pd

df = pd.read_csv('sales_data.csv')
df.head()

app = Dash()

regions = df['Region'].unique()

color_map = {
    'north': '#1f77b4',
    'south': '#ff7f0e',
    'east': '#2ca02c',
    'west': '#d62728',
}

app.layout = html.Div(children=[
    html.H1(children='Pink Morsel Sales'),

    html.Div(children='''
        A Line Chart Visualization of Pink Morsel Sales Over Time in Various Regions.
    '''),

    dcc.Checklist(
        id='region-selection',
        options=[{'label': r, 'value': r} for r in regions],
        value=list(regions),
        inline=True
    ),

    dcc.Graph(
        id='example-graph',
    )
])

@app.callback(Output('example-graph', 'figure'),
              Input('region-selection', 'value')
              )

def update_chart(selected_region):
    filtered_df = df[df['Region'].isin(selected_region)]
    fig = px.line(filtered_df, x="Date", y="Sales", color="Region", color_discrete_map=color_map)
    return fig

if __name__ == '__main__':
    app.run(debug=True)
