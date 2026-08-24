import streamlit as st

def render_python_tab():
    st.markdown("""
        <div dir="rtl" style="text-align: center; padding: 20px 10px;">
        <h3 style="font-weight: 700; margin-bottom: 8px;">🐍 Python, Libraries & Advanced Math</h3>
        <p style="opacity: 0.8; font-size: 14.5px; line-height: 1.6;">
        المحطة الأساسية لترجمة المفاهيم النظرية إلى كود عملي ومشاريع برمجية قوية. هنا هتلاقي ملخصات، أكواد، ومكتبات تحليل البيانات الخطوة بخطوة.
        </p>
        </div>
        """, unsafe_allow_html=True)

    # تقسيم قسم بايثون لمجالات فرعية مرتبة
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
            <div dir="rtl" style="padding: 15px; border: 1px solid #333; border-radius: 10px; background-color: rgba(255,255,255,0.02); margin-bottom: 15px;">
            <h4 style="font-size: 16px; margin-bottom: 8px;">⚙️ Python Fundamentals</h4>
            <p style="font-size: 13px; opacity: 0.8; line-height: 1.5;">
            الأساسيات البرمجية اللازمة للتعامل مع البيانات: (Variables, Data Structures, Control Flow, Functions, OOP basics).
            </p>
            </div>
            """, unsafe_allow_html=True)

        st.markdown("""
            <div dir="rtl" style="padding: 15px; border: 1px solid #333; border-radius: 10px; background-color: rgba(255,255,255,0.02); margin-bottom: 15px;">
            <h4 style="font-size: 16px; margin-bottom: 8px;">🔢 NumPy & Math for Data</h4>
            <p style="font-size: 13px; opacity: 0.8; line-height: 1.5;">
            الرياضيات الأساسية، الجبر الخطي، والإحصاء التطبيقي باستخدام المصفوفات لتسريع الحسابات.
            </p>
            </div>
            """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
            <div dir="rtl" style="padding: 15px; border: 1px solid #333; border-radius: 10px; background-color: rgba(255,255,255,0.02); margin-bottom: 15px;">
            <h4 style="font-size: 16px; margin-bottom: 8px;">🐼 Pandas & Data Wrangling</h4>
            <p style="font-size: 13px; opacity: 0.8; line-height: 1.5;">
            العمود الفقري لتحليل البيانات: تنظيف، معالجة، دمج، وتحليل الجداول والملفات الضخمة باحترافية.
            </p>
            </div>
            """, unsafe_allow_html=True)

        st.markdown("""
            <div dir="rtl" style="padding: 15px; border: 1px solid #333; border-radius: 10px; background-color: rgba(255,255,255,0.02); margin-bottom: 15px;">
            <h4 style="font-size: 16px; margin-bottom: 8px;">📈 Data Visualization (Seaborn/Plotly)</h4>
            <p style="font-size: 13px; opacity: 0.8; line-height: 1.5;">
            تحويل الأرقام الصماء لرسوم بيانية تفاعلية وجذابة توضح القصة وراء البيانات.
            </p>
            </div>
            """, unsafe_allow_html=True)

    # تنبيه بحالة المحتوى
    st.markdown("""
        <div dir="rtl" style="text-align: center; padding: 15px; background: rgba(255, 255, 255, 0.03); border-radius: 8px; margin-top: 10px;">
        <span style="font-size: 14px; font-weight: 600;">🚀 وقريبًا جداً:</span>
        <p style="font-size: 13px; opacity: 0.75; margin-top: 5px;">سيتم إضافة شيتات تفاعلية، أكواد جاهزة للتجربة الفورية، ومشاريع مصغرة لكل مكتبة!</p>
        </div>
        """, unsafe_allow_html=True)
