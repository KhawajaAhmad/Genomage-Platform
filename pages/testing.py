# import random
# from twilio.rest import Client
#
# otp = random.randint(1000, 9999)
# print(otp)
# account_sid = "AC815db52f7f21b65983ef43ee5e0f6bf1"
# auth_token = "306344df0289ecb92a347bc97cf9b1da"
# client = Client(account_sid, auth_token)
#
# message = client.messages.create(
#     body="Your OTP is " + str(otp),
#     from_="+12523169147",
#     to="+923204646767"
# )
#
# print(message.sid)


# =====================================================================================================================
import dash
import dash_cytoscape as cyto
import dash_html_components as html

cyto.load_extra_layouts()

app = dash.Dash(__name__)

app.layout = html.Div([
    cyto.Cytoscape(
        style={'width': '100%', 'height': '96vh'},
        responsive=True,
        minZoom=0.2,
        maxZoom=2,
        layout={
            'name': 'dagre',
            'rankDir': "RL",
        },
        elements=[{'data': {'id': 'one', 'label': 'Text_head'}, 'locked': True, 'selectable': False},
                  {'data': {'id': 'two', 'label': 'Text_head'}, 'locked': True, 'selectable': False},
                  {'data': {'id': 'three', 'label': 'Text_head'}, 'locked': True, 'selectable': False},
                  {'data': {'id': 'four', 'label': 'Text_head'}, 'locked': True, 'selectable': False},
                  {'data': {'source': 'one', 'target': 'two'}},
                  {'data': {'source': 'two', 'target': 'three'}},
                  {'data': {'source': 'three', 'target': 'four'}},
                  {'data': {'source': 'two', 'target': 'four'}},
                  ]
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)

# ===================================================================================================================
# import dash
# import math
#
# import dash_cytoscape as cyto
# import dash_html_components as html
# cyto.load_extra_layouts()
#
# app = dash.Dash(__name__)
#
# nodes = [
#     {
#         'data': {'id': short, 'label': label}
#     }
#     for short, label in (
#         ('la', 'Los Angeles'),
#         ('nyc', 'New York'),
#         ('to', 'Toronto'),
#         ('mtl', 'Montreal'),
#         ('van', 'Vancouver'),
#         ('chi', 'Chicago'),
#         ('bos', 'Boston'),
#         ('hou', 'Houston')
#     )
# ]
#
# edges = [
#     {'data': {'source': source, 'target': target}}
#     for source, target in (
#         ('van', 'la'),
#         ('la', 'chi'),
#         ('hou', 'chi'),
#         ('to', 'mtl'),
#         ('mtl', 'bos'),
#         ('nyc', 'bos'),
#         ('to', 'hou'),
#         ('to', 'nyc'),
#         ('la', 'nyc'),
#         ('nyc', 'bos')
#     )
# ]
#
# elements = nodes + edges
#
# app.layout = html.Div([
#     cyto.Cytoscape(
#         id='cytoscape-layout-9',
#         elements=elements,
#         style={'width': '100%', 'height': '350px'},
#         layout={
#             'name': 'dagre',
#             'rankDir': "RL",
#         }
#     )
# ])
#
# if __name__ == '__main__':
#     app.run_server(debug=True)