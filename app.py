from dash import Dash, dcc, html, Input, Output, callback, State
import dash_bootstrap_components as dbc
import pandas as pd
from dash.exceptions import PreventUpdate

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.title = 'Voice Adaptation'

app.layout = dbc.Container([
    dbc.Row(
        dbc.Col(
            dbc.Card([
                dbc.CardHeader("Voice Adaptation", style={'backgroundColor': '#0049B4', 'color': 'white'}),
                dbc.CardBody([
                    html.Label([
                    "Choose a .wav file",
                    ], className="mb-2"),
                    dcc.Upload(
                        id='upload-data',
                        children=html.Div(['Drag and Drop or Select a File'], className="upload-text"),
                        style={
                            'width': '100%', 'height': '60px', 'lineHeight': '60px',
                            'borderWidth': '1px', 'borderStyle': 'dashed',
                            'borderRadius': '5px', 'textAlign': 'center', 'margin': '10px'
                        },
                        multiple=False
                    ),
                    dcc.Store(id="file-name-display"),
                    html.Div(id='alert-container'),
                    dcc.Loading(
                    id="loading-dropdowns",
                    type="default",
                    children=[
                    html.Label("Type or select a voice adaptation", className="mb-2 mt-4"),
                    dcc.Dropdown(
                        id='site-name-dropdown',
                        options=['helium gas voice', 'whispering voice','robotic voice','male to female voice'], 
                        placeholder="Type or select an option...",
                        searchable=True,
                        multi=False
                    ),
                    
                    ]),
                    html.Div([
                        dbc.Button("Download", id="download-button", className="mt-4", color="primary", n_clicks=0)
                    ], className="d-flex justify-content-center"),
                    dcc.Loading(
                        id="loading-download",
                        type="default",
                        children=[
                        dcc.Download(id='download-zip'),
                        html.Div(id='alert-for-download')], style={'marginTop': '20px'})
                ]),
            ]),
            width=12, lg=6
        ),
        justify="center"
    )
], fluid=True)

if __name__ == '__main__':
    app.run_server(debug=False, host='0.0.0.0', port=8088)