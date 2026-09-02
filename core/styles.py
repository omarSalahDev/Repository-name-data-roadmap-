import streamlit as st

from core.constants import (
    PRIMARY_COLOR,
    SUCCESS_COLOR,
    WARNING_COLOR,
    ERROR_COLOR,
    BACKGROUND_COLOR,
    SURFACE_COLOR,
    BORDER_COLOR,
)


# ============================================================
# DataLab — Global Styles
# ============================================================

def load_global_styles():
    """Load the global visual system for DataLab."""

    st.markdown(
        f"""
        <style>

        /* =====================================================
           Global
        ===================================================== */

        html, body, [class*="css"] {{
            font-family: "Segoe UI", Tahoma, Geneva, Verdana, sans-serif;
        }}

        .stApp {{
            background-color: {BACKGROUND_COLOR};
        }}


        /* =====================================================
           Main Container
           ===================================================== */

        .block-container {{
            max-width: 1200px;
            padding-top: 2rem;
            padding-bottom: 3rem;
        }}


        /* =====================================================
           Typography
           ===================================================== */

        .datalab-title {{
            font-size: 36px;
            font-weight: 800;
            color: {PRIMARY_COLOR};
            text-align: center;
            margin-bottom: 8px;
        }}

        .datalab-subtitle {{
            font-size: 15px;
            line-height: 1.8;
            opacity: 0.85;
            text-align: center;
            margin-bottom: 30px;
        }}


        /* =====================================================
           RTL Content
           ===================================================== */

        .rtl-content {{
            direction: rtl;
            text-align: right;
        }}

        .rtl-content * {{
            direction: rtl;
            text-align: right;
        }}


        /* =====================================================
           Cards
           ===================================================== */

        .datalab-card {{
            background: {SURFACE_COLOR};
            border: 1px solid {BORDER_COLOR};
            border-radius: 14px;
            padding: 20px;
            margin-bottom: 16px;
        }}


        /* =====================================================
           Buttons
           ===================================================== */

        .stButton > button {{
            width: 100%;
            border-radius: 10px;
            font-weight: 600;
        }}


        /* =====================================================
           Expanders
           ===================================================== */

        [data-testid="stExpander"] {{
            border: 1px solid {BORDER_COLOR};
            border-radius: 12px;
            margin-bottom: 12px;
        }}

        [data-testid="stExpander"] summary {{
            font-weight: 600;
        }}


        /* =====================================================
           Sidebar
           ===================================================== */

        [data-testid="stSidebar"] {{
            border-right: 1px solid {BORDER_COLOR};
        }}


        /* =====================================================
           Links
           ===================================================== */

        a {{
            color: {PRIMARY_COLOR} !important;
        }}

        </style>
        """,
        unsafe_allow_html=True,
    )
