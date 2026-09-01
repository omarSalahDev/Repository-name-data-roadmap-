import streamlit as st
import sys
from pathlib import Path

# ضبط المسار الرئيسي للمشروع لمنع أخطاء الـ Imports
sys.path.append(str(Path(__file__).resolve().parent))

from components.cards import render_header

# 1. إعدادات الصفحة
st.set_page_config(
    page_title="DataLab | by Omar Saleh", 
    page_icon="🧭",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. عرض الهيدر
render_header()

# 3. شريط التنقل الجانبي
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

# 4. توجيه الصفحات بأسلوب نظيف وحقيقي
if page_selection == "🗺️ مسار التعلم (Roadmap)":
    from views.roadmap import render_roadmap_page
    render_roadmap_page()

elif page_selection == "🐍 تعلم Python (Lessons)":
    from views.python_lessons import render_python_tab
    render_python_tab()

elif page_selection == "💼 معرض المشاريع (Portfolio)":
    st.subheader("💼 بناء معرَض أعمالك (Portfolio Builder)")
    st.write("طبق ما تعلمته في مشاريع حقيقية وشاركها مباشرة.")

    st.markdown("""
        <div dir="rtl" style="text-align: center; padding: 20px 10px;">
        <h3>💼 Featured Projects & Prototypes</h3>
        <p style="opacity: 0.8; font-size: 14px;">أبرز المشاريع التقنية والحلول اللي ببنيها في رحلتي لعالم البيانات:</p>
        </div>
        """, unsafe_allow_html=True)

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
