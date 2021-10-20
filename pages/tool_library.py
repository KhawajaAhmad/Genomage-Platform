from utils.import_utils import *
from app import app
from pages import sidebar, topbar


def Box(head, detail):
    return html.Div([
        html.P(head, className="tools_boxes_head"),
        html.P(detail, className="tools_boxes_text"),
    ], className="tools_boxes")


def create_layout():
    return html.Div([
        html.Div([
            sidebar.create_layout(),
        ], className="screen_division_left"),
        html.Div([
            topbar.create_layout(),
            html.Div([
                html.P("Tools", className="tools_title"),
                dbc.Form([
                    dbc.FormGroup(
                        [
                            dbc.Checklist(
                                options=[{"label": "Genomics", "value": 1},
                                         {"label": "Transcriptomics", "value": 2},
                                         {"label": "SARS Covid", "value": 3}],
                                value=[], inline=True, switch=True, id="switches_inline_input",
                                className="tools_toggle"
                            )
                        ])
                ], style={'display': 'inline-block', 'margin-left': 10}),
                dbc.Button("Analysis", className="tools_analysis", color="primary"),
                html.Div([
                    Box("FastQC", "fastq read quality assesment"),
                    Box("Cutadapt", "For primers and adapter removal from fastq files"),
                    Box("Trimmomatic", "For primers and adapter removal from fastq files"),
                    Box("Fastp", "fastq read quality assesment"),
                    Box("Hisat2", "Index and Alignment"),
                    Box("STAR", "Index and Alignment"),
                    Box("TopHat", "Index and Alignment"),
                    Box("Feature Counts", "Feature counts"),
                    Box("HTSeq", "Feature counts"),
                    Box("RSEM", "Feature counts"),
                    Box("Cufflinks", "Feature counts"),
                    Box("DESeq2/ limma/ edgeR/ CuffDiff", "Differential expression analysis"),
                    Box("Kegg/ Rectome/ Gene-ontology", "Gene set enrichment analysis"),
                    Box("sarttools", "Differential expression analysis and report"),
                    Box("BWA", "Index and Alignment"),
                    Box("BOWTIE", "Index and Alignment"),
                    Box("Samtools", ".sam to .bam, sort and index, stats"),
                    Box("Picard Tools", "Markduplicate, dictionary, merge vcfs"),
                    Box("snpEff", "Annotation"),
                    Box("Importer tools", "To import data on Platform"),
                    Box("Strelka2", "Germline and somatic  variant calling"),
                    Box("Sentieon", "Germline and somatic  variant calling"),
                    Box("GATK", "Vcf calling"),
                    Box("bcftools", "Vcf calling and Variant filteration"),
                    Box("freebayes", "Vcf calling"),
                    Box("Vcf calling", "Annotation"),
                    Box("Deep_variant", "Vcf calling")
                ])
            ], className="tools_sub_main"),
        ], className="screen_division_right"),
    ], className="tools_main")
