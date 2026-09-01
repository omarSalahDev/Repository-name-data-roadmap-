import streamlit as st

# 1. إعدادات الصفحة والتصميم
st.set_page_config(
    page_title="DataLab | by Omar Saleh", 
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# تنسيق CSS مخصص لجعل المنصة تبدو كمنصة تعليمية احترافية
st.markdown("""
    <style>
    .main-header { font-size: 32px; font-weight: bold; color: #4A90E2; text-align: center; }
    .sub-header { font-size: 16px; opacity: 0.8; text-align: center; margin-bottom: 25px; }
    .pro-badge { background-color: #FF4B4B; color: white; padding: 2px 8px; border-radius: 5px; font-size: 12px; }
    </style>
""", unsafe_allow_html=True)

# 2. الهيدر الرئيسي للمنصة
st.markdown('<div class="main-header">⚡ DataLab | by Omar Saleh</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">بوابتك التفاعلية المتكاملة لاحتراف عالم البيانات من الصفر حتى سوق العمل 🚀</div>', unsafe_allow_html=True)

# 3. القائمة الجانبية (Sidebar)
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
# 4. الأقسام والمحتوى
# ---------------------------------------------------------

# === القسم الأول: مسار التعلم الشامل ===
if menu_choice == "🗺️ مسار التعلم الشامل (Roadmap)":
    st.subheader("🗺️ مسار التعلم الشامل لعلوم البيانات")
    st.write("إليك الـ 10 مراحل الأساسية المكتوبة خصيصاً لتغطية الجانب النظري والعملي:")

    # هيدر المراحل (يمكن استدعاء الدوال الخاصة بك هنا أو وضع المحتوى مباشر)
    with st.expander("📁 Phase 01: Introduction & Mindset"):
        st.markdown("""
        ### مرحباً بك في رحلة عالم البيانات
        في هذه المرحلة الأولى، ستتعلم مفهوم البيانات، أهمية التفكير التحليلي، وكيف تجهز شغفك للرحلة.
        """)
        
    with st.expander("📁 Phase 02: Data Gathering & Sources"):
        st.markdown("### جمع البيانات ومصادرها المتنوعة (Web Scraping, APIs, Databases)")

    with st.expander("📁 Phase 03: Data Cleaning & Preprocessing"):
        st.markdown("### تنظيف البيانات ومعالجة القيم المفقودة (Data Wrangling)")

    with st.expander("📁 Phase 04: Exploratory Data Analysis (EDA)"):
        st.markdown("### الاستكشاف التحليلي للبيانات وفهم الأنماط")

    with st.expander("📁 Phase 05: SQL & Relational Databases"):
        st.markdown("### قواعد البيانات وكتبابة الاستعلامات المعقدة")

    with st.expander("📁 Phase 06: Big Data Basics"):
        st.markdown("### أساسيات التعامل مع البيانات الضخمة")

    with st.expander("📁 Phase 07: Data Visualization & Storytelling"):
        st.markdown("### تمثيل البيانات وسرد القصص الرقمية")

    with st.expander("📁 Phase 08: Machine Learning Fundamentals"):
        st.markdown("### أساسيات وتعلم الآلة والخوارزميات")

    with st.expander("📁 Phase 09: Data Career Roadmap"):
        st.markdown("### خريطة الطريق المهنية وتجهيز السيرة الذاتية")

    with st.expander("📁 Phase 10: Advanced Insights & Data Ethics"):
        st.markdown("### أخلاقيات البيانات ورؤى مستقبليّة متقدمة")


# === القسم الثاني: محرك بايثون التفاعلي ===
elif menu_choice == "🐍 محرك بايثون التفاعلي (Python Engine)":
    st.subheader("🐍 محرك تطبيق Python التفاعلي")
    st.write("اكتب كود بايثون جربه مباشرة داخل المنصة بدون الحاجة لتثبيت أي برامج!")
    
    default_code = "# اكتب كود بايثون هنا\nname = 'DataLab'\nprint(f'Welcome to {name} by Omar Saleh!')"
    user_code = st.text_area("محرر الأكواد:", value=default_code, height=180)
    
    if st.button("▶️ تشغيل الكود"):
        st.subheader("النتيجة (Output):")
        try:
            # تشغيل الأكواد بشكل مباشر وآمن
            import sys, io
            buffer = io.StringIO()
            sys.stdout = buffer
            exec(user_code)
            sys.stdout = sys.__stdout__
            st.code(buffer.getvalue(), language="text")
        except Exception as e:
            st.error(f"خطأ في الكود: {e}")


# === القسم الثالث: مكتبة المراجع والكتب ===
elif menu_choice == "📚 مكتبة المراجع والكتب (Resources)":
    st.subheader("📚 مكتبة المراجع الموصى بها")
    st.write("أفضل الكتب والمصادر الشاملة لمساعدتك أثناء التعلم:")
    
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


# === القسم الرابع: قسم المشاريع (المدفوع / VIP) ===
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
        
        if passcode == "omar2026": # كلمة السر التجريبية
            st.success("تم تفعيل اشتراكك بنجاح! إليك المشاريع الكبرى:")
            st.write("🚀 **Project Pro 1:** بناء نموذج ذكاء اصطناعي للتنبؤ بأسعار العقارات برابط حي.")
            st.write("🚀 **Project Pro 2:** خط معالجة بيانات ضخمة كلياً (End-to-End Pipeline).")
        elif passcode:
            st.error("رمز الاشتراك غير صحيح. يتطلب هذا القسم الترقية للنسخة المدفوعة.")
