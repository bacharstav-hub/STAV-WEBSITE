# -*- coding: utf-8 -*-
"""
shared.py — Cross-page chrome & global state for the multi-page app.

Every page (app.py and everything under pages/) must call init_page() as its
FIRST Streamlit interaction. It guarantees identical behavior everywhere:

    * st.set_page_config (must be the first Streamlit call on each page)
    * global session state (language, last-refresh timestamp)
    * the shared sidebar (language switcher, cache refresh, disclaimer)
    * base CSS + RTL stylesheet when Hebrew is active

Language survives page navigation because it lives in st.session_state and the
same widget key ("lang_choice") is re-registered on every page run.
"""

from __future__ import annotations

import logging
import os
from datetime import datetime

import streamlit as st

from i18n import BASE_CSS, LANGUAGES, RTL_CSS, is_rtl, t

logger = logging.getLogger(__name__)

_CODE_TO_LABEL = {code: label for label, code in LANGUAGES.items()}

# Show tracebacks in the UI only when explicitly opted in (local dev).
# In production this stays off so raw stack traces never reach the client.
_DEBUG = os.environ.get("APP_DEBUG", "").strip().lower() in ("1", "true", "yes")


def init_page(page_title: str, page_icon: str) -> str:
    """
    Standard page bootstrap. Returns the active language code ('en' / 'he').

    Call this before any other Streamlit command on the page.
    """
    st.set_page_config(
        page_title=page_title,
        page_icon=page_icon,
        layout="wide",
        initial_sidebar_state="expanded",
    )
    _ensure_state()
    lang = _render_sidebar()

    st.markdown(BASE_CSS, unsafe_allow_html=True)
    if is_rtl(lang):
        st.markdown(RTL_CSS, unsafe_allow_html=True)
    return lang


def _ensure_state() -> None:
    if "lang" not in st.session_state:
        st.session_state.lang = "en"
    if "last_refresh" not in st.session_state:
        st.session_state.last_refresh = datetime.now()


def _render_sidebar() -> str:
    with st.sidebar:
        # Re-seed the widget key if Streamlit dropped it during navigation,
        # so the chosen language always survives page switches.
        if "lang_choice" not in st.session_state:
            st.session_state.lang_choice = _CODE_TO_LABEL.get(
                st.session_state.lang, "English"
            )
        choice = st.radio(
            "🌐 " + t("language_label", st.session_state.lang),
            options=list(LANGUAGES.keys()),
            key="lang_choice",
        )
        st.session_state.lang = LANGUAGES[choice]
        lang = st.session_state.lang

        st.divider()
        if st.button("🔄 " + t("refresh_button", lang), width="stretch"):
            st.cache_data.clear()
            st.session_state.last_refresh = datetime.now()
            st.rerun()

        st.caption(
            f"{t('last_updated', lang)}: "
            f"{st.session_state.last_refresh.strftime('%Y-%m-%d %H:%M:%S')}"
        )
        st.divider()
        st.caption(t("disclaimer", lang))
    return lang


def render_page_error(exc: Exception, lang: str) -> None:
    """
    Uniform error surface. The full traceback is logged SERVER-SIDE only; the
    client sees a friendly message. Set APP_DEBUG=1 (local dev) to reveal the
    traceback in the UI — it is never shown in production.
    """
    logger.exception("Page render failed: %s", exc)
    st.error(t("data_error", lang))
    if _DEBUG:
        with st.expander("Debug (APP_DEBUG)"):
            st.exception(exc)
