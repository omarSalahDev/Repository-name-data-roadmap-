import os
import sys
import pathlib
import streamlit as st

# 1. إعدادات المسارات البرمجية
current_dir = pathlib.Path(__file__).parent.resolve()
sys.path.insert(0, str(current_dir))

# 2. إعدادات الصفحة والتصميم
st.set_page_config(
    page_title="DataLab | by Omar Saleh", 
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# تنسيق الجمالي للمنصة
st.markdown("""
    <style>
    .main-header { font-size: 32px; font-weight: bold; color: #4A90E2; text-align: center; }
    .sub-header { font-size: 16px; opacity: 0.8; text-align: center; margin-bottom: 25px; }
    </style>
""", unsafe_allow_html=True)

# 3. الهيدر الرئيسي
st.markdown('<div class="main-header">⚡ DataLab | by Omar Saleh</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">بوابتك التفاعلية المتكاملة لاحتراف عالم البيانات من الصفر حتى سوق العمل 🚀</div>', unsafe_allow_html=True)

# 4. القائمة الجانبية (Sidebar)
st.sidebar.title("🧭 القائمة الرئيسية")
menu_choice = st.sidebar.radio(
    "اختر القسم:",
    [
        "🗺️ مسار التعلم الشامل (Roadmap)",
        "🐍 محرك بايثون التفاعلي (Python Engine)",
        "📚 مكتبة المراجع والكتب (Resources)",
        "🔒 معرض المشاريع الاحترافية (Portfolio Pro)"
    ]
)

st.sidebar.markdown("---")
st.sidebar.info("💡 **DataLab:** المنصة مصممة لتأهيلك كاملاً لسوق العمل بالتطبيق العملي.")

# ---------------------------------------------------------
# 5. عرض المحتوى الحقيقي للمنشورات
# ---------------------------------------------------------

if menu_choice == "🗺️ مسار التعلم الشامل (Roadmap)":
    st.subheader("🗺️ مسار التعلم الشامل لعلوم البيانات")
    st.write("إليك الـ 10 مراحل الأساسية بالمنشورات الشاملة المكتوبة بالكامل:")

    # استدعاء منشوراتك الـ 10 الحقيقية بأمان من ملف data/roadmap.py
    try:
        import importlib.util
        
        # البحث عن ملف roadmap.py سواء كان داخل data/ أو بجانب app.py مباشرة
        possible_paths = [
            current_dir / "data" / "roadmap.py",
            current_dir / "roadmap.py"
        ]
        
        roadmap_path = next((p for p in possible_paths if p.exists()), None)
        
        if roadmap_path:
            spec = importlib.util.spec_from_file_location("roadmap_data", roadmap_path)
            roadmap_module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(roadmap_module)

            # قائمة المراحل الـ 10 مع ربطها بالدوال الحقيقية للمنشورات
            phases = [
                ("Phase 01: Introduction & Mindset", getattr(roadmap_module, "render_phase_1", None)),
                ("Phase 02: Data Gathering & Sources", getattr(roadmap_module, "render_phase_2", None)),
                ("Phase 03: Data Cleaning & Preprocessing", getattr(roadmap_module, "render_phase_3", None)),
                ("Phase 04: Exploratory Data Analysis (EDA)", getattr(roadmap_module, "render_phase_4", None)),
                ("Phase 05: SQL & Relational Databases", getattr(roadmap_module, "render_phase_5", None)),
                ("Phase 06: Big Data Basics", getattr(roadmap_module, "render_phase_6", None)),
                ("Phase 07: Data Visualization & Storytelling", getattr(roadmap_module, "render_phase_7", None)),
                ("Phase 08: Machine Learning Fundamentals", getattr(roadmap_module, "render_phase_8", None)),
                ("Phase 09: Data Career Roadmap", getattr(roadmap_module, "render_phase_9", None)),
                ("Phase 10: Advanced Insights & Data Ethics", getattr(roadmap_module, "render_phase_10", None)),
            ]

            for title, render_func in phases:
                with st.expander(f"📁 {title} (اضغط لقراءة المنشور كاملاً)", expanded=False):
                    if render_func:
                        render_func()
                    else:
                        st.warning("جاري تحميل المحتوى التفصيلي لهذه المرحلة...")
        else:
            st.error("تأكد من وجود ملف roadmap.py داخل مجلد data أو بجانب app.py")

    except Exception as e:
        st.error(f"حدث خطأ أثناء عرض المنشورات: {e}")


elif menu_choice == "🐍 محرك بايثون التفاعلي (Python Engine)":
    st.subheader("🐍 محرك تطبيق Python التفاعلي")
    st.write("اكتب كود بايثون جربه مباشرة داخل المنصة بدون الحاجة لتثبيت أي برامج!")
    
    default_code = "# اكتب كود بايثون هنا\nimport pandas as pd\nimport numpy as np\n\nprint('Welcome to DataLab Engine!')"
    user_code = st.text_area("محرر الأكواد:", value=default_code, height=180)
    
    if st.button("▶️ تشغيل الكود"):
        st.subheader("النتيجة (Output):")
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
    st.subheader("📚 مكتبة المراجع الموصى بها")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        #### 📖 كتب أساسية
        * **Python for Data Analysis** - Wes McKinney
        * **Hands-On Machine Learning** - Aurélien Géron
        """)
    with col2:
        st.markdown("""
        #### 🔗 روابط وأدوات
        * [Kaggle Datasets](https://www.kaggle.com)
        * [Pandas Documentation](https://pandas.pydata.org)
        """)


elif menu_choice == "🔒 معرض المشاريع الاحترافية (Portfolio Pro)":
    st.subheader("💼 معرض المشاريع والتطبيقات العملية")
    tab1, tab2 = st.tabs(["🔓 مشاريع مجانية", "🔒 مشاريع VIP الاحترافية"])
    
    with tab1:
        st.success("هذه المشاريع متاحة لجميع طلاب DataLab:")
        st.write("1. مشروع تحليل مبيعات متجر إلكتروني (Excel & Power BI)")
        st.write("2. مشروع استكشاف بيانات كورونا (Python EDA)")
        
    with tab2:
        st.warning("🔒 هذا القسم مخصص للمشاريع المتقدمة الكبيرة (المدفوعة).")
        passcode = st.text_input("أدخل رمز الاشتراك للفتح (Passcode):", type="password")
        if passcode == "omar2026":
            st.success("تم تفعيل اشتراكك بنجاح!")
            st.write("🚀 **Project Pro 1:** بناء نموذج ذكاء اصطناعي للتنبؤ بأسعار العقارات.")
        elif passcode:
            st.error("رمز الاشتراك غير صحيح.")
