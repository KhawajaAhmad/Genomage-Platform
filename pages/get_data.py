from utils.import_utils import *
from app import app
from pages import sidebar, topbar
import pandas as pd


def get_node(image, text_head, text):
    return html.Div([
        html.Div(html.Img(src=image, className="get_data_icons"),
                 className="get_data_icons_container"),
        html.P(text_head, className="get_data_text_head"),
        html.P(text, className="get_data_text")
    ], style={'text-align': 'center', 'height': 120})


def create_layout():
    return html.Div([
        html.Div([
            sidebar.create_layout(),
        ], className="screen_division_left"),
        html.Div([
            topbar.create_layout(),
            html.Div([
                html.P("Analysis", className="get_data_title"),
                dbc.Row([
                    dbc.Col([
                        html.Div([
                            get_node("assets/read1.png", "text head", "text-detail"),
                            get_node("assets/read2.png", "text head", "text-detail"),
                            get_node("assets/read3.png", "text head", "text-detail"),
                            get_node("assets/read4.png", "text head", "text-detail"),
                        ], className="get_data_vertical_div"),
                    ], width=2),
                    dbc.Col([
                        html.Div([
                            html.P("BWA-MEM FAST Read Mapper", className="get_data_step2")
                        ], className="get_data_vertical_div"),
                    ], width=2),
                    dbc.Col([
                        html.Div([
                            html.Div(style={"height": 60}),
                            get_node("assets/read5.png", "text head", "text-detail"),
                            get_node("assets/read6.png", "text head", "text-detail"),
                            get_node("assets/read7.png", "text head", "text-detail"),
                            html.Div(style={"height": 60}),
                        ], className="get_data_vertical_div"),
                    ], width=2),
                    dbc.Col([
                        html.Div([
                            html.Div(style={"height": 190}),
                            get_node("assets/read8.png", "text head", "text-detail"),
                            html.Div(style={"height": 190}),
                        ], className="get_data_vertical_div"),
                    ], width=2),
                    dbc.Col([
                        html.Div([
                            html.P("BWA-MEM FAST Read Mapper", className="get_data_step2")
                        ], className="get_data_vertical_div"),
                    ], width=2),
                    dbc.Col([
                        html.Div([
                            html.Div(style={"height": 120}),
                            get_node("assets/read9.png", "text head", "text-detail"),
                            get_node("assets/read10.png", "text head", "text-detail"),
                            html.Div(style={"height": 120}),
                        ], className="get_data_vertical_div"),
                    ], width=2),
                ], no_gutters=True),
            ], className="get_data_sub_main")
        ], className="screen_division_right")
    ], className="get_data_main")


