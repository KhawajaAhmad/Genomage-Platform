from utils.import_utils import *
from pages import login_page, dashboard, projects, analysis, tool_library, documentation, new_project, create_pipeline,\
    get_data, analysis_dashboard, existing_pipeline, notification, user_profile

from app import app

# Setting up the layout
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content'),
])


# URL Callback
@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == "/dashboard":
        return dashboard.create_layout()
    elif pathname == "/projects":
        return projects.create_layout()
    elif pathname == "/tools":
        return tool_library.create_layout()
    elif pathname == "/analysis":
        return analysis.create_layout()
    elif pathname == "/documentation":
        return documentation.create_layout()
    elif pathname == "/create_pipeline":
        return create_pipeline.create_layout()
    elif pathname == "/get_data":
        return get_data.create_layout()
    elif pathname == "/new_project":
        return new_project.create_layout()
    elif pathname == "/analysis_dashboard":
        return analysis_dashboard.create_layout()
    elif pathname == "/existing_pipeline":
        return existing_pipeline.create_layout()
    elif pathname == "/user_profile":
        return user_profile.create_layout()
    elif pathname == "/notification":
        return notification.create_layout()
    return login_page.create_layout()


# host='0.0.0.0', port=8080
if __name__ == '__main__':
    app.run_server(host='0.0.0.0', port=8080)
