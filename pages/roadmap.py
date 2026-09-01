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
