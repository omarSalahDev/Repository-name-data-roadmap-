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

# 3. الهيدر الرئيسي
st.markdown('<h1 style="text-align: center; color: #4A90E2;">⚡ DataLab | by Omar Saleh</h1>', unsafe_allow_html=True)
st.markdown('<p style="text-align: center; opacity: 0.8;">بوابتك التفاعلية المتكاملة لاحتراف عالم البيانات من الصفر حتى سوق العمل 🚀</p>', unsafe_allow_html=True)

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
st.sidebar.info("💡 **DataLab:** التطبيق العملي اليومي هو السلاح الحقيقي للوصول لسوق العمل.")

# ---------------------------------------------------------
# 5. عرض المحتوى وقراءة ملف roadmap.py
# ---------------------------------------------------------

if menu_choice == "🗺️ مسار التعلم الشامل (Roadmap)":
    st.subheader("🗺️ مسار التعلم الشامل لعلوم البيانات")
    st.write("إليك الـ 10 مراحل الأساسية بالمنشورات الشاملة المكتوبة بالكامل:")

    try:
        import importlib.util

        # البحث الذكي عن مكان ملف roadmap.py
        roadmap_path = None
        
        # تفتيش كل الملفات والمجلدات في المشروع لمعرفة مسار roadmap.py بالضبط
        for root, dirs, files in os.walk(str(current_dir)):
            for file in files:
                if file.lower() == "roadmap.py":
                    roadmap_path = pathlib.Path(root) / file
                    break
            if roadmap_path:
                break

        if roadmap_path and roadmap_path.exists():
            # تحميل الملف ديناميكياً
            spec = importlib.util.spec_from_file_location("roadmap_data", roadmap_path)
            roadmap_module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(roadmap_module)

            # المراحل الـ 10
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
                        st.warning("الدالة الخاصة بهذه المرحلة غير معرفة داخل الملف.")
        else:
            st.error("⚠️ لم يتم العثور على ملف roadmap.py في مشروعك على GitHub!")
            st.info("تأكد أن الملف مرفوع على GitHub باسم roadmap.py وليس باسم آخر.")

    except Exception as e:
        st.error(f"حدث خطأ أثناء تحميل المنشورات: {e}")


elif menu_choice == "🐍 محرك بايثون التفاعلي (Python Engine)":
    st.subheader("🐍 محرك تطبيق Python التفاعلي")
    default_code = "print('Welcome to DataLab Engine by Omar Saleh!')"
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
    st.subheader("📚 مكتبة المراجع الموصى بها")
    st.write("* **Python for Data Analysis** - Wes McKinney")
    st.write("* **Hands-On Machine Learning** - Aurélien Géron")


elif menu_choice == "🔒 معرض المشاريع الاحترافية (Portfolio Pro)":
    st.subheader("💼 معرض المشاريع والتطبيقات العملية")
    passcode = st.text_input("أدخل رمز الاشتراك لفتح مشاريع VIP:", type="password")
    if passcode == "omar2026":
        st.success("تم تفعيل اشتراكك بنجاح!")
        st.write("🚀 **Project Pro 1:** بناء نموذج ذكاء اصطناعي للتنبؤ بأسعار العقارات.")
