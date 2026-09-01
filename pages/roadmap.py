import streamlit as st
from data.roadmap import render_phase_1

def render_roadmap_page():
    """صفحة مسار التعلم الشاملة"""
    st.title("🗺️ مسار التعلم الشامل للبيانات")
    st.caption("تعرف على المفاهيم والخطوات الأساسية لبناء مسارك المهني في عالم البيانات.")
    st.markdown("---")
    
    # --- Phase 01 ---
    with st.expander("📁 Phase 01: Read: Understanding Data (اضغط للقراءة الكاملة)", expanded=False):
        render_phase_1()

# --- Phase 02 ---
    with st.expander("📁 Phase 02: Read: Data Science Fundamentals (اضغط للقراءة الكاملة)", expanded=False):
        from data.roadmap import render_phase_2
        render_phase_2()

# --- Phase 03 ---
    with st.expander("📁 Phase 03: Read: Think Like a Data Analyst (اضغط للقراءة الكاملة)", expanded=False):
        from data.roadmap import render_phase_3
        render_phase_3()

# --- Phase 04 ---
    with st.expander("📁 Phase 04: Read: Data Ecosystem (اضغط للقراءة الكاملة)", expanded=False):
        from data.roadmap import render_phase_4
        render_phase_4()

# --- Phase 05 ---
    with st.expander("📁 Phase 05: Read: Data Analytics Toolbox (اضغط للقراءة الكاملة)", expanded=False):
        from data.roadmap import render_phase_5
        render_phase_5()
