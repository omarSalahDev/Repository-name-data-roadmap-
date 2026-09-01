import streamlit as st

def render_header():
    """عرض الهيدر الرئيسي والتنسيقات الجمالية للمنصة"""
    
    # 1. التنسيقات الجمالية (CSS Customization)
    st.markdown("""
        <style>
        .stButton>button { 
            width: 100%; 
            border-radius: 8px; 
            height: 2.8em; 
            font-weight: 600; 
            transition: all 0.3s ease;
        }
        .main-header {
            text-align: center; 
            padding: 10px 0 20px 0;
        }
        .main-title {
            font-size: 38px; 
            font-weight: 800; 
            letter-spacing: -0.5px;
        }
        .main-subtitle {
            font-size: 16px; 
            font-weight: 500; 
            line-height: 1.8; 
            max-width: 820px; 
            margin: 0 auto; 
            padding: 10px 15px;
            color: #4A5568;
        }
        </style>
        """, unsafe_allow_html=True)

    # 2. الهيدر والوصف الشخصي
    st.markdown("""
        <div class="main-header">
            <h1 class="main-title">
                ⚡ DataLab <span style="font-weight: 300; opacity: 0.6; font-size: 24px;">| by Omar Saleh</span>
            </h1>
            <div dir="rtl" class="main-subtitle">
            بوابتك المرجعية المتكاملة لعالم الـ <span dir="ltr">Data</span> 🧭 
            <br>مش مجرد مسار، دي رحلة بناء حقيقية بتبدأ من أدوات الـ <span dir="ltr">Data Analysis</span>، مروراً بمكتبات الـ <span dir="ltr">Python</span> والرياضة، وصولاً لخوارزميات الـ <span dir="ltr">Machine Learning</span>.. بمشاريع عملية تتدرج معاك لحد ما تبني أقوى <span dir="ltr">Portfolio</span> و <span dir="ltr">CV</span> ينافس في السوق ✨
            </div>
        </div>
        """, unsafe_allow_html=True)
