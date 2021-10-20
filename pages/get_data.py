from utils.import_utils import *
from app import app
from pages import sidebar, topbar
import pandas as pd
import dash_cytoscape as cyto


def get_modal(modal_id, close_id, upload_id, heading):
    return html.Div([
        dbc.Modal([
            dbc.ModalBody([
                html.P(heading, className="modal_headings"),
                dcc.Upload("Upload Files", className="get_data_upload"),
                ]),
            dbc.ModalFooter([
                dbc.Button("Close", id=close_id, color="light", n_clicks=0, className="modal_closing"),
                dbc.Button("Upload", id=upload_id, color="success", n_clicks=0, className="modal_saving"),
            ]
            ),
        ],
            id=modal_id,
            is_open=False,
        ),
    ]
    )

default_stylesheet = [
    {
        "selector": "edge",
        "style": {
            "width": "0.3",
            "height": "0.3",
            "line-color": "black",
            # "curve-style": "bezier",
        }
    },
    {
        "selector": "node",
        "style": {
            "width": "20",
            "height": "20",
            "label": "data(label)"
        }
    },
    # Class selectors
    {
        'selector': '.read1',
        'style': {
            'width': 100,
            'height': 100,
            'background-image': ['./assets/read1.png'],
            'background-color': 'white'
        }
    },
    {
        'selector': '.read2',
        'style': {
            'width': 100,
            'height': 100,
            'background-image': ['./assets/read2.png'],
            'background-color': 'white'
        }
    },
    {
        'selector': '.read3',
        'style': {
            'width': 100,
            'height': 100,
            'background-image': ['./assets/read3.png'],
            'background-color': 'white'
        }
    },
{
        'selector': '.read4',
        'style': {
            'width': 100,
            'height': 100,
            'background-image': ['./assets/read4.png'],
            'background-color': 'white'
        }
    },
    {
        'selector': '.read5',
        'style': {
            'width': 100,
            'height': 100,
            'background-image': ['./assets/read5.png'],
            'background-color': 'white'
        }
    },
    {
        'selector': '.read6',
        'style': {
            'width': 100,
            'height': 100,
            'background-image': ['./assets/read6.png'],
            'background-color': 'white'
        }
    },
    {
        'selector': '.read7',
        'style': {
            'width': 100,
            'height': 100,
            'background-image': ['./assets/read7.png'],
            'background-color': 'white'
        }
    },
    {
        'selector': '.read8',
        'style': {
            'width': 100,
            'height': 100,
            'background-image': ['./assets/read8.png'],
            'background-color': 'white'
        }
    },
    {
        'selector': '.read9',
        'style': {
            'width': 100,
            'height': 100,
            'background-image': ['./assets/read9.png'],
            'background-color': 'white'
        }
    },
    {
        'selector': '.read10',
        'style': {
            'width': 100,
            'height': 100,
            'background-image': ['./assets/read10.png'],
            'background-color': 'white'
        }
    },
    {
        'selector': '.square',
        'style': {
            'shape': 'square',
        }
    },
]


def create_layout():
    community = pd.DataFrame({'nodes': ['node1', 'node2', 'node3', 'node4', 'node5', 'node6', 'node7', 'node8', 'node9',
                                        'node10', 'node11', 'node12'],
                              'image_class': ['read1', 'read2', 'read3', 'read4', 'square', 'read5', 'read6', 'read7',
                                              'read8', 'square', 'read9', 'read10'],
                              'x-position': [0, 0, 0, 0, 200, 400, 400, 400, 600, 800, 1000, 1000],
                              'y-position': [0, 150, 300, 450, 225, 100, 250, 400, 225, 225, 150, 300],
                              'labels': ['reads_fastqgzs', 'reads2_fastqgzs', 'rg_info_csv', 'genomeindex_targz',
                                         'Read Mapper', 'sorted_bam', 'sorted_bai', 'duplication_metrics', 'sorted_bam',
                                         'GATK-Lite Pipeline', 'variants_vcfgz', 'variants_tbi']
                              })
    edges = pd.DataFrame({'source': ['node1', 'node2', 'node3', 'node4', 'node5', 'node5', 'node5', 'node6', 'node9',
                                     'node10', 'node10'],
                          'target': ['node5', 'node5', 'node5', 'node5', 'node6', 'node7', 'node8', 'node9', 'node10',
                                     'node11', 'node12']
                          })

    elements = []
    for i in range(len(community.axes[0])):
        elements.append({'data': {'id': community['nodes'][i], 'label': community['labels'][i]},
                         'classes': community['image_class'][i],
                         'position': {'x': community['x-position'][i], 'y': community['y-position'][i]}
                         # 'classes': get_gender(community.iloc[i, 0]) + ' ' + str(get_country(community.iloc[i, 0])),
                         # 'size': 10
                         })

    source = edges['source'].tolist()
    target = edges['target'].tolist()
    community_list = community['nodes'].tolist()
    counter = 0
    for i in range(len(source)):
        if source[i] in community_list and target[i] in community_list:
            elements.append({'data': {'source': source[i], 'target': target[i]},
                             # 'position': {'x': community['x-position'][i], 'y': community['y-position'][i]}
                             })
            counter += 1
    return html.Div([
        html.Div([
            sidebar.create_layout(),
        ], className="screen_division_left"),
        html.Div([
            topbar.create_layout(),
            html.Div([
                html.P("Analysis", className="get_data_title"),
                html.Div([
                    get_modal("modal_1", 'close_1', 'upload_1', 'read fastqgzs'),
                    cyto.Cytoscape(
                        id='cytoscape',
                        style={'width': '100%', 'height': '80vh'},
                        responsive=True,
                        minZoom=0.2,
                        maxZoom=2,
                        elements=elements,
                        layout={'name': 'preset'},
                        stylesheet=default_stylesheet
                    )])
            ], className="get_data_sub_main")
        ], className="screen_division_right")
    ], className="get_data_main")



# import dash  # pip install dash
# import dash_cytoscape as cyto  # pip install dash-cytoscape==0.2.0 or higher
# import dash_html_components as html
# import dash_core_components as dcc
# from dash.dependencies import Output, Input
# import pandas as pd  # pip install pandas
# import plotly.express as px
#
# external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
# app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
#
# df = pd.read_csv("https://raw.githubusercontent.com/Coding-with-Adam/Dash-by-Plotly/master/Cytoscape/org-data.csv")
#
# app.layout = html.Div([
#     html.Div([
#         cyto.Cytoscape(
#             id='org-chart',
#             layout={'name': 'preset'},
#             style={'width': '100%', 'height': '500px'},
#             elements=[
#                 # Nodes elements
#                 {'data': {'id': 'ed', 'label': 'Executive Director (Harriet)'},
#                  'position': {'x': 250, 'y': 150},
#                  'locked': True
#                 },
#
#                 {'data': {'id': 'vp1', 'label': 'Vice President (Sarah)'},
#                  'position': {'x': 120, 'y': 150},
#                  'grabbable': False
#                 },
#                 #
#                 # {'data': {'id': 'vp2', 'label': 'Vice President (Charlotte)'},
#                 #  'position': {'x': 300, 'y': 150},
#                 # 'selectable': False
#                 # },
#                 #
#                 # {'data': {'id': 'po1', 'label': 'Program Officer (Sojourner)'},
#                 #  'position': {'x': -100, 'y': 250},
#                 #  'selected': True
#                 # },
#                 #
#                 # {'data': {'id': 'po2', 'label': 'Program Officer (Elizabeth)'},
#                 #  'position': {'x': 150, 'y': 250}
#                 # },
#                 #
#                 # {'data': {'id': 'pa', 'label': 'Program Associate (Ellen)'},
#                 #  'position': {'x': 300, 'y': 350}
#                 # },
#                 #
#                 # # Edge elements
#                 # {'data': {'source': 'ed', 'target': 'vp1', 'label': 'ED to VP1'}},
#                 # {'data': {'source': 'ed', 'target': 'vp2'}},
#                 # {'data': {'source': 'vp1', 'target': 'po1'}},
#                 # {'data': {'source': 'vp1', 'target': 'po2'}},
#                 # {'data': {'source': 'vp2', 'target': 'pa'}},
#             ]
#         )
#     ], className='six columns'),
#
#     html.Div([
#         dcc.Graph(id='my-graph')
#     ], className='six columns'),
#
# ], className='row')
#
#
# @app.callback(
#     Output('my-graph','figure'),
#     Input('org-chart','tapNodeData'),
# )
# def update_nodes(data):
#     if data is None:
#         dff = df.copy()
#         dff.loc[dff.name == 'Program Officer (Sojourner)', 'color'] = "yellow"
#         fig = px.bar(dff, x='name', y='slaves_freed')
#         fig.update_traces(marker={'color': dff['color']})
#         return fig
#     else:
#         print(data)
#         dff = df.copy()
#         dff.loc[dff.name == data['label'], 'color'] = "yellow"
#         print(dff)
#         fig = px.bar(dff, x='name', y='slaves_freed')
#         fig.update_traces(marker={'color': dff['color']})
#         return fig
#
#
# if __name__ == '__main__':
#     app.run_server(debug=True)




@app.callback(
    Output("modal_1", "is_open"),
    [Input("node1", "n_clicks"), Input("close_1", "n_clicks"), Input("upload_1", "n_clicks")],
    [State("modal_1", "is_open")],
)
def toggle_modal(n1, n2, n3, is_open):
    if n1 or n2 or n3:
        return not is_open
    return is_open

