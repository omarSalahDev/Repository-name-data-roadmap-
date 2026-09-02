import streamlit as st


APP_NAME = "DataLab"

AUTHOR = "Omar Saleh"

VERSION = "1.0.0"

PAGE_TITLE = "DataLab | Learn • Build • Grow"

PAGE_ICON = "⚡"

LAYOUT = "wide"

SIDEBAR = "expanded"


def configure_page():
    st.set_page_config(
        page_title=PAGE_TITLE,
        page_icon=PAGE_ICON,
        layout=LAYOUT,
        initial_sidebar_state=SIDEBAR,
    )
