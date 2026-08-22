import streamlit as st

# 1. إعدادات الصفحة (Apple & Notion Minimalist Style)
st.set_page_config(page_title="DataLab | by Omar Saleh", page_icon="🧭")

# 2. بعض اللمسات الجمالية للتنسيق
st.markdown("""
    <style>
    .stButton>button { width: 100%; border-radius: 10px; height: 3em; font-weight: bold; }
    .title { text-align: center; color: #1e1e1e; }
    .subheader { text-align: center; color: #555; }
    </style>
    """, unsafe_allow_html=True)

# 3. هيكل البيانات واللينكات الحقيقية
Phase = {
    "01": {
        "title": "Understanding Data", 
        "link": "https://www.linkedin.com/posts/omarsaleh-cs_%D9%82%D8%B5%D8%A9-%D9%83%D8%B1%D8%B3%D9%8A-%D9%82%D8%AF%D9%8A%D9%85-%D8%A3%D8%B8%D9%87%D8%B1%D8%AA-%D8%B3%D8%B1-%D8%A3%D8%BA%D9%84%D9%89-%D9%85%D8%AC%D8%A7%D9%84-%D9%81%D9%8A-%D8%A7%D9%84%D8%B9%D8%A7%D9%84%D9%85-activity-7491739030548664320-wMk4?utm_source=share&utm_medium=member_android&rcm=ACoAAFfGkf4Bchnn1vdJPOkg2UryBOqvABwrOGk"
    },
    "02": {
        "title": "Data Science Fundamentals", 
        "link": "https://linkedin.com/posts/omarsaleh-cs_%D8%A3%D9%83%D8%A8%D8%B1-%D8%A3%D8%B3%D8%B7%D9%88%D8%B1%D8%A9-%D9%81%D9%8A-%D8%B9%D8%A7%D9%84%D9%85-%D8%A7%D9%84%D8%A8%D9%8A%D8%A7%D9%86%D8%A7%D8%AA-%D9%84%D9%88-%D9%81%D8%A7%D9%83%D8%B1-activity-7492472508844101632-zK5l?rcm=ACoAAFfGkf4Bchnn1vdJPOkg2UryBOqvABwrOGk"
    },
    "03": {"title": "Think Like a Data Analyst", "link": None},
    "04": {"title": "Data Ecosystem", "link": None},
    "05": {"title": "Data Analytics Toolbox", "link": None},
    "06": {"title": "Big Data", "link": None},
    "07": {"title": "Data Visualization", "link": None},
    "08": {"title": "Machine Learning Basics", "link": None},
    "09": {"title": "Data Career Roadmap", "link": None},
}

# 4. تصميم الواجهة الرئيسية
st.markdown("<h1 class='title'>⚡ DataLab | by Omar Saleh</h1>", unsafe_allow_html=True)
st.markdown("<p class='subheader'>مرجعك الشامل وخريطتك العملية من تحليل البيانات إلى علوم البيانات والذكاء الاصطناعي 🚀</p>", unsafe_allow_html=True)
st.divider()

# عرض الأزرار بشكل تفاعلي ومرتب
for ph, info in Phase.items():
    col1, col2 = st.columns([1, 4])
    with col1:
        st.button(f"Phase {ph}", disabled=True)
    with col2:
        if info["link"]:
            st.link_button(f"Read: {info['title']}", url=info["link"])
        else:
            st.button(f"{info['title']} - قريباً ⏳", disabled=True)

st.divider()
st.caption("Engineered & Maintained by Omar Saleh")
