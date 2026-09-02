import streamlit as st


# ============================================================
# DataLab — Application Configuration
# ============================================================

APP_NAME = "DataLab"
AUTHOR = "Omar Saleh"
VERSION = "1.0.0"

PAGE_TITLE = "DataLab | Learn • Build • Grow"
PAGE_ICON = "⚡"

LAYOUT = "wide"
SIDEBAR_STATE = "expanded"


def configure_page():
    """Configure Streamlit page settings."""

    st.set_page_config(
        page_title=PAGE_TITLE,
        page_icon=PAGE_ICON,
        layout=LAYOUT,
        initial_sidebar_state=SIDEBAR_STATE,
    )
