import streamlit as st

# 1. إعدادات الصفحة (Apple & Notion Minimalist Style)
st.set_page_config(
    page_title="DataLab | by Omar Saleh", 
    page_icon="🧭",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# 2. بعض اللمسات الجمالية للتنسيق
st.markdown("""
    <style>
    .stButton>button { width: 100%; border-radius: 8px; height: 2.8em; font-weight: 600; }
    </style>
    """, unsafe_allow_html=True)

# 3. الهيدر والعنوان الرئيسي
st.markdown("""
    <div style="text-align: center; padding: 5px 0;">
        <h1 style="font-size: 36px; font-weight: 800; letter-spacing: -0.5px;">
            ⚡ DataLab <span style="font-weight: 300; opacity: 0.6;">| by Omar Saleh</span>
        </h1>
    </div>
    """, unsafe_allow_html=True)

# 4. الوصف التفصيلي (مع عزل النصوص والنسب المئوية لضبط الاتجاهات)
st.markdown("""
    <div dir="rtl" style="text-align: center; font-size: 15.5px; font-weight: 500; line-height: 1.8; max-width: 820px; margin: 0 auto; padding: 0 10px;">
    بوابتك المرجعية المتكاملة لعالم الـ <span dir="ltr">Data</span> (<span dir="ltr">100% مفتوحة ومجانية بالكامل</span>) 🧭 
    <br>مش مجرد مسار، دي رحلة بناء حقيقية بتبدأ من أدوات الـ <span dir="ltr">Data Analysis</span>، مروراً بمكتبات الـ <span dir="ltr">Python</span> والرياضة، وصولاً لخوارزميات الـ <span dir="ltr">Machine Learning</span>.. بمشاريع عملية تتدرج معاك لحد ما تبني أقوى <span dir="ltr">Portfolio</span> و <span dir="ltr">CV</span> ينافس في السوق ✨
    </div>
    """, unsafe_allow_html=True)

# 5. نظام الأبواب (Tabs) لتنظيم المنصة واحترافيتها
tab1, tab2, tab3 = st.tabs(["🧭 Data Roadmap", "🐍 Python & Tools", "💼 Portfolio & Projects"])

# --- Tab 1: Roadmap (9 Phases) ---
with tab1:
    st.markdown("""
        <div dir="rtl" style="text-align: center; font-size: 13px; margin-top: 15px; margin-bottom: 20px; opacity: 0.75;">
        👇 اضغط على أي مرحلة لفتح الشرح المباشر على لينكد إن.. وتابع معانا باقي المحطات خطوة بخطوة!
        </div>
        """, unsafe_allow_html=True)

    Phase = {
        "01": {
            "title": "Understanding Data", 
            "link": "https://www.linkedin.com/posts/omarsaleh-cs_%D9%82%D8%B5%D8%A9-%D9%83%D8%B1%D8%B3%D9%8A-%D9%82%D8%AF%D9%8A%D9%85-%D8%A3%D8%B8%D9%87%D8%B1%D8%AA-%D8%B3%D8%B1-%D8%A3%D8%BA%D9%84%D9%89-%D9%85%D8%AC%D8%A7%D9%84-%D9%81%D9%8A-%D8%A7%D9%84%D8%B9%D8%A7%D9%84%D9%85-activity-7491739030548664320-wMk4?utm_source=share&utm_medium=member_android&rcm=ACoAAFfGkf4Bchnn1vdJPOkg2UryBOqvABwrOGk"
        },
        "02": {
            "title": "Data Science Fundamentals", 
            "link": "https://linkedin.com/posts/omarsaleh-cs_%D8%A3%D9%83%D8%A8%D8%B1-%D8%A3%D8%B3%D8%B7%D9%88%D8%B1%D8%A9-%D9%81%D9%8A-%D8%B9%D8%A7%D9%84%D9%85-%D8%A7%D9%84%D8%A8%D9%8A%D8%A7%D9%86%D8%A7%D8%AA-%D9%84%D9%88-%D9%81%D8%A7%D9%83%D8%B1-activity-7492472508844101632-zK5l?rcm=ACoAAFfGkf4Bchnn1vdJPOkg2UryBOqvABwrOGk"
        },
        "03": {
            "title": "Think Like a Data Analyst",
            "link": "https://lnkd.in/p/eJ-j8eSV"
        },
        "04": {"title": "Data Ecosystem", "link": None},
        "05": {"title": "Data Analytics Toolbox", "link": None},
        "06": {"title": "Big Data", "link": None},
        "07": {"title": "Data Visualization", "link": None},
        "08": {"title": "Machine Learning Basics", "link": None},
        "09": {"title": "Data Career Roadmap", "link": None},
    }

    for ph, info in Phase.items():
        col1, col2 = st.columns([1, 4])
        with col1:
            st.button(f"Phase {ph}", disabled=True, key=f"phase_btn_{ph}")
        with col2:
            if info["link"]:
                st.link_button(f"Read: {info['title']}", url=info["link"])
            else:
                st.button(f"{info['title']} - قريباً ⏳", disabled=True, key=f"soon_btn_{ph}")

# --- Tab 2: Python & Tools (Future Content) ---
with tab2:
    st.markdown("""
        <div dir="rtl" style="text-align: center; padding: 40px 10px; opacity: 0.8;">
        <h3>🐍 Python, Libraries & Advanced Math</h3>
        <p>المحطة القادمة بعد الانتهاء من أساسيات تحليل البيانات.. انتظروا المحتوى العملي والمكتبات الخرافية قريباً جداً! ✨</p>
        </div>
        """, unsafe_allow_html=True)

# --- Tab 3: Portfolio & Projects ---
with tab3:
   # --- Tab 3: Portfolio & Projects (Professional Showcase) ---
with tab3:
    st.markdown("""
        <div dir="rtl" style="text-align: center; padding: 20px 10px;">
        <h3>💼 Featured Projects & Prototypes</h3>
        <p style="opacity: 0.8; font-size: 14px;">أبرز المشاريع التقنية والحلول اللي ببنيها في رحلتي لعالم البيانات:</p>
        </div>
        """, unsafe_allow_html=True)

    # مشروع 1: Novyra (المشروع الكبير)
    with st.container():
        st.markdown("""
            <div dir="rtl" style="padding: 15px; border: 1px solid #333; border-radius: 10px; margin-bottom: 15px; background-color: rgba(255,255,255,0.02);">
            <h4 style="margin-bottom: 5px;"> منصة Novyra (قيد Entwicklung / Prototype)</h4>
            <p style="font-size: 13.5px; opacity: 0.85; line-height: 1.6;">
            رؤيتنا المبتكرة لحل فجوة سوق العمل، دعم الخريجين والعائدين من الجيش، وتقديم نظام تتبع ذكي للمهارات والمسارات المهنية في البنوك والجهات الحكومية.
            </p>
            </div>
            """, unsafe_allow_html=True)

    # مشروع 2: Data Analytics Portfolio
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
# 6. الفوتر الاحترافي (Footer) مع الروابط والإيميل الجامعي
st.divider()
st.markdown("""
    <div style="text-align: center; font-size: 13px; opacity: 0.75; line-height: 1.8;">
    Built with 🤍 by <b>Omar Saleh</b><br>
    <a href="https://www.linkedin.com/in/omarsaleh-cs" target="_blank" style="text-decoration: none; margin: 0 8px; color: inherit;">LinkedIn</a> | 
    <a href="https://github.com/omarSalahDev" target="_blank" style="text-decoration: none; margin: 0 8px; color: inherit;">GitHub</a> | 
    <a href="https://omarsalahdev.github.io/portfolio/" target="_blank" style="text-decoration: none; margin: 0 8px; color: inherit;">Portfolio</a> | 
    <a href="mailto:2401601@student.eelu.edu.eg" style="text-decoration: none; margin: 0 8px; color: inherit;">Email</a>
    </div>
    """, unsafe_allow_html=True)
