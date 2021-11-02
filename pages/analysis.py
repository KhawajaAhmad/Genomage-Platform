from utils.import_utils import *
from app import app
from pages import sidebar, topbar


# =================================== Genomage =================================================
def create_layout():
    return html.Div([
        html.Div([
            sidebar.create_layout(),
        ], className="screen_division_left"),
        html.Div([
            topbar.create_layout(),
            html.Div([
                html.Div([
                    dbc.Button("Create pipeline", className='analysis_btn1', outline=True,
                               href="/create_pipeline"),
                    dbc.Button("Use an existing pipeline", className='analysis_btn2', outline=True,
                               href="/existing_pipeline"),
                ], className='analysis_btn_container'),
                html.Div([
                    html.Div([
                        html.P("Project Title", className="analysis_table_head"),
                        html.P("Analysis Type", className="analysis_table_head"),
                        html.P("Pipeline", className="analysis_table_head"),
                        html.P("Current Step", className="analysis_table_head"),
                        html.P("Computing Power", className="analysis_table_head"),
                        html.P("Status", className="analysis_table_head"),
                        html.P("Action", className="analysis_table_head"),
                    ], className='analysis_table_top'),
                    html.Div([
                        html.P("Project 0", className="analysis_table_text"),
                        html.P("WGS", className="analysis_table_text"),
                        html.P("BWA-GATK", className="analysis_table_text"),
                        html.P("Variant Calling", className="analysis_table_text"),
                        html.P("High", className="analysis_table_text"),
                        html.P("◉", className="analysis_table_text_status", style={'color': 'red'}),
                        html.Div(['Pause │ ', html.Span(' Abort', style={'color': 'red'})],
                                 className="analysis_table_text")
                    ], className='analysis_table_bottom'),
                    html.Div([
                        html.P("Project 1", className="analysis_table_text"),
                        html.P("WES", className="analysis_table_text"),
                        html.P("BWA-GATK", className="analysis_table_text"),
                        html.P("Variant Calling", className="analysis_table_text"),
                        html.P("High", className="analysis_table_text"),
                        html.P("◉", className="analysis_table_text_status", style={'color': 'green'}),
                        html.Div(['Pause │ ', html.Span(' Abort', style={'color': 'red'})],
                                 className="analysis_table_text")
                    ], className='analysis_table_bottom'),
                    html.Div([
                        html.P("Project 2", className="analysis_table_text"),
                        html.P("RNA-seq", className="analysis_table_text"),
                        html.P("BWA-GATK", className="analysis_table_text"),
                        html.P("Variant Calling", className="analysis_table_text"),
                        html.P("High", className="analysis_table_text"),
                        html.P("◉", className="analysis_table_text_status", style={'color': 'orange'}),
                        html.Div(['Pause │ ', html.Span(' Abort', style={'color': 'red'})],
                                 className="analysis_table_text")
                    ], className='analysis_table_bottom'),
                    html.Div([
                        html.P("Project 3", className="analysis_table_text"),
                        html.P("SARS-COV2", className="analysis_table_text"),
                        html.P("BWA-GATK", className="analysis_table_text"),
                        html.P("Variant Calling", className="analysis_table_text"),
                        html.P("High", className="analysis_table_text"),
                        html.P("◉", className="analysis_table_text_status", style={'color': 'red'}),
                        html.Div(['Pause │ ', html.Span(' Abort', style={'color': 'red'})],
                                 className="analysis_table_text")
                    ], className='analysis_table_bottom'),
                    html.Div([
                        html.P("Project 4", className="analysis_table_text"),
                        html.P("WES", className="analysis_table_text"),
                        html.P("BWA-GATK", className="analysis_table_text"),
                        html.P("Variant Calling", className="analysis_table_text"),
                        html.P("High", className="analysis_table_text"),
                        html.P("◉", className="analysis_table_text_status", style={'color': 'green'}),
                        html.Div(['Pause │ ', html.Span(' Abort', style={'color': 'red'})],
                                 className="analysis_table_text")
                    ], className='analysis_table_bottom')
                ], className='analysis_table_display')
            ], className='analysis_sub_main')
        ], className="screen_division_right")
    ], className='analysis_main')
