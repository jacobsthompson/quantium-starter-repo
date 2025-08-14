# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.


from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import pandas as pd

df = pd.read_csv('sales_data.csv')
df.head()

app = Dash(__name__)

regions = df['Region'].unique()

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

color_map = {
    'north': '#D9415D',
    'south': '#856DA6',
    'east': '#4EA67D',
    'west': '#F2AC57',
}

app.layout = html.Div(style={
    'backgroundColor': colors['background'],
    'fontFamily': 'Arial, sans-serif',
    'textAlign': 'center',
    'color': colors['text']
},children=[
    html.H1(id='header', children='Pink Morsel Sales'),

    html.Div(children='''
        A Line Chart Visualization of Pink Morsel Sales Over Time in Various Regions.
    '''),

    dcc.RadioItems(
        id='radio',
        options=[{'label': 'All', 'value': 'All'}] +
                [{'label': r, 'value': r} for r in regions],
        value='All',
        inline=True,
        style={'margin': '20px'}
    ),

    dcc.Graph(
        id='graph',
    )
])

@app.callback(Output('graph', 'figure'),
              Input('radio', 'value')
              )

def update_chart(selected_region):
    if selected_region == 'All':
        filtered_df = df
    else:
        filtered_df = df[df['Region'] == selected_region]

    fig = px.line(
        filtered_df,
        x="Date",
        y="Sales",
        color="Region",
        color_discrete_map=color_map,
        template='seaborn',
        )

    fig.update_traces(line=dict(width=1))
    fig.update_layout(
        plot_bgcolor=colors['background'],
        paper_bgcolor=colors['background'],
        font_color=colors['text']
    )
    return fig

if __name__ == '__main__':
    app.run(debug=True)
