from utils.import_utils import *
from app import app
from pages import sidebar, topbar


def create_layout():
    return html.Div([
        html.Div([
            sidebar.create_layout(),
        ], className="screen_division_left"),
        html.Div([
            topbar.create_layout(),
            html.Div([
                html.P("Existing Pipeline", className="existing_pipeline_title"),
                dbc.Button([
                    html.P("※", className="existing_pipeline_btn_bullet"),
                    html.P("BWA-GATK", className="existing_pipeline_btn_text"),
                    html.Img(src="assets/right_arrow.png", className="existing_pipeline_btn_icon")
                ], className="existing_pipeline_btn", href="/get_data"),
                dbc.Button([
                    html.P("※", className="existing_pipeline_btn_bullet"),
                    html.P("BWA-DeepVarient", className="existing_pipeline_btn_text"),
                    html.Img(src="assets/right_arrow.png", className="existing_pipeline_btn_icon")
                ], className="existing_pipeline_btn", href="/get_data"),
                dbc.Button([
                    html.P("※", className="existing_pipeline_btn_bullet"),
                    html.P("STAR-DESEQ2", className="existing_pipeline_btn_text"),
                    html.Img(src="assets/right_arrow.png", className="existing_pipeline_btn_icon")
                ], className="existing_pipeline_btn", href="/get_data")
            ], className="existing_pipeline_sub_main")
        ], className="screen_division_right")
    ], className="existing_pipeline_main")
