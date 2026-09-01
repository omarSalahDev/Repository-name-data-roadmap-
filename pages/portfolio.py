import streamlit as st

def render_portfolio_page():
    """عرض صفحة معرض المشاريع والأعمال الشخصية"""
    
    st.title("💼 Featured Projects & Prototypes")
    st.caption("أبرز المشاريع التقنية والحلول التي أبنيها في رحلتي لعالم البيانات")
    st.markdown("---")
    
    # كارت المشروع الرئيسي
    with st.container():
        st.subheader("📊 Data Analysis Portfolio & Dashboards")
        st.write("""
        مجموعة من التحليلات البرمجية ومشاريع أدوات تحليل البيانات (Excel, SQL, Power BI, Python) 
        المعروضة بشكل كامل على منصتي الشخصية وحسابي على GitHub.
        """)
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # أزرار الروابط الخارجية
        col1, col2 = st.columns(2)
        with col1:
            st.link_button(
                "🌐 زيارة البورتفوليو الشامل", 
                "https://omarsalahdev.github.io/portfolio/",
                use_container_width=True
            )
        with col2:
            st.link_button(
                "📂 تصفح أكواد GitHub", 
                "https://github.com/omarSalahDev",
                use_container_width=True
            )
