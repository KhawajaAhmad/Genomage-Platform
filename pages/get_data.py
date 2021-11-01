from utils.import_utils import *
from app import app
from pages import sidebar, topbar
import pandas as pd
import dash_cytoscape as cyto


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
            'background-image': ['./assets/read9.png'],
            'background-color': 'white'
        }
    },
    {
        'selector': '.read8',
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
    {
        'selector': '.read_bam1',
        'style': {
            'width': 100,
            'height': 100,
            'background-image': ['./assets/read1.png'],
            'background-color': 'white'
        }
    },
    {
        'selector': '.read_bam2',
        'style': {
            'width': 100,
            'height': 100,
            'background-image': ['./assets/read2.png'],
            'background-color': 'white'
        }
    },
    {
        'selector': '.read_bam3',
        'style': {
            'width': 100,
            'height': 100,
            'background-image': ['./assets/read3.png'],
            'background-color': 'white'
        }
    },
    {
        'selector': '.read_bam4',
        'style': {
            'width': 100,
            'height': 100,
            'background-image': ['./assets/read5.png'],
            'background-color': 'white'
        }
    },
    {
        'selector': '.read_bam5',
        'style': {
            'width': 100,
            'height': 100,
            'background-image': ['./assets/read9.png'],
            'background-color': 'white'
        }
    },
    {
        'selector': '.square_bam',
        'style': {
            'shape': 'square',
        }
    }
]


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
        )]
    )


def get_elements(data_format, mapping):
    if data_format != 'bam':
        community = pd.DataFrame(
            {'nodes': ['node1', 'node2', 'node3', 'node4', 'node5', 'node6', 'node7',
                       'node8', 'node9'],
             'image_class': ['read1', 'read2', 'read3', 'read4', 'square', 'read5',
                             'read6', 'square', 'read7'],
             'x-position': [0, 0, 0, 0, 200, 400, 400, 600, 800],
             'y-position': [0, 150, 300, 450, 225, 150, 300, 225, 225],
             'labels': ['reads1_fastq', 'reads2_fastq', 'rg_info_csv', 'reference_genome',
                        mapping.upper(), 'sorted_bam', 'sorted_bai',
                        'GATK-Lite Pipeline', 'variants_vcfgz']
             })
        edges = pd.DataFrame(
            {'source': ['node1', 'node2', 'node3', 'node4', 'node5', 'node5', 'node6', 'node7',
                        'node8'],
             'target': ['node5', 'node5', 'node5', 'node5', 'node6', 'node7', 'node8', 'node8',
                        'node9']
             })

        elements = []
        for i in range(len(community.axes[0])):
            elements.append({'data': {'id': community['nodes'][i], 'label': community['labels'][i]},
                             'classes': community['image_class'][i],
                             'position': {'x': community['x-position'][i], 'y': community['y-position'][i]}
                             })

        source = edges['source'].tolist()
        target = edges['target'].tolist()
        community_list = community['nodes'].tolist()

        for i in range(len(source)):
            if source[i] in community_list and target[i] in community_list:
                elements.append({'data': {'source': source[i], 'target': target[i]},
                                 # 'position': {'x': community['x-position'][i], 'y': community['y-position'][i]}
                                 })
    else:
        community = pd.DataFrame(
            {'nodes': ['node1', 'node2', 'node3', 'node4', 'node5', 'node6'],
             'image_class': ['read_bam1', 'read_bam2', 'read_bam3', 'read_bam4', 'square_bam', 'read_bam5'],
             'x-position': [0, 0, 0, 200, 400, 600],
             'y-position': [0, 150, 300, 150, 150, 150],
             'labels': ['*.bam', 'rg_info_csv', 'reference_genome',
                        '*.sorted_markduplicated_bam',
                        'GATK-Lite Pipeline', 'variants_vcfgz']
             })
        edges = pd.DataFrame(
            {'source': ['node1', 'node2', 'node3', 'node4', 'node5'],
             'target': ['node4', 'node4', 'node4', 'node5', 'node6']
             })

        elements = []
        for i in range(len(community.axes[0])):
            elements.append({'data': {'id': community['nodes'][i], 'label': community['labels'][i]},
                             'classes': community['image_class'][i],
                             'position': {'x': community['x-position'][i], 'y': community['y-position'][i]}
                             })

        source = edges['source'].tolist()
        target = edges['target'].tolist()
        community_list = community['nodes'].tolist()

        for i in range(len(source)):
            if source[i] in community_list and target[i] in community_list:
                elements.append({'data': {'source': source[i], 'target': target[i]},
                                 # 'position': {'x': community['x-position'][i], 'y': community['y-position'][i]}
                                 })
    return elements


def create_layout():
    return html.Div([
        html.Div([
            sidebar.create_layout(),
        ], className="screen_division_left"),
        html.Div([
            topbar.create_layout(),
            html.Div([
                html.Div([
                    dbc.Button("Back", className="back_button", color='light', href="/create_pipeline"),
                    dbc.Button("Analysis Dashboard", className="next_button", color='light', href="/analysis_dashboard")
                ]),
                html.P("Analysis", className="get_data_title"),
                html.Div(html.Div(id='get_cytoscape'))
            ], className="get_data_sub_main")
        ], className="screen_division_right")
    ], className="get_data_main")


@app.callback(Output('get_cytoscape', 'children'),
              [Input('data-format-store', 'data'), Input('mapping-store', 'data')])
def get_cytoscape(json_object, json_object2):
    data_format_df = pd.read_json(json_object, orient='split')
    data_format = data_format_df.value[0]

    if data_format != 'bam':
        mapping_df = pd.read_json(json_object2, orient='split')
        mapping = mapping_df.value[0]
        return html.Div([
            get_modal("modal_1", 'close_1', 'upload_1', 'Read fastq'),
            get_modal("modal_2", 'close_2', 'upload_2', 'Read fastq'),
            get_modal("modal_3", 'close_3', 'upload_3', 'Read group'),
            get_modal("modal_4", 'close_4', 'upload_4', 'Reference Genome'),
            cyto.Cytoscape(
                id='cytoscape',
                style={'width': '100%', 'height': '80vh'},
                responsive=True,
                minZoom=0.2,
                maxZoom=2,
                elements=get_elements(data_format, mapping),
                layout={'name': 'preset'},
                stylesheet=default_stylesheet
            )]
        )
    else:
        return html.Div([
            get_modal("modal_bam_1", 'close_bam_1', 'upload_bam_1', 'Read bam'),
            get_modal("modal_bam_2", 'close_bam_2', 'upload_bam_2', 'Read group'),
            get_modal("modal_bam_3", 'close_bam_3', 'upload_bam_3', 'Reference Genome'),
            cyto.Cytoscape(
                id='cytoscape',
                style={'width': '100%', 'height': '62vh'},
                responsive=True,
                minZoom=0.2,
                maxZoom=2,
                elements=get_elements(data_format, None),
                layout={'name': 'preset'},
                stylesheet=default_stylesheet
            )]
        )


@app.callback(
    Output("modal_1", "is_open"),
    [Input('cytoscape', 'tapNode'), Input("close_1", "n_clicks"), Input("upload_1", "n_clicks")],
    [State("modal_1", "is_open")],
)
def toggle_modal(node, n1, n2, is_open):
    if node is not None:
        if node['data']['id'] == 'node1':
            return not is_open
    return is_open


@app.callback(
    Output("modal_2", "is_open"),
    [Input('cytoscape', 'tapNode'), Input("close_2", "n_clicks"), Input("upload_2", "n_clicks")],
    [State("modal_2", "is_open")],
)
def toggle_modal(node, n1, n2, is_open):
    if node is not None:
        if node['data']['id'] == 'node2':
            return not is_open
    return is_open


@app.callback(
    Output("modal_3", "is_open"),
    [Input('cytoscape', 'tapNode'), Input("close_3", "n_clicks"), Input("upload_3", "n_clicks")],
    [State("modal_3", "is_open")],
)
def toggle_modal(node, n1, n2, is_open):
    if node is not None:
        if node['data']['id'] == 'node3':
            return not is_open
    return is_open


@app.callback(
    Output("modal_4", "is_open"),
    [Input('cytoscape', 'tapNode'), Input("close_4", "n_clicks"), Input("upload_4", "n_clicks")],
    [State("modal_4", "is_open")],
)
def toggle_modal(node, n1, n2, is_open):
    if node is not None:
        if node['data']['id'] == 'node4':
            return not is_open
    return is_open


@app.callback(
    Output("modal_bam_1", "is_open"),
    [Input('cytoscape', 'tapNode'), Input("close_bam_1", "n_clicks"), Input("upload_bam_1", "n_clicks")],
    [State("modal_bam_1", "is_open")],
)
def toggle_modal(node, n1, n2, is_open):
    if node is not None:
        if node['data']['id'] == 'node1':
            return not is_open
    return is_open


@app.callback(
    Output("modal_bam_2", "is_open"),
    [Input('cytoscape', 'tapNode'), Input("close_bam_2", "n_clicks"), Input("upload_bam_2", "n_clicks")],
    [State("modal_bam_2", "is_open")],
)
def toggle_modal(node, n1, n2, is_open):
    if node is not None:
        if node['data']['id'] == 'node2':
            return not is_open
    return is_open


@app.callback(
    Output("modal_bam_3", "is_open"),
    [Input('cytoscape', 'tapNode'), Input("close_bam_3", "n_clicks"), Input("upload_bam_3", "n_clicks")],
    [State("modal_bam_3", "is_open")],
)
def toggle_modal(node, n1, n2, is_open):
    if node is not None:
        if node['data']['id'] == 'node3':
            return not is_open
    return is_open
