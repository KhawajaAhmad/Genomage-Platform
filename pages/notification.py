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
                html.P("Notifications", className="notification_title"),
                html.Div([
                    dbc.Button([
                        html.P("⪢", className="notification_btn_bullet"),
                        html.P("Analysis Completed successfully", className="notification_btn_text"),
                        html.P("7/23/2021 11:15", className="notification_date")
                    ], className="notification_btn"),
                    dbc.Button([
                        html.P("⪢", className="notification_btn_bullet"),
                        html.P("Analysis Completed successfully", className="notification_btn_text"),
                        html.P("7/23/2021 11:15", className="notification_date")
                    ], className="notification_btn"),
                    dbc.Button([
                        html.P("⪢", className="notification_btn_bullet"),
                        html.P("Analysis Completed successfully", className="notification_btn_text"),
                        html.P("7/23/2021 11:15", className="notification_date")
                    ], className="notification_btn"),
                    dbc.Button([
                        html.P("⪢", className="notification_btn_bullet"),
                        html.P("Analysis Completed successfully", className="notification_btn_text"),
                        html.P("7/23/2021 11:15", className="notification_date")
                    ], className="notification_btn"),                    dbc.Button([
                        html.P("⪢", className="notification_btn_bullet"),
                        html.P("Analysis Completed successfully", className="notification_btn_text"),
                        html.P("7/23/2021 11:15", className="notification_date")
                    ], className="notification_btn"),

                ])
            ], className="notification_sub_main")
        ], className="screen_division_right"),
    ], className="notification_main")
