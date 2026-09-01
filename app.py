import os
import sys
import streamlit as st

# إجبار بايثون على قراءة المجلد الحالي كـ Root Directory
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from components.cards import render_header

# 1. إعدادات الصفحة الرئيسية
st.set_page_config(
    page_title="DataLab | by Omar Saleh", 
    page_icon="🧭",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. عرض الهيدر والوصف الرئيسي
render_header()

# 3. شريط التنقل الجانبي (Sidebar)
st.sidebar.title("🚀 DataLab")
st.sidebar.caption("منصتك التفاعلية لاحتراف بيانات المستقبل")

page_selection = st.sidebar.radio(
    "انتقل إلى:",
    [
        "🗺️ مسار التعلم (Roadmap)",
        "🐍 تعلم Python (Lessons)",
        "💼 معرض المشاريع (Portfolio)"
    ]
)

st.sidebar.markdown("---")
st.sidebar.info("💡 **تلميحة اليوم:** التطبيق العملي اليومي هو السلاح الحقيقي للوصول لسوق العمل.")

# 4. توجيه الصفحات
if page_selection == "🗺️ مسار التعلم (Roadmap)":
    st.subheader("🗺️ مسار التعلم الشامل للبيانات")
    st.write("اختر المرحلة التي تريد قراءتها وتطبيقها:")
    
    # استدعاء دالي مباشر من ملف data/roadmap.py
    try:
        from data.roadmap import (
            render_phase_1, render_phase_2, render_phase_3, render_phase_4, render_phase_5,
            render_phase_6, render_phase_7, render_phase_8, render_phase_9, render_phase_10
        )
        
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
                
    except Exception as e:
        st.error(f"حدث خطأ أثناء تحميل المراحل: {e}")

elif page_selection == "🐍 تعلم Python (Lessons)":
    st.subheader("🐍 محرك تعلم Python التفاعلي")
    st.write("دروس وتحديات تفاعلية مصممة خصيصاً لتطوير مهاراتك البرمجية (قيد التجهيز).")

elif page_selection == "💼 معرض المشاريع (Portfolio)":
    st.subheader("💼 بناء معرَض أعمالك (Portfolio Builder)")
    st.write("طبق ما تعلمته في مشاريع حقيقية وشاركها مباشرة.")

    with st.container():
        st.markdown("""
            <div dir="rtl" style="padding: 15px; border: 1px solid #333; border-radius: 10px; margin-bottom: 15px; background-color: rgba(255,255,255,0.02);">
            <h4 style="margin-bottom: 5px;">📊 Data Analysis Portfolio & Dashboards</h4>
            <p style="font-size: 13.5px; opacity: 0.85; line-height: 1.6;">
            مجموعة من التحليلات البرمجية ومشاريع أدوات تحليل البيانات (Excel, SQL, Power BI) المعروضة بشكل كامل على منصتي الشخصية وجيت هب.
            </p>
            </div>
            """, unsafe_allow_html=True)
        
        col_p1, col_p2 = st.columns(2)
        with col_p1:
            st.link_button("🌐 زيارة البورتفوليو الشامل", url="https://omarsalahdev.github.io/portfolio/")
        with col_p2:
            st.link_button("📂 تصفح أكواد GitHub", url="https://github.com/omarSalahDev")
