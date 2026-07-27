#!/usr/bin/env python3
"""
Casitas Report Generator — Professional Investment Analysis
Generates 2-page bilingual PDF: English + Spanish
Structure: Summary → Analysis → Findings → Conclusions
"""

import glob
import pandas as pd
from datetime import datetime
from pathlib import Path

try:
    from reportlab.lib.pagesizes import A4
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.lib.units import inch
    from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, Table, TableStyle, PageBreak
    from reportlab.lib import colors
    from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT, TA_JUSTIFY
except ImportError:
    print("Install: uv pip install reportlab")
    exit(1)

PROJECT_ROOT = Path(__file__).parent.parent
DATA_OUTPUT = PROJECT_ROOT / "data" / "output"
REPORT_PATH = DATA_OUTPUT / f"report_casitas_{datetime.now().strftime('%Y%m%d_%H%M')}.pdf"

# Load ranking
ranking_files = sorted(glob.glob(str(DATA_OUTPUT / "ranking_final_*.csv")))
if not ranking_files:
    print("Ranking not found")
    exit(1)

df = pd.read_csv(ranking_files[-1])
df_viable = df[(df["recommendation"] != "discard") & (df["score_total"] > 0)].copy()
df_viable = df_viable[~df_viable["titulo"].str.contains("Alquiler", case=False, na=False)].copy()
df_viable = df_viable[df_viable["precio"].notna()].copy()

if "precio" in df_viable.columns and "m2" in df_viable.columns:
    df_viable["precio_por_m2"] = (df_viable["precio"] / df_viable["m2"]).round(0).astype("Int64")

# Metrics
total_analyzed = len(df)
total_recommended = len(df_viable)
avg_price = df_viable["precio"].mean() if "precio" in df_viable.columns else 0
avg_price_per_sqm = df_viable["precio_por_m2"].mean() if "precio_por_m2" in df_viable.columns else 0
price_min = df_viable["precio"].median() if "precio" in df_viable.columns else 0
price_max = df_viable["precio"].max() if "precio" in df_viable.columns else 0

dist_rec = df["recommendation"].value_counts()
strong_opp = dist_rec.get("strong_opportunity", 0)
worth_visit = dist_rec.get("worth_visit", 0)
price_only = dist_rec.get("price_only", 0)

top5 = df_viable.nlargest(5, "score_total")[["titulo", "precio", "score_total", "recommendation"]]

# PDF Setup
doc = SimpleDocTemplate(str(REPORT_PATH), pagesize=A4, topMargin=0.3*inch, bottomMargin=0.3*inch,
                       leftMargin=0.5*inch, rightMargin=0.5*inch)
styles = getSampleStyleSheet()
story = []

# Design System Colors (Luis Dotto Portfolio)
PRIMARY_BG = colors.HexColor("#f8f8f6")      # Blanco cálido
TEXT_PRIMARY = colors.HexColor("#1d1d1f")    # Negro Apple
TEXT_SECONDARY = colors.HexColor("#6e6e73")  # Muted
ACCENT = colors.HexColor("#193747")          # Azul marino
BORDER = colors.HexColor("#d2d2d7")          # Bordes delicados

# Styles
title_style = ParagraphStyle(
    'Title', parent=styles['Heading1'], fontSize=20, textColor=ACCENT,
    spaceAfter=1, alignment=TA_CENTER, fontName='Helvetica-Bold'
)
subtitle_style = ParagraphStyle(
    'Subtitle', parent=styles['Normal'], fontSize=9, textColor=TEXT_SECONDARY,
    spaceAfter=3, alignment=TA_CENTER
)
heading_style = ParagraphStyle(
    'Heading', parent=styles['Heading2'], fontSize=11, textColor=ACCENT,
    spaceAfter=2, spaceBefore=3, fontName='Helvetica-Bold'
)
body_style = ParagraphStyle(
    'Body', parent=styles['Normal'], fontSize=8, spaceAfter=3, leading=12, alignment=TA_JUSTIFY,
    textColor=TEXT_PRIMARY
)
small_style = ParagraphStyle(
    'Small', parent=styles['Normal'], fontSize=7, spaceAfter=1, textColor=TEXT_SECONDARY, alignment=TA_JUSTIFY
)
language_style = ParagraphStyle(
    'Language', parent=styles['Normal'], fontSize=6, spaceAfter=1, textColor=colors.HexColor("#aaaaaa"),
    alignment=TA_RIGHT, fontName='Helvetica'
)

# ─────────────────────────────────────────────────────────────────────────────
# PAGE 1: ENGLISH
# ─────────────────────────────────────────────────────────────────────────────

story.append(Paragraph("CASITAS", title_style))
story.append(Paragraph("Real Estate Investment Analysis — Malaga 2026", subtitle_style))
story.append(Paragraph("ENGLISH", language_style))
story.append(Spacer(1, 0.01*inch))

# Brief intro
intro = "Comprehensive analysis of 136 residential properties across Málaga using AI-powered composite scoring. This report identifies 97 viable investment targets across three opportunity tiers."
story.append(Paragraph(intro, small_style))
story.append(Spacer(1, 0.06*inch))

# SUMMARY (Quick Facts)
story.append(Paragraph("SUMMARY", heading_style))
story.append(Spacer(1, 0.02*inch))
summary_data = [
    ["Analyzed", f"{total_analyzed}", "Recommended", f"{total_recommended}", "Avg Price", f"EUR {avg_price:,.0f}"],
    ["Price Range", f"EUR {price_min:,.0f}—{price_max:,.0f}", "Strong Opp.", f"{strong_opp}", "Worth Visit", f"{worth_visit}"]
]
t_summary = Table(summary_data, colWidths=[0.9*inch, 1.2*inch, 0.9*inch, 0.7*inch, 0.9*inch, 1.0*inch])
t_summary.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, -1), PRIMARY_BG),
    ('TEXTCOLOR', (0, 0), (-1, -1), TEXT_PRIMARY),
    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
    ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),
    ('FONTSIZE', (0, 0), (-1, -1), 7),
    ('BOTTOMPADDING', (0, 0), (-1, -1), 3),
    ('TOPPADDING', (0, 0), (-1, -1), 3),
    ('GRID', (0, 0), (-1, -1), 0.5, BORDER),
    ('ROWBACKGROUNDS', (0, 0), (-1, -1), [PRIMARY_BG, PRIMARY_BG]),
]))
story.append(t_summary)
story.append(Spacer(1, 0.08*inch))

# ANALYSIS
story.append(Paragraph("ANALYSIS", heading_style))
story.append(Spacer(1, 0.02*inch))
analysis_intro = (
    "This report evaluates 136 residential properties across Málaga using a composite scoring model "
    "(Location 25%, Condition 25%, Distribution 20%, Financial 20%, Intangibles 10%). "
    "Properties are classified into three tiers: <b>Strong Opportunities</b> (score 85-100), "
    "<b>Worth Visiting</b> (70-84), and <b>Price Only</b> (60-69). Below is the opportunity distribution and price analysis."
)
story.append(Paragraph(analysis_intro, small_style))
story.append(Spacer(1, 0.005*inch))

# PIE CHART
rec_charts = sorted(glob.glob(str(DATA_OUTPUT / "graphic_recommendation_distribution_*.png")))
if rec_charts:
    img_rec = Image(rec_charts[-1], width=3.15*inch, height=3.15*inch)
    story.append(img_rec)
    story.append(Spacer(1, 0.005*inch))
    pie_explain = (
        "<b>Recommendation Breakdown:</b> Of 97 viable properties, 13% are strong opportunities with excellent fundamentals, "
        "69% warrant site visits with good potential, and 18% are price-driven plays requiring negotiation."
    )
    story.append(Paragraph(pie_explain, small_style))
    story.append(Spacer(1, 0.08*inch))

# BOX PLOT
box_charts = sorted(glob.glob(str(DATA_OUTPUT / "graphic_price_range_by_recommendation_*.png")))
if box_charts:
    img_box = Image(box_charts[-1], width=5.4*inch, height=2.45*inch)
    story.append(img_box)
    story.append(Spacer(1, 0.005*inch))
    box_explain = (
        "<b>Price Distribution by Tier:</b> Strong opportunities cluster around EUR 200K (tight range EUR 175K—245K), "
        "indicating consistent market pricing. Worth-Visit properties span EUR 100K—270K (broader range, more variation). "
        "Price-Only deals concentrate EUR 200K—225K with selective outliers."
    )
    story.append(Paragraph(box_explain, small_style))
    story.append(Spacer(1, 0.06*inch))

# PAGE BREAK
story.append(PageBreak())

# ─────────────────────────────────────────────────────────────────────────────
# PAGE 2: ENGLISH (FINDINGS)
# ─────────────────────────────────────────────────────────────────────────────

story.append(Paragraph("MARKET DISTRIBUTION", heading_style))
story.append(Spacer(1, 0.02*inch))
market_intro = (
    "The EUR/m² metric reveals market positioning. Strong opportunities average EUR 3,031/m² (competitive), "
    "while the overall market clusters EUR 2,500—3,500/m². The Score-vs-Price scatter visualizes ranking positions across price tiers."
)
story.append(Paragraph(market_intro, small_style))
story.append(Spacer(1, 0.02*inch))

# HISTOGRAM
hist_charts = sorted(glob.glob(str(DATA_OUTPUT / "graphic_price_per_sqm_histogram_*.png")))
if hist_charts:
    img_hist = Image(hist_charts[-1], width=4.5*inch, height=2.05*inch)
    story.append(img_hist)
    story.append(Spacer(1, 0.01*inch))
    hist_explain = (
        "<b>Market Baseline:</b> EUR/m² distribution reveals market positioning. Strong opportunities cluster around EUR 3,031/m², "
        "indicating competitive pricing. Overall market spans EUR 2,500—3,500/m²."
    )
    story.append(Paragraph(hist_explain, small_style))
    story.append(Spacer(1, 0.04*inch))

# SCATTER (larger, more emphasis)
score_charts = sorted(glob.glob(str(DATA_OUTPUT / "graphic_score-price_*.png")))
if score_charts:
    img_scatter = Image(score_charts[-1], width=5.2*inch, height=3.05*inch)
    story.append(img_scatter)
    story.append(Spacer(1, 0.01*inch))
    scatter_explain = (
        "<b>Investment Ranking:</b> Score-vs-Price visualization maps all 97 properties across the investment landscape. "
        "Green indicates strong opportunities, red requires caution, yellow represents price-driven plays. Threshold lines mark tier boundaries."
    )
    story.append(Paragraph(scatter_explain, small_style))
    story.append(Spacer(1, 0.06*inch))

# TOP 5 OPPORTUNITIES
story.append(Paragraph("TOP 5 OPPORTUNITIES", heading_style))
story.append(Spacer(1, 0.02*inch))
top5_data = [["Title", "Price (EUR)", "Score"]]
for idx, row in top5.iterrows():
    title_short = str(row["titulo"])[:30]
    top5_data.append([
        title_short,
        f"{row['precio']:,.0f}",
        f"{row['score_total']:.0f}"
    ])
t_top5 = Table(top5_data, colWidths=[2.8*inch, 1.1*inch, 0.7*inch])
t_top5.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), ACCENT),
    ('TEXTCOLOR', (0, 0), (-1, 0), PRIMARY_BG),
    ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
    ('ALIGN', (1, 0), (-1, -1), 'CENTER'),
    ('ALIGN', (2, 0), (-1, -1), 'CENTER'),
    ('TEXTCOLOR', (0, 1), (-1, -1), TEXT_PRIMARY),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('FONTSIZE', (0, 0), (-1, -1), 5),
    ('BOTTOMPADDING', (0, 0), (-1, -1), 1),
    ('TOPPADDING', (0, 0), (-1, -1), 1),
    ('GRID', (0, 0), (-1, -1), 0.5, BORDER),
    ('ROWBACKGROUNDS', (0, 1), (-1, -1), [PRIMARY_BG, PRIMARY_BG]),
]))
story.append(t_top5)
story.append(Spacer(1, 0.005*inch))

# KEY INSIGHTS
story.append(Paragraph("KEY INSIGHTS", heading_style))
insights_text = f"""
• <b>{total_recommended}/{total_analyzed}</b> properties are viable investment targets (score > 0, not discarded)<br/>
• <b>{strong_opp} strong opportunities</b> identified with price range EUR {price_min:,.0f}—EUR {price_max:,.0f}<br/>
• Market baseline: EUR {avg_price_per_sqm:,.0f}/m² | Analysis date: {datetime.now().strftime('%Y-%m-%d')}
"""
story.append(Paragraph(insights_text, body_style))
story.append(Spacer(1, 0.005*inch))

# METHODOLOGY
story.append(Paragraph("METHODOLOGY", heading_style))
story.append(Paragraph(
    "Scoring 0-100: Location (25%), Condition (25%), Distribution (20%), Financial (20%), Intangibles (10%). "
    "Recommended properties: score > 0 and not discarded. Analysis covers sales listings only (rentals excluded).",
    small_style
))
story.append(Spacer(1, 0.005*inch))
footer_text = "Disclaimer: This analysis is for investment research only. Consult professionals before deciding. | Analyst: Luis Dotto"
story.append(Paragraph(footer_text, small_style))

# ─────────────────────────────────────────────────────────────────────────────
# PAGE 3: SPANISH (Página 1 de resumen)
# ─────────────────────────────────────────────────────────────────────────────

story.append(PageBreak())

story.append(Paragraph("CASITAS", title_style))
story.append(Paragraph("Análisis de Inversión Inmobiliaria — Málaga 2026", subtitle_style))
story.append(Paragraph("ESPAÑOL", language_style))
story.append(Spacer(1, 0.01*inch))

# RESUMEN
story.append(Paragraph("RESUMEN", heading_style))
summary_data_es = [
    ["Analizadas", f"{total_analyzed}", "Recomendadas", f"{total_recommended}", "Precio medio", f"EUR {avg_price:,.0f}"],
    ["Rango Precio", f"EUR {price_min:,.0f}—{price_max:,.0f}", "Oportunidad", f"{strong_opp}", "Vale Visita", f"{worth_visit}"]
]
t_summary_es = Table(summary_data_es, colWidths=[0.9*inch, 1.2*inch, 0.9*inch, 0.7*inch, 0.9*inch, 1.0*inch])
t_summary_es.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, -1), PRIMARY_BG),
    ('TEXTCOLOR', (0, 0), (-1, -1), TEXT_PRIMARY),
    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
    ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),
    ('FONTSIZE', (0, 0), (-1, -1), 7),
    ('BOTTOMPADDING', (0, 0), (-1, -1), 3),
    ('TOPPADDING', (0, 0), (-1, -1), 3),
    ('GRID', (0, 0), (-1, -1), 0.5, BORDER),
    ('ROWBACKGROUNDS', (0, 0), (-1, -1), [PRIMARY_BG, PRIMARY_BG]),
]))
story.append(t_summary_es)
story.append(Spacer(1, 0.01*inch))

# ANALISIS
story.append(Paragraph("ANÁLISIS", heading_style))
analysis_intro_es = (
    "Este informe evalúa 136 propiedades residenciales en Málaga usando un modelo de scoring compuesto "
    "(Ubicación 25%, Condición 25%, Distribución 20%, Financiero 20%, Intangibles 10%). "
    "Las propiedades se clasifican en tres categorías: <b>Oportunidades Fuertes</b> (score 85-100), "
    "<b>Vale la Pena Visita</b> (70-84), y <b>Solo por Precio</b> (60-69). A continuación, análisis de distribución y precios."
)
story.append(Paragraph(analysis_intro_es, small_style))
story.append(Spacer(1, 0.005*inch))

# PIE CHART (Spanish)
if rec_charts:
    img_rec = Image(rec_charts[-1], width=3.15*inch, height=3.15*inch)
    story.append(img_rec)
    story.append(Spacer(1, 0.005*inch))
    pie_explain_es = (
        "<b>Distribución de Recomendaciones:</b> De 97 propiedades viables, 13% son oportunidades fuertes con fundamentales excelentes, "
        "69% merecen visitas en sitio con buen potencial, y 18% son oportunidades por precio que requieren negociación."
    )
    story.append(Paragraph(pie_explain_es, small_style))
    story.append(Spacer(1, 0.005*inch))

# BOX PLOT (Spanish)
if box_charts:
    img_box = Image(box_charts[-1], width=5.4*inch, height=2.45*inch)
    story.append(img_box)
    story.append(Spacer(1, 0.005*inch))
    box_explain_es = (
        "<b>Distribución de Precios por Categoría:</b> Las oportunidades fuertes se concentran alrededor EUR 200K (rango estrecho EUR 175K—245K), "
        "indicando consistencia de mercado. Las de visita varían EUR 100K—270K (rango amplio). "
        "Las de precio se concentran EUR 200K—225K con outliers selectivos."
    )
    story.append(Paragraph(box_explain_es, small_style))

# PAGE BREAK
story.append(PageBreak())

# ─────────────────────────────────────────────────────────────────────────────
# PAGE 4: SPANISH (Página 2 de findings)
# ─────────────────────────────────────────────────────────────────────────────

story.append(Paragraph("DISTRIBUCIÓN DE MERCADO", heading_style))
market_intro_es = (
    "La métrica EUR/m² revela posicionamiento en el mercado. Las oportunidades fuertes promedian EUR 3,031/m² (competitivo), "
    "mientras que el mercado general se concentra EUR 2,500—3,500/m². El gráfico Score-vs-Precio visualiza posiciones de ranking por rango de precio."
)
story.append(Paragraph(market_intro_es, small_style))
story.append(Spacer(1, 0.005*inch))

# HISTOGRAM (Spanish)
if hist_charts:
    img_hist = Image(hist_charts[-1], width=3.85*inch, height=1.75*inch)
    story.append(img_hist)
    story.append(Spacer(1, 0.005*inch))

# SCATTER (Spanish)
if score_charts:
    img_scatter = Image(score_charts[-1], width=3.85*inch, height=2.24*inch)
    story.append(img_scatter)
    story.append(Spacer(1, 0.005*inch))

# TOP 5 (Spanish)
story.append(Paragraph("TOP 5 OPORTUNIDADES", heading_style))
top5_data_es = [["Título", "Precio (EUR)", "Score"]]
for idx, row in top5.iterrows():
    title_short = str(row["titulo"])[:30]
    top5_data_es.append([
        title_short,
        f"{row['precio']:,.0f}",
        f"{row['score_total']:.0f}"
    ])
t_top5_es = Table(top5_data_es, colWidths=[2.8*inch, 1.1*inch, 0.7*inch])
t_top5_es.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), ACCENT),
    ('TEXTCOLOR', (0, 0), (-1, 0), PRIMARY_BG),
    ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
    ('ALIGN', (1, 0), (-1, -1), 'CENTER'),
    ('ALIGN', (2, 0), (-1, -1), 'CENTER'),
    ('TEXTCOLOR', (0, 1), (-1, -1), TEXT_PRIMARY),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('FONTSIZE', (0, 0), (-1, -1), 6),
    ('BOTTOMPADDING', (0, 0), (-1, -1), 2),
    ('TOPPADDING', (0, 0), (-1, -1), 2),
    ('GRID', (0, 0), (-1, -1), 0.5, BORDER),
    ('ROWBACKGROUNDS', (0, 1), (-1, -1), [PRIMARY_BG, PRIMARY_BG]),
]))
story.append(t_top5_es)
story.append(Spacer(1, 0.005*inch))

# HALLAZGOS CLAVE
story.append(Paragraph("HALLAZGOS CLAVE", heading_style))
insights_es = f"""
• <b>{total_recommended}/{total_analyzed}</b> propiedades son objetivos de inversión viables (score > 0, no descartadas)<br/>
• <b>{strong_opp} oportunidades fuertes</b> identificadas con rango de precio EUR {price_min:,.0f}—EUR {price_max:,.0f}<br/>
• Línea base de mercado: EUR {avg_price_per_sqm:,.0f}/m² | Fecha análisis: {datetime.now().strftime('%d-%m-%Y')}
"""
story.append(Paragraph(insights_es, body_style))
story.append(Spacer(1, 0.005*inch))

# METODOLOGÍA
story.append(Paragraph("METODOLOGÍA", heading_style))
story.append(Paragraph(
    "Scoring 0-100: Ubicación (25%), Condición (25%), Distribución (20%), Financiero (20%), Intangibles (10%). "
    "Propiedades recomendadas: score > 0 y no descartadas. Análisis cubre solo ventas (alquileres excluidos).",
    small_style
))
story.append(Spacer(1, 0.005*inch))
footer_es = "Descargo: Este análisis es solo para investigación de inversión. Consulta profesionales antes de decidir. | Analista: Luis Dotto"
story.append(Paragraph(footer_es, small_style))

# Build PDF
doc.build(story)
print(f"Report: {REPORT_PATH.name}")
print(f"Size: {REPORT_PATH.stat().st_size / 1024:.1f} KB")
print(f"Pages: 4 (2x English + 2x Spanish)")
