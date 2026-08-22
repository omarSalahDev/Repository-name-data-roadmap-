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

# --- Tab 1: Roadmap (9 Phases with In-App Reading) ---
with tab1:
    st.markdown("""
        <div dir="rtl" style="text-align: center; font-size: 14px; margin-top: 15px; margin-bottom: 25px; opacity: 0.8;">
        ✨ اختر المرحلة المطلوبة واستمتع بقراءة الشرح والدروس المبسطة مباشرة داخل منصة DataLab
        </div>
        """, unsafe_allow_html=True)

    # --- Phase 01: Understanding Data (Clean & Professional Notion Style) ---
    with st.expander("📁 Phase 01: Read: Understanding Data (اضغط للقراءة الكاملة)", expanded=False):
        st.markdown("""
        <div dir="rtl" style="font-family: sans-serif; font-size: 16px; line-height: 2.1; padding: 25px; background-color: #1a1a1a; border-radius: 12px; border: 1px solid #333; color: #e0e0e0;">
        
        <h2 style="color: #ff4b4b; font-size: 24px; font-weight: 800; margin-bottom: 20px; border-bottom: 2px solid #333; padding-bottom: 10px;">
            🪑 قصة كرسي قديم.. أظهرت سر أغلى مجال في العالم!
        </h2>
        
        <p style="margin-bottom: 15px;">
            تخيل معايا إنك شفت كرسي خشب قديم ومكسور في الشارع، غالباً مش هتدفع فيه جنيه..<br>
            لكن لو حد جه وحكى لك قصة الكرسي ده وقال لك إن ده الكرسي اللي كان بيقعد عليه عالم مشهور وهو بيكتب أفكاره، قيمته في لحظة هتنط لآلاف الدولارات!
        </p>
        
        <p style="margin-bottom: 15px; background: rgba(255, 255, 255, 0.05); padding: 12px; border-radius: 8px; border-right: 4px solid #ff4b4b;">
            <b>السؤال هنا: هل الكرسي اتغير؟</b><br>
            لأ، الكرسي هو هو.. اللي اتغير هو <b>"المعلومة"</b> اللي ارتبطت بيه!
        </p>
        
        <p style="margin-bottom: 20px;">
            وده بالصدفة أول وأهم درس في عالم البيانات:<br>
            البيانات (<span dir="ltr" style="color: #4da6ff;">Data</span>) لوحدها زي الكرسي القديم مالهاش قيمة.. لكن لما نفهمها ونحطها في السياق الصح، تتحول لـ (<span dir="ltr" style="color: #4da6ff;">Information</span>) ومنها بناخد قرار (<span dir="ltr" style="color: #4da6ff;">Decision</span>) بيساوي ملايين!
        </p>
        
        <hr style="border: 0.5px solid #444; margin: 25px 0;">
        
        <h3 style="color: #fff; font-size: 20px; font-weight: 700; margin-bottom: 12px;">
            📺 هو الموضوع ده قريب مننا للدرجادي؟
        </h3>
        <p style="margin-bottom: 20px;">
            أكيد! يعني لما تفتح يوتيوب أو نتفليكس أو أمازون وتلاقيه بيقولك <i>"مقترح لك بناءً على اهتمامك"</i>.. هو مش بيخمن ولا بيقرأ الفنجان!<br>
            هو بيشوف بيانات ملايين المستخدمين، يدرس سلوكهم ويتوقع إيه اللي هيعجبك.. سواء في ترتيب منشورات فيسبوك، كشف المعاملات البنكية المشبوهة، أو التنبؤ بأسعار العقارات. البيانات هي المحرك الأساسي لكل ده.
        </p>
        
        <hr style="border: 0.5px solid #444; margin: 25px 0;">
        
        <h3 style="color: #fff; font-size: 20px; font-weight: 700; margin-bottom: 12px;">
            🔍 إيه الفرق بين <span dir="ltr">Data Analysis</span> و <span dir="ltr">Data Science</span>؟
        </h3>
        <p style="margin-bottom: 15px;">تخيل شركة باعت مليون منتج الشهر اللي فات:</p>
        
        <div style="background: rgba(0, 0, 0, 0.2); padding: 15px; border-radius: 8px; margin-bottom: 15px;">
            <p style="margin-bottom: 8px;"><b>1. تحليل البيانات (<span dir="ltr" style="color: #4da6ff;">Data Analysis</span>):</b></p>
            <p style="margin-bottom: 0; opacity: 0.9;">هنا المدير بيدخل يسألك: <i>"إيه أكثر منتج اتباع؟ وليه المبيعات وقعت في فرع القاهرة؟"</i> دورك هنا بتحلل اللي حصل في الماضي (قرار ➔ استنتاجات ➔ تحليل ➔ بيانات). والأدوات الأساسية هي: (<span dir="ltr" style="color: #ff9933;">Excel - SQL - Power BI - Python</span>).</p>
        </div>

        <div style="background: rgba(0, 0, 0, 0.2); padding: 15px; border-radius: 8px; margin-bottom: 20px;">
            <p style="margin-bottom: 8px;"><b>2. علم البيانات (<span dir="ltr" style="color: #4da6ff;">Data Science</span>):</b></p>
            <p style="margin-bottom: 0; opacity: 0.9;">هنا الدور أكبر.. أنت مش بس بتشوف الماضي، أنت بتبني نموذج (<span dir="ltr" style="color: #ff9933;">Model</span>) يتعلم من بيانات الماضي علشان يتوقع المستقبل ويقولك ننتج إيه السنة الجاية! وعشان كده بيسموه "الخلاط" لأنه مزيج بين البرمجة، الإحصاء، والرياضيات، والـ Machine Learning.</p>
        </div>
        
        <hr style="border: 0.5px solid #444; margin: 25px 0;">
        
        <h3 style="color: #fff; font-size: 20px; font-weight: 700; margin-bottom: 12px;">
            🚀 ابدأ منين لو تايه بين المنصات؟
        </h3>
        <ul style="margin-bottom: 20px; padding-right: 20px;">
            <li style="margin-bottom: 8px;"><b>Kaggle:</b> الأفضل للتطبيق العملي والمسابقات.</li>
            <li style="margin-bottom: 8px;"><b>DataCamp & Dataquest:</b> ممتازان لتعلم SQL و Python بالتطبيق المباشر.</li>
            <li style="margin-bottom: 8px;"><b>365 Data Science:</b> منهج منظم بيبدأ معاك من الصفر.</li>
        </ul>
        <p style="background: rgba(255, 153, 0, 0.1); padding: 10px; border-radius: 6px; border-left: 4px solid #ff9933;">
            <b>نصيحة ذهبية:</b> ما تشتتش نفسك، اختار منصة واحدة وركز عليها ولاتشتت انتباهك بكثرة المصادر!
        </p>
        
        </div>
        """, unsafe_allow_html=True)
        
        # زرار آمن ومنسق لمشاركة النقاش
        st.markdown("""
            <div style="text-align: center; margin-top: 15px;">
                <a href="https://www.linkedin.com" target="_blank" style="background-color: #0a66c2; color: white; padding: 10px 20px; border-radius: 6px; text-decoration: none; font-weight: bold; display: inline-block;">
                    💬 ناقش هذا الدرس على لينكد إن
                </a>
            </div>
            """, unsafe_allow_html=True)

    # --- Phase 02: Data Science Fundamentals ---
    with st.expander("📁 Phase 02: Read: Data Science Fundamentals (قريباً)", expanded=False):
        st.markdown("<div dir='rtl' style='padding: 15px; color: #888;'>جاري تجهيز المقال الثاني بنفس التنسيق الفخم.. انتظرونا قريباً! ✨</div>", unsafe_allow_html=True)

    # باقي المراحل (من 3 لـ 9)
    other_phases = {
        "03": "Think Like a Data Analyst",
        "04": "Data Ecosystem", 
        "05": "Data Analytics Toolbox", 
        "06": "Big Data", 
        "07": "Data Visualization", 
        "08": "Machine Learning Basics", 
        "09": "Data Career Roadmap"
    }
    
    for ph, title in other_phases.items():
        with st.expander(f"📁 Phase {ph}: {title} - قريباً ⏳", expanded=False):
            st.markdown(f"<div dir='rtl' style='padding: 10px; opacity: 0.8;'>هذا الفصل قيد التجهيز وسيتم إطلاقه ضمن سلسلة DataLab التعليمية.</div>", unsafe_allow_html=True)
   
# --- Tab 2: Python & Tools (Future Content) ---
with tab2:
    st.markdown("""
        <div dir="rtl" style="text-align: center; padding: 40px 10px; opacity: 0.8;">
        <h3>🐍 Python, Libraries & Advanced Math</h3>
        <p>المحطة القادمة بعد الانتهاء من أساسيات تحليل البيانات.. انتظروا المحتوى العملي والمكتبات الخرافية قريباً جداً! ✨</p>
        </div>
        """, unsafe_allow_html=True)

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
            <h4 style="margin-bottom: 5px;">🚀 منصة Novyra (قيد التطوير / Prototype)</h4>
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
