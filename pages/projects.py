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
                dbc.Button("+ Project", className='add_project_btn', color='light', outline=True,
                           href="/new_project"),
                html.Div([
                    html.Div([
                        html.P("Name", className="project_table_head"),
                        html.P("Access", className="project_table_head"),
                        html.P("Tags", className="project_table_head"),
                        html.P("Modified", className="project_table_head"),
                    ], className='project_table_top'),
                    html.Div([
                        html.P("New Project", className="project_table_text"),
                        html.P("AK", className="project_table_text"),
                        html.P("1", className="project_table_text"),
                        html.P("7/23/2021 11:15", className="project_table_text"),
                    ], className='project_table_bottom'),
                    html.Div([
                        html.P("Project 1", className="project_table_text"),
                        html.P("KE", className="project_table_text"),
                        html.P("1", className="project_table_text"),
                        html.P("2/13/2021 11:00", className="project_table_text"),
                    ], className='project_table_bottom'),
                    html.Div([
                        html.P("Project 2", className="project_table_text"),
                        html.P("BS", className="project_table_text"),
                        html.P("2", className="project_table_text"),
                        html.P("12/16/2021 1:45", className="project_table_text"),
                    ], className='project_table_bottom'),
                    html.Div([
                        html.P("Project 3", className="project_table_text"),
                        html.P("BS", className="project_table_text"),
                        html.P("1", className="project_table_text"),
                        html.P("1/28/2021 10:12", className="project_table_text"),
                    ], className='project_table_bottom'),
                    html.Div([
                        html.P("Project 4", className="project_table_text"),
                        html.P("AK", className="project_table_text"),
                        html.P("6", className="project_table_text"),
                        html.P("7/23/2021 11:15", className="project_table_text"),
                    ], className='project_table_bottom')
                ], className='project_table_display')
            ], className="project_sub_main")
        ], className="screen_division_right")
    ], className="project_main")
