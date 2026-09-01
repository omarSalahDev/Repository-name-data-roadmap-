import streamlit as st
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

# 4. توجيه الصفحات بأسلوب نظيف (Page Routing)
if page_selection == "🗺️ مسار التعلم (Roadmap)":
    # استدعاء صفحة الـ Roadmap
    try:
        from pages.roadmap import render_roadmap_page
        render_roadmap_page()
    except ImportError:
        st.subheader("🗺️ مسار التعلم الشامل للبيانات")
        st.info("صفحة المسار قيد الربط بالتطبيقات.")

elif page_selection == "🐍 تعلم Python (Lessons)":
    # استدعاء صفحة دروس بايثون
    try:
        from pages.python_lessons import render_python_tab
        render_python_tab()
    except ImportError:
        st.subheader("🐍 محرك تعلم Python التفاعلي")
        st.write("دروس وتحديات تفاعلية مصممة خصيصاً لتطوير مهاراتك البرمجية.")

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
