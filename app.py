import streamlit as st
from python_tools import render_python_tab 
# استدعاء ملف بايثون الجديد

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

# 4. الوصف التفصيلي
st.markdown("""
    <div dir="rtl" style="text-align: center; font-size: 15.5px; font-weight: 500; line-height: 1.8; max-width: 820px; margin: 0 auto; padding: 0 10px;">
    بوابتك المرجعية المتكاملة لعالم الـ <span dir="ltr">Data</span> </span>) 🧭 
    <br>مش مجرد مسار، دي رحلة بناء حقيقية بتبدأ من أدوات الـ <span dir="ltr">Data Analysis</span>، مروراً بمكتبات الـ <span dir="ltr">Python</span> والرياضة، وصولاً لخوارزميات الـ <span dir="ltr">Machine Learning</span>.. بمشاريع عملية تتدرج معاك لحد ما تبني أقوى <span dir="ltr">Portfolio</span> و <span dir="ltr">CV</span> ينافس في السوق ✨
    </div>
    """, unsafe_allow_html=True)

# 5. نظام الأبواب (Tabs)
tab1, tab2, tab3 = st.tabs(["🧭 Data Roadmap", "🐍 Python & Tools", "💼 Portfolio & Projects"])

# --- Tab 1: Roadmap (9 Phases with In-App Reading) ---
with tab1:
    st.markdown("""
        <div dir="rtl" style="text-align: center; direction: rtl; font-size: 14px; margin-top: 15px; margin-bottom: 25px; opacity: 0.8;">
        ✨ اختر المرحلة المطلوبة واستمتع بقراءة الشرح والدروس المبسطة مباشرة داخل منصة DataLab
        </div>
        """, unsafe_allow_html=True)

    # --- Phase 01: Understanding Data ---
    with st.expander("📁 Phase 01: Read: Understanding Data (اضغط للقراءة الكاملة)", expanded=False):
        st.markdown("""
        <div dir="rtl" style="direction: rtl; text-align: right; font-family: sans-serif; font-size: 16px; line-height: 2.1; padding: 25px; background-color: #1a1a1a; border-radius: 12px; border: 1px solid #333; color: #e0e0e0;">
        
        <h2 style="direction: rtl; text-align: right; color: #ff4b4b; font-size: 24px; font-weight: 800; margin-bottom: 20px; border-bottom: 2px solid #333; padding-bottom: 10px;">
            🪑 قصة كرسي قديم.. أظهرت سر أغلى مجال في العالم!
        </h2>
        
        <p style="direction: rtl; text-align: right; margin-bottom: 15px;">
            تخيل معايا إنك شفت كرسي خشب قديم ومكسور في الشارع، غالباً مش هتدفع فيه جنيه..<br>
            لكن لو حد جه وحكى لك قصة الكرسي ده وقال لك إن ده الكرسي اللي كان بيقعد عليه عالم مشهور وهو بيكتب أفكاره، قيمته في لحظة هتنط لآلاف الدولارات!
        </p>
        
        <p style="direction: rtl; text-align: right; margin-bottom: 15px; background: rgba(255, 255, 255, 0.05); padding: 12px; border-radius: 8px; border-left: 4px solid #ff4b4b;">
            <b>السؤال هنا: هل الكرسي اتغير؟</b><br>
            لأ، الكرسي هو هو.. اللي اتغير هو <b>"المعلومة"</b> اللي ارتبطت بيه!
        </p>
        
        <p style="direction: rtl; text-align: right; margin-bottom: 20px;">
            وده بالصدفة أول وأهم درس في عالم البيانات:<br>
            البيانات (<span dir="ltr" style="color: #4da6ff;">Data</span>) لوحدها زي الكرسي القديم مالهاش قيمة.. لكن لما نفهمها ونحطها في السياق الصح، تتحول لـ (<span dir="ltr" style="color: #4da6ff;">Information</span>) ومنها بناخد قرار (<span dir="ltr" style="color: #4da6ff;">Decision</span>) بيساوي ملايين!
        </p>
        
        <hr style="border: 0.5px solid #444; margin: 25px 0;">
        
        <h3 style="direction: rtl; text-align: right; color: #fff; font-size: 20px; font-weight: 700; margin-bottom: 12px;">
            📺 هو الموضوع ده قريب مننا للدرجادي؟
        </h3>
        <p style="direction: rtl; text-align: right; margin-bottom: 20px;">
            أكيد! يعني لما تفتح يوتيوب أو نتفليكس أو أمازون وتلاقيه بيقولك <i>"مقترح لك بناءً على اهتمامك"</i>.. هو مش بيخمن ولا بيقرأ الفنجان!<br>
            هو بيشوف بيانات ملايين المستخدمين، يدرس سلوكهم ويتوقع إيه اللي هيعجبك.. سواء في ترتيب منشورات فيسبوك، كشف المعاملات البنكية المشبوهة، أو التنبؤ بأسعار العقارات. البيانات هي المحرك الأساسي لكل ده.
        </p>
        
        <hr style="border: 0.5px solid #444; margin: 25px 0;">
        
        <h3 style="direction: rtl; text-align: right; color: #fff; font-size: 20px; font-weight: 700; margin-bottom: 12px;">
            🔍 إيه الفرق بين <span dir="ltr">Data Analysis</span> و <span dir="ltr">Data Science</span>؟
        </h3>
        <p style="direction: rtl; text-align: right; margin-bottom: 15px;">تخيل شركة باعت مليون منتج الشهر اللي فات:</p>
        
        <div style="direction: rtl; text-align: right; background: rgba(0, 0, 0, 0.2); padding: 15px; border-radius: 8px; margin-bottom: 15px;">
            <p style="direction: rtl; text-align: right; margin-bottom: 8px;"><b>1. تحليل البيانات (<span dir="ltr" style="color: #4da6ff;">Data Analysis</span>):</b></p>
            <p style="direction: rtl; text-align: right; margin-bottom: 0; opacity: 0.9;">هنا المدير بيدخل يسألك: <i>"إيه أكثر منتج اتباع؟ وليه المبيعات وقعت في فرع القاهرة؟"</i> دورك هنا بتحلل اللي حصل في الماضي (قرار ➔ استنتاجات ➔ تحليل ➔ بيانات). والأدوات الأساسية هي: (<span dir="ltr" style="color: #ff9933;">Excel - SQL - Power BI - Python</span>).</p>
        </div>

        <div style="direction: rtl; text-align: right; background: rgba(0, 0, 0, 0.2); padding: 15px; border-radius: 8px; margin-bottom: 20px;">
            <p style="direction: rtl; text-align: right; margin-bottom: 8px;"><b>2. علم البيانات (<span dir="ltr" style="color: #4da6ff;">Data Science</span>):</b></p>
            <p style="direction: rtl; text-align: right; margin-bottom: 0; opacity: 0.9;">هنا الدور أكبر.. أنت مش بس بتشوف الماضي، أنت بتبني نموذج (<span dir="ltr" style="color: #ff9933;">Model</span>) يتعلم من بيانات الماضي علشان يتوقع المستقبل ويقولك ننتج إيه السنة الجاية! وعشان كده بيسموه "الخلاط" لأنه مزيج بين البرمجة، الإحصاء، والرياضيات، والـ Machine Learning.</p>
        </div>
        
        <hr style="border: 0.5px solid #444; margin: 25px 0;">
        
        <h3 style="direction: rtl; text-align: right; color: #fff; font-size: 20px; font-weight: 700; margin-bottom: 12px;">
            🚀 ابدأ منين لو تايه بين المنصات؟
        </h3>
        <ul style="direction: rtl; text-align: right; margin-bottom: 20px; padding-right: 20px;">
            <li style="margin-bottom: 8px;"><b>Kaggle:</b> الأفضل للتطبيق العملي والمسابقات.</li>
            <li style="margin-bottom: 8px;"><b>DataCamp & Dataquest:</b> ممتازان لتعلم SQL و Python بالتطبيق المباشر.</li>
            <li style="margin-bottom: 8px;"><b>365 Data Science:</b> منهج منظم بيبدأ معاك من الصفر.</li>
        </ul>
        <p style="direction: rtl; text-align: right; background: rgba(255, 153, 0, 0.1); padding: 10px; border-radius: 6px; border-right: 4px solid #ff9933;">
            <b>نصيحة ذهبية:</b> ما تشتتش نفسك، اختار منصة واحدة وركز عليها ولاتشتت انتباهك بكثرة المصادر!
        </p>
        
        </div>
        """, unsafe_allow_html=True)
        
        # زرار مشاركة لينكد إن
        st.markdown("""
            <div style="text-align: center; margin-top: 15px;">
                <a href="https://www.linkedin.com" target="_blank" style="background-color: #0a66c2; color: white; padding: 10px 20px; border-radius: 6px; text-decoration: none; font-weight: bold; display: inline-block;">
                    💬 ناقش هذا الدرس على لينكد إن
                </a>
            </div>
            """, unsafe_allow_html=True)

 # --- Phase 02: Data Science Fundamentals ---
    with st.expander("📁 Phase 02: Read: Data Science Fundamentals (اضغط للقراءة الكاملة)", expanded=False):
        st.markdown("""
        <div dir="rtl" style="direction: rtl; text-align: right; font-family: sans-serif; font-size: 16px; line-height: 2.1; padding: 25px; background-color: #1a1a1a; border-radius: 12px; border: 1px solid #333; color: #e0e0e0;">
        
        <h2 style="direction: rtl; text-align: right; color: #ff4b4b; font-size: 24px; font-weight: 800; margin-bottom: 20px; border-bottom: 2px solid #333; padding-bottom: 10px;">
            💻 أكبر أسطورة في عالم البيانات: ما هو الـ <span dir="ltr">Data Science</span> فعلياً؟
        </h2>
        
        <p style="direction: rtl; text-align: right; margin-bottom: 15px;">
            لو فاكر إن وظيفة عالم البيانات (<span dir="ltr" style="color: #4da6ff;">Data Scientist</span>) إنه يقعد على اللاب توب يكتب أكواد معقدة وخلاص.. فالبوست ده معمول علشان يغير فكرتك تماماً!<br>
            في الدرس الثاني من سلسلتنا، تعالوا نجاوب على سؤال أعمق: إيه هو الـ <span dir="ltr">Data Science</span> فعلياً؟ وإزاي البيزنس الكبير بيعتمد عليه عشان يكسب ملايين؟
        </p>
        
        <hr style="border: 0.5px solid #444; margin: 25px 0;">
        
        <h3 style="direction: rtl; text-align: right; color: #fff; font-size: 20px; font-weight: 700; margin-bottom: 12px;">
            🔬 أولاً: يعني إيه "علم" البيانات؟
        </h3>
        <p style="direction: rtl; text-align: right; margin-bottom: 15px;">
            تخيل لو حد سألك: يعني إيه علم الأحياء (<span dir="ltr">Biology</span>)؟<br>
            هتقول له: هو علم دراسة الكائنات الحية.. لكن الباحث مش بيقف يتفرج على الكائن الحي وخلاص!<br>
            هو بيحاول يفهم: ليه بيتحرك كده؟ إيه الأسباب؟ إيه النتائج؟ وإزاي نستفيد من الفهم ده؟
        </p>
        <p style="direction: rtl; text-align: right; margin-bottom: 20px; background: rgba(255, 255, 255, 0.05); padding: 12px; border-radius: 8px; border-right: 4px solid #ff4b4b;">
            وده بالصدفة اللي بيعمله الـ <span dir="ltr" style="color: #4da6ff;">Data Scientist</span>:<br>
            هو مش بيجمع أرقام وخلاص، ولكن بيجمع البيانات عشان يحولها لـ معرفة (<span dir="ltr">Knowledge</span>) ويديك في الآخر حاجة اسمها <span dir="ltr" style="color: #ff9933;">Insight</span>.
        </p>
        
        <hr style="border: 0.5px solid #444; margin: 25px 0;">
        
        <h3 style="direction: rtl; text-align: right; color: #fff; font-size: 20px; font-weight: 700; margin-bottom: 12px;">
            💡 كلمة السر في المجال: هي إيه الـ Insight دي أصلاً؟
        </h3>
        <p style="direction: rtl; text-align: right; margin-bottom: 15px;">
            الـ <span dir="ltr" style="color: #ff9933;">Insight</span> مش مجرد رقم ولا معلومة مجردة.. الـ Insight هي الفكرة الذكية اللي مستخبية جوة الأرقام وبتاخد بناءً عليها قرار يغير اللعبة!
        </p>
        <div style="direction: rtl; text-align: right; background: rgba(0, 0, 0, 0.2); padding: 15px; border-radius: 8px; margin-bottom: 15px;">
            <p style="margin-bottom: 8px;"><b>مثال عملي:</b></p>
            <p style="margin-bottom: 0; opacity: 0.9;">لو تحليل البيانات أظهر إن 70% من عملاء السوبرماركت بيشتروا منتج معين يوم الجمعة بالليل..<br>
            الرقم ده لوحده عادي.. لكن الـ <span dir="ltr" style="color: #ff9933;">Insight</span> هنا هي: <i>"لازم نزود مخزون المنتج ده ونعمل عليه عرض يوم الجمعة!"</i></p>
        </div>
        <p style="direction: rtl; text-align: right; margin-bottom: 20px; font-weight: bold; color: #4da6ff;">
            بالتالي الدورة الحقيقية لشغلك هي: Data ➔ Information ➔ Insight ➔ Decision
        </p>
        
        <hr style="border: 0.5px solid #444; margin: 25px 0;">
        
        <h3 style="direction: rtl; text-align: right; color: #fff; font-size: 20px; font-weight: 700; margin-bottom: 12px;">
            ⏳ فزورة: هل الـ Data Science علم جديد ولا قديم؟
        </h3>
        <p style="direction: rtl; text-align: right; margin-bottom: 15px;">
            <b>الإجابة: نعم ولا.. طب إزاي؟!</b>
        </p>
        <ul style="direction: rtl; text-align: right; margin-bottom: 20px; padding-right: 20px;">
            <li style="margin-bottom: 8px;"><b>لا:</b> لأن جذوره قديمة جداً ومبنية على الإحصاء والرياضيات من زمان.</li>
            <li style="margin-bottom: 8px;"><b>نعم (كاسم وانتشار):</b> لأن انفجار الإنترنت، الموبايلات والسحابة الرقمية (<span dir="ltr">Cloud Computing</span>) خلى الشركات تطبع مليارات البيانات يومياً وظهرت حاجة ماسة لـ "خلاط" يجمع الإحصاء بالبرمجة بالـ <span dir="ltr">Machine Learning</span> عشان يتعامل مع الحجم المثير ده!</li>
        </ul>
        
        <hr style="border: 0.5px solid #444; margin: 25px 0;">
        
        <h3 style="direction: rtl; text-align: right; color: #fff; font-size: 20px; font-weight: 700; margin-bottom: 12px;">
            🚕 أمثلة من الواقع: أوبر، جيميل، ويوتيوب!
        </h3>
        <p style="direction: rtl; text-align: right; margin-bottom: 15px;">
            <b>أوبر مش شركة مواصلات.. ولكن هي شركة بيانات!</b><br>
            تطبيق زي Uber مش مجرد أبلكيشن بياخدك من مكان لمكان.. أوبر بيحلل فوراً: أماكن السائقين، أماكن العملاء، نسبة الإلغاء، وحالة الزحمة.. عشان يجاوب على أسئلة لحظية زي: <i>"هل المنطقة دي محتاجة سواقين أكتر دلوقتي؟ هل نرفع السعر مؤقتاً (Surge Pricing)؟"</i> الهدف مش جمع البيانات، ولكن الهدف هو تحسين القرار ورفع أرباح الشركة.
        </p>
        <p style="direction: rtl; text-align: right; margin-bottom: 20px;">
            <b>وده نفس اللي بيحصل في:</b>
            <br>• <b>Gmail:</b> لما يقرر إن الرسالة دي <span dir="ltr">Spam</span> من غير ما إنسان يقرأها (بناءً على نموذج تصنيف ذكي).
            <br>• <b>YouTube & Netflix:</b> لما بيقترحوا عليك الفيلم أو الفيديو اللي هيعجبك بالضبط عن طريق الـ <span dir="ltr">Domain Knowledge</span> والبيانات السابقة.
        </p>
        
        <p style="direction: rtl; text-align: right; background: rgba(255, 153, 0, 0.1); padding: 12px; border-radius: 6px; border-right: 4px solid #ff9933; margin-bottom: 0;">
            <b>خلاصة القول:</b> المجال مش صعب ولكنه مش عشوائي.. لما تتعلمه بالترتيب الصح وتأسس نفسك في تحليل البيانات (<span dir="ltr">Data Analysis</span>) الأول، كل قطعة بازل هتركب في مكانها الصح.
        </p>
        
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
            <div style="text-align: center; margin-top: 15px;">
                <a href="https://www.linkedin.com" target="_blank" style="background-color: #0a66c2; color: white; padding: 10px 20px; border-radius: 6px; text-decoration: none; font-weight: bold; display: inline-block;">
                    💬 ناقش هذا الدرس على لينكد إن
                </a>
            </div>
            """, unsafe_allow_html=True)

# --- Phase 03: Think Like a Data Analyst ---
    with st.expander("📁 Phase 03: Read: Think Like a Data Analyst (اضغط للقراءة الكاملة)", expanded=False):
        st.markdown("""
        <div dir="rtl" style="direction: rtl; text-align: right; font-family: sans-serif; font-size: 16px; line-height: 2.1; padding: 25px; background-color: #1a1a1a; border-radius: 12px; border: 1px solid #333; color: #e0e0e0;">
        
        <h2 style="direction: rtl; text-align: right; color: #ff4b4b; font-size: 24px; font-weight: 800; margin-bottom: 20px; border-bottom: 2px solid #333; padding-bottom: 10px;">
            🍔 لو شفت شخص أكل 20 برجر في وجبة واحدة.. تفتكر عقلك هيفكر إزاي؟
        </h2>
        
        <p style="direction: rtl; text-align: right; margin-bottom: 15px;">
            والإجابة هتقولك: أنت بتفكر كشخص عادي.. ولا كمحلل بيانات؟ 🤔<br>
            الشخص العادي هيقف مصدوم ويقول: <i>"يا ساتر! إزاي قدر ياكل 20 برجر مرة واحدة؟!"</i> وينتهي الموضوع عنده هنا..
        </p>
        
        <p style="direction: rtl; text-align: right; margin-bottom: 15px; background: rgba(255, 255, 255, 0.05); padding: 12px; border-radius: 8px; border-right: 4px solid #ff4b4b;">
            <b>أما محلل البيانات (<span dir="ltr" style="color: #4da6ff;">Data Analyst</span>):</b> عقله في اللحظة دي بيشتغل بأسئلة مختلفة تماماً:<br>
            • هل ده معدل أكل طبيعي للشخص ده؟<br>
            • "يا ترى عمره كام؟ وزنه كام؟ وهل بيمارس رياضة عنيفة؟"<br>
            • "طب هل الرقم ده مجرد حالة فردية شاذة (<span dir="ltr" style="color: #ff9933;">Outlier</span>) ولا المنيو بتاع المطعم كبر بزيادة؟ 😂"
        </p>
        
        <p style="direction: rtl; text-align: right; margin-bottom: 20px;">
            وهنا يكمن الدرس الثالث والأهم في رحلتنا: الفرق بين الشخص العادي والمحلل مش الأدوات اللي بيستخدمها.. ولكن الفرق في <b>طريقة التفكير والسياق (<span dir="ltr">Context</span>)</b>!
        </p>
        
        <hr style="border: 0.5px solid #444; margin: 25px 0;">
        
        <h3 style="direction: rtl; text-align: right; color: #fff; font-size: 20px; font-weight: 700; margin-bottom: 12px;">
            🔍 أهم مهارة لأي <span dir="ltr">Data Analyst</span>: "اسأل ليه؟"
        </h3>
        <p style="direction: rtl; text-align: right; margin-bottom: 15px;">
            في المثل التقني الشهير بنقول:<br>
            <span dir="ltr" style="display: block; background: rgba(0, 0, 0, 0.3); padding: 10px; border-radius: 6px; margin: 8px 0; color: #ff9933; text-align: center; font-weight: bold;">"A good question is worth more than a thousand charts."</span>
            (السؤال الذكي قيمته أعلى من ألف رسم بياني).
        </p>
        <p style="direction: rtl; text-align: right; margin-bottom: 20px;">
            المحلل الشاطر مش شغلته يحفظ معادلات <span dir="ltr">Excel</span> أو أوامر <span dir="ltr">SQL</span> وخلاص.. ولكن شغلته يطرح الأسئلة الصح، لأنك لو سألت السؤال الصح، البيانات هتساعدك توصل للإجابة!
        </p>
        
        <hr style="border: 0.5px solid #444; margin: 25px 0;">
        
        <h3 style="direction: rtl; text-align: right; color: #fff; font-size: 20px; font-weight: 700; margin-bottom: 12px;">
            🔄 رحلة المحلل: دورة حياة تحليل البيانات (<span dir="ltr">Data Analysis Workflow</span>)
        </h3>
        <p style="direction: rtl; text-align: right; margin-bottom: 15px;">علشان تحل أي مشكلة بيزنس من الصفر، بتعدي بـ 5 مراحل متتالية:</p>
        
        <div style="direction: rtl; text-align: right; background: rgba(0, 0, 0, 0.2); padding: 15px; border-radius: 8px; margin-bottom: 15px;">
            <p style="margin-bottom: 5px;"><b>1. طرح الأسئلة (<span dir="ltr" style="color: #4da6ff;">Ask</span>):</b></p>
            <p style="margin-bottom: 0; opacity: 0.9;">كل رحلة بتبدأ بسؤال بيزنس واضح. مثلاً المدير بيدخل يقولك: <i>"ليه المبيعات وقعت في فرع الإسكندرية الشهر ده؟"</i> (من غير سؤال واضح، تحليلك هيبقى عشوائي وتايه).</p>
        </div>

        <div style="direction: rtl; text-align: right; background: rgba(0, 0, 0, 0.2); padding: 15px; border-radius: 8px; margin-bottom: 15px;">
            <p style="margin-bottom: 5px;"><b>2. تنظيف البيانات (<span dir="ltr" style="color: #4da6ff;">Data Wrangling</span>):</b></p>
            <p style="margin-bottom: 0; opacity: 0.9;">في مشاريع كتير، تنظيف البيانات ممكن يستهلك الجزء الأكبر من وقتك! يعني بتبدأ تجمع الداتا وتشيل الأخطاء وتعالج القيم المفقودة (<span dir="ltr">Missing Values</span>) وتوحد الصيغ علشان الداتا تبقى جاهزة ونضيفة.</p>
        </div>

        <div style="direction: rtl; text-align: right; background: rgba(0, 0, 0, 0.2); padding: 15px; border-radius: 8px; margin-bottom: 15px;">
            <p style="margin-bottom: 5px;"><b>3. استكشاف البيانات (<span dir="ltr" style="color: #4da6ff;">Exploratory Data Analysis - EDA</span>):</b></p>
            <p style="margin-bottom: 0; opacity: 0.9;">قلب شغل المحلل! هنا بتبدأ تبص على الأرقام وتكتشف الأنماط (<span dir="ltr">Patterns</span>) والعلاقات بين المتغيرات والنقاط الشاذة.. هنا البيانات بتبدأ "تتكلم".</p>
        </div>

        <div style="direction: rtl; text-align: right; background: rgba(0, 0, 0, 0.2); padding: 15px; border-radius: 8px; margin-bottom: 15px;">
            <p style="margin-bottom: 5px;"><b>4. النمذجة (<span dir="ltr" style="color: #4da6ff;">Modeling & Prediction</span>):</b></p>
            <p style="margin-bottom: 0; opacity: 0.9;">لو المشكلة محتاجة تنبؤ للمستقبل، بنبدأ نبني نموذج (<span dir="ltr">Model</span>) يتعلم من بيانات الماضي عشان يتوقع إيه اللي هيحصل الشهر الجاي.</p>
        </div>

        <div style="direction: rtl; text-align: right; background: rgba(0, 0, 0, 0.2); padding: 15px; border-radius: 8px; margin-bottom: 20px;">
            <p style="margin-bottom: 5px;"><b>5. العرض والقصة (<span dir="ltr" style="color: #4da6ff;">Presentation & Storytelling</span>):</b></p>
            <p style="margin-bottom: 0; opacity: 0.9;">أهم مرحلة بيغفل عنها كتير! لو عملت تحليل عبقري وما عرفتش تشرحه لمديرك بلغة بسيطة وقصة واضحة عن طريق أدوات زي (<span dir="ltr">Power BI</span> أو <span dir="ltr">Excel Dashboards</span>).. يبقى تحليلك ملوش قيمة!</p>
        </div>
        
        <hr style="border: 0.5px solid #444; margin: 25px 0;">
        
        <h3 style="direction: rtl; text-align: right; color: #fff; font-size: 20px; font-weight: 700; margin-bottom: 12px;">
            📊 المستويات الأربعة للتحليل (<span dir="ltr">Types of Analytics</span>)
        </h3>
        <ul style="direction: rtl; text-align: right; margin-bottom: 20px; padding-right: 20px;">
            <li style="margin-bottom: 8px;"><b>التحليل الوصفي (<span dir="ltr">Descriptive</span>):</b> "إيه اللي حصل؟" (مبيعات الشهر اللي فات كام؟)</li>
            <li style="margin-bottom: 8px;"><b>التحليل التشخيصي (<span dir="ltr">Diagnostic</span>):</b> "ليه ده حصل؟" (ليه المبيعات قلت في الفرع ده بالذات؟)</li>
            <li style="margin-bottom: 8px;"><b>التحليل التنبؤي (<span dir="ltr">Predictive</span>):</b> "إيه اللي هيحصل في المستقبل؟" (متوقع نبيع كام الشهر الجاي؟)</li>
            <li style="margin-bottom: 8px;"><b>التحليل التوجيهي (<span dir="ltr">Prescriptive</span>):</b> "إيه القرار المفروض ناخده دلوقتي؟" (هل نزود خصومات ولا نغير المنتج؟)</li>
        </ul>
        
        <p style="direction: rtl; text-align: right; background: rgba(255, 153, 0, 0.1); padding: 12px; border-radius: 6px; border-right: 4px solid #ff9933; margin-bottom: 0;">
            <b>💡 نصيحة ذهبية:</b> لا تكن مجرد "مُنفّذ" يحفظ الأكواد والمعادلات، بل كن "باحثاً عن الحقيقة" يفهم السياق ويسأل السؤال الصح قبل فتح أي أداة. تذكر دائماً: الأدوات تتغير وتتطور، لكن عقلية المحلِّل هي الأساس الذي لا غنى عنه!
        </p>
        
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
            <div style="text-align: center; margin-top: 15px;">
                <a href="[https://www.linkedin.com](https://www.linkedin.com)" target="_blank" style="background-color: #0a66c2; color: white; padding: 10px 20px; border-radius: 6px; text-decoration: none; font-weight: bold; display: inline-block;">
                    💬 ناقش هذا الدرس على لينكد إن
                </a>
            </div>
            """, unsafe_allow_html=True)

# --- Phase 04: Data Ecosystem ---
    with st.expander("📁 Phase 04: Read: Data Ecosystem (اضغط للقراءة الكاملة)", expanded=False):
        st.markdown("""
        <div dir="rtl" style="direction: rtl; text-align: right; font-family: sans-serif; font-size: 16px; line-height: 2.1; padding: 25px; background-color: #1a1a1a; border-radius: 12px; border: 1px solid #333; color: #e0e0e0;">
        
        <h2 style="direction: rtl; text-align: right; color: #ff4b4b; font-size: 24px; font-weight: 800; margin-bottom: 20px; border-bottom: 2px solid #333; padding-bottom: 10px;">
            🗺️ لو حاسس إنك تايه بين مصطلحات <span dir="ltr">(AI - Machine Learning - BI)</span>.. البوست ده ليك!
        </h2>
        
        <p style="direction: rtl; text-align: right; margin-bottom: 15px;">
            أول ما تنوي تدخل عالم البيانات، بتلاقي نفسك غرقان في بحر مصطلحات وبتقول لنفسك:<br>
            <i>"هو أنا المفروض أتعلم ذكاء اصطناعي ولا داتا ساينس؟ ولا أطلع <span dir="ltr" style="color: #4da6ff;">Data Engineer</span>؟ هو إيه الفرق بين كل ده أصلاً؟!"</i><br>
            في الدرس الرابع من سلسلتنا، تعالوا نفك الخيوط دي سوا، ونرسم الخريطة الكاملة لـ <span dir="ltr">Data Science</span> وعلاقته بباقي المجالات!
        </p>
        
        <hr style="border: 0.5px solid #444; margin: 25px 0;">
        
        <h3 style="direction: rtl; text-align: right; color: #fff; font-size: 20px; font-weight: 700; margin-bottom: 12px;">
            🎼 أولاً: الـ <span dir="ltr">Data Science</span> ليس أداة.. بل "قائد المايسترو"!
        </h3>
        <p style="direction: rtl; text-align: right; margin-bottom: 15px;">
            عالم البيانات مش برنامج، ولا لغة برمجة، ولا معادلة إحصائية.. الـ <span dir="ltr" style="color: #4da6ff;">Data Science</span> هو "المظلة الكبيرة" اللي بتجمع تحتها تخصصات مختلفة، وكل تخصص ليه دور محدد بيخدم نفس الهدف: <b>(حل مشاكل البيزنس باستخدام البيانات)</b>.
        </p>
        <p style="direction: rtl; text-align: right; margin-bottom: 15px;">
            عشان تتخيل الفريق بيشتغل إزاي.. تخيل إننا بنفتح مطعم فاخر: 🍽️
        </p>
        
        <div style="direction: rtl; text-align: right; background: rgba(0, 0, 0, 0.2); padding: 15px; border-radius: 8px; margin-bottom: 15px;">
            <p style="margin-bottom: 5px; color: #4da6ff; font-weight: bold;">• الـ Data Engineer (مهندس البيانات):</p>
            <p style="margin-bottom: 0; opacity: 0.9;">ده الشخص اللي بيجهز المطبخ وشبكات المياه والغاز ويوصل الخضار طازة ومغسول! هو اللي بيعمل البنية التحتية، قواعد البيانات، وخطوط نقل البيانات (<span dir="ltr">Data Pipelines</span>). من غيره، بقية الفريق مش هيلاقي داتا يشتغل عليها.</p>
        </div>

        <div style="direction: rtl; text-align: right; background: rgba(0, 0, 0, 0.2); padding: 15px; border-radius: 8px; margin-bottom: 15px;">
            <p style="margin-bottom: 5px; color: #4da6ff; font-weight: bold;">• الـ Data Analyst & BI Developer (محلل البيانات وذكاء الأعمال):</p>
            <p style="margin-bottom: 0; opacity: 0.9;">ده "الشيف" اللي بيمسك البيانات المجهزة، يطبخها، ويطلع منها تقارير ولوحات عرض (<span dir="ltr">Dashboards</span>) بتشرح أداء المطعم: <i>"إيه أكثر أكلة أتباعت؟ والمبيعات زادت ولا قلت مقارنة بالشهر اللي فات؟"</i>.</p>
        </div>

        <div style="direction: rtl; text-align: right; background: rgba(0, 0, 0, 0.2); padding: 15px; border-radius: 8px; margin-bottom: 20px;">
            <p style="margin-bottom: 5px; color: #4da6ff; font-weight: bold;">• الـ Data Scientist (عالم البيانات):</p>
            <p style="margin-bottom: 0; opacity: 0.9;">ده بقى "الماستر شيف" اللي بيمسك البيانات، يتوقع إيه الأكلة الجديدة اللي الزبون هيطلبها الشتاء الجاي، ويبني أفكار ونماذج ذكية تساعد المطعم يتوسع ويكسب ملايين!</p>
        </div>
        
        <hr style="border: 0.5px solid #444; margin: 25px 0;">
        
        <h3 style="direction: rtl; text-align: right; color: #fff; font-size: 20px; font-weight: 700; margin-bottom: 12px;">
            🤖 ثانياً: شجرة الذكاء الاصطناعي <span dir="ltr">(AI vs ML vs Deep Learning)</span>
        </h3>
        <p style="direction: rtl; text-align: right; margin-bottom: 15px;">
            كتير بيلخبطوا بينهم وفاكرينهم حاجة واحدة، لكن العلاقات بينهم زي الدمى الروسية (جوة بعض):
        </p>
        <ul style="direction: rtl; text-align: right; margin-bottom: 20px; padding-right: 20px;">
            <li style="margin-bottom: 10px;"><b>الذكاء الاصطناعي (<span dir="ltr" style="color: #ff9933;">Artificial Intelligence - AI</span>):</b> الشجرة الكبيرة.. أي نظام بيحاكي الذكاء البشري (زي القيادة الذاتية، الترجمة، فهم الكلام).</li>
            <li style="margin-bottom: 10px;"><b>تعلم الآلة (<span dir="ltr" style="color: #ff9933;">Machine Learning - ML</span>):</b> فرع جوه الـ AI.. بدل ما تكتب شروط بنفسك للكمبيوتر، بتديه بيانات كتير وهو بيتعلم الأنماط لوحده عشان يتوقع القادم (زي نظام كشف الـ <span dir="ltr">Spam</span> في <span dir="ltr">Gmail</span>).</li>
            <li style="margin-bottom: 10px;"><b>التعلم العميق (<span dir="ltr" style="color: #ff9933;">Deep Learning</span>):</b> فرع جوه الـ ML.. قائم على شبكات عصبية ضخمة (<span dir="ltr">Neural Networks</span>) بتتعلم أنماط معقدة جداً، وده اللي فتح الباب لتطبيقات زي <span dir="ltr">ChatGPT</span> والتعرف على الوجوه!</li>
        </ul>
        
        <hr style="border: 0.5px solid #444; margin: 25px 0;">
        
        <h3 style="direction: rtl; text-align: right; color: #fff; font-size: 20px; font-weight: 700; margin-bottom: 12px;">
            📌 مصطلحات تانية بتسمعها كتير
        </h3>
        <ul style="direction: rtl; text-align: right; margin-bottom: 20px; padding-right: 20px;">
            <li style="margin-bottom: 8px;"><b>Business Intelligence (BI):</b> مراقبة وتقييم أداء الشركة في الماضي والحاضر من خلال تقارير و<span dir="ltr">Dashboards</span> في <span dir="ltr">Power BI</span> أو <span dir="ltr">Tableau</span>.</li>
            <li style="margin-bottom: 8px;"><b>Big Data:</b> لما حجم البيانات يبقى ضخم جداً وسريع جداً (زي بيانات فيسبوك والبنوك) لدرجة إن الأدوات العادية مش قادرة تتعامل معاه.</li>
            <li style="margin-bottom: 8px;"><b>Data Mining:</b> عملية التنقيب القديمة لاكتشاف الأنماط والعلاقات المخفية جوة الداتا.</li>
        </ul>
        
        <hr style="border: 0.5px solid #444; margin: 25px 0;">
        
        <h3 style="direction: rtl; text-align: right; color: #fff; font-size: 20px; font-weight: 700; margin-bottom: 12px;">
            🎯 كيف يفكر المبتدئ وكيف يفكر المحترف؟
        </h3>
        <p style="direction: rtl; text-align: right; margin-bottom: 10px;">
            • <b>المبتدئ يسأل:</b> <i>"أنا أتعلم AI ولا Data Science ولا Machine Learning الأول؟"</i><br>
            • <b>المحترف يسأل:</b> <i>"إيه المشكلة اللي بحاول أحلها في الشغل؟ وإيه التخصص أو الأداة الأنسب لحلها؟"</i>
        </p>
        <p style="direction: rtl; text-align: right; margin-bottom: 20px;">
            علشان كده في الشركات الحقيقية، التخصصات دي مش بتتنافس.. التخصصات دي بتتكامل مع بعضها!
        </p>
        
        <p style="direction: rtl; text-align: right; background: rgba(255, 153, 0, 0.1); padding: 12px; border-radius: 6px; border-right: 4px solid #ff9933; margin-bottom: 0;">
            <b>💡 نصيحة ذهبية:</b> لا تبدد وقتك في محاولة تعلم كل شيء دفعة واحدة. خطوتك الأولى والأساسية دايماً هي البدء بتحليل البيانات (<span dir="ltr">Data Analysis</span>)، فهي حجر الأساس الذي سيفهمك كيف تدور عجلة البيانات قبل الغوص في الفروع المعقدة!
        </p>
        
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
            <div style="text-align: center; margin-top: 15px;">
                <a href="https://www.linkedin.com" target="_blank" style="background-color: #0a66c2; color: white; padding: 10px 20px; border-radius: 6px; text-decoration: none; font-weight: bold; display: inline-block;">
                    💬 ناقش هذا الدرس على لينكد إن
                </a>
            </div>
            """, unsafe_allow_html=True)


# --- Phase 05: Data Analytics Toolbox ---
    with st.expander("📁 Phase 05: Read: Data Analytics Toolbox (اضغط للقراءة الكاملة)", expanded=False):
        st.markdown("""
        <div dir="rtl" style="direction: rtl; text-align: right; font-family: sans-serif; font-size: 16px; line-height: 2.1; padding: 25px; background-color: #1a1a1a; border-radius: 12px; border: 1px solid #333; color: #e0e0e0;">
        
        <h2 style="direction: rtl; text-align: right; color: #ff4b4b; font-size: 24px; font-weight: 800; margin-bottom: 20px; border-bottom: 2px solid #333; padding-bottom: 10px;">
            🛠️ صندوق أدوات عالم البيانات: كيف تختار السلاح المناسب لمهمتك؟
        </h2>
        
        <p style="direction: rtl; text-align: right; margin-bottom: 15px;">
            أول ما تقرر تدخل عالم البيانات وتفتح يوتيوب.. هتتخض من كمية الأسماء: <span dir="ltr">(Python - SQL - Power BI - Spark - TensorFlow)</span>! 🤯<br>
            وبتلاقي نفسك واقف محتار وسؤال واحد شاغل بالك: <i>"هو أنا المفروض أتعلم كل البرامج والأدوات دي علشان أكون شغال صح؟"</i><br>
            في الدرس الخامس، تعالوا نفهم "صندوق أدوات عالم البيانات" (<span dir="ltr">Data Ecosystem</span>).. مش علشان نحفظ أسماء وخلاص، لكن علشان نعرف وظيفة كل أداة ومتى نستخدمها!
        </p>
        
        <hr style="border: 0.5px solid #444; margin: 25px 0;">
        
        <h3 style="direction: rtl; text-align: right; color: #fff; font-size: 20px; font-weight: 700; margin-bottom: 12px;">
            🧰 الحقيقة الأولى: أنت مش محتاج تحفظ كل الأدوات دي!
        </h3>
        <p style="direction: rtl; text-align: right; margin-bottom: 20px;">
            تخيل ميكانيكي عنده صندوق مفاتيح ضخم فيه 100 أداة مختلفة.. هل بيستخدمهم كلهم عشان يغير زيت العربية؟ طبعاً لأ!<br>
            الميكانيكي الشاطر بيعرف متى وإزاي يستخدم المفتاح المناسب للمشكلة اللي قدامه.. وده بالضبط اللي بيعمله المحترف في عالم البيانات.
        </p>
        
        <hr style="border: 0.5px solid #444; margin: 25px 0;">
        
        <h3 style="direction: rtl; text-align: right; color: #fff; font-size: 20px; font-weight: 700; margin-bottom: 12px;">
            📦 تقسيم الأدوات حسب دورها في اللعبة:
        </h3>
        
        <div style="direction: rtl; text-align: right; background: rgba(0, 0, 0, 0.2); padding: 15px; border-radius: 8px; margin-bottom: 15px;">
            <p style="margin-bottom: 5px; color: #4da6ff; font-weight: bold;">1. لغة البرمجة الأساسية (<span dir="ltr">Python vs R</span>):</p>
            <p style="margin-bottom: 0; opacity: 0.9;">• <span dir="ltr" style="color: #ff9933;">Python (الملكة):</span> الأكثر انتشاراً في الشركات العالمية (Google, Meta, Netflix)؛ سهلة، ذات مكتبات ضخمة، وبيئة <span dir="ltr">Jupyter Notebook</span> بتخليك تكتب الكود وتشوف النتائج والشارتات في نفس الصفحة زي "دفتر ملاحظات ذكي".<br>
            • <span dir="ltr">R:</span> لغة ممتازة في الإحصاء والبحث العلمي، لكن كفة Python هي الأرجح دائماً في سوق العمل.</p>
        </div>

        <div style="direction: rtl; text-align: right; background: rgba(0, 0, 0, 0.2); padding: 15px; border-radius: 8px; margin-bottom: 15px;">
            <p style="margin-bottom: 5px; color: #4da6ff; font-weight: bold;">2. البطل الخفي في كل وظيفة (<span dir="ltr">SQL</span>):</p>
            <p style="margin-bottom: 0; opacity: 0.9;">كتير بيقفروا للذكاء الاصطناعي ونسوا يتأسسوا في الـ <span dir="ltr" style="color: #ff9933;">SQL</span> وده أكبر خطأ! البيانات في الشغل متخزنة في قواعد بيانات (<span dir="ltr">Databases</span>) زي MySQL أو PostgreSQL، ومن غير SQL مش هتعرف تطلب البيانات أو تستخرجها أصلاً عشان تبدأ تحليلها.</p>
        </div>

        <div style="direction: rtl; text-align: right; background: rgba(0, 0, 0, 0.2); padding: 15px; border-radius: 8px; margin-bottom: 15px;">
            <p style="margin-bottom: 5px; color: #4da6ff; font-weight: bold;">3. أدوات العرض ولوحات التحكم (<span dir="ltr">Dashboards</span>):</p>
            <p style="margin-bottom: 0; opacity: 0.9;">• <span dir="ltr" style="color: #ff9933;">Power BI:</span> الأداة الأقوى والأكثر طلباً في سوق العمل، مدمجة بشكل ممتاز مع بيئة مايكروسوفت.<br>
            • <span dir="ltr">Tableau:</span> أداة قوية جداً ومشهورة في الشركات العالمية الكبرى.</p>
        </div>

        <div style="direction: rtl; text-align: right; background: rgba(0, 0, 0, 0.2); padding: 15px; border-radius: 8px; margin-bottom: 15px;">
            <p style="margin-bottom: 5px; color: #4da6ff; font-weight: bold;">4. المكتبات الجاهزة في بايثون (<span dir="ltr">Libraries</span>):</p>
            <p style="margin-bottom: 0; opacity: 0.9;">مش هتبدأ من الصفر، زمايلك طوروا مكتبات تسهل عليك المهمة:<br>
            • <span dir="ltr">Pandas & NumPy:</span> لتنظيف وتحليل البيانات وتجهيز الجداول.<br>
            • <span dir="ltr">Matplotlib & Seaborn:</span> لرسم المخططات البيانية.<br>
            • <span dir="ltr">Scikit-learn:</span> لبناء موديلات تعلم الآلة الأساسية.</p>
        </div>

        <div style="direction: rtl; text-align: right; background: rgba(0, 0, 0, 0.2); padding: 15px; border-radius: 8px; margin-bottom: 20px;">
            <p style="margin-bottom: 5px; color: #4da6ff; font-weight: bold;">5. أدوات العمالقة (<span dir="ltr">Big Data & Deep Learning</span>):</p>
            <p style="margin-bottom: 0; opacity: 0.9;">أدوات زي <span dir="ltr">Apache Spark</span> للبيانات الضخمة، أو <span dir="ltr">TensorFlow</span> للذكاء الاصطناعي المتقدم.. دي أدوات متقدمة ما تشغلش بالك بيها وإنت لسه في بداية الطريق!</p>
        </div>
        
        <hr style="border: 0.5px solid #444; margin: 25px 0;">
        
        <h3 style="direction: rtl; text-align: right; color: #fff; font-size: 20px; font-weight: 700; margin-bottom: 12px;">
            🗺️ خريطة الترتيب الصحيح لتعلم الأدوات:
        </h3>
        <ol style="direction: rtl; text-align: right; margin-bottom: 20px; padding-right: 20px;">
            <li style="margin-bottom: 6px;">أساسيات لغة البرمجة (<span dir="ltr">Python</span>).</li>
            <li style="margin-bottom: 6px;">استخراج وتعديل البيانات عبر (<span dir="ltr">SQL</span>).</li>
            <li style="margin-bottom: 6px;">معالجة البيانات وتنظيفها باستخدام (<span dir="ltr">Pandas & NumPy</span>).</li>
            <li style="margin-bottom: 6px;">تصميم لوحات العرض المتقدمة (<span dir="ltr">Power BI / Data Visualization</span>).</li>
            <li style="margin-bottom: 6px;">فهم الإحصاء (<span dir="ltr">Statistics</span>) وتفسير النتائج بدقة.</li>
            <li style="margin-bottom: 6px;">الانتقال لـ تعلم الآلة (<span dir="ltr">Machine Learning</span>) بعد التأسيس القوي.</li>
        </ol>

        <p style="direction: rtl; text-align: right; margin-bottom: 15px; background: rgba(255, 255, 255, 0.05); padding: 12px; border-radius: 8px;">
            <b>💡 من أين تحصل على داتا للتدريب العملي؟</b><br>
            يمكنك البدء بمنصات مجتمعية ممتازة للتدريب وبناء البورتفوليو مثل: <span dir="ltr" style="color: #4da6ff;">Kaggle</span>، أو قواعد بيانات الأمم المتحدة، ومرشحات بيانات الحكومات المفتوحة (<span dir="ltr">Open Data</span>).
        </p>
        
        <hr style="border: 0.5px solid #444; margin: 25px 0;">
        
        <h3 style="direction: rtl; text-align: right; color: #fff; font-size: 20px; font-weight: 700; margin-bottom: 12px;">
            🎯 عقلية المبتدئ vs عقلية المحترف
        </h3>
        <p style="direction: rtl; text-align: right; margin-bottom: 20px;">
            • <b>المبتدئ يسأل:</b> <i>"إيه أفضل أداة في العالم لازم أتعلمها دفعة واحدة؟"</i><br>
            • <b>المحترف يسأل:</b> <i>"إيه أنسب أداة في صندوق أدواتي تقدر تحل مشكلة البيزنس الحالية بأسرع وقت وأقل مجهود؟"</i>
        </p>
        
        <p style="direction: rtl; text-align: right; background: rgba(255, 153, 0, 0.1); padding: 12px; border-radius: 6px; border-right: 4px solid #ff9933; margin-bottom: 0;">
            <b>💡 نصيحة ذهبية:</b> لا تغرق نفسك في محاولة إتقان كل البرامج في وقت واحد. ركّز على إتقان الأدوات الأساسية (<span dir="ltr">Python & SQL</span>) واجعل هدفك هو حل المشاكل وليس جمع الشهادات أو حفظ الأكواد؛ فالمحترف الحقيقي يُقاس بمدى قدرته على تسليم "الحل" في وقته المناسب!
        </p>
        
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
            <div style="text-align: center; margin-top: 15px;">
                <a href="https://www.linkedin.com" target="_blank" style="background-color: #0a66c2; color: white; padding: 10px 20px; border-radius: 6px; text-decoration: none; font-weight: bold; display: inline-block;">
                    💬 ناقش هذا الدرس على لينكد إن
                </a>
            </div>
            """, unsafe_allow_html=True)
    

# --- Phase 06: Big Data ---
    with st.expander("📁 Phase 06: Read: Big Data (اضغط للقراءة الكاملة)", expanded=False):
        st.markdown("""
        <div dir="rtl" style="direction: rtl; text-align: right; font-family: sans-serif; font-size: 16px; line-height: 2.1; padding: 25px; background-color: #1a1a1a; border-radius: 12px; border: 1px solid #333; color: #e0e0e0;">
        
        <h2 style="direction: rtl; text-align: right; color: #ff4b4b; font-size: 24px; font-weight: 800; margin-bottom: 20px; border-bottom: 2px solid #333; padding-bottom: 10px;">
            🤯🌊 تخيل إنك في الثواني الخمسة اللي قريت فيها أول سطرين دول..
        </h2>
        
        <p style="direction: rtl; text-align: right; margin-bottom: 15px;">
            اتبعث ملايين الإيميلات، واتشافت آلاف الساعات على يوتيوب، وعشرات الآلاف دفعوا بفيزاتهم!<br>
            في الدرس السادس من سلسلتنا، محتاجين نجاوب على سؤال جوهري:<br>
            <i>"ليه ظهرت كل الأدوات المعقدة دي؟ وإيه هي الـ <span dir="ltr" style="color: #4da6ff;">Big Data</span> الحقيقية بعيداً عن التعقيد الأكاديمي؟"</i>
        </p>
        
        <hr style="border: 0.5px solid #444; margin: 25px 0;">
        
        <h3 style="direction: rtl; text-align: right; color: #fff; font-size: 20px; font-weight: 700; margin-bottom: 12px;">
            ❌ هل أي ملف <span dir="ltr">Excel</span> كبير يعتبر <span dir="ltr">Big Data</span>؟
        </h3>
        <p style="direction: rtl; text-align: right; margin-bottom: 20px;">
            أول وأكبر غلطة بيقع فيها المبتدئ إنه يفتكر إن الـ <span dir="ltr" style="color: #ff9933;">Big Data</span> معناها: <i>"عندي ملف Excel مساحته 10 جيجا على اللابتوب!"</i><br>
            الحقيقة أن البيانات الضخمة مش بتتقاس بالحجم فقط.. وعشان نفهمها صح، اتفق الخبراء على شفرة الـ <span dir="ltr">5Vs</span> الشهيرة اللي بتحدد هل إحنا قدام بيانات ضخمة فعلاً ولا لأ:
        </p>
        
        <h3 style="direction: rtl; text-align: right; color: #fff; font-size: 20px; font-weight: 700; margin-bottom: 12px;">
            🔑 شفرة الـ <span dir="ltr">5Vs</span>:
        </h3>
        
        <div style="direction: rtl; text-align: right; background: rgba(0, 0, 0, 0.2); padding: 15px; border-radius: 8px; margin-bottom: 15px;">
            <p style="margin-bottom: 5px; color: #4da6ff; font-weight: bold;">1. Volume (الحجم):</p>
            <p style="margin-bottom: 0; opacity: 0.9;">كمية بيانات مهولة بتتخزن يومياً. شركة زي <span dir="ltr">Netflix</span> بتسجل كل حركة للعميل: اتفرج على إيه، وقف إمتى، وغير الجودة كام مرة!</p>
        </div>

        <div style="direction: rtl; text-align: right; background: rgba(0, 0, 0, 0.2); padding: 15px; border-radius: 8px; margin-bottom: 15px;">
            <p style="margin-bottom: 5px; color: #4da6ff; font-weight: bold;">2. Velocity (السرعة):</p>
            <p style="margin-bottom: 0; opacity: 0.9;">البيانات مش بس ضخمة، دي بتدفق بسرعة الصاروخ! في بورصة الأسهم مثلاً، لو النظام استنى دقيقة واحدة عشان يحلل البيانات.. الصفقة بتتأخر والشركة تخسر ملايين.</p>
        </div>

        <div style="direction: rtl; text-align: right; background: rgba(0, 0, 0, 0.2); padding: 15px; border-radius: 8px; margin-bottom: 15px;">
            <p style="margin-bottom: 5px; color: #4da6ff; font-weight: bold;">3. Variety (التنوع):</p>
            <p style="margin-bottom: 0; opacity: 0.9;">زمان البيانات كانت أرقام وجداول بس (<span dir="ltr">Structured Data</span>). النهاردة 80% من البيانات غير منظمة (<span dir="ltr">Unstructured Data</span>) زي: الصور، الفيديوهات، بصمة الصوت، وموقع الـ <span dir="ltr">GPS</span>.</p>
        </div>

        <div style="direction: rtl; text-align: right; background: rgba(0, 0, 0, 0.2); padding: 15px; border-radius: 8px; margin-bottom: 15px;">
            <p style="margin-bottom: 5px; color: #4da6ff; font-weight: bold;">4. Veracity (المصداقية والجودة):</p>
            <p style="margin-bottom: 0; opacity: 0.9;">هل البيانات دي موثوقة أصلاً؟ لو بنيت موديل ذكاء اصطناعي عبقري على بيانات مغلوطة أو قديمة، هتطلع نتائج كارثية!<br>
            وفي المجال بنقول مقولة شهيرة:<br>
            <span dir="ltr" style="display: block; background: rgba(0, 0, 0, 0.3); padding: 8px; border-radius: 6px; margin: 8px 0; color: #ff9933; text-align: center; font-weight: bold;">"Garbage In, Garbage Out (GIGO)"</span>
            (لو دخلت داتا زبالة.. هتطلع نتائج زبالة!).</p>
        </div>

        <div style="direction: rtl; text-align: right; background: rgba(0, 0, 0, 0.2); padding: 15px; border-radius: 8px; margin-bottom: 20px;">
            <p style="margin-bottom: 5px; color: #4da6ff; font-weight: bold;">5. Value (القيمة البيزنس - الأهم):</p>
            <p style="margin-bottom: 0; opacity: 0.9;">لو عندك 100 تيرابايت بيانات ومحطوطة على سيرفر ومش بتستفيد منها.. مالهاش أي قيمة! الهدف مش جمع البيانات، الهدف: <i>"إزاي المعلومة دي تزود المبيعات وتطور القرار؟"</i></p>
        </div>
        
        <hr style="border: 0.5px solid #444; margin: 25px 0;">
        
        <h3 style="direction: rtl; text-align: right; color: #fff; font-size: 20px; font-weight: 700; margin-bottom: 12px;">
            🛠️ حل المشكلة: إزاي بنعالج المليارات دي؟
        </h3>
        <p style="direction: rtl; text-align: right; margin-bottom: 15px;">
            لما السيرفر العادي ما بيقدرش يشيل البيانات دي، بنلجأ لأدوات الـ <span dir="ltr">Big Data</span>:
        </p>
        <ul style="direction: rtl; text-align: right; margin-bottom: 20px; padding-right: 20px;">
            <li style="margin-bottom: 8px;"><b>Hadoop:</b> بدل ما نخزن البيانات على جهاز واحد، بنوزعها على شبكة مكونة من مئات الأجهزة.</li>
            <li style="margin-bottom: 8px;"><b>MapReduce:</b> بدل ما جهاز واحد يحلل مليار سطر، بنقسم المهمة على 100 جهاز يشتغلوا في نفس اللحظة (<span dir="ltr">Parallel Processing</span>).</li>
            <li style="margin-bottom: 8px;"><b>Apache Spark:</b> التطور السريع والحديث.. بيعالج البيانات جوة الذاكرة (<span dir="ltr">In-Memory</span>)، وهو الأسرع والأكثر استخداماً في الشركات حالياً.</li>
        </ul>
        
        <hr style="border: 0.5px solid #444; margin: 25px 0;">
        
        <h3 style="direction: rtl; text-align: right; color: #fff; font-size: 20px; font-weight: 700; margin-bottom: 12px;">
            🎯 عقلية المبتدئ vs عقلية المحترف
        </h3>
        <p style="direction: rtl; text-align: right; margin-bottom: 15px;">
            • <b>المبتدئ يقول:</b> <i>"عندي بيانات كتير، يلا نستخدم Spark و Hadoop!"</i><br>
            • <b>المحترف يسأل:</b><br>
            - هل الأدوات العادية (<span dir="ltr">SQL & Python</span>) فعلاً عاجزة عن التعامل مع البيانات دي؟<br>
            - هل سرعة تدفق البيانات محتاجة بنية سحابية ضخمة؟<br>
            - هل تكلفة أدوات الـ <span dir="ltr">Big Data</span> هتطلع قيمة تجارية حقيقية ترجع التكلفة دي؟
        </p>
        
        <p style="direction: rtl; text-align: right; background: rgba(255, 153, 0, 0.1); padding: 12px; border-radius: 6px; border-right: 4px solid #ff9933; margin-bottom: 0;">
            <b>💡 نصيحة ذهبية:</b> إذا كنت تبدأ رحلتك كمحلل بيانات (<span dir="ltr">Data Analyst</span>)، فلن يُطلب منك بناء أنظمة <span dir="ltr">Big Data</span> معقدة، فمعظم مشاكل الشركات تُحل بكفاءة عالية جداً باستخدام الأدوات التقليدية الذكية. افهم الفكرة العامة للـ <span dir="ltr">5Vs</span> ولا تدع مصطلحات التضخم البياناتية تشتت تركيزك عن أساسيات التحليل السليم!
        </p>
        
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
            <div style="text-align: center; margin-top: 15px;">
                <a href="https://www.linkedin.com" target="_blank" style="background-color: #0a66c2; color: white; padding: 10px 20px; border-radius: 6px; text-decoration: none; font-weight: bold; display: inline-block;">
                    💬 ناقش هذا الدرس على لينكد إن
                </a>
            </div>
            """, unsafe_allow_html=True)


# --- Phase 07: Data Visualization ---
    with st.expander("📁 Phase 07: Read: Data Visualization (اضغط للقراءة الكاملة)", expanded=False):
        st.markdown("""
        <div dir="rtl" style="direction: rtl; text-align: right; font-family: sans-serif; font-size: 16px; line-height: 2.1; padding: 25px; background-color: #1a1a1a; border-radius: 12px; border: 1px solid #333; color: #e0e0e0;">
        
        <h2 style="direction: rtl; text-align: right; color: #ff4b4b; font-size: 24px; font-weight: 800; margin-bottom: 20px; border-bottom: 2px solid #333; padding-bottom: 10px;">
            📺 تخيل إن شركة صرفت ملايين عشان إعلان تلفزيوني عبقري.. ثم أذاعوه في الراديو! 🤦‍♂️
        </h2>
        
        <p style="direction: rtl; text-align: right; margin-bottom: 15px;">
            الإعلان نفسه عبقري وممتاز.. لكن طريقة عرضه ومكانه كانوا غلط.. والنتيجة؟ فشل ذريع وضياع للملايين!<br>
            في الدرس السابع من سلسلتنا، تعالوا نتكلم عن <b>تمثيل البيانات بصرياً (<span dir="ltr" style="color: #4da6ff;">Data Visualization</span>)</b>.. وليه هو السلاح الأقوى في إيد أي محلل بيانات!
        </p>
        
        <hr style="border: 0.5px solid #444; margin: 25px 0;">
        
        <h3 style="direction: rtl; text-align: right; color: #fff; font-size: 20px; font-weight: 700; margin-bottom: 12px;">
            🎨 هل العرض مجرد رسم شارتات أشكالها حلوة؟
        </h3>
        <p style="direction: rtl; text-align: right; margin-bottom: 15px;">
            تخيل لو عندك شيت <span dir="ltr">Excel</span> فيه 500 ألف صف بيانات، ودخل عليك المدير يسألك: <i>"إيه أكتر منتج أتباع السنة دي وليه المبيعات وقعت الشهر اللي فات؟"</i><br>
            هل هيقعد يقرا الـ 500 ألف صف؟ طبعاً لأ!
        </p>
        <p style="direction: rtl; text-align: right; margin-bottom: 20px;">
            هنا بييجي دور الـ <span dir="ltr">Data Visualization</span>: هو مش مجرد ألوان ورسومات للتجميل.. هو عملية تحويل الأرقام المعقدة لـ <span dir="ltr">Dashboards & Charts</span> بتخلي صاحب القرار يفهم القصة كلها في ثوانٍ معدودة ويخرج بقرار حاسم!
        </p>
        
        <hr style="border: 0.5px solid #444; margin: 25px 0;">
        
        <h3 style="direction: rtl; text-align: right; color: #fff; font-size: 20px; font-weight: 700; margin-bottom: 12px;">
            👥 القواعد الذهبية: "اعرف جمهورك الأول!"
        </h3>
        <p style="direction: rtl; text-align: right; margin-bottom: 15px;">
            الخطأ القاتل اللي بيقع فيه المبتدئ إنه بيعمل تقرير واحد بنفس الشكل لكل الناس.. وده غلط! المحترف بيغير طريقة العرض حسب الشخص اللي هيشوف البيانات:
        </p>
        
        <div style="direction: rtl; text-align: right; background: rgba(0, 0, 0, 0.2); padding: 15px; border-radius: 8px; margin-bottom: 15px;">
            <p style="margin-bottom: 5px; color: #4da6ff; font-weight: bold;">• محلل البيانات (<span dir="ltr">Data Analyst</span>):</p>
            <p style="margin-bottom: 0; opacity: 0.9;">تعرض له التفاصيل التقنية، الخوارزميات، والرسوم التفصيلية.</p>
        </div>

        <div style="direction: rtl; text-align: right; background: rgba(0, 0, 0, 0.2); padding: 15px; border-radius: 8px; margin-bottom: 15px;">
            <p style="margin-bottom: 5px; color: #4da6ff; font-weight: bold;">• مدير المبيعات:</p>
            <p style="margin-bottom: 0; opacity: 0.9;">مش مهتم بالبرمجة ولا الكود، عايز يعرف بس: <i>"المبيعات زادت ولا قلت؟ وإيه السبب؟ ونعمل إيه؟"</i></p>
        </div>

        <div style="direction: rtl; text-align: right; background: rgba(0, 0, 0, 0.2); padding: 15px; border-radius: 8px; margin-bottom: 20px;">
            <p style="margin-bottom: 5px; color: #4da6ff; font-weight: bold;">• رئيس الشركة (<span dir="ltr">CEO</span>):</p>
            <p style="margin-bottom: 0; opacity: 0.9;">الراجل ده عنده 10 دقائق بالظبط! محتاج <span dir="ltr">Dashboard</span> بسيطة فيها أهم 4 أو 5 مؤشرات قياسية (<span dir="ltr">KPIs</span>) تخليه ياخد قرار مصيري.</p>
        </div>
        
        <p style="direction: rtl; text-align: right; margin-bottom: 20px; background: rgba(255, 255, 255, 0.05); padding: 12px; border-radius: 8px; border-right: 4px solid #ff4b4b;">
            وهي دي المهارة الأغلى في سوق العمل حالياً: <b>حكاية القصة بالبيانات (<span dir="ltr" style="color: #ff9933;">Data Storytelling</span>)</b>!
        </p>
        
        <hr style="border: 0.5px solid #444; margin: 25px 0;">
        
        <h3 style="direction: rtl; text-align: right; color: #fff; font-size: 20px; font-weight: 700; margin-bottom: 12px;">
            📊 إزاي تختار الرسم البياني الصح؟
        </h3>
        <p style="direction: rtl; text-align: right; margin-bottom: 10px;">مش بنختار الشارت عشان شكله جميل.. بنختاره حسب نوع المعلومة:</p>
        <ul style="direction: rtl; text-align: right; margin-bottom: 20px; padding-right: 20px;">
            <li style="margin-bottom: 8px;"><b><span dir="ltr">Bar Chart</span>:</b> للمقارنة المباشرة بين الأقسام والفئات.</li>
            <li style="margin-bottom: 8px;"><b><span dir="ltr">Line Chart</span>:</b> لمتابعة تغير الأرقام والمبيعات مع الزمن.</li>
            <li style="margin-bottom: 8px;"><b><span dir="ltr">Scatter Plot</span>:</b> لاكتشاف العلاقة والتأثير بين متغيرين.</li>
            <li style="margin-bottom: 8px;"><b><span dir="ltr">Heatmap</span>:</b> لإظهار كشوف الأنماط والكثافة.</li>
        </ul>
        <p style="direction: rtl; text-align: right; margin-bottom: 20px; color: #ff9933; font-size: 15px;">
            💡 <i>نصيحة سريعة: ابعد عن الـ Pie Chart الكتير لأنها بتبدو مضللة للعين لو الفئات زيادة عن 3.</i>
        </p>
        
        <hr style="border: 0.5px solid #444; margin: 25px 0;">
        
        <h3 style="direction: rtl; text-align: right; color: #fff; font-size: 20px; font-weight: 700; margin-bottom: 12px;">
            🛠️ أهم الأدوات في الشغل الحقيقي
        </h3>
        <ul style="direction: rtl; text-align: right; margin-bottom: 20px; padding-right: 20px;">
            <li style="margin-bottom: 8px;"><b><span dir="ltr">Microsoft Excel</span>:</b> البداية السريعة والأساسية لأي تحليل بسيط.</li>
            <li style="margin-bottom: 8px;"><b><span dir="ltr">Power BI</span>:</b> الأداة الأكثر طلباً في سوق العمل، بتسمح لك تبني Dashboards تفاعلية وتربط أكتر من مصدر بيانات.</li>
            <li style="margin-bottom: 8px;"><b><span dir="ltr">Tableau</span>:</b> أداة قوية جداً ومشهورة في الشركات العالمية الكبرى.</li>
        </ul>
        
        <h3 style="direction: rtl; text-align: right; color: #fff; font-size: 20px; font-weight: 700; margin-bottom: 12px;">
            ❌ أخطاء شائعة تبعد عنها فوراً:
        </h3>
        <ul style="direction: rtl; text-align: right; margin-bottom: 20px; padding-right: 20px;">
            <li style="margin-bottom: 6px;">استخدام ألوان كتيرة ومزعجة بدون معنى واضح.</li>
            <li style="margin-bottom: 6px;">وضع كمية معلومات ضخمة جداً في شاشة واحدة تتوه العين.</li>
            <li style="margin-bottom: 6px;">الاهتمام بالجماليات ونسيان السؤال الجوهري: <i>"إيه القرار المفروض نطلع بيه هنا؟"</i></li>
        </ul>
        
        <p style="direction: rtl; text-align: right; background: rgba(255, 153, 0, 0.1); padding: 12px; border-radius: 6px; border-right: 4px solid #ff9933; margin-bottom: 0;">
            <b>💡 نصيحة ذهبية:</b> تذكر دائماً أن التحليل العبقري من غير عرض بسيط وقصة واضحة قيمته صفر! صمم تقاريرك بعقلية المشاهد الذي لا يملك وقتاً، واجعل هدفك الأول هو توصيل "القرار" لا استعراض المهارات البرمجية أو الأشكال المعقدة.
        </p>
        
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
            <div style="text-align: center; margin-top: 15px;">
                <a href="https://www.linkedin.com" target="_blank" style="background-color: #0a66c2; color: white; padding: 10px 20px; border-radius: 6px; text-decoration: none; font-weight: bold; display: inline-block;">
                    💬 ناقش هذا الدرس على لينكد إن
                </a>
            </div>
            """, unsafe_allow_html=True)

# --- Phase 08: Machine Learning Basics ---
    with st.expander("📁 Phase 08: Read: Machine Learning Basics (اضغط للقراءة الكاملة)", expanded=False):
        st.markdown("""
        <div dir="rtl" style="direction: rtl; text-align: right; font-family: sans-serif; font-size: 16px; line-height: 2.1; padding: 25px; background-color: #1a1a1a; border-radius: 12px; border: 1px solid #333; color: #e0e0e0;">
        
        <h2 style="direction: rtl; text-align: right; color: #ff4b4b; font-size: 24px; font-weight: 800; margin-bottom: 20px; border-bottom: 2px solid #333; padding-bottom: 10px;">
            🤖 لو من 20 سنة حد قالك إن جهاز صغير في إيدك هيعرف أفكارك.. كنت هتقول بيحلم!
        </h2>
        
        <p style="direction: rtl; text-align: right; margin-bottom: 15px;">
            لكن النهاردة ده بقى طبيعي جداً في حياتنا اليومية..<br>
            بعد ما فهمنا يعني إيه بيانات، وإزاي بنجمعها، وننظفها، ونعرضها في تقارير.. بييجي السؤال المنطقي:<br>
            <i>"إيه الخطوة العبقرية اللي بعد كده؟"</i><br>
            الإجابة هي: <b>تعلم الآلة (<span dir="ltr" style="color: #4da6ff;">Machine Learning</span>)</b>!<br>
            في الدرس الثامن، تعالوا نفهم إزاي التكنولوجيا دي غيرت طريقة تفكير البرمجة في العالم.
        </p>
        
        <hr style="border: 0.5px solid #444; margin: 25px 0;">
        
        <h3 style="direction: rtl; text-align: right; color: #fff; font-size: 20px; font-weight: 700; margin-bottom: 12px;">
            🔄 الثورة الحقيقية: الفرق بين البرمجة العادية والـ <span dir="ltr">Machine Learning</span>!
        </h3>
        
        <div style="direction: rtl; text-align: right; background: rgba(0, 0, 0, 0.2); padding: 15px; border-radius: 8px; margin-bottom: 15px;">
            <p style="margin-bottom: 5px; color: #4da6ff; font-weight: bold;">• في البرمجة التقليدية، أنت اللي بتكتب القواعد بنفسك:</p>
            <p style="margin-bottom: 0; opacity: 0.9; text-align: center; background: rgba(0,0,0,0.3); padding: 8px; border-radius: 6px; font-family: monospace;" dir="ltr">Rules + Data ➔ Program ➔ Output</p>
            <p style="margin-top: 5px; margin-bottom: 0; opacity: 0.8; font-size: 14px;">(مثال: لو درجة الطالب أكتر من 50 يكتب ناجح، لو أقل يكتب راسب).</p>
        </div>

        <div style="direction: rtl; text-align: right; background: rgba(0, 0, 0, 0.2); padding: 15px; border-radius: 8px; margin-bottom: 20px;">
            <p style="margin-bottom: 5px; color: #4da6ff; font-weight: bold;">• أما في الـ <span dir="ltr">Machine Learning</span>، العكس تماماً هو اللي بيحصل:</p>
            <p style="margin-bottom: 0; opacity: 0.9; text-align: center; background: rgba(0,0,0,0.3); padding: 8px; border-radius: 6px; font-family: monospace;" dir="ltr">Data + Output ➔ Model ➔ Rules</p>
            <p style="margin-top: 5px; margin-bottom: 0; opacity: 0.8; font-size: 14px;">(مثال: بتدي الموديل مليون صورة قطة وكلب متصنفة، وهو بيستنتج النمط بنفسه ويتوقع القادم!).</p>
        </div>
        
        <hr style="border: 0.5px solid #444; margin: 25px 0;">
        
        <h3 style="direction: rtl; text-align: right; color: #fff; font-size: 20px; font-weight: 700; margin-bottom: 12px;">
            🧠 فزورة: هل الكمبيوتر فعلاً "بيفكر"؟
        </h3>
        <p style="direction: rtl; text-align: right; margin-bottom: 20px;">
            علمياً.. الكمبيوتر لا يفكر ولا يشعر كالإنسان! كلمة "الآلة بتفكر" هي كلمة مجازية للتبسيط.. الكمبيوتر كل اللي بيعمله إنه بيحسب أرجحية وإحصائيات رياضية معقدة جداً لاكتشاف الأنماط (<span dir="ltr">Patterns</span>) في البيانات، ويتوقع القادم بناءً عليها.
        </p>
        
        <hr style="border: 0.5px solid #444; margin: 25px 0;">
        
        <h3 style="direction: rtl; text-align: right; color: #fff; font-size: 20px; font-weight: 700; margin-bottom: 12px;">
            🎓 الأنواع الأربعة للـ <span dir="ltr">Machine Learning</span> (بأبسط طريقة)
        </h3>
        <ul style="direction: rtl; text-align: right; margin-bottom: 20px; padding-right: 20px;">
            <li style="margin-bottom: 10px;"><b>التعلم بإشراف (<span dir="ltr" style="color: #ff9933;">Supervised Learning</span>):</b> بتديله البيانات ومعاها الإجابة النموذجية (<span dir="ltr">Labels</span>) عشان يتعلم منها. (مثل كشف الـ <span dir="ltr">Spam</span> وتوقعات الأسعار).</li>
            <li style="margin-bottom: 10px;"><b>التعلم بدون إشراف (<span dir="ltr" style="color: #ff9933;">Unsupervised Learning</span>):</b> بتديله البيانات من غير إجابات، وهو يستكشف النمط بنفسه. (مثل تقسيم العملاء لمجموعات <span dir="ltr">Clustering</span>).</li>
            <li style="margin-bottom: 10px;"><b>التعلم شبه المشرف (<span dir="ltr">Semi-Supervised</span>):</b> مزيج بينهم؛ جزء صغير من البيانات متصنف والجزء الأكبر لأ.</li>
            <li style="margin-bottom: 10px;"><b>التعلم بالتعزيز (<span dir="ltr" style="color: #ff9933;">Reinforcement Learning</span>):</b> التدريب بمبدأ الثواب والعقاب! الموديل بيجرب، لو صح ياخد مكافأة (<span dir="ltr">Reward</span>) ولو غلط ياخد عقاب (<span dir="ltr">Penalty</span>). (مستخدم في السيارات ذاتية القيادة).</li>
        </ul>
        
        <hr style="border: 0.5px solid #444; margin: 25px 0;">
        
        <h3 style="direction: rtl; text-align: right; color: #fff; font-size: 20px; font-weight: 700; margin-bottom: 12px;">
            🔄 دورة حياة مشروع الـ <span dir="ltr">Machine Learning</span> في الشركات
        </h3>
        <p style="direction: rtl; text-align: right; margin-bottom: 10px;">مشروع الـ ML مش مجرد كود بيكتب في يوم.. دي رحلة كاملة:</p>
        <ol style="direction: rtl; text-align: right; margin-bottom: 20px; padding-right: 20px;">
            <li style="margin-bottom: 6px;">جمع البيانات (<span dir="ltr">Collect Data</span>).</li>
            <li style="margin-bottom: 6px;">تنظيف البيانات وتجهيزها (<span dir="ltr">Data Cleaning & Preprocessing</span>).</li>
            <li style="margin-bottom: 6px;">تقسيم البيانات (مثلاً 80% للتدريب، و20% للاختبار).</li>
            <li style="margin-bottom: 6px;">تدريب الموديل وتقييم أدائه (<span dir="ltr">Training & Testing</span>).</li>
            <li style="margin-bottom: 6px;">نشر الموديل في الشغل الحقيقي ومتابعته (<span dir="ltr">Deployment & Monitoring</span>).</li>
        </ol>
        
        <hr style="border: 0.5px solid #444; margin: 25px 0;">
        
        <h3 style="direction: rtl; text-align: right; color: #fff; font-size: 20px; font-weight: 700; margin-bottom: 12px;">
            💡 هل الذكاء الاصطناعي هيستبدل البشر؟
        </h3>
        <p style="direction: rtl; text-align: right; margin-bottom: 20px;">
            الحقيقة الأكثر توازناً هي: الذكاء الاصطناعي مش هيستبدل كل البشر.. لكن الشخص اللي بيعرف يستخدم أدوات الذكاء الاصطناعي هيستبدل الشخص اللي مابيعرفش يستخدمها!<br>
            وتظل لغة <span dir="ltr" style="color: #4da6ff;">Python</span> هي الملك بلا منازع، ومكتبة <span dir="ltr">scikit-learn</span> هي البداية الأهم لأي حد حابب يدخل عالم الـ ML بالتطبيق العملي.
        </p>
        
        <p style="direction: rtl; text-align: right; background: rgba(255, 153, 0, 0.1); padding: 12px; border-radius: 6px; border-right: 4px solid #ff9933; margin-bottom: 0;">
            <b>💡 نصيحة ذهبية:</b> لا تخف من تطور الذكاء الاصطناعي، بل اجعله مساعدك الشخصي لتسريع مهامك. الآلة تحسب الأرقام والأنماط، لكن العقل البشري هو وحده القادر على طرح "السؤال الصحيح" وتوجيه التحليل نحو القيمة الحقيقية!
        </p>
        
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
            <div style="text-align: center; margin-top: 15px;">
                <a href="https://www.linkedin.com" target="_blank" style="background-color: #0a66c2; color: white; padding: 10px 20px; border-radius: 6px; text-decoration: none; font-weight: bold; display: inline-block;">
                    💬 ناقش هذا الدرس على لينكد إن
                </a>
            </div>
            """, unsafe_allow_html=True)


# --- Phase 09: Data Career Roadmap ---
    with st.expander("📁 Phase 09: Read: Data Career Roadmap (اضغط للقراءة الكاملة)", expanded=False):
        st.markdown("""
        <div dir="rtl" style="direction: rtl; text-align: right; font-family: sans-serif; font-size: 16px; line-height: 2.1; padding: 25px; background-color: #1a1a1a; border-radius: 12px; border: 1px solid #333; color: #e0e0e0;">
        
        <h2 style="direction: rtl; text-align: right; color: #ff4b4b; font-size: 24px; font-weight: 800; margin-bottom: 20px; border-bottom: 2px solid #333; padding-bottom: 10px;">
            ⚽ تخيل لو شركة زي <span dir="ltr">Amazon</span> أو <span dir="ltr">Spotify</span> تعين شخص واحد لكل المهام!
        </h2>
        
        <p style="direction: rtl; text-align: right; margin-bottom: 15px;">
            تفتكر الشغل هيطلع إزاي؟ زي فريق كرة القدم بالضبط! المدافع ليه دور، صانع الألعاب ليه دور، والمهاجم هو اللي بيجيب الجول..<br>
            في الدرس التاسع من سلسلتنا النظري ، جه الوقت نجاوب على السؤال الأهم:<br>
            <i>"مين بيعمل إيه في سوق العمل؟ وإيه الفرق الحقيقي بين المسميات الوظيفية في مجال البيانات؟"</i>
        </p>
        
        <hr style="border: 0.5px solid #444; margin: 25px 0;">
        
        <h3 style="direction: rtl; text-align: right; color: #fff; font-size: 20px; font-weight: 700; margin-bottom: 12px;">
            🗺️ خريطة وظائف عالم البيانات (<span dir="ltr">Data Industry Map</span>)
        </h3>
        
        <div style="direction: rtl; text-align: right; background: rgba(0, 0, 0, 0.2); padding: 15px; border-radius: 8px; margin-bottom: 15px;">
            <p style="margin-bottom: 5px; color: #4da6ff; font-weight: bold;">1. الـ Data Detective (محلل البيانات - <span dir="ltr">Data Analyst</span>):</p>
            <p style="margin-bottom: 0; opacity: 0.9;">أقرب دور للمبتدئين! عامل زي "المحقق"، بيمسك البيانات ويستجوبها يسألها: <i>"ليه المبيعات قلت؟ مين أفضل عميل؟ وأني فرع بيخسر؟"</i>.<br>أدواته الرئيسية: (<span dir="ltr">SQL - Python - Power BI - Excel</span>).</p>
        </div>

        <div style="direction: rtl; text-align: right; background: rgba(0, 0, 0, 0.2); padding: 15px; border-radius: 8px; margin-bottom: 15px;">
            <p style="margin-bottom: 5px; color: #4da6ff; font-weight: bold;">2. الـ Data Architect (المهندس المعماري للبيانات):</p>
            <p style="margin-bottom: 0; opacity: 0.9;">الشخص اللي بيصمم شكل البيانات والرسم الهندسي (<span dir="ltr">Blueprint</span>) جوة الشركة، بيحدد البيانات هتتخزن فين، شكل الجداول، الأمان، والعلاقات بينهم.</p>
        </div>

        <div style="direction: rtl; text-align: right; background: rgba(0, 0, 0, 0.2); padding: 15px; border-radius: 8px; margin-bottom: 15px;">
            <p style="margin-bottom: 5px; color: #4da6ff; font-weight: bold;">3. الـ Data Engineer (مهندس البنية التحتية):</p>
            <p style="margin-bottom: 0; opacity: 0.9;">من أقوى الوظائف طلباً! هو اللي بيبني المطبخ والمواسير (<span dir="ltr">Data Pipelines</span>)، يجمع البيانات من مصادر مختلفة ويوصلها نظيفة وجاهزة للمحللين. من غيره الفريق كله بيفصل!</p>
        </div>

        <div style="direction: rtl; text-align: right; background: rgba(0, 0, 0, 0.2); padding: 15px; border-radius: 8px; margin-bottom: 15px;">
            <p style="margin-bottom: 5px; color: #4da6ff; font-weight: bold;">4. الـ Business Analyst (محلل الأعمال):</p>
            <p style="margin-bottom: 0; opacity: 0.9;">بيتركز أكتر على "مشكلة البيزنس" نفسها وتطوير العمليات: <i>"ليه العملاء بيشتكوا؟ وإزاي نطور خدماتنا؟"</i> بينما الـ Data Analyst بيكتفي بتحليل البيانات الرقمية.</p>
        </div>

        <div style="direction: rtl; text-align: right; background: rgba(0, 0, 0, 0.2); padding: 15px; border-radius: 8px; margin-bottom: 20px;">
            <p style="margin-bottom: 5px; color: #4da6ff; font-weight: bold;">5. الـ Curious Data Wizard (عالم البيانات - <span dir="ltr">Data Scientist</span>):</p>
            <p style="margin-bottom: 0; opacity: 0.9;">أهم وأصعب دور! بيمزج بين البرمجة، الإحصاء، والـ <span dir="ltr">Machine Learning</span> عشان يبني موديلات ذكية بتتنبأ بالمستقبل (زي توقع العملاء اللي هيسيبوا الشركة أو نظام التوصيات في <span dir="ltr">Netflix</span>).</p>
        </div>
        
        <hr style="border: 0.5px solid #444; margin: 25px 0;">
        
        <h3 style="direction: rtl; text-align: right; color: #fff; font-size: 20px; font-weight: 700; margin-bottom: 12px;">
            🎧 إزاي مشروع واحد بيشتغل في شركة زي <span dir="ltr">Spotify</span>؟
        </h3>
        <ul style="direction: rtl; text-align: right; margin-bottom: 20px; padding-right: 20px;">
            <li style="margin-bottom: 8px;"><b><span dir="ltr">Data Engineer</span>:</b> بيجمع بيانات آلاف الأغاني وتشغيل المستخدمين.</li>
            <li style="margin-bottom: 8px;"><b><span dir="ltr">Data Architect</span>:</b> بيصمم هيكل تخزين البيانات دي بأمان.</li>
            <li style="margin-bottom: 8px;"><b><span dir="ltr">Data Analyst</span>:</b> بيحلل أكثر الأغاني والمغنيين استماعاً السنة دي.</li>
            <li style="margin-bottom: 8px;"><b><span dir="ltr">Data Scientist</span>:</b> بيبني نموذج الذكاء الاصطناعي اللي بيرشح الأغاني الجديدة.</li>
            <li style="margin-bottom: 8px;"><b><span dir="ltr">Business Analyst</span>:</b> بياخد النتائج دي ويترجمها لقرارات استثمارية مع المطربين.</li>
        </ul>
        
        <hr style="border: 0.5px solid #444; margin: 25px 0;">
        
        <h3 style="direction: rtl; text-align: right; color: #fff; font-size: 20px; font-weight: 700; margin-bottom: 12px;">
            🎯 إيه الخطة الموصى بيها للبداية الصح؟
        </h3>
        <p style="direction: rtl; text-align: right; margin-bottom: 15px;">
            بما إن محاولة القفز المباشر لـ <span dir="ltr">Data Science</span> بتسبب تشتت لكثير من الناس.. التدرج المنطقي والعملي في سوق العمل بيكون كالتالي:
        </p>
        <p style="direction: ltr; text-align: center; background: rgba(0,0,0,0.3); padding: 12px; border-radius: 8px; color: #4da6ff; font-weight: bold; margin-bottom: 20px; font-size: 14px;">
            Computer Basics ➔ Python & SQL ➔ Power BI & Excel ➔ Data Analysis ➔ Statistics ➔ Machine Learning ➔ Data Science
        </p>
        
        <p style="direction: rtl; text-align: right; background: rgba(255, 153, 0, 0.1); padding: 12px; border-radius: 6px; border-right: 4px solid #ff9933; margin-bottom: 0;">
            <b>💡 ختام السلسلة ونقطة انطلاقك:</b> بكده نكون قفلنا "الصورة الكاملة" لرحلة البيانات من الصفر! فهمت المفهوم، الأدوات، طريقة التفكير، والخريطة الوظيفية !
        </p>
        
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
            <div style="text-align: center; margin-top: 15px;">
                <a href="https://www.linkedin.com" target="_blank" style="background-color: #0a66c2; color: white; padding: 10px 20px; border-radius: 6px; text-decoration: none; font-weight: bold; display: inline-block;">
                    💬 ناقش هذا الدرس على لينكد إن
                </a>
            </div>
            """, unsafe_allow_html=True)


# --- Phase 10: Advanced Insights & Data Ethics (Bonus) ---
    with st.expander("📁 Phase 10: Read: Advanced Insights & Data Ethics (اضغط للقراءة الكاملة)", expanded=False):
        st.markdown("""
        <div dir="rtl" style="direction: rtl; text-align: right; font-family: sans-serif; font-size: 16px; line-height: 2.1; padding: 25px; background-color: #1a1a1a; border-radius: 12px; border: 1px solid #333; color: #e0e0e0;">
        
        <h2 style="direction: rtl; text-align: right; color: #ff4b4b; font-size: 24px; font-weight: 800; margin-bottom: 20px; border-bottom: 2px solid #333; padding-bottom: 10px;">
            🚀 التكات المخفية: كواليس البيانات، أخلاقيات الذكاء الاصطناعي، وقرارات الملايين!
        </h2>
        
        <p style="direction: rtl; text-align: right; margin-bottom: 15px;">
            في الدرس العاشر والأخير من رحلتنا النظرية، هنقفل الدائرة ونعرف الأسرار اللي مش بتتقال في الكورسات العادية..<br>
            <i>"إزاي البيانات بتوصلنا أصلاً؟ وإيه الخطورة لو استخدمناها غلط؟ وإزاي الشركات الكبيرة مش بتخمن في قراراتها أبداً؟"</i>
        </p>
        
        <hr style="border: 0.5px solid #444; margin: 25px 0;">
        
        <h3 style="direction: rtl; text-align: right; color: #fff; font-size: 20px; font-weight: 700; margin-bottom: 12px;">
            ⚙️ 1. كواليس رحلة البيانات (<span dir="ltr">ETL / ELT Pipelines</span>)
        </h3>
        <p style="direction: rtl; text-align: right; margin-bottom: 15px;">
            عمرك سالت نفسك: البيانات الخام اللي في التطبيق بتوصل إزاي لشاشات التحليل بتاعتك؟ الحكاية بتعدى على 3 محطات أساسية:
        </p>
        <ul style="direction: rtl; text-align: right; margin-bottom: 20px; padding-right: 20px;">
            <li style="margin-bottom: 6px;"><b>Extract (استخراج):</b> سحب الداتا من قواعد بيانات التطبيقات، السيرفرات، ومواقع الإنترنت.</li>
            <li style="margin-bottom: 6px;"><b>Transform (تحويل وتنظيف):</b> تنقية الداتا، توحيد العملات وتنسيق التواريخ (ودي أكتر مرحلة بياخد فيها المحلل وقته).</li>
            <li style="margin-bottom: 6px;"><b>Load (تحميل):</b> تخزين الداتا النهئية النظيفة في مستودعات مركزية زي <span dir="ltr">Data Warehouse</span> عشان المحللين يسحبوها بسهولة.</li>
        </ul>
        
        <hr style="border: 0.5px solid #444; margin: 25px 0;">
        
        <h3 style="direction: rtl; text-align: right; color: #fff; font-size: 20px; font-weight: 700; margin-bottom: 12px;">
            ⚖️ 2. أخلاقيات البيانات والتحيز الملعون (<span dir="ltr">Data Ethics & Bias</span>)
        </h3>
        <p style="direction: rtl; text-align: right; margin-bottom: 15px;">
            مش كل بيانات متاح للشركات جمعها بسبب قوانين الخصوصية العالمية الصارمة زي الـ <span dir="ltr">GDPR</span>.. والأخطر هو <b>التحيز في البيانات (<span dir="ltr">Data Bias</span>)</b>!<br>
            لو شركة عملت موديل ذكاء اصطناعي يوافق أو يرفض القروض بناءً على "تاريخ العملاء القدامى"، وكان التاريخ ده فيه تمييز ضد فئة معينة.. الموديل هيكرر نفس الظلم وبشكل تلقائي! المحترف الحقيقي مش بس ذكي برمجياً، ده شخص مسؤول وأخلاقي في معالجة البيانات.
        </p>
        
        <hr style="border: 0.5px solid #444; margin: 25px 0;">
        
        <h3 style="direction: rtl; text-align: right; color: #fff; font-size: 20px; font-weight: 700; margin-bottom: 12px;">
            🧪 3. إزاي الشركات الكبرى بتقرر بدون تخمين؟ (<span dir="ltr">A/B Testing</span>)
        </h3>
        <p style="direction: rtl; text-align: right; margin-bottom: 15px;">
            لما <span dir="ltr">Netflix</span> تحب تغير لون زرار التشغيل، أو <span dir="ltr">Amazon</span> تحب تغير مكان سلة الشراء.. مش بيعتمدوا على الإحساس!<br>
            بيلجاؤا لـ <b><span dir="ltr">A/B Testing</span></b>: بيقسموا المستخدمين نصين، النص (أ) يشوف التصميم القديم والنص (ب) يشوف التصميم الجديد، وبيسيبوا الأرقام والبيانات الحقيقية تحكم مين كسب بالمللي!
        </p>
        
        <hr style="border: 0.5px solid #444; margin: 25px 0;">
        
        <h3 style="direction: rtl; text-align: right; color: #fff; font-size: 20px; font-weight: 700; margin-bottom: 12px;">
            🏁 خط النهاية: الانطلاق نحو عالم التطبيق العملي
        </h3>
        <p style="direction: rtl; text-align: right; margin-bottom: 20px;">
            بكده نكون قفلنا 100% من الصورة الكبيرة، المفاهيم الأساسية، الأدوات، الوظائف، وحتى التكات المتقدمة لعالم البيانات.<br>
            أنت جاهز تماماً دلوقتي عشان تفتح برامجك وتكتب أول كود، وتبني أول تقرير، وتنفذ أول مشروع حقيقي!
        </p>
        
        <p style="direction: rtl; text-align: right; background: rgba(255, 153, 0, 0.1); padding: 12px; border-radius: 6px; border-right: 4px solid #ff9933; margin-bottom: 0;">
            <b>💡 نصيحة ختامية للسلسلة:</b> العلم النظري هو البوصلة، لكن التطبيق العملي هو اللي بيحرك السفينة. لا تقف مكانك في القراءة، واجعل يدك دائماً على لوحة المفاتيح تطبق كل فكرة بتتعلمها!
        </p>
        
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
            <div style="text-align: center; margin-top: 15px;">
                <a href="https://www.linkedin.com" target="_blank" style="background-color: #0a66c2; color: white; padding: 10px 20px; border-radius: 6px; text-decoration: none; font-weight: bold; display: inline-block;">
                    💬 ناقش ختام السلسلة على لينكد إن
                </a>
            </div>
            """, unsafe_allow_html=True)

    
    other_phases = {
      
    }
    
    for ph, title in other_phases.items():
        with st.expander(f"📁 Phase {ph}: {title} - قريباً ⏳", expanded=False):
            st.markdown(f"<div dir='rtl' style='padding: 10px; opacity: 0.8;'>هذا الفصل قيد التجهيز وسيتم إطلاقه ضمن سلسلة DataLab التعليمية.</div>", unsafe_allow_html=True)
   
# --- Tab 2: Python & Tools (Future Content) ---
with tab2:
    # تشغيل محتوى ملف بايثون المنفصل
    render_python_tab()

with tab3:
    st.markdown("""
        <div dir="rtl" style="text-align: center; padding: 20px 10px;">
        <h3>💼 Featured Projects & Prototypes</h3>
        <p style="opacity: 0.8; font-size: 14px;">أبرز المشاريع التقنية والحلول اللي ببنيها في رحلتي لعالم البيانات:</p>
        </div>
        """, unsafe_allow_html=True)


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
