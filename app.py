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

# 3. حقن التنسيقات الذكية لعزل المشاكل
st.markdown("""
    <style>
    /* 1. ضبط هيدر المنصة */
    .main-header { font-size: 34px; font-weight: 800; color: #4A90E2; text-align: center; }
    .sub-header { font-size: 15px; opacity: 0.85; text-align: center; margin-bottom: 25px; line-height: 1.6; }

    /* 2. جعل الفولدرات وسهم الفتح LTR على الشمال بدون خطوط مشوهة */
    .stStreamlitExpander > details > summary {
        direction: ltr !important;
        text-align: left !important;
        background-color: #0E1117 !important;
        border-radius: 8px !important;
        font-size: 16px !important;
        font-weight: bold !important;
    }

    .stStreamlitExpander {
        border: 1px solid #262730 !important;
        border-radius: 8px !important;
        margin-bottom: 12px !important;
        box-shadow: 0 4px 6px rgba(0,0,0,0.2);
    }

    /* 3. إجبار كافة النصوص والفقرات والعناوين داخل المنشور على الاتجاه الأيمن (RTL) */
    [data-testid="stExpanderDetails"] {
        direction: rtl !important;
        text-align: right !important;
    }

    [data-testid="stExpanderDetails"] *, 
    .arabic-content, 
    .arabic-content p, 
    .arabic-content h1, 
    .arabic-content h2, 
    .arabic-content h3, 
    .arabic-content div {
        direction: rtl !important;
        text-align: right !important;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif !important;
    }

    /* 4. زر تشغيل الكود */
    .stButton>button {
        width: 100%;
        background-color: #FF4B4B;
        color: white;
        border-radius: 8px;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# 4. الهيدر الرئيسي للمنصة
st.markdown('<div class="main-header">⚡ DataLab | by Omar Saleh</div>', unsafe_allow_html=True)
st.markdown("""
    <div class="sub-header" dir="rtl">
    <b>بوابتك المرجعية المتكاملة لمجال الـ Data Scientist ( مفتوحة ومجانية بالكامل ) </b><br>
    مش مجرد مسار، دي رحلة بناء حقيقية بتبدأ من أدوات الـ Data Analysis، مروراً بمكتبات الـ Python والرياضة، وصولاً لخوارزميات الـ Machine Learning.. بمشاريع عملية تتدرج معاك لحد ما تبني أقوى Portfolio و CV ينافس في السوق ✨
    </div>
""", unsafe_allow_html=True)

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
