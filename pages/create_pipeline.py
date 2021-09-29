from utils.import_utils import *
from app import app
from pages import sidebar, topbar


def cards(image, text, card_id):
    return html.Div([
        dbc.Card([
            dbc.CardBody([
                dbc.CardImg(src=image, top=True, className="pipeline_card_img"),
                html.P(text, className="analysis_card_text"),
            ], className="pipeline_card_body"
            ),
        ], className="pipeline_card"
        )
    ], id=card_id, n_clicks=0)


def radio_items(options, id):
    return dcc.RadioItems(
        options=options,
        id=id,
        labelStyle={'font-size': 13, 'display': 'flex', 'align-items': 'center',
                    'padding': 0,
                    'margin': 5},
        style={'vertical-align': -4, 'display': 'inline-block', 'margin': 5},
        inputStyle={"margin-right": 6}
    )


def modal_content(modal_id):
    if modal_id == "analysis_type_modal":
        options = [{'label': 'WGS', 'value': 'WGS'},
                   {'label': 'WES', 'value': 'WES'},
                   {'label': 'RNA Seq', 'value': 'rna'}]
        return html.Div([
            radio_items(options, "analysis_type_radio")
        ])
    elif modal_id == "data_format_modal":
        options = [{'label': 'fastq', 'value': 'fastq'},
                   {'label': 'fastq.gz', 'value': 'fastq.gz'},
                   {'label': '.BAM', 'value': 'bam'}]
        options2 = [{'label': '.fasta', 'value': 'fasta'},
                    {'label': '.fa', 'value': 'fa'},
                    {'label': '.fna', 'value': 'fna'},
                    {'label': '.bed file', 'value': 'bed'}]

        return html.Div([
            html.P("Input File:", className="modal_sub_headings"),
            radio_items(options, "data_format1"),
            html.P("Reference Genome", className="modal_sub_headings"),
            radio_items(options2, "data_format2")
        ])
    elif modal_id == "qc_modal":
        options = [{'label': 'FASTQC', 'value': 'fastqc'},
                   {'label': 'FASTP', 'value': 'fastp'}]
        return html.Div([
            radio_items(options, "qc_radio")
        ])
    elif modal_id == "trimming_modal":
        options = [{'label': 'Trimomatic', 'value': 'trimomatic'},
                   {'label': 'Cutadapt', 'value': 'cutadapt'}]
        return html.Div([
            radio_items(options, "trimming_radio")
        ])
    elif modal_id == "reference_genome_index_modal":
        options = [{'label': 'SAM Tools', 'value': 'sam'},
                   {'label': 'BWA', 'value': 'bwa'},
                   {'label': 'Bowtie2', 'value': 'bowtie2'},
                   {'label': 'PiCard Tools', 'value': 'picard'}]
        options2 = [{'label': 'fastq.gz', 'value': 'fastq.gz'},
                    {'label': 'fa.gz', 'value': 'fa.gz'},
                    {'label': 'fasta', 'value': 'fasta'}]
        return html.Div([
            html.P("Set a Tool:", className="modal_sub_headings"),
            radio_items(options, "reference_genome_tool_index_radio"),
            html.P("Set a data format", className="modal_sub_headings"),
            radio_items(options2, "reference_genome_dataformat_index_radio")
        ])

    elif modal_id == "alignment_modal":
        options = [{'label': 'SAM Tools', 'value': 'sam'},
                   {'label': 'BWA', 'value': 'bwa'},
                   {'label': 'Bowtie2', 'value': 'bowtie2'}]
        return html.Div([
            radio_items(options, "alignment_radio")
        ])
    elif modal_id == "duplicates_modal":
        options = [{'label': 'Picard Tools', 'value': 'picard'}]
        return html.Div([
            radio_items(options, "duplicates_radio")
        ])
    elif modal_id == "BQSR_modal":
        options = [{'label': 'Picard Tools', 'value': 'picard'}]
        return html.Div([
            radio_items(options, "BQSR_radio")
        ])
    elif modal_id == "variant_calling_modal":
        options = [{'label': 'Mutect 2', 'value': 'mutect'},
                   {'label': 'Haplotype', 'value': 'haplotype'},
                   {'label': 'DeepVariant', 'value': 'deepvariant'}]
        return html.Div([
            radio_items(options, "variant_calling_radio")
        ])
    elif modal_id == "variant_filt_ration_modal":
        options = [{'label': 'bcftools', 'value': 'bcftools'}]
        return html.Div([
            radio_items(options, "variant_filt_ration_radio")
        ])
    elif modal_id == "computing_power_modal":
        options = [{'label': 'High', 'value': 'high'},
                   {'label': 'Medium', 'value': 'medium'},
                   {'label': 'Low', 'value': 'low'}]
        return html.Div([
            # radio_items(options, "computing_power_radio"),
            html.Div([
                dcc.Slider(
                    className="computing_power_slider",
                    min=1,
                    max=3,
                    step=None,
                    id="computing_power_radio",
                    marks={
                        1: {'label': 'low', 'style': {'color': '#004677', 'font-size': 14}},
                        2: {'label': 'medium', 'style': {'color': '#004677', 'font-size': 14}},
                        3: {'label': 'high', 'style': {'color': '#004677', 'font-size': 14}},
                    },
                ),
                html.Div([
                    html.P("RAM: 10GB", className="modal_box_text"),
                    html.P("CPU: 7GHz", className="modal_box_text"),
                    html.P("Estimated Cost: $10", className="modal_box_text")
                ], className="modal_box"),
                html.Div([
                    html.P("RAM: 10GB", className="modal_box_text"),
                    html.P("CPU: 7GHz", className="modal_box_text"),
                    html.P("Estimated Cost: $10", className="modal_box_text")
                ], className="modal_box"),
                html.Div([
                    html.P("RAM: 10GB", className="modal_box_text"),
                    html.P("CPU: 7GHz", className="modal_box_text"),
                    html.P("Estimated Cost: $10", className="modal_box_text")
                ], className="modal_box"),
            ], style={'text-align': 'center', 'padding': "20px 0px"}),
        ])


def get_modal(modal_id, close_id, save_id, heading):
    return html.Div([
        dbc.Modal([
            dbc.ModalBody([
                html.P(heading, className="modal_headings"),
                modal_content(modal_id)]),
            dbc.ModalFooter([
                dbc.Button("Close", id=close_id, color="light", n_clicks=0, className="modal_closing"),
                dbc.Button("Save", id=save_id, color="success", n_clicks=0, className="modal_saving"),
            ]
            ),
        ],
            id=modal_id,
            is_open=False,
        ),
    ]
    )


def get_modal2(modal_id, close_id, save_id, heading):
    return html.Div([
        dbc.Modal([
            dbc.ModalBody([
                html.P(heading, className="modal_headings"),
                modal_content(modal_id)]),
            dbc.ModalFooter([
                dbc.Button("Close", id=close_id, color="light", n_clicks=0, className="modal_closing"),
                dbc.Button("Save", id=save_id, color="success", n_clicks=0, className="modal_saving"),
            ]
            ),
        ],
            id=modal_id,
            is_open=False,
            size='lg'
        ),
    ]
    )


def create_layout():
    return html.Div([
        html.Div([
            sidebar.create_layout(),
        ], className="screen_division_left"),
        html.Div([
            topbar.create_layout(),
            html.Div([
                html.Div([
                    html.Div([
                        html.P("Analysis", className="pipeline_title", id="pipeline_title"),
                        dbc.Button(html.Img(src="/assets/edit.png", className="pipeline_share_icon"),
                                   className="pipeline_title_edit", id="pipeline_title_edit"),
                        dbc.Button(html.Img(src="/assets/share.png", className="pipeline_share_icon"),
                                   className="pipeline_title_edit"),
                        dbc.Modal(
                            [
                                dbc.ModalBody([
                                    html.P("Change Title", className="modal_headings"),
                                    dbc.Input(id="title_input", placeholder="Enter New title", type="text",
                                              className="title_modal_input"),
                                ]),
                                dbc.ModalFooter(
                                    dbc.Button("Close", id="pipeline_title_edit_close", color="light", n_clicks=0,
                                               className="modal_closing"),
                                ),
                            ],
                            id="pipeline_title_edit_modal",
                            is_open=False,
                        ),
                        dbc.Button("Save as draft", color="light", className="pipeline_save_as_draft")
                    ]),
                    dbc.Row([
                        get_modal("analysis_type_modal", "analysis_type_close", "analysis_type_save",
                                  'Select Analysis Type'),
                        get_modal("data_format_modal", "data_format_close", "data_format_save",
                                  'Select Data Format'),
                        get_modal("qc_modal", "qc_close", "qc_save", "Quality Control"),
                        get_modal("trimming_modal", "trimming_close", "trimming_save",
                                  "Read Manipulation/ Trimming"),
                        get_modal("reference_genome_index_modal", "reference_genome_index_close",
                                  "reference_genome_index_save", "Reference Genome Index"),
                        get_modal("alignment_modal", "alignment_close", "alignment_save", "Alignment"),
                        get_modal("duplicates_modal", "duplicates_close", "duplicates_save", "Mark Duplicates"),
                        get_modal("BQSR_modal", "BQSR_close", "BQSR_save", "BQSR"),
                        get_modal("variant_calling_modal", "variant_calling_close", "variant_calling_save",
                                  "variant Calling"),
                        get_modal("variant_filt_ration_modal", "variant_filt_ration_close",
                                  "variant_filt_ration_save", "variant filt ration"),
                        get_modal2("computing_power_modal", "computing_power_close", "computing_power_save",
                                   "computing Power"),
                        html.Div(html.Div(cards("assets/img1.png", "Select Analysis Type", 'analysis_type')),
                                 className="visible_div"),
                        html.Div(id="visible_div1", className="visible_div"),
                        html.Div(id="visible_div2", className="visible_div"),
                        html.Div(id="visible_div3", className="visible_div"),
                        html.Div(id="visible_div4", className="visible_div"),
                        html.Div(id="visible_div5", className="visible_div"),
                        html.Div(id="visible_div6", className="visible_div"),
                        html.Div(id="visible_div7", className="visible_div"),
                        html.Div(id="visible_div8", className="visible_div"),
                        html.Div(id="visible_div9", className="visible_div"),
                        html.Div(id="visible_div10", className="visible_div"),
                        html.Div(id="visible_div11", className="visible_div"),
                    ], no_gutters=True),
                ])
            ], className="pipeline_sub_main")
        ], className="screen_division_right")
    ], className="pipeline_main")


def toggle_modal(n1, n2, n3, is_open):
    if n1 or n2 or n3:
        return not is_open
    return is_open


app.callback(
    Output("analysis_type_modal", "is_open"),
    [Input("analysis_type", "n_clicks"), Input("analysis_type_close", "n_clicks"),
     Input("analysis_type_save", "n_clicks")],
    [State("analysis_type_modal", "is_open")])(toggle_modal)

app.callback(
    Output("data_format_modal", "is_open"),
    [Input("data_format", "n_clicks"), Input("data_format_close", "n_clicks"),
     Input("data_format_save", "n_clicks")],
    [State("data_format_modal", "is_open")])(toggle_modal)

app.callback(
    Output("qc_modal", "is_open"),
    [Input("qc", "n_clicks"), Input("qc_close", "n_clicks"),
     Input("qc_save", "n_clicks")],
    [State("qc_modal", "is_open")])(toggle_modal)

app.callback(
    Output("trimming_modal", "is_open"),
    [Input("trimming", "n_clicks"), Input("trimming_close", "n_clicks"),
     Input("trimming_save", "n_clicks")],
    [State("trimming_modal", "is_open")])(toggle_modal)

app.callback(
    Output("reference_genome_index_modal", "is_open"),
    [Input("reference_genome_index", "n_clicks"), Input("reference_genome_index_close", "n_clicks"),
     Input("reference_genome_index_save", "n_clicks")],
    [State("reference_genome_index_modal", "is_open")])(toggle_modal)

app.callback(
    Output("alignment_modal", "is_open"),
    [Input("alignment", "n_clicks"), Input("alignment_close", "n_clicks"),
     Input("alignment_save", "n_clicks")],
    [State("alignment_modal", "is_open")])(toggle_modal)

app.callback(
    Output("duplicates_modal", "is_open"),
    [Input("duplicates", "n_clicks"), Input("duplicates_close", "n_clicks"),
     Input("duplicates_save", "n_clicks")],
    [State("duplicates_modal", "is_open")])(toggle_modal)

app.callback(
    Output("BQSR_modal", "is_open"),
    [Input("BQSR", "n_clicks"), Input("BQSR_close", "n_clicks"),
     Input("BQSR_save", "n_clicks")],
    [State("BQSR_modal", "is_open")])(toggle_modal)

app.callback(
    Output("variant_calling_modal", "is_open"),
    [Input("variant_calling", "n_clicks"), Input("variant_calling_close", "n_clicks"),
     Input("variant_calling_save", "n_clicks")],
    [State("variant_calling_modal", "is_open")])(toggle_modal)

app.callback(
    Output("variant_filt_ration_modal", "is_open"),
    [Input("variant_filt_ration", "n_clicks"), Input("variant_filt_ration_close", "n_clicks"),
     Input("variant_filt_ration_save", "n_clicks")],
    [State("variant_filt_ration_modal", "is_open")])(toggle_modal)

app.callback(
    Output("computing_power_modal", "is_open"),
    [Input("computing_power", "n_clicks"), Input("computing_power_close", "n_clicks"),
     Input("computing_power_save", "n_clicks")],
    [State("computing_power_modal", "is_open")])(toggle_modal)


@app.callback(Output("visible_div1", "children"),
              Input("analysis_type_save", "n_clicks"),
              State("analysis_type_radio", "value"))
def invisible_div(n1, v1):
    if n1 and v1:
        return html.Div(cards("assets/img2.png", "Select Data Format", 'data_format'))
    return html.Div(cards("assets/img2.png", "Select Data Format", 'data_format'))


@app.callback(Output("visible_div2", "children"),
              Input("data_format_save", "n_clicks"),
              [State("data_format1", "value"),
               State("data_format2", "value")])
def invisible_div(n1, v1, v2):
    if n1 and v1 and v2:
        return html.Div(cards("assets/img3.png", "Quality Control", 'qc'))
    return html.Div(cards("assets/img3.png", "Quality Control", 'qc'))


@app.callback(Output("visible_div3", "children"),
              Input("qc_save", "n_clicks"),
              State("qc_radio", "value"))
def invisible_div(n1, v1):
    if n1 and v1:
        return html.Div(cards("assets/img4.png", "Read Manipulation/ Trimming", 'trimming'))
    return html.Div(cards("assets/img4.png", "Read Manipulation/ Trimming", 'trimming'))


@app.callback(Output("visible_div4", "children"),
              Input("trimming_save", "n_clicks"),
              State("trimming_radio", "value"))
def invisible_div(n1, v1):
    if n1 and v1:
        return html.Div(cards("assets/img5.png", "Reference Genome Index", 'reference_genome_index'))
    return html.Div(cards("assets/img5.png", "Reference Genome Index", 'reference_genome_index'))


@app.callback(Output("visible_div5", "children"),
              Input("reference_genome_index_save", "n_clicks"),
              [State("reference_genome_tool_index_radio", "value"),
               State('reference_genome_dataformat_index_radio', 'value')])
def invisible_div(n1, v1, v2):
    if n1 and v1 and v2:
        return html.Div(cards("assets/img6.png", "Alignment", 'alignment'))
    return html.Div(cards("assets/img6.png", "Alignment", 'alignment'))


@app.callback(Output("visible_div6", "children"),
              Input("alignment_save", "n_clicks"),
              State("alignment_radio", "value"))
def invisible_div(n1, v1):
    if n1 and v1:
        return html.Div(cards("assets/img7.png", "Mark Duplicates", 'duplicates'))
    return html.Div(cards("assets/img7.png", "Mark Duplicates", 'duplicates'))

@app.callback(Output("visible_div7", "children"),
              Input("duplicates_save", "n_clicks"),
              State("duplicates_radio", "value"))
def invisible_div(n1, v1):
    if n1 and v1:
        return html.Div(cards("assets/img8.png", "BQSR", 'BQSR'))
    return html.Div(cards("assets/img8.png", "BQSR", 'BQSR'))


@app.callback(Output("visible_div8", "children"),
              Input("BQSR_save", "n_clicks"),
              State("BQSR_radio", "value"))
def invisible_div(n1, v1):
    if n1 and v1:
        return html.Div(cards("assets/img9.png", "Variant Calling", 'variant_calling'))
    return html.Div(cards("assets/img9.png", "Variant Calling", 'variant_calling'))


@app.callback(Output("visible_div9", "children"),
              Input("variant_calling_save", "n_clicks"),
              State("variant_calling_radio", "value"))
def invisible_div(n1, v1):
    if n1 and v1:
        return html.Div(cards("assets/img10.png", "Variant Filtration", 'variant_filt_ration'))
    return html.Div(cards("assets/img10.png", "Variant Filtration", 'variant_filt_ration'))


@app.callback(Output("visible_div10", "children"),
              Input("variant_filt_ration_save", "n_clicks"),
              State("variant_filt_ration_radio", "value"))
def invisible_div(n1, v1):
    if n1 and v1:
        return html.Div(cards("assets/img11.png", "Computing Power", 'computing_power'))
    return html.Div(cards("assets/img11.png", "Computing Power", 'computing_power'))


@app.callback(Output("visible_div11", "children"),
              Input("computing_power_save", "n_clicks"),
              State("computing_power_radio", "value"))
def invisible_div(n1, v1):
    if n1 and v1:
        return html.Div(dbc.Button("Finish Setup", color="success", className="pipeline_finish_button", href="/get_data"))
    return html.Div(dbc.Button("Finish Setup", color="success", className="pipeline_finish_button", href="/get_data"))


@app.callback(
    Output("pipeline_title_edit_modal", "is_open"),
    [Input("pipeline_title_edit", "n_clicks"), Input("pipeline_title_edit_close", "n_clicks")],
    [State("pipeline_title_edit_modal", "is_open")],
)
def toggle_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open


@app.callback(Output("pipeline_title", "children"), [Input("title_input", "value")])
def output_text(value):
    if value is None:
        return "Analysis"
    return value

