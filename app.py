import os
import sys
import pathlib
import streamlit as st

# 1. إعدادات المسارات البرمجية
current_dir = pathlib.Path(__file__).parent.resolve()
sys.path.insert(0, str(current_dir))

# 2. إعدادات الصفحة
st.set_page_config(
    page_title="DataLab | by Omar Saleh", 
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 3. CSS مخصص ومضبوط لعزل الاتجاهات
st.markdown("""
    <style>
    /* جعل عنوان الفولدر وسهم الفتح ناحيه الشمال LTR */
    .stStreamlitExpander > details > summary {
        direction: ltr !important;
        text-align: left !important;
        font-size: 16px !important;
        font-weight: 600 !important;
    }

    /* ضبط حاوية المنشور العربي من الداخل لتكون يمين RTL بنسبة 100% */
    .post-container {
        direction: rtl !important;
        text-align: right !important;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        font-size: 18px !important;
        line-height: 1.8 !important;
        padding: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# 4. الهيدر الرئيسي
st.markdown('<h1 style="text-align: center; color: #4A90E2;">⚡ DataLab | by Omar Saleh</h1>', unsafe_allow_html=True)
st.markdown('<p style="text-align: center; color: #888;" dir="rtl">بوابتك المرجعية المتكاملة لمجال الـ Data Science 🎯</p>', unsafe_allow_html=True)

# 5. القائمة الجانبية (Sidebar)
st.sidebar.title("🧭 القائمة الرئيسية")
menu_choice = st.sidebar.radio(
    "انتقل إلى:",
    [
        "🗺️ مسار التعلم الشامل (Roadmap)",
        "🐍 محرك بايثون التفاعلي (Python Engine)",
        "📚 مكتبة المراجع والكتب (Resources)",
        "🔒 معرض المشاريع الاحترافية (Portfolio Pro)"
    ]
)

# 6. عرض المحتوى والمنشورات
if menu_choice == "🗺️ مسار التعلم الشامل (Roadmap)":
    st.markdown("<h3 style='text-align: right; color: #4A90E2;'>🗺️ مسار التعلم الشامل لعلوم البيانات</h3>", unsafe_allow_html=True)

    try:
        import importlib.util

        roadmap_path = None
        for root, dirs, files in os.walk(str(current_dir)):
            for file in files:
                if file.lower() == "roadmap.py":
                    roadmap_path = pathlib.Path(root) / file
                    break
            if roadmap_path:
                break

        if roadmap_path and roadmap_path.exists():
            spec = importlib.util.spec_from_file_location("roadmap_data", roadmap_path)
            roadmap_module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(roadmap_module)

            phases = [
                ("Phase 01: Read: Understanding Data 📁", getattr(roadmap_module, "render_phase_1", None)),
                ("Phase 02: Read: Data Science Fundamentals 📁", getattr(roadmap_module, "render_phase_2", None)),
                ("Phase 03: Read: Think Like a Data Analyst 📁", getattr(roadmap_module, "render_phase_3", None)),
                ("Phase 04: Read: Data Ecosystem 📁", getattr(roadmap_module, "render_phase_4", None)),
                ("Phase 05: Read: Data Analytics Toolbox 📁", getattr(roadmap_module, "render_phase_5", None)),
                ("Phase 06: Read: Big Data Basics 📁", getattr(roadmap_module, "render_phase_6", None)),
                ("Phase 07: Read: Data Visualization & Storytelling 📁", getattr(roadmap_module, "render_phase_7", None)),
                ("Phase 08: Read: Machine Learning Fundamentals 📁", getattr(roadmap_module, "render_phase_8", None)),
                ("Phase 09: Read: Data Career Roadmap 📁", getattr(roadmap_module, "render_phase_9", None)),
                ("Phase 10: Read: Advanced Insights & Ethics 📁", getattr(roadmap_module, "render_phase_10", None)),
            ]

            for title, render_func in phases:
                with st.expander(title, expanded=False):
                    if render_func:
                        # غلاف محلي يجبر النص الداخلي على اليمين 100%
                        st.markdown('<div class="post-container">', unsafe_allow_html=True)
                        render_func()
                        st.markdown('</div>', unsafe_allow_html=True)
                    else:
                        st.warning("جاري إعداد محتوى هذه المرحلة...")
        else:
            st.error("لم يتم العثور على ملف roadmap.py!")

    except Exception as e:
        st.error(f"حدث خطأ أثناء تحميل المنشورات: {e}")
