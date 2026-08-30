# -*- coding: utf-8 -*-
"""
app.py — Main entrypoint & landing page of the multi-page Streamlit app.

Pages (Streamlit auto-discovers pages/ and orders them by numeric prefix):
    app.py                          ← this landing page
    pages/1_Macro_Analysis.py       ← Daily Macro Pulse & Sector Fund Flows
    pages/2_Stock_Screener.py       ← Dynamic Aggressive-Movers Scanner
    pages/3_My_Portfolio.py         ← Personal Portfolio Manager
    pages/4_Company_Screener.py     ← Finviz-style Fundamental Screener
    pages/5_Company_Deep_Dive.py    ← Full-Market Company Research
    pages/6_Options_Scanner.py      ← Credit-Spread / IV Rank Scanner

This file only renders the landing experience: navigation cards and a light
live market snapshot. All heavy UI lives in components/, all quant logic in
analysis/, all data access in data/, and all cross-page chrome (language,
sidebar, RTL CSS, session state) in shared.py.

Run with:
    streamlit run app.py
"""

from __future__ import annotations

import numpy as np
import streamlit as st

import shared
from analysis import macro_signals
from data import macro_data
from i18n import h, instrument_name, t

lang = shared.init_page("Macro & Equity Analytics", "📊")

st.title(t("app_title", lang))
st.caption(t("app_caption", lang))

# --------------------------------------------------------------------------- #
# Navigation cards
# --------------------------------------------------------------------------- #
st.markdown(f"### {t('home_pages_header', lang)}")
st.caption(t("nav_hint", lang))

col_macro, col_scanner, col_screener2, col_portfolio = st.columns(4)

with col_macro:
    with st.container(border=True):
        st.markdown(f"#### {t('tab_macro', lang)}")
        st.write(t("home_macro_desc", lang))
        st.page_link(
            "pages/1_Macro_Analysis.py",
            label=t("open_macro", lang),
            icon="📊",
        )

with col_scanner:
    with st.container(border=True):
        st.markdown(f"#### {t('tab_scanner', lang)}")
        st.write(t("home_scanner_desc", lang))
        st.page_link(
            "pages/2_Stock_Screener.py",
            label=t("open_scanner", lang),
            icon="🔥",
        )
        st.page_link(
            "pages/6_Options_Scanner.py",
            label=t("open_options_scanner", lang),
            icon="🧮",
        )
        st.page_link(
            "pages/7_Options_Flow.py",
            label=t("open_flow", lang),
            icon="📊",
        )

with col_screener2:
    with st.container(border=True):
        st.markdown(f"#### {t('tab_screener2', lang)}")
        st.write(t("home_screener2_desc", lang))
        st.page_link(
            "pages/4_Company_Screener.py",
            label=t("open_screener2", lang),
            icon="🏢",
        )
        st.page_link(
            "pages/5_Company_Deep_Dive.py",
            label=t("deep_dive_title", lang),
            icon="🔎",
        )

with col_portfolio:
    with st.container(border=True):
        st.markdown(f"#### {t('tab_portfolio', lang)}")
        st.write(t("home_portfolio_desc", lang))
        st.page_link(
            "pages/3_My_Portfolio.py",
            label=t("open_portfolio", lang),
            icon="💼",
        )

# --------------------------------------------------------------------------- #
# Quick live snapshot (light: reuses the same 5-minute cache as page 1)
# --------------------------------------------------------------------------- #
st.divider()
st.markdown(f"### {t('home_snapshot_title', lang)}")

try:
    idx_data = macro_data.fetch_global_indices()
    vol_data = macro_data.fetch_volatility()
    sec_data = macro_data.fetch_sector_flows()

    snap_idx = macro_signals.performance_snapshot(idx_data)
    vix_info = macro_signals.volatility_regime(vol_data.get("^VIX"))
    flow = macro_signals.sector_flow_table(sec_data)
    pulse = macro_signals.macro_pulse(snap_idx, vix_info, flow)

    def _pct(x: float) -> str:
        if x is None or (isinstance(x, float) and np.isnan(x)):
            return "—"
        return f"{x * 100:+.2f}%"

    m1, m2, m3, m4, m5 = st.columns(5)

    m1.metric(
        t("pulse_gauge_title", lang),
        f"{pulse['score']:+.0f}",
        t(pulse["label_key"], lang),
        delta_color="off",
        help=h("h_pulse_score", lang),
    )

    for col, tk in ((m2, "^GSPC"), (m3, "^NDX")):
        if not snap_idx.empty and tk in snap_idx.index:
            row = snap_idx.loc[tk]
            col.metric(
                instrument_name(tk, lang),
                f"{row['price']:,.2f}",
                _pct(row["ret_1d"]),
                help=h("h_index_card", lang),
            )

    if vix_info:
        m4.metric(
            instrument_name("^VIX", lang),
            f"{vix_info['level']:.2f}",
            t(vix_info["regime_key"], lang),
            delta_color="off",
            help=h("h_vix", lang),
        )

    if not flow.empty:
        top = flow.iloc[0]
        m5.metric(
            t("top_inflow_label", lang),
            instrument_name(top.name, lang),
            _pct(top["ret_1d"]),
            help=h("h_top_inflow", lang),
        )
except Exception:  # snapshot is decorative — never block the landing page
    st.info(t("no_data", lang))
