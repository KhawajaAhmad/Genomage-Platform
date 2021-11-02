from utils.import_utils import *
from app import app


# =================================== Genomage =================================================
def create_layout():
    return html.Div([
        dbc.Nav(
            [
                dbc.NavItem([
                    html.Img(src="assets/logo.png", className="sidebar_logo")
                ]),
                dbc.NavItem(
                    dbc.NavLink([
                        html.Img(src="assets/dashboard.png", className='sidebar_nav_img'),
                        html.P("Dashboard", className='sidebar_nav_text'),
                    ], active=True, href='/dashboard', className='nav_link')),
                dbc.NavItem(
                    dbc.NavLink([
                        html.Img(src="assets/project.png", className='sidebar_nav_img'),
                        html.P("Projects", className='sidebar_nav_text'),
                    ], active=True, href='/projects', className='nav_link')),
                dbc.NavItem(
                    dbc.NavLink([
                        html.Img(src="assets/analysis.png", className='sidebar_nav_img'),
                        html.P("Analysis", className='sidebar_nav_text'),
                    ], active=True, href='analysis', className='nav_link')),
                dbc.NavItem(
                    dbc.NavLink([
                        html.Img(src="assets/tools.png", className='sidebar_nav_img'),
                        html.P("Tool Library", className='sidebar_nav_text'),
                    ], active=True, href='tools', className='nav_link')),
                dbc.NavItem(
                    dbc.NavLink([
                        html.Img(src="assets/documentation.png", className='sidebar_nav_img'),
                        html.P("Documentation", className='sidebar_nav_text'),
                    ], active=True, href='documentation', className='nav_link')),
                dbc.NavItem(
                    dbc.NavLink([
                        html.Img(src="assets/power-off.png", className='sidebar_nav_img'),
                        html.P("Logout", className='sidebar_nav_text'),
                    ], active=True, href='/login_page', className='nav_link')),
            ],
            vertical="sm",
        )
    ], className='sidebar_main')
