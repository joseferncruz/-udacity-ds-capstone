from dash import Dash, dcc, html, Input, Output, Dash

from fig_preparation import generate_figures

import plotly.express as px

import pandas as pd

# Create the app
webapp = Dash(
    __name__, 
    meta_tags=[
        {'name': 'viewport'},
        {'content': 'width=device-width, initial-scale=1.0'}
    ]
)

H2_STYLE = {
    'text-align': 'center', 
    'font-weight': 'bold'
}
    
df = pd.read_csv('../data/processed/merged_datasets.csv', index_col=0, parse_dates=['ticketcreationdate'])

figures = generate_figures(df)

## APP LAYOUT
webapp.layout = html.Div(children=[
    html.H1(children='Customer Satisfaction KPIs', style=H2_STYLE),


    # Pie Chart
    html.Div([

        html.Div([html.H2(children='Customer Satisfation')],
                  className="six columns", 
                  style=H2_STYLE),
        html.Div([html.H2(children='Customer Satisfaction May-August')], 
                  className="six columns",
                  style=H2_STYLE)

    ], className='row'),



    html.Div([
        ## plot left
        html.Div([dcc.Graph(id='csat-bar', figure=figures.get('csat_pie'))],
                className='six columns'),

        # plot right
        html.Div([dcc.Graph(id='month-barh', figure=figures.get('monthly_bar'))],
                className='six columns'),
    ], className="row"),



    # Average Reply time
    html.Div([html.H2(children='Agent Reply Time'),], style=H2_STYLE),

    html.Div([
        ## plot left
        html.Div([dcc.Graph(id='replytime-bar', figure=figures.get('replytime_bar'))],
                className='six columns'),

        # plot right
        html.Div([dcc.Graph(id='replytime-hist', figure=figures.get('replytime_hist'))],
                className='six columns'),
    ], className="row"), 

    # Full resolution Time
    html.Div([html.H2(children='Full Resolution Time'),], style=H2_STYLE),
    html.Div([
        ## plot left
        html.Div([dcc.Graph(id='fullresolutiontime-bar', figure=figures.get('fullresolutiontime_bar'))],
                className='six columns'),

        # plot right
        html.Div([dcc.Graph(id='rullresolutiontime-hist', figure=figures.get('fullresolutiontime_hist'))],
                className='six columns'),
    ], className="row"),

    # First Time Resolution and Contacts per Case > CPC
    html.Div([

        html.Div([html.H2(children='First contact Resolution')],
                  className="six columns", 
                  style=H2_STYLE),
        html.Div([html.H2(children='Contacts Per Case')], 
                  className="six columns",
                  style=H2_STYLE)

    ], className='row'),



    html.Div([
        ## plot left
        html.Div([dcc.Graph(id='firstcontactresolution-bar', figure=figures.get('firstcontactresolution_bar'))],
                className='six columns'),

        # plot right
        html.Div([dcc.Graph(id='cpc-hist', figure=figures.get('cpc_hist'))],
                className='six columns'),
    ], className="row")
    

])



if __name__ == '__main__':

    webapp.run_server(debug=False)