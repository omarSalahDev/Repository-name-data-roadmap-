import streamlit as st
from data.roadmap import get_roadmap_phases, render_phase_1_content

def render_roadmap_page():
    """عرض صفحة خريطة الطريق الكاملة"""
    
    st.title("🗺️ مسار التعلم الشامل للبيانات")
    st.caption("تعرف على المفاهيم والخطوات الأساسية لبناء مسارك المهني في عالم البيانات.")
    st.markdown("---")
    
    phase_1 = get_roadmap_phases()
    
    # 1. عرض المرحلة الأولى داخل Expander شيك
    with st.expander(f"📁 {phase_1['title']} (اضغط للقراءة الكاملة)", expanded=False):
        
        # عرض محتوى المرحلة
        render_phase_1_content()
        
        # زر مشاركة لينكد إن
        st.markdown("<br>", unsafe_allow_html=True)
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.link_button(
                "💬 ناقش هذا الدرس على لينكد إن", 
                phase_1["linkedin_url"],
                use_container_width=True
            )
