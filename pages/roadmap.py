import streamlit as st
import sys
from pathlib import Path

# إضافة المسار الرئيسي للمشروع
sys.path.append(str(Path(__file__).resolve().parent.parent))

from data.roadmap import (
    render_phase_1, render_phase_2, render_phase_3, render_phase_4, render_phase_5,
    render_phase_6, render_phase_7, render_phase_8, render_phase_9, render_phase_10
)

def render_roadmap_page():
    st.subheader("🗺️ مسار التعلم الشامل للبيانات")
    st.write("اختر المرحلة التي تريد قراءتها وتطبيقها:")
    
    phases = [
        ("Phase 01: Introduction & Mindset", render_phase_1),
        ("Phase 02: Data Gathering & Sources", render_phase_2),
        ("Phase 03: Data Cleaning & Preprocessing", render_phase_3),
        ("Phase 04: Exploratory Data Analysis (EDA)", render_phase_4),
        ("Phase 05: SQL & Relational Databases", render_phase_5),
        ("Phase 06: Big Data Basics", render_phase_6),
        ("Phase 07: Data Visualization & Storytelling", render_phase_7),
        ("Phase 08: Machine Learning Fundamentals", render_phase_8),
        ("Phase 09: Data Career Roadmap", render_phase_9),
        ("Phase 10: Advanced Insights & Data Ethics (Bonus)", render_phase_10)
    ]
    
    for title, render_func in phases:
        with st.expander(f"📁 {title} (اضغط للقراءة الكاملة)", expanded=False):
            render_func()
