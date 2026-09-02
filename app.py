import streamlit as st

from core.config import configure_page
from core.styles import load_global_styles

# ============================================================
# DataLab — Application Entry Point
# ============================================================

# 1. Configure Streamlit
configure_page()

# 2. Load global visual system
load_global_styles()


# ============================================================
# DataLab — Header
# ============================================================

st.markdown(
    """
    <div class="datalab-title">
        ⚡ DataLab
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="datalab-subtitle" dir="rtl">
        <b>
            بوابتك المرجعية المتكاملة لعالم الـ Data
        </b>
        <br>
        مش مجرد مسار، دي رحلة بناء حقيقية بتبدأ من أدوات الـ Data Analysis،
        مرورًا ببايثون ومكتبات تحليل البيانات، وصولًا إلى الـ Machine Learning،
        مع تطبيقات ومشاريع عملية تساعدك تبني Portfolio قوي.
    </div>
    """,
    unsafe_allow_html=True,
)
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

st.sidebar.markdown("---")
st.sidebar.info("💡 **تلميحة اليوم:** التطبيق العملي اليومي هو السلاح الحقيقي للوصول لسوق العمل.")

# ---------------------------------------------------------
# 6. عرض المحتوى والـ 10 منشورات
# ---------------------------------------------------------

if menu_choice == "🗺️ مسار التعلم الشامل (Roadmap)":
    st.markdown("<h3 style='text-align: right; color: #4A90E2;' dir='rtl'>🗺️ مسار التعلم الشامل لعلوم البيانات</h3>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: right; color: #888;' dir='rtl'>اضغط على أي مرحلة لفتح الشرح المباشر وتتبع باقي المحطات خطوة بخطوة:</p>", unsafe_allow_html=True)

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
                ("Phase 10: Read: Advanced Insights & Data Ethics 📁", getattr(roadmap_module, "render_phase_10", None)),
            ]

            for title, render_func in phases:
                with st.expander(title, expanded=False):
                    if render_func:
                        st.markdown('<div class="arabic-content" dir="rtl">', unsafe_allow_html=True)
                        render_func()
                        st.markdown('</div>', unsafe_allow_html=True)
                    else:
                        st.warning("جاري إعداد محتوى هذه المرحلة...")
        else:
            st.error("لم يتم العثور على ملف roadmap.py!")

    except Exception as e:
        st.error(f"حدث خطأ أثناء تحميل المنشورات: {e}")

elif menu_choice == "🐍 محرك بايثون التفاعلي (Python Engine)":
    st.subheader("🐍 محرك تطبيق Python التفاعلي")
    default_code = "# اكتب كود بايثون هنا\nprint('Welcome to DataLab Engine by Omar Saleh!')"
    user_code = st.text_area("محرر الأكواد:", value=default_code, height=180)
    
    if st.button("▶️ تشغيل الكود"):
        try:
            import sys, io
            buffer = io.StringIO()
            sys.stdout = buffer
            exec(user_code)
            sys.stdout = sys.__stdout__
            st.code(buffer.getvalue(), language="text")
        except Exception as e:
            st.error(f"خطأ في الكود: {e}")

elif menu_choice == "📚 مكتبة المراجع والكتب (Resources)":
    st.subheader("📚 مكتبة المراجع والكتب")
    st.write("* **Python for Data Analysis** - Wes McKinney")
    st.write("* **Hands-On Machine Learning** - Aurélien Géron")

elif menu_choice == "🔒 معرض المشاريع الاحترافية (Portfolio Pro)":
    st.subheader("💼 معرض المشاريع والتطبيقات العملية")
    passcode = st.text_input("أدخل رمز الاشتراك لفتح مشاريع VIP:", type="password")
    if passcode == "omar2026":
        st.success("تم تفعيل اشتراكك بنجاح!")
        st.write("🚀 **Project Pro 1:** بناء نموذج ذكاء اصطناعي للتنبؤ بأسعار العقارات.")
