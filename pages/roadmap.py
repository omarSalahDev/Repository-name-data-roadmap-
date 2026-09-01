import streamlit as st
from data.roadmap import get_roadmap_phases, render_phase_1_content

def render_roadmap_page():
    """عرض صفحة خريطة الطريق الكاملة"""
    
    st.title("🗺️ مسار التعلم الشامل للبيانات")
    st.caption("تعرف على المفاهيم والخطوات الأساسية لبناء مسارك المهني في عالم البيانات.")
    st.markdown("---")
    
    phase_1 = get_roadmap_phases()
    
    # 1. عرض المرحلة الأولى
    with st.expander(f"📁 {phase_1['title']} (اضغط للقراءة الكاملة)", expanded=False):
        render_phase_1_content()
