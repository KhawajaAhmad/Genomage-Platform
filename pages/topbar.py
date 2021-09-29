from utils.import_utils import *
from app import app


def create_layout():
    return html.Div([
        dbc.Row([
            dbc.Col(width=1),
            dbc.Col([
                html.Div([
                    html.Img(src="assets/notification1.png", className='topbar_notification_icon'),
                    html.Img(src="assets/profile_icon.png", className='topbar_profile_icon')],
                         className='topbar_imgs_container'),
            ], width=11),
        ], no_gutters=True),
    ], className='top_bar_main')
