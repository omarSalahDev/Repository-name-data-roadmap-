import streamlit as st

def render_python_tab():
    # الهيدر الرئيسي للقسم بستايل Apple & Notion البراند
    st.markdown("""
        <div dir="rtl" style="direction: rtl; text-align: right; padding: 10px 0 20px 0;">
            <h3 style="font-weight: 800; font-size: 26px; margin-bottom: 5px; color: #fff;">🐍 بايثون من الصفر لاحتراف البيانات</h3>
            <p style="opacity: 0.8; font-size: 14.5px; line-height: 1.6;">رحلة متكاملة مقسمة لمحطات عملية واضحة. اختر المحطة اللي تحب تدرسها وابدأ التطبيق الفوري:</p>
        </div>
        """, unsafe_allow_html=True)

    # -------------------------------------------------------------
    # 📚 جدول المحطات والدروس
    # -------------------------------------------------------------
    lessons_registry = {
        "المحطة 1: قبل ما نبدأ + أول برنامج print()": render_python_lesson_1,
        "المحطة 2: Data Types (أنواع البيانات في Python)": render_python_lesson_2,
        "المحطة 3: Lists (القوائم وكيفية إدارتها)": render_python_lesson_3,
        "المحطة 4: Tuples (البيانات الثابتة ومقارنتها بالـ Lists)": render_python_lesson_4,
        "المحطة 5: Dictionaries (المفاتيح والقيم والتعامل مع البيانات)": render_python_lesson_5,
        "المحطة 6: Sets (المجموعات والقيم الفريدة وعمليات الـ Union والـ Difference)": render_python_lesson_6,
        "المحطة 7: Python Logic (المنطق وشروط الاتخاذ والقرار If, Elif, Else)": render_python_lesson_7,
        "المحطة 8: While Loop (الحلقات التكرارية والتحكم بـ break و continue)": render_python_lesson_8,
        "المحطة 9: For Loop (التكرار الذكي على العناصر والتعامل مع القواميس)": render_python_lesson_9,  # السطر الجديد
        "المحطة 10: الدوال (Functions)": lambda: render_placeholder_lesson(10, "الدوال Functions"),
    }

    # اختيار المحطة عبر قائمة منسدلة أنيقة
    selected_lesson_title = st.selectbox(
        label="اختر المحطة الدراسية:",
        options=list(lessons_registry.keys()),
        label_visibility="collapsed"
    )

    st.markdown("---")

    # تشغيل الدالة الخاصة بالمحطة المختارة
    lessons_registry[selected_lesson_title]()

# =============================================================
# 🚀 تفاصيل المحطة الأولى
# =============================================================
def render_python_lesson_1():
    st.markdown("""
        <div dir="rtl" style="direction: rtl; text-align: right;">
            <h2 style="font-weight: 800; font-size: 22px; color: #fff; margin-bottom: 8px;">🚀 المحطة 1: قبل ما نبدأ Python</h2>
            <p style="opacity: 0.8; font-size: 14px; margin-bottom: 20px;"><strong>هدف المحطة:</strong> في أقل من 10 دقائق تكون جاهز تكتب أول برنامج.</p>
        </div>
        """, unsafe_allow_html=True)

    # الخطوة الأولى: التثبيت
    st.markdown("""
        <div dir="rtl" style="direction: rtl; text-align: right; padding: 18px; border: 1px solid rgba(255,255,255,0.1); border-radius: 12px; margin-bottom: 15px; background-color: rgba(255,255,255,0.02);">
            <h4 style="font-size: 17px; font-weight: 700; margin-bottom: 10px;">1️⃣ هنستخدم إيه؟</h4>
            <p style="font-size: 13.5px; opacity: 0.85; line-height: 1.6;">
            تقدر تكتب أكواد <span dir="ltr">Python</span> بأكتر من طريقة، لكن لو أنت مبتدئ، أرشح تبدأ بـ <span dir="ltr">Visual Studio Code (VS Code)</span> مع <span dir="ltr">Python</span>.
            </p>
            <hr style="border: 0; border-top: 1px solid rgba(255,255,255,0.05); margin: 12px 0;">
            <h5 style="font-size: 15px; font-weight: 600; margin-bottom: 8px;">🛠️ مش عارف تثبتهم؟</h5>
            <p style="font-size: 13px; opacity: 0.8; line-height: 1.5;">
            بدل ما نمشي في شرح هيبقى قديم بعد كام شهر، استخدم <span dir="ltr">ChatGPT</span> أو أي مساعد ذكاء اصطناعي وانسخ له الأمر ده:
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    st.code("ساعدني خطوة بخطوة في تثبيت أحدث إصدار من Python وVisual Studio Code على نظام Windows، وتأكد إن Python اتضاف إلى PATH، وبعدها ساعدني أشغل أول ملف Python.", language="text")

    st.markdown("""
        <div dir="rtl" style="direction: rtl; text-align: right; padding: 15px; border: 1px solid rgba(255,255,255,0.1); border-radius: 12px; margin-bottom: 20px; background-color: rgba(255,255,255,0.02);">
            <p style="font-size: 13px; opacity: 0.85; margin: 0;">
            💡 <strong>ملحوظة:</strong> لو قابلتك أي مشكلة، انسخ رسالة الخطأ واسأله عنها، وهيشرحها لك فوراً.
            </p>
        </div>
        """, unsafe_allow_html=True)

    # التحقق من التثبيت
    st.markdown("""
        <div dir="rtl" style="direction: rtl; text-align: right; padding: 18px; border: 1px solid rgba(255,255,255,0.1); border-radius: 12px; margin-bottom: 15px; background-color: rgba(255,255,255,0.02);">
            <h4 style="font-size: 17px; font-weight: 700; margin-bottom: 10px;">3️⃣ هل التثبيت نجح؟</h4>
            <p style="font-size: 13.5px; opacity: 0.85; margin-bottom: 10px;">افتح الـ <span dir="ltr">Terminal</span> واكتب أحد الأمرين:</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.code("python --version\n# أو لو مشتغلش:\npy --version", language="bash")

    st.markdown("""
        <div dir="rtl" style="direction: rtl; text-align: right; padding: 15px; border-radius: 8px; margin-bottom: 25px; background: rgba(0, 255, 150, 0.05); border: 1px solid rgba(0, 255, 150, 0.15);">
            <p style="font-size: 13.5px; margin: 0;">✨ <strong>النتيجة المتوقعة:</strong> لو ظهر رقم الإصدار، يبقى أنت جاهز تماماً للانطلاق!</p>
        </div>
        """, unsafe_allow_html=True)

    # الدرس الأول: أمر الطباعة print()
    st.markdown("""
        <div dir="rtl" style="direction: rtl; text-align: right;">
            <h2 style="font-weight: 800; font-size: 20px; color: #fff; margin-bottom: 10px; margin-top: 30px;">🖨️ الدرس الأول: أمر الطباعة print()</h2>
            <p style="opacity: 0.85; font-size: 14px; line-height: 1.7; margin-bottom: 15px;">
            تخيل... الكمبيوتر مش هيعرف يعرض أي حاجة إلا لو طلبت منه بوضوح. وده بالضبط دور الدالة <code style="color: #61afef;">print()</code>.<br>
            هي بتقول للكمبيوتر ببساطة: <strong>"اعرض اللي بين القوسين على الشاشة."</strong>
            </p>
        </div>
        """, unsafe_allow_html=True)

    st.code('print("Hello, DataLab!")', language="python")
    
    st.markdown("""
        <div dir="rtl" style="direction: rtl; text-align: right; padding: 12px; border-radius: 8px; margin-bottom: 20px; background: rgba(255,255,255,0.03);">
            <p style="font-size: 13.5px; margin: 0;">📤 <strong>الناتج المتوقع:</strong> <code style="color: #98c379;" dir="ltr">Hello, DataLab!</code></p>
        </div>
        """, unsafe_allow_html=True)

    # جرب بنفسك
    st.markdown("""
        <div dir="rtl" style="direction: rtl; text-align: right; padding: 15px; border: 1px solid rgba(255,255,255,0.1); border-radius: 12px; margin-bottom: 20px; background-color: rgba(255,255,255,0.02);">
            <h4 style="font-size: 16px; font-weight: 700; margin-bottom: 8px;">🎮 جرب بنفسك:</h4>
            <p style="font-size: 13.5px; opacity: 0.85; margin-bottom: 10px;">غير الكود إلى:</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.code('print("Welcome Omar")', language="python")
    
    st.markdown("""
        <div dir="rtl" style="direction: rtl; text-align: right; margin-bottom: 25px;">
            <p style="font-size: 13.5px; opacity: 0.85;">بسيطة، صح؟ هيظهر معاك الناتج بكل سهولة 🎉</p>
        </div>
        """, unsafe_allow_html=True)

    # ألعاب وتحديات سريعة
    st.markdown("""
        <div dir="rtl" style="direction: rtl; text-align: right; padding: 18px; border: 1px solid rgba(255,255,255,0.1); border-radius: 12px; margin-bottom: 20px; background-color: rgba(255,255,255,0.02);">
            <h4 style="font-size: 17px; font-weight: 700; margin-bottom: 12px;">🕹️ تحدي السريع (فكر 5 ثواني قبل ما تشوف الإجابة):</h4>
            <p style="font-size: 14px; margin-bottom: 8px;"><strong>التحدي الأول:</strong> إيه الناتج؟</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.code('print("Python")', language="python")
    
    st.markdown("""
        <div dir="rtl" style="direction: rtl; text-align: right; padding: 12px; border-radius: 8px; margin-bottom: 20px; background: rgba(0, 200, 255, 0.05); border: 1px solid rgba(0, 200, 255, 0.15);">
            <p style="font-size: 13.5px; margin: 0;">✅ <strong>الإجابة:</strong> <code style="color: #98c379;" dir="ltr">Python</code> (لو إجابتك صح، عاش جداً!)</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("""
        <div dir="rtl" style="direction: rtl; text-align: right; padding: 18px; border: 1px solid rgba(255,255,255,0.1); border-radius: 12px; margin-bottom: 15px; background-color: rgba(255,255,255,0.02);">
            <p style="font-size: 14px; margin-bottom: 8px;"><strong>التحدي الثاني:</strong> إيه اللي هيحصل هنا؟</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.code('print(100)', language="python")

    st.markdown("""
        <div dir="rtl" style="direction: rtl; text-align: right; padding: 12px; border-radius: 8px; margin-bottom: 25px; background: rgba(0, 200, 255, 0.05); border: 1px solid rgba(0, 200, 255, 0.15);">
            <p style="font-size: 13.5px; margin: 0;">✅ <strong>الإجابة:</strong> <code style="color: #98c379;" dir="ltr">100</code><br>
            <span style="font-size: 12.5px; opacity: 0.8;">لاحظ إن الرقم هنا مش محتاج علامات تنصيص <code style="color: #e06c75;">""</code>. ليه؟ هنعرف بعد شوية لما نتكلم عن أنواع البيانات <span dir="ltr">(Data Types)</span>!</span></p>
        </div>
        """, unsafe_allow_html=True)

    # أشهر غلطة
    st.markdown("""
        <div dir="rtl" style="direction: rtl; text-align: right; padding: 18px; border: 1px solid rgba(224, 108, 117, 0.2); border-radius: 12px; margin-bottom: 25px; background-color: rgba(224, 108, 117, 0.03);">
            <h4 style="font-size: 16px; font-weight: 700; color: #e06c75; margin-bottom: 8px;">❌ أشهر غلطة بيقع فيها المبتدئين:</h4>
            <p style="font-size: 13.5px; opacity: 0.85; margin-bottom: 10px;">كتبت الكود ده من غير أقواس تنصيص:</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.code('print(Hello)', language="python")

    st.markdown("""
        <div dir="rtl" style="direction: rtl; text-align: right; margin-bottom: 25px;">
            <p style="font-size: 13.5px; opacity: 0.85; line-height: 1.6;">
            <strong>ليه مش هيشتغل؟</strong> لأن بايثون هتفتكر إن <code style="color: #e06c75;">Hello</code> اسم متغير (Variable) تم تخزين قيمة فيه، مش مجرد نص عادي.<br>
            <strong>الصحيح دائماً للنصوص:</strong> <code style="color: #98c379;">print("Hello")</code>
            </p>
        </div>
        """, unsafe_allow_html=True)

    # 💡 خلاصة من الكتب والخبراء (Pro-Tip)
    st.markdown("""
        <div dir="rtl" style="direction: rtl; text-align: right; padding: 18px; border: 1px solid rgba(229, 192, 123, 0.3); border-radius: 12px; margin-bottom: 25px; background-color: rgba(229, 192, 123, 0.04);">
            <h4 style="font-size: 16px; font-weight: 700; color: #e5c07b; margin-bottom: 8px;">💡 Pro-Tip (من كواليس كتب البرمجة العالمية):</h4>
            <p style="font-size: 13.5px; opacity: 0.9; line-height: 1.6;">
            زي ما كتب زي <em>"Automate the Boring Stuff with Python"</em> بتوضح، البرمجة في جوهرها مش حفظ أكواد، هي <strong>"فن إعطاء أوامر دقيقة جداً لآلة غبية جداً لا تفهم التلميحات"</strong>. حرف واحد ناقص زي قوس مفقود أو علامة تنصيص منسيّة يوقف البرنامج كله! اتعود دايمًا تدقق في تفاصيلك.
            </p>
        </div>
        """, unsafe_allow_html=True)

    # ملخص سريع
    st.markdown("""
        <div dir="rtl" style="direction: rtl; text-align: right; padding: 20px; border: 1px solid rgba(255,255,255,0.1); border-radius: 12px; background-color: rgba(255,255,255,0.02);">
            <h3 style="font-size: 18px; font-weight: 700; margin-bottom: 12px;">📝 ملخص سريع للدرس:</h3>
            <ul style="font-size: 13.5px; opacity: 0.85; line-height: 1.8; padding-right: 20px; margin: 0;">
                <li>الدالة <code style="color: #61afef;">print()</code> هي بوابتك الأساسية لعرض أي قيمة على الشاشة.</li>
                <li>النصوص الصريحة <code style="color: #98c379;">Strings</code> لازم تُحاط بعلامات تنصيص <code style="color: #98c379;">""</code>.</li>
                <li>الأرقام <code style="color: #d19a66;">Numbers</code> ممكن تتكتب وتتعامل مباشرة من غير علامات تنصيص.</li>
                <li>في الدرس الجاي، هنعرف ليه أساساً فيه فرق جوهري بين الرقم والنصوص في عقل الكمبيوتر!</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)



# =============================================================
# 📦 تفاصيل المحطة الثانية: Data Types
# =============================================================
def render_python_lesson_2():
    st.markdown("""
        <div dir="rtl" style="direction: rtl; text-align: right;">
            <h2 style="font-weight: 800; font-size: 22px; color: #fff; margin-bottom: 8px;">📦 المحطة 2: Data Types — ليه Python لازم تعرف نوع البيانات؟</h2>
            <p style="opacity: 0.85; font-size: 14.5px; line-height: 1.7; margin-bottom: 20px;">
            خلينا نسألك سؤال: لو قولت لك <code style="color: #d19a66;">50</code> دي إيه؟ ممكن تقول: رقم.<br>
            طيب لو قولت لك <code style="color: #98c379;">"50"</code> دي برضو رقم؟ الإجابة... <strong>❌ لأ، دي نص!</strong> رغم إن اللي قدامك هو الرقم 50. ليه؟
            </p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("""
        <div dir="rtl" style="direction: rtl; text-align: right; padding: 15px; border: 1px solid rgba(255,255,255,0.1); border-radius: 12px; margin-bottom: 20px; background-color: rgba(255,255,255,0.02);">
            <p style="font-size: 14px; opacity: 0.9; line-height: 1.6; margin: 0;">
            لان الكمبيوتر مش بيبص على شكل الحاجة.. هو بيبص على <strong>نوعها (Type)</strong>. وكل قيمة بتدخلها لازم تعرف هي (رقم؟ نص؟ صح ولا غلط؟) علشان تعرف تتعامل معاها صح.
            </p>
        </div>
        """, unsafe_allow_html=True)

    # 1. Integer
    st.markdown("""
        <div dir="rtl" style="direction: rtl; text-align: right; padding: 18px; border: 1px solid rgba(255,255,255,0.1); border-radius: 12px; margin-bottom: 15px; background-color: rgba(255,255,255,0.02);">
            <h4 style="font-size: 17px; font-weight: 700; margin-bottom: 8px; color: #61afef;">1️⃣ Integer (int) — الأرقام الصحيحة</h4>
            <p style="font-size: 13.5px; opacity: 0.85; line-height: 1.6;">
            أمثلة: <code style="color: #d19a66;" dir="ltr">10, 25, -3, 1000</code><br>
            تستخدمها لما يكون مفيش كسور؛ زي: عدد الطلاب، عدد المنتجات، أو العمر.
            </p>
        </div>
        """, unsafe_allow_html=True)

    # 2. Float
    st.markdown("""
        <div dir="rtl" style="direction: rtl; text-align: right; padding: 18px; border: 1px solid rgba(255,255,255,0.1); border-radius: 12px; margin-bottom: 15px; background-color: rgba(255,255,255,0.02);">
            <h4 style="font-size: 17px; font-weight: 700; margin-bottom: 8px; color: #98c379;">2️⃣ Float — الأرقام العشرية</h4>
            <p style="font-size: 13.5px; opacity: 0.85; line-height: 1.6;">
            أمثلة: <code style="color: #98c379;" dir="ltr">10.5, 99.99, 3.14</code><br>
            تستخدمها في: الأسعار، النسب، ومتوسط الدرجات (أي رقم فيه فاصلة عشرية).
            </p>
        </div>
        """, unsafe_allow_html=True)

    # 3. String
    st.markdown("""
        <div dir="rtl" style="direction: rtl; text-align: right; padding: 18px; border: 1px solid rgba(255,255,255,0.1); border-radius: 12px; margin-bottom: 15px; background-color: rgba(255,255,255,0.02);">
            <h4 style="font-size: 17px; font-weight: 700; margin-bottom: 8px; color: #e5c07b;">3️⃣ String (str) — النصوص</h4>
            <p style="font-size: 13.5px; opacity: 0.85; line-height: 1.6;">
            سواء كلمة، جملة، أو حتى رقم مكتوب بين Quotes: <code style="color: #e5c07b;" dir="ltr">"Omar", "Python", "123"</code><br>
            لاحظ: آخر مثال ده <strong>مش رقم</strong>، ده نص محاط بعلامات تنصيص.
            </p>
        </div>
        """, unsafe_allow_html=True)

    # 4. Boolean
    st.markdown("""
        <div dir="rtl" style="direction: rtl; text-align: right; padding: 18px; border: 1px solid rgba(255,255,255,0.1); border-radius: 12px; margin-bottom: 25px; background-color: rgba(255,255,255,0.02);">
            <h4 style="font-size: 17px; font-weight: 700; margin-bottom: 8px; color: #c678dd;">4️⃣ Boolean (bool) — القيم المنطقية</h4>
            <p style="font-size: 13.5px; opacity: 0.85; line-height: 1.6;">
            أبسط نوع بيانات، ليه قيمتين فقط: <code style="color: #c678dd;" dir="ltr">True</code> أو <code style="color: #c678dd;" dir="ltr">False</code>.<br>
            بيستخدم في اتخاذ القرارات؛ زي: هل المستخدم سجل دخول؟ (<code style="color: #c678dd;" dir="ltr">True</code>) أو هل الطالب نجح؟ (<code style="color: #c678dd;" dir="ltr">False</code>).
            </p>
        </div>
        """, unsafe_allow_html=True)

    # جدول الملخص السريع
    st.markdown("""
        <div dir="rtl" style="direction: rtl; text-align: right; padding: 20px; border: 1px solid rgba(255,255,255,0.1); border-radius: 12px; background-color: rgba(255,255,255,0.02); margin-bottom: 20px;">
            <h3 style="font-size: 18px; font-weight: 700; margin-bottom: 15px;">📝 ملخص أنواع البيانات الأساسية:</h3>
            <table style="width: 100%; text-align: right; border-collapse: collapse; font-size: 14px;">
                <tr style="border-bottom: 1px solid rgba(255,255,255,0.1);">
                    <th style="padding: 8px;">القيمة</th>
                    <th style="padding: 8px;">النوع (Type)</th>
                </tr>
                <tr style="border-bottom: 1px solid rgba(255,255,255,0.05);">
                    <td style="padding: 8px;" dir="ltr">100</td>
                    <td style="padding: 8px;">Integer (int)</td>
                </tr>
                <tr style="border-bottom: 1px solid rgba(255,255,255,0.05);">
                    <td style="padding: 8px;" dir="ltr">25.5</td>
                    <td style="padding: 8px;">Float</td>
                </tr>
                <tr style="border-bottom: 1px solid rgba(255,255,255,0.05);">
                    <td style="padding: 8px;" dir="ltr">"Hello"</td>
                    <td style="padding: 8px;">String (str)</td>
                </tr>
                <tr>
                    <td style="padding: 8px;" dir="ltr">True</td>
                    <td style="padding: 8px;">Boolean (bool)</td>
                </tr>
            </table>
        </div>
        """, unsafe_allow_html=True)

    # Pro-Tip
    st.markdown("""
        <div dir="rtl" style="direction: rtl; text-align: right; padding: 18px; border: 1px solid rgba(229, 192, 123, 0.3); border-radius: 12px; background-color: rgba(229, 192, 123, 0.04);">
            <h4 style="font-size: 16px; font-weight: 700; color: #e5c07b; margin-bottom: 8px;">💡 معلومة مهمة جداً (Data Analyst Mindset):</h4>
            <p style="font-size: 13.5px; opacity: 0.9; line-height: 1.6;">
            مش مطلوب منك تحفظ كل التفاصيل من أول مرة، لكن المهم جداً إنك أول ما تشوف أي عمود في داتا أو قيمة برمجية، تلقائي <strong>تعرف هي من أي نوع</strong>. لأن 80% من مشاكل تنظيف البيانات (Data Cleaning) في سوق العمل بتتحل لما تكتشف إن رقم مكتوب في شكل نص (String) والعكس صحيح!
            </p>
        </div>
        """, unsafe_allow_html=True)

def render_python_lesson_3():
    # الهيدر الرئيسي للمحطة
    st.markdown("""
        <div dir="rtl" style="direction: rtl; text-align: right;">
            <h2 style="font-weight: 800; font-size: 22px; color: #fff; margin-bottom: 8px;">📦 المحطة 3: Lists — ليه نستخدم List بدل ما نعمل 100 متغير؟</h2>
            <p style="opacity: 0.85; font-size: 14.5px; line-height: 1.7; margin-bottom: 20px;">
            لحد دلوقتي اتعلمنا إزاي نخزن قيمة واحدة في متغير، زي:<br>
            <code style="color: #61afef;" dir="ltr">name = "Omar"</code><br>
            طيب... لو عندك أسماء أول 5 عملاء سجلوا في الموقع؟ (<code style="color: #98c379;" dir="ltr">Ahmed, Sara, Omar, Nada, Ali</code>).
            </p>
        </div>
        """, unsafe_allow_html=True)

    # معضلة المتغيرات المتعددة مقابل القوائم
    st.markdown("""
        <div dir="rtl" style="direction: rtl; text-align: right; padding: 18px; border: 1px solid rgba(255,255,255,0.1); border-radius: 12px; margin-bottom: 20px; background-color: rgba(255,255,255,0.02);">
            <h4 style="font-size: 16px; font-weight: 700; color: #e06c75; margin-bottom: 10px;">❌ هل الطريقة التقليدية عملية؟</h4>
            <p style="font-size: 13.5px; opacity: 0.9; line-height: 1.6; margin-bottom: 12px;">
            لو فكرت تعمل لكل عميل متغير منفصل:<br>
            <code style="color: #e06c75;" dir="ltr">customer1 = "Ahmed"</code><br>
            <code style="color: #e06c75;" dir="ltr">customer2 = "Sara"</code><br>
            ... وهكذا. ينفع؟ <strong>آه ينفع، بس هل ده عملي؟ إطلاقاً!</strong> تخيل لو عندك 50,000 عميل، مستحيل تعمل 50 ألف متغير.
            </p>
            <p style="font-size: 13.5px; opacity: 0.9; line-height: 1.6; margin: 0;">
            علشان كده Python وفرت حاجة اسمها <strong>List</strong>؛ مكان تقدر تخزن فيه أكتر من قيمة داخل متغير واحد.
            </p>
        </div>
        """, unsafe_allow_html=True)

    # إنشاء الـ List
    st.markdown("""
        <div dir="rtl" style="direction: rtl; text-align: right; padding: 18px; border: 1px solid rgba(255,255,255,0.1); border-radius: 12px; margin-bottom: 15px; background-color: rgba(255,255,255,0.02);">
            <h4 style="font-size: 17px; font-weight: 700; color: #61afef; margin-bottom: 8px;">📝 إنشاء List</h4>
            <p style="font-size: 13.5px; opacity: 0.85; line-height: 1.6; margin-bottom: 12px;">
            بتكتبها بين أقواس مربعة <code style="color: #e5c07b;" dir="ltr">[]</code>. إليك أمثلة متنوعة لأنواع البيانات اللي ممكن تخزنها:
            </p>
        </div>
        """, unsafe_allow_html=True)

    st.code("""# 1. قائمة أسماء (Text)
customers = ["Ahmed", "Sara", "Omar", "Nada", "Ali"]

# 2. قائمة أرقام (Numbers/Sales)
sales = [1200, 950, 1800, 2200]

# 3. قائمة قيم منطقية (Booleans)
status = [True, False, True]""", language="python")

    st.markdown("""
        <div dir="rtl" style="direction: rtl; text-align: right; padding: 15px; border-radius: 8px; margin-bottom: 20px; background: rgba(97, 175, 239, 0.05); border: 1px solid rgba(97, 175, 239, 0.15);">
            <p style="font-size: 13.5px; margin: 0;">
            🎮 <strong>سؤال سريع:</strong> هل الـ List ينفع تحتوي على أرقام ونصوص مع بعض؟<br>
            ✅ <strong>الإجابة:</strong> أيوه، زي: <code style="color: #98c379;" dir="ltr">data = ["Ahmed", 25, True]</code>. لكن في شغلك، حاول تخلي البيانات من نفس النوع كلما أمكن؛ لأن ده بيسهل التعامل معها لاحقاً.
            </p>
        </div>
        """, unsafe_allow_html=True)

    # الوصول لعنصر معين (Index)
    st.markdown("""
        <div dir="rtl" style="direction: rtl; text-align: right; padding: 18px; border: 1px solid rgba(255,255,255,0.1); border-radius: 12px; margin-bottom: 15px; background-color: rgba(255,255,255,0.02);">
            <h4 style="font-size: 17px; font-weight: 700; color: #98c379; margin-bottom: 8px;">🔍 الوصول لعنصر معين (Index)</h4>
            <p style="font-size: 13.5px; opacity: 0.85; line-height: 1.6; margin-bottom: 10px;">
            كل عنصر في الـ List ليه رقم (Index)، والعد في بايثون دايماً <strong>بيبدأ من 0</strong> مش من 1!
            </p>
        </div>
        """, unsafe_allow_html=True)

    st.code("""customers = ["Ahmed", "Sara", "Omar", "Nada"]
# Ahmed -> Index 0
# Sara  -> Index 1
# Omar  -> Index 2
# Nada  -> Index 3

print(customers[0])  # الناتج: Ahmed
print(customers[2])  # الناتج: Omar""", language="python")

    st.markdown("""
        <div dir="rtl" style="direction: rtl; text-align: right; padding: 12px; border-radius: 8px; margin-bottom: 20px; background: rgba(255,255,255,0.03);">
            <p style="font-size: 13.5px; margin: 0;">
            🎮 <strong>سؤال سريع:</strong> لو عندك <code style="color: #e5c07b;" dir="ltr">numbers = [10, 20, 30]</code> ونفذت <code style="color: #e5c07b;" dir="ltr">print(numbers[1])</code> إيه الناتج؟<br>
            ✅ <strong>الإجابة:</strong> <code style="color: #98c379;" dir="ltr">20</code> (لأن العنصر الأول هو 0 والثاني هو 1).
            </p>
        </div>
        """, unsafe_allow_html=True)

    # تعديل وإضافة وحذف البيانات
    st.markdown("""
        <div dir="rtl" style="direction: rtl; text-align: right; padding: 18px; border: 1px solid rgba(255,255,255,0.1); border-radius: 12px; margin-bottom: 15px; background-color: rgba(255,255,255,0.02);">
            <h4 style="font-size: 17px; font-weight: 700; color: #e5c07b; margin-bottom: 10px;">✏️ تعديل وإدارة محتوى الـ List</h4>
            <p style="font-size: 13.5px; opacity: 0.85; line-height: 1.6; margin-bottom: 10px;">
            القوائم في بايثون قابلة للتعديل (Mutable)، وده بيعطيك مرونة كاملة في معالجة البيانات:
            </p>
        </div>
        """, unsafe_allow_html=True)

    st.code("""# 1. تعديل عنصر معين بالـ Index
customers = ["Ahmed", "Sara", "Omar"]
customers[1] = "Mona"
print(customers)  # الناتج: ['Ahmed', 'Mona', 'Omar'] (Sara اتغيرت لـ Mona)

# 2. إضافة عنصر جديد في الآخر باستخدام append()
customers.append("Omar")
print(customers)  # الناتج: ['Ahmed', 'Mona', 'Omar', 'Omar']

# 3. حذف آخر عنصر باستخدام pop()
customers.pop()
print(customers)  # الناتج: ['Ahmed', 'Mona', 'Omar']
# أو حذف عنصر بـ Index محدد، مثل customers.pop(0) لحذف الأول.

# 4. معرفة عدد العناصر باستخدام len()
print(len(customers))  # الناتج: 3""", language="python")

    # ترتيب وعكس ودمج القوائم
    st.markdown("""
        <div dir="rtl" style="direction: rtl; text-align: right; padding: 18px; border: 1px solid rgba(255,255,255,0.1); border-radius: 12px; margin-bottom: 15px; background-color: rgba(255,255,255,0.02);">
            <h4 style="font-size: 17px; font-weight: 700; color: #c678dd; margin-bottom: 10px;">🔠 ترتيب، عكس، ودمج البيانات</h4>
        </div>
        """, unsafe_allow_html=True)

    st.code("""# 1. ترتيب الأرقام أو النصوص (sort())
numbers = [8, 2, 10, 1]
numbers.sort()
print(numbers)  # الناتج: [1, 2, 8, 10]

# 2. عكس الترتيب (reverse())
numbers.reverse()
print(numbers)  # الناتج: [10, 8, 2, 1]

# 3. دمج قائمتين (Concatenation)
group1 = ["Ahmed", "Sara"]
group2 = ["Omar", "Nada"]
students = group1 + group2
print(students)  # الناتج: ['Ahmed', 'Sara', 'Omar', 'Nada']""", language="python")

    # القوائم المتداخلة والـ type والأخطاء الشائعة
    st.markdown("""
        <div dir="rtl" style="direction: rtl; text-align: right; padding: 18px; border: 1px solid rgba(255,255,255,0.1); border-radius: 12px; margin-bottom: 15px; background-color: rgba(255,255,255,0.02);">
            <h4 style="font-size: 17px; font-weight: 700; color: #61afef; margin-bottom: 10px;">📦 تفاصيل متقدمة وأشهر الأخطاء</h4>
        </div>
        """, unsafe_allow_html=True)

    st.code("""# 1. القوائم داخل القوائم (Nested Lists) - شكل هتشوفه كتير قبل الجداول في Pandas:
data = [
    ["Ahmed", 95],
    ["Sara", 88],
    ["Omar", 91]
]

# 2. معرفة نوع البيانات (type())
print(type(customers))  # الناتج: <class 'list'>

# ⚠️ أشهر الأخطاء (IndexError):
# لو الـ List فيها 3 عناصر بس، وطلبت customers[5]، هيطلع Error. 
# لازم تتأكد دايماً إن الـ Index موجود ضمن نطاق القائمة!""", language="python")

    # Pro-Tip / Data Analysis Connection
    st.markdown("""
        <div dir="rtl" style="direction: rtl; text-align: right; padding: 18px; border: 1px solid rgba(229, 192, 123, 0.3); border-radius: 12px; background-color: rgba(229, 192, 123, 0.04);">
            <h4 style="font-size: 16px; font-weight: 700; color: #e5c07b; margin-bottom: 8px;">💼 هستخدم Lists فين في Data Analysis؟</h4>
            <p style="font-size: 13.5px; opacity: 0.9; line-height: 1.6; margin-bottom: 10px;">
            في شغل تحليل البيانات، الـ Lists بتمثّل العمود الفقري لجمع البيانات الأولية؛ زي: أسماء العملاء، أسعار المنتجات، المدن، درجات الطلاب، ونتائج المبيعات.
            </p>
            <p style="font-size: 13.5px; opacity: 0.9; line-height: 1.6; margin: 0;">
            💡 <strong>معلومة من كواليس علم البيانات:</strong> لما نبدأ نشتغل بـ <strong>Pandas</strong>، هتكتشف إن فكرة الـ Series والـ DataFrame مبنية في الأساس على تطويرات لمفهوم الـ Lists والـ Dictionaries دي، بس بطريقة مخصصة لتحليل ملايين الصفوف بسرعة البرق!
            </p>
        </div>
        """, unsafe_allow_html=True)


def render_python_lesson_4():
    # الهيدر الرئيسي للمحطة
    st.markdown("""
        <div dir="rtl" style="direction: rtl; text-align: right;">
            <h2 style="font-weight: 800; font-size: 22px; color: #fff; margin-bottom: 8px;">📦 المحطة 4: Tuples — إمتى أستخدم Tuple بدل List؟</h2>
            <p style="opacity: 0.85; font-size: 14.5px; line-height: 1.7; margin-bottom: 20px;">
            لحد دلوقتي اتعلمنا الـ Lists وعرفنا إنها بتخلينا نخزن أكتر من قيمة ونضيف ونحذف ونعدل براحتنا. لكن... هل كل البيانات ينفع تتغير؟ <strong>الإجابة: لأ!</strong>
            </p>
        </div>
        """, unsafe_allow_html=True)

    # مفهوم الثبات (Immutability) مقابل المتغيرات
    st.markdown("""
        <div dir="rtl" style="direction: rtl; text-align: right; padding: 18px; border: 1px solid rgba(255,255,255,0.1); border-radius: 12px; margin-bottom: 20px; background-color: rgba(255,255,255,0.02);">
            <h4 style="font-size: 16px; font-weight: 700; color: #61afef; margin-bottom: 10px;">🔒 البيانات الثابتة تحتاج Tuple</h4>
            <p style="font-size: 13.5px; opacity: 0.9; line-height: 1.6; margin-bottom: 10px;">
            تخيل عندك بيانات ثابته مش المفروض تتغير أثناء تشغيل البرنامج؛ زي:<br>
            • أيام الأسبوع، شهور السنة.<br>
            • إحداثيات موقع جغرافية.<br>
            • ألوان شعار الشركة الأساسية.
            </p>
            <p style="font-size: 13.5px; opacity: 0.9; line-height: 1.6; margin: 0;">
            هنا بيجي دور الـ <strong>Tuple</strong>؛ هي شبه الـ List جداً، لكن الفرق الجوهري إنها <strong>لا يمكن تعديلها بعد إنشائها</strong>.
            </p>
        </div>
        """, unsafe_allow_html=True)

    # إنشاء الـ Tuple
    st.markdown("""
        <div dir="rtl" style="direction: rtl; text-align: right; padding: 18px; border: 1px solid rgba(255,255,255,0.1); border-radius: 12px; margin-bottom: 15px; background-color: rgba(255,255,255,0.02);">
            <h4 style="font-size: 17px; font-weight: 700; color: #98c379; margin-bottom: 8px;">📝 إنشاء Tuple</h4>
            <p style="font-size: 13.5px; opacity: 0.85; line-height: 1.6;">
            الـ Tuple بتتكتب بين أقواس عادية <code style="color: #e5c07b;" dir="ltr">()</code> بدل الأقواس المربعة <code style="color: #e5c07b;" dir="ltr">[]</code>.
            </p>
        </div>
        """, unsafe_allow_html=True)

    st.code("""# أمثلة لإنشاء Tuples
days = ("Saturday", "Sunday", "Monday")
numbers = (10, 20, 30, 40)""", language="python")

    st.markdown("""
        <div dir="rtl" style="direction: rtl; text-align: right; padding: 15px; border-radius: 8px; margin-bottom: 20px; background: rgba(152, 195, 121, 0.05); border: 1px solid rgba(152, 195, 121, 0.15);">
            <p style="font-size: 13.5px; margin: 0;">
            🎮 <strong>سؤال سريع:</strong> الكود ده List ولا Tuple؟<br>
            <code style="color: #e5c07b;" dir="ltr">cities = ("Cairo", "Alexandria", "Giza")</code><br>
            ✅ <strong>الإجابة:</strong> <code style="color: #98c379;" dir="ltr">Tuple</code> (لأنها مكتوبة بين أقواس عادية <code style="color: #e5c07b;" dir="ltr">()</code>).
            </p>
        </div>
        """, unsafe_allow_html=True)

    # الوصول للعناصر (Index)
    st.markdown("""
        <div dir="rtl" style="direction: rtl; text-align: right; padding: 18px; border: 1px solid rgba(255,255,255,0.1); border-radius: 12px; margin-bottom: 15px; background-color: rgba(255,255,255,0.02);">
            <h4 style="font-size: 17px; font-weight: 700; color: #e5c07b; margin-bottom: 8px;">🔍 الوصول للعناصر (Index)</h4>
            <p style="font-size: 13.5px; opacity: 0.85; line-height: 1.6;">
            الوصول للعناصر بيتم بنفس طريقة الـ List تماماً، حيث يبدأ العد من 0.
            </p>
        </div>
        """, unsafe_allow_html=True)

    st.code("""cities = ("Cairo", "Alexandria", "Giza")

print(cities[0])  # الناتج: Cairo
print(cities[2])  # الناتج: Giza""", language="python")

    st.markdown("""
        <div dir="rtl" style="direction: rtl; text-align: right; padding: 12px; border-radius: 8px; margin-bottom: 20px; background: rgba(255,255,255,0.03);">
            <p style="font-size: 13.5px; margin: 0;">
            🎮 <strong>سؤال سريع:</strong> لو عندك <code style="color: #e5c07b;" dir="ltr">numbers = (5, 10, 15)</code> ونفذت <code style="color: #e5c07b;" dir="ltr">print(numbers[1])</code> إيه الناتج؟<br>
            ✅ <strong>الإجابة:</strong> <code style="color: #98c379;" dir="ltr">10</code>.
            </p>
        </div>
        """, unsafe_allow_html=True)

    # أهم فرق: Immutable
    st.markdown("""
        <div dir="rtl" style="direction: rtl; text-align: right; padding: 18px; border: 1px solid rgba(229, 192, 123, 0.3); border-radius: 12px; margin-bottom: 20px; background-color: rgba(229, 192, 123, 0.04);">
            <h4 style="font-size: 17px; font-weight: 700; color: #e5c07b; margin-bottom: 8px;">⚠️ أهم فرق بين Tuple و List</h4>
            <p style="font-size: 13.5px; opacity: 0.9; line-height: 1.6; margin-bottom: 10px;">
            لو جربت تعدل عنصر في الـ Tuple بالشكل ده:
            </p>
        </div>
        """, unsafe_allow_html=True)

    st.code("""cities = ("Cairo", "Alexandria")
cities[0] = "Giza"  # ❌ هيطلع Error!""", language="python")

    st.markdown("""
        <div dir="rtl" style="direction: rtl; text-align: right; padding: 15px; border-radius: 8px; margin-bottom: 20px; background: rgba(224, 108, 117, 0.05); border: 1px solid rgba(224, 108, 117, 0.15);">
            <p style="font-size: 13.5px; margin: 0;">
            ❌ <strong>ليه بيحصل خطأ؟</strong> لأن الـ Tuple تصنف كـ <strong>Immutable</strong> (غير قابلة للتغيير). بعد ما تنشئها، مينفعش تغير، تحذف، أو تضيف عناصر جديدة. وده أهم فرق بيخلينا نختارها بدل الـ List.
            </p>
        </div>
        """, unsafe_allow_html=True)

    # دوال البحث والعد
    st.markdown("""
        <div dir="rtl" style="direction: rtl; text-align: right; padding: 18px; border: 1px solid rgba(255,255,255,0.1); border-radius: 12px; margin-bottom: 15px; background-color: rgba(255,255,255,0.02);">
            <h4 style="font-size: 17px; font-weight: 700; color: #c678dd; margin-bottom: 10px;">🔢 البحث عن عنصر والعد (index() & count())</h4>
        </div>
        """, unsafe_allow_html=True)

    st.code("""# 1. معرفة مكان عنصر معين باستخدام index()
cities = ("Cairo", "Alexandria", "Giza")
print(cities.index("Alexandria"))  # الناتج: 1 (لأنها في الـ Index رقم 1)

# 2. عدّ تكرار عنصر باستخدام count()
numbers = (10, 20, 10, 30, 10)
print(numbers.count(10))  # الناتج: 3 (لأن الرقم 10 تكرر 3 مرات)""", language="python")

    st.markdown("""
        <div dir="rtl" style="direction: rtl; text-align: right; padding: 12px; border-radius: 8px; margin-bottom: 20px; background: rgba(255,255,255,0.03);">
            <p style="font-size: 13.5px; margin: 0;">
            🎮 <strong>سؤال سريع:</strong> لو عندك <code style="color: #e5c07b;" dir="ltr">letters = ("A", "B", "A", "C")</code> ونفذت <code style="color: #e5c07b;" dir="ltr">print(letters.count("A"))</code> إيه الناتج؟<br>
            ✅ <strong>الإجابة:</strong> <code style="color: #98c379;" dir="ltr">2</code>.
            </p>
        </div>
        """, unsafe_allow_html=True)

    # مقارنة حاسمة بين List و Tuple
    st.markdown("""
        <div dir="rtl" style="direction: rtl; text-align: right; padding: 20px; border: 1px solid rgba(255,255,255,0.1); border-radius: 12px; background-color: rgba(255,255,255,0.02); margin-bottom: 20px;">
            <h3 style="font-size: 18px; font-weight: 700; margin-bottom: 15px;">📌 مقارنة حاسمة: Tuple ولا List؟</h3>
            <table style="width: 100%; text-align: right; border-collapse: collapse; font-size: 14px;">
                <tr style="border-bottom: 1px solid rgba(255,255,255,0.1);">
                    <th style="padding: 10px;">الميزة</th>
                    <th style="padding: 10px;">List</th>
                    <th style="padding: 10px;">Tuple</th>
                </tr>
                <tr style="border-bottom: 1px solid rgba(255,255,255,0.05);">
                    <td style="padding: 10px;">الشكل (Syntax)</td>
                    <td style="padding: 10px;" dir="ltr">[]</td>
                    <td style="padding: 10px;" dir="ltr">()</td>
                </tr>
                <tr style="border-bottom: 1px solid rgba(255,255,255,0.05);">
                    <td style="padding: 10px;">إمكانية التعديل</td>
                    <td style="padding: 10px;">ينفع تعدلها (Mutable)</td>
                    <td style="padding: 10px;">لا يمكن تعديلها (Immutable)</td>
                </tr>
                <tr style="border-bottom: 1px solid rgba(255,255,255,0.05);">
                    <td style="padding: 10px;">الإضافة والحذف</td>
                    <td style="padding: 10px;">متاحة (append, pop)</td>
                    <td style="padding: 10px;">غير متاحة نهائياً</td>
                </tr>
                <tr>
                    <td style="padding: 10px;">الاستخدام الأبرز</td>
                    <td style="padding: 10px;">بيانات متغيرة ومتجددة</td>
                    <td style="padding: 10px;">للبيانات الثابتة والحماية</td>
                </tr>
            </table>
        </div>
        """, unsafe_allow_html=True)

    # Pro-Tip / Data Analysis Connection
    st.markdown("""
        <div dir="rtl" style="direction: rtl; text-align: right; padding: 18px; border: 1px solid rgba(229, 192, 123, 0.3); border-radius: 12px; background-color: rgba(229, 192, 123, 0.04);">
            <h4 style="font-size: 16px; font-weight: 700; color: #e5c07b; margin-bottom: 8px;">💼 هستخدم Tuples فين في Data Analysis؟</h4>
            <p style="font-size: 13.5px; opacity: 0.9; line-height: 1.6; margin-bottom: 10px;">
            في تحليل البيانات، صح إنك مش هتستخدم الـ Tuples بنفس كتافة الـ Lists، لكنها بتظهر في مواقف حاسمة جداً؛ زي إحداثيات الجغرافيا للمتاجر (<code style="color: #98c379;" dir="ltr">Latitude, Longitude</code>)، أو القيم الثابتة في إعدادات ملفات الـ Configuration.
            </p>
            <p style="font-size: 13.5px; opacity: 0.9; line-height: 1.6; margin: 0;">
            💡 <strong>معلومة من كواليس بايثون:</strong> كود الـ Tuples أسرع في التنفيذ وأقل استهلاكاً للذاكرة مقارنة بالـ Lists، وده لأن بايثون عارفة إن محتواها مش هيتغير أبداً فبتوفر في تخصيص الذاكرة (Memory Allocation).
            </p>
        </div>
        """, unsafe_allow_html=True)


def render_python_lesson_5():
    # الهيدر الرئيسي للمحطة
    st.markdown("""
        <div dir="rtl" style="direction: rtl; text-align: right;">
            <h2 style="font-weight: 800; font-size: 22px; color: #fff; margin-bottom: 8px;">🗂️ المحطة 5: Dictionaries — لما كل قيمة يكون ليها اسم</h2>
            <p style="opacity: 0.85; font-size: 14.5px; line-height: 1.7; margin-bottom: 20px;">
            تخيل إن عندك بيانات عميل واحد:<br>
            <code style="color: #61afef;" dir="ltr">name = "Omar"</code><br>
            <code style="color: #61afef;" dir="ltr">age = 21</code><br>
            <code style="color: #61afef;" dir="ltr">city = "Alexandria"</code><br>
            المشكلة إن كل معلومة موجودة في Variable منفصل. فلو عايزين نجمع بيانات العميل كلها في مكان واحد؟ هنا بيجي دور الـ <strong>Dictionary</strong>.
            </p>
        </div>
        """, unsafe_allow_html=True)

    # مفهوم Key → Value
    st.markdown("""
        <div dir="rtl" style="direction: rtl; text-align: right; padding: 18px; border: 1px solid rgba(255,255,255,0.1); border-radius: 12px; margin-bottom: 20px; background-color: rgba(255,255,255,0.02);">
            <h4 style="font-size: 16px; font-weight: 700; color: #98c379; margin-bottom: 10px;">🔑 فكرة الـ Key-Value</h4>
            <p style="font-size: 13.5px; opacity: 0.9; line-height: 1.6; margin-bottom: 10px;">
            الـ Dictionary بيخزن البيانات بنظام المفتاح والقيمة (<code style="color: #e5c07b;" dir="ltr">Key → Value</code>)؛ يعني كل معلومة ليها اسم دلالي بيميزها، وبنكتبه في بايثون باستخدام الأقواس المعقوصة <code style="color: #e5c07b;" dir="ltr">{}</code>:
            </p>
        </div>
        """, unsafe_allow_html=True)

    st.code("""customer = {
    "name": "Omar",
    "age": 21,
    "city": "Alexandria"
}
# "name" هو الـ Key و "Omar" هي الـ Value""", language="python")

    # الوصول للبيانات باستخدام الـ Key
    st.markdown("""
        <div dir="rtl" style="direction: rtl; text-align: right; padding: 18px; border: 1px solid rgba(255,255,255,0.1); border-radius: 12px; margin-bottom: 15px; background-color: rgba(255,255,255,0.02);">
            <h4 style="font-size: 17px; font-weight: 700; color: #e5c07b; margin-bottom: 8px;">🔍 الوصول للبيانات باستخدام الـ Key</h4>
            <p style="font-size: 13.5px; opacity: 0.85; line-height: 1.6;">
            في الـ List كنا بنستخدم الـ Index، أما هنا فمش محتاج تحفظ رقم العنصر؛ بتستخدم الـ Key مباشرة:
            </p>
        </div>
        """, unsafe_allow_html=True)

    st.code("""print(customer["name"])  # الناتج: Omar
print(customer["city"])  # الناتج: Alexandria""", language="python")

    st.markdown("""
        <div dir="rtl" style="direction: rtl; text-align: right; padding: 12px; border-radius: 8px; margin-bottom: 20px; background: rgba(255,255,255,0.03);">
            <p style="font-size: 13.5px; margin: 0;">
            🎮 <strong>سؤال سريع:</strong> لو عندك <code style="color: #e5c07b;" dir="ltr">product = {"name": "Laptop", "price": 25000}</code> ونفذت <code style="color: #e5c07b;" dir="ltr">print(product["price"])</code> إيه الناتج؟<br>
            ✅ <strong>الإجابة:</strong> <code style="color: #98c379;" dir="ltr">25000</code> (لأننا طلبنا القيمة المرتبطة بالـ Key "price").
            </p>
        </div>
        """, unsafe_allow_html=True)

    # Keys و Values
    st.markdown("""
        <div dir="rtl" style="direction: rtl; text-align: right; padding: 18px; border: 1px solid rgba(255,255,255,0.1); border-radius: 12px; margin-bottom: 15px; background-color: rgba(255,255,255,0.02);">
            <h4 style="font-size: 17px; font-weight: 700; color: #c678dd; margin-bottom: 10px;">📋 استعراض الـ Keys والـ Values</h4>
        </div>
        """, unsafe_allow_html=True)

    st.code("""customer = {"name": "Omar", "age": 21}

print(customer.keys())    # الناتج: استعراض المفاتيح (name, age)
print(customer.values())  # الناتج: استعراض القيم (Omar, 21)""", language="python")

    # إضافة وتعديل البيانات
    st.markdown("""
        <div dir="rtl" style="direction: rtl; text-align: right; padding: 18px; border: 1px solid rgba(255,255,255,0.1); border-radius: 12px; margin-bottom: 15px; background-color: rgba(255,255,255,0.02);">
            <h4 style="font-size: 17px; font-weight: 700; color: #61afef; margin-bottom: 10px;">➕ إضافة، تغيير، وتحديث البيانات</h4>
        </div>
        """, unsafe_allow_html=True)

    st.code("""# 1. إضافة بيانات جديدة
customer["city"] = "Alexandria"

# 2. تغيير قيمة موجودة (Replace)
customer["age"] = 22  # العمر اتغير من 21 لـ 22

# 3. استخدام دالة update() لتحديث أو إضافة عدة قيم دفعة واحدة
customer.update({
    "age": 22,
    "city": "Cairo",
    "job": "Data Analyst"  # لو الـ Key مش موجود، هتضيفه تلقائياً
})""", language="python")

    st.markdown("""
        <div dir="rtl" style="direction: rtl; text-align: right; padding: 12px; border-radius: 8px; margin-bottom: 20px; background: rgba(97, 175, 239, 0.05); border: 1px solid rgba(97, 175, 239, 0.15);">
            <p style="font-size: 13.5px; margin: 0;">
            🎮 <strong>سؤال سريع:</strong> لو عندك <code style="color: #e5c07b;" dir="ltr">product = {"name": "Laptop", "price": 20000}</code> ونفذت <code style="color: #e5c07b;" dir="ltr">product["price"] = 22000</code>، إيه قيمة price؟<br>
            ✅ <strong>الإجابة:</strong> <code style="color: #98c379;" dir="ltr">22000</code> (تم عمل Replace للقيمة القديمة).
            </p>
        </div>
        """, unsafe_allow_html=True)

    # الحذف والمسح
    st.markdown("""
        <div dir="rtl" style="direction: rtl; text-align: right; padding: 18px; border: 1px solid rgba(255,255,255,0.1); border-radius: 12px; margin-bottom: 15px; background-color: rgba(255,255,255,0.02);">
            <h4 style="font-size: 17px; font-weight: 700; color: #e06c75; margin-bottom: 10px;">🗑️ حذف ومسح البيانات</h4>
        </div>
        """, unsafe_allow_html=True)

    st.code("""# 1. حذف Key معين باستخدام pop()
customer.pop("age")

# 2. حذف آخر Key-Value pair باستخدام popitem()
customer.popitem()

# 3. تفريغ الـ Dictionary بالكامل مع الاحتفاظ به كـ Object فارغ باستخدام clear()
customer.clear()  # الناتج: {}""", language="python")

    # مقارنة حاسمة: List ولا Dictionary؟
    st.markdown("""
        <div dir="rtl" style="direction: rtl; text-align: right; padding: 20px; border: 1px solid rgba(255,255,255,0.1); border-radius: 12px; background-color: rgba(255,255,255,0.02); margin-bottom: 20px;">
            <h3 style="font-size: 18px; font-weight: 700; margin-bottom: 15px;">🧠 مقارنة حاسمة: List ولا Dictionary؟</h3>
            <p style="font-size: 13.5px; opacity: 0.9; line-height: 1.6; margin-bottom: 12px;">
            • لو عندك عناصر متتابعة بتتعامل معها بالـ Index (زي <code style="color: #98c379;" dir="ltr">products = ["Laptop", "Mouse", "Keyboard"]</code>) استخدم <strong>List</strong>.<br>
            • لو عندك بيانات كل جزء فيها ليه اسم ومعنى واضح (زي بيانات منتج أو عميل متكاملة) استخدم <strong>Dictionary</strong>.
            </p>
        </div>
        """, unsafe_allow_html=True)

    # أشهر الأخطاء
    st.markdown("""
        <div dir="rtl" style="direction: rtl; text-align: right; padding: 18px; border: 1px solid rgba(224, 108, 117, 0.3); border-radius: 12px; margin-bottom: 20px; background-color: rgba(224, 108, 117, 0.04);">
            <h4 style="font-size: 16px; font-weight: 700; color: #e06c75; margin-bottom: 8px;">⚠️ أشهر الأخطاء (KeyError)</h4>
            <p style="font-size: 13.5px; opacity: 0.9; line-height: 1.6; margin: 0;">
            لو كتبت <code style="color: #e06c75;" dir="ltr">print(customer["phone"])</code> وكلمة phone مش موجودة كـ Key أساساً، بايثون هتطلع لك خطأ يسمى <code style="color: #e06c75;" dir="ltr">KeyError</code>. علشان كده لازم تتأكد إن المفتاح موجود، أو تستخدم طرق أكثر أماناً زي دالة <code style="color: #98c379;" dir="ltr">get()</code>.
            </p>
        </div>
        """, unsafe_allow_html=True)

    # Pro-Tip / Data Analysis Connection
    st.markdown("""
        <div dir="rtl" style="direction: rtl; text-align: right; padding: 18px; border: 1px solid rgba(229, 192, 123, 0.3); border-radius: 12px; background-color: rgba(229, 192, 123, 0.04);">
            <h4 style="font-size: 16px; font-weight: 700; color: #e5c07b; margin-bottom: 8px;">💼 هستخدم Dictionaries فين في Data Analysis؟</h4>
            <p style="font-size: 13.5px; opacity: 0.9; line-height: 1.6; margin-bottom: 10px;">
            تخيل بيانات منتج بالشكل ده:<br>
            <code style="color: #98c379;" dir="ltr">product = {"product_name": "Laptop", "category": "Electronics", "price": 25000, "stock": 15}</code><br>
            هذا الشكل يتطابق تماماً مع هيكل ملفات الـ JSON ونتائج الـ APIs في مشاريع الـ Data Analysis الحقيقية.
            </p>
            <p style="font-size: 13.5px; opacity: 0.9; line-height: 1.6; margin: 0;">
            💡 <strong>معلومة من كواليس علم البيانات:</strong> مكتبة Pandas العملاقة في تحليل البيانات تتعامل مع الجداول (DataFrames) في الأساس باعتبارها مجموعة من الـ Dictionaries المترابطة (Columns as Keys & Rows as Values)، وفهمك للـ Dictionaries هو المفتاح السحري لربط بايثون بقواعد البيانات والويب APIs!
            </p>
        </div>
        """, unsafe_allow_html=True)

    # اختبار سريع (آخر سؤال في المنشور)
    st.markdown("""
        <div dir="rtl" style="direction: rtl; text-align: right; padding: 15px; border-radius: 8px; margin-bottom: 10px; background: rgba(152, 195, 121, 0.05); border: 1px solid rgba(152, 195, 121, 0.15);">
            <p style="font-size: 13.5px; margin: 0;">
            🎮 <strong>آخر اختبار:</strong> لو عندك <code style="color: #e5c07b;" dir="ltr">student = {"name": "Ahmed", "grade": 85}</code> وعايز تغير الدرجة إلى 95، إيه الصح؟<br>
            ✅ <strong>الإجابة الصحيحة هي (A):</strong> <code style="color: #98c379;" dir="ltr">student["grade"] = 95</code> لأننا بنوصل للـ Key ونغير الـ Value مباشرة.
            </p>
        </div>
        """, unsafe_allow_html=True)


def render_python_lesson_6():
    # الهيدر الرئيسي للمحطة
    st.markdown("""
        <div dir="rtl" style="direction: rtl; text-align: right;">
            <h2 style="font-weight: 800; font-size: 22px; color: #fff; margin-bottom: 8px;">🧩 المحطة 6: Sets — لما التكرار مش مهم</h2>
            <p style="opacity: 0.85; font-size: 14.5px; line-height: 1.7; margin-bottom: 20px;">
            تخيل إن عندك قائمتين من العملاء:<br>
            القائمة الأولى: <code style="color: #61afef;" dir="ltr">customers_a = ["Ahmed", "Sara", "Omar", "Ahmed"]</code><br>
            والقائمة الثانية: <code style="color: #61afef;" dir="ltr">customers_b = ["Omar", "Ali", "Sara", "Ali"]</code><br>
            لو سألتك: <strong>كام عميل مختلف عندي؟</strong> هنا هتبدأ تواجه مشكلة التكرار، وهنا بيجي دور الـ <strong>Set</strong>.
            </p>
        </div>
        """, unsafe_allow_html=True)

    # يعني إيه Set؟
    st.markdown("""
        <div dir="rtl" style="direction: rtl; text-align: right; padding: 18px; border: 1px solid rgba(255,255,255,0.1); border-radius: 12px; margin-bottom: 20px; background-color: rgba(255,255,255,0.02);">
            <h4 style="font-size: 16px; font-weight: 700; color: #98c379; margin-bottom: 10px;">🎯 يعني إيه Set؟</h4>
            <p style="font-size: 13.5px; opacity: 0.9; line-height: 1.6; margin-bottom: 10px;">
            الـ Set هي نوع من أنواع البيانات في Python بتخزن مجموعة من القيم <strong>من غير تكرار</strong>، وبنكتبها باستخدام الأقواس المعقوصة <code style="color: #e5c07b;" dir="ltr">{}</code>:
            </p>
        </div>
        """, unsafe_allow_html=True)

    st.code("""customers = {"Ahmed", "Sara", "Omar", "Ahmed"}
# Python هتحتفظ بالقيم المختلفة فقط:
# {"Ahmed", "Sara", "Omar"}""", language="python")

    # نقطة مهمة جداً (مش List)
    st.markdown("""
        <div dir="rtl" style="direction: rtl; text-align: right; padding: 18px; border: 1px solid rgba(224, 108, 117, 0.3); border-radius: 12px; margin-bottom: 20px; background-color: rgba(224, 108, 117, 0.04);">
            <h4 style="font-size: 16px; font-weight: 700; color: #e06c75; margin-bottom: 8px;">⚠️ نقطة مهمة جداً</h4>
            <p style="font-size: 13.5px; opacity: 0.9; line-height: 1.6; margin: 0;">
            الـ Set <strong>مش List</strong>؛ يعني متتعاملش معاها على أساس إن كل عنصر له Index ثابت (زي <code style="color: #e06c75;" dir="ltr">customers[0]</code>)، لأن الـ Set مش معمولة للوصول للعناصر عن طريق Index.
            </p>
        </div>
        """, unsafe_allow_html=True)

    # ليه أحتتاجها كـ Data Analyst (Unique Values)
    st.markdown("""
        <div dir="rtl" style="direction: rtl; text-align: right; padding: 18px; border: 1px solid rgba(229, 192, 123, 0.3); border-radius: 12px; background-color: rgba(229, 192, 123, 0.04); margin-bottom: 20px;">
            <h4 style="font-size: 16px; font-weight: 700; color: #e5c07b; margin-bottom: 8px;">💼 طب ليه ممكن أحتاجها كـ Data Analyst؟</h4>
            <p style="font-size: 13.5px; opacity: 0.9; line-height: 1.6; margin-bottom: 10px;">
            لو عندك بيانات عملاء متكررة وعايز تعرف القيم الفريدة (<strong style="color: #98c379;">Unique Values</strong>)، تقدر تحولها فوراً لـ Set:
            </p>
        </div>
        """, unsafe_allow_html=True)

    st.code("""customers = ["Ahmed", "Sara", "Ahmed", "Omar", "Sara"]
unique_customers = set(customers)

print(unique_customers)  # هتلاقي التكرار اختفى!""", language="python")

    # Union — إيه الموجود في المجموعتين مع بعض؟
    st.markdown("""
        <div dir="rtl" style="direction: rtl; text-align: right; padding: 18px; border: 1px solid rgba(255,255,255,0.1); border-radius: 12px; margin-bottom: 15px; background-color: rgba(255,255,255,0.02);">
            <h4 style="font-size: 17px; font-weight: 700; color: #61afef; margin-bottom: 10px;">🔗 Union — إيه الموجود في المجموعتين مع بعض؟</h4>
            <p style="font-size: 13.5px; opacity: 0.85; line-height: 1.6;">
            لما تحب تجمع كل الأشخاص أو العناصر الموجودة في مجموعتين بدون تكرار، بتستخدم دالة <code style="color: #e5c07b;" dir="ltr">union()</code>:
            </p>
        </div>
        """, unsafe_allow_html=True)

    st.code("""team_a = {"Ahmed", "Sara", "Omar"}
team_b = {"Omar", "Ali", "Sara"}

all_members = team_a.union(team_b)
print(all_members)  # يدمج المجموعتين ويتخلص من التكرار""", language="python")

    st.markdown("""
        <div dir="rtl" style="direction: rtl; text-align: right; padding: 12px; border-radius: 8px; margin-bottom: 20px; background: rgba(255,255,255,0.03);">
            <p style="font-size: 13.5px; margin: 0;">
            🎮 <strong>سؤال سريع:</strong> لو عندك <code style="color: #e5c07b;" dir="ltr">a = {"Python", "SQL"}</code> و <code style="color: #e5c07b;" dir="ltr">b = {"Python", "Power BI"}</code>، إيه العناصر الموجودة في المجموعتين مع بعض؟<br>
            ✅ <strong>الإجابة:</strong> <code style="color: #98c379;" dir="ltr">Python, SQL, Power BI</code> (لأن union() بتجمع العناصر المختلفة).
            </p>
        </div>
        """, unsafe_allow_html=True)

    # Difference — إيه الموجود هنا ومش موجود هناك؟
    st.markdown("""
        <div dir="rtl" style="direction: rtl; text-align: right; padding: 18px; border: 1px solid rgba(255,255,255,0.1); border-radius: 12px; margin-bottom: 15px; background-color: rgba(255,255,255,0.02);">
            <h4 style="font-size: 17px; font-weight: 700; color: #c678dd; margin-bottom: 10px;">➖ Difference — إيه الموجود هنا ومش موجود هناك؟</h4>
            <p style="font-size: 13.5px; opacity: 0.85; line-height: 1.6;">
            من أهم أفكار الـ Sets؛ لمعرفة العناصر الموجودة في مجموعة ومش موجودة في الأخرى باستخدام <code style="color: #e5c07b;" dir="ltr">difference()</code>:
            </p>
        </div>
        """, unsafe_allow_html=True)

    st.code("""python_students = {"Ahmed", "Sara", "Omar"}
sql_students = {"Sara", "Omar", "Ali"}

# مين بيتعلم Python ومش بيتعلم SQL؟
print(python_students.difference(sql_students))  # الناتج: {"Ahmed"}""", language="python")

    st.markdown("""
        <div dir="rtl" style="direction: rtl; text-align: right; padding: 12px; border-radius: 8px; margin-bottom: 20px; background: rgba(198, 120, 221, 0.05); border: 1px solid rgba(198, 120, 221, 0.15);">
            <p style="font-size: 13.5px; margin: 0;">
            🔄 <strong>خلاصة الاتجاه:</strong> <code style="color: #e5c07b;" dir="ltr">python_students.difference(sql_students)</code> مش زي العكس! الأولى بتسأل (إيه في بايثون ومش في إس كيو إل؟)، ودي غلطة شائعة جداً لازم تاخد بالك منها.
            </p>
        </div>
        """, unsafe_allow_html=True)

    # الحذف (remove و pop)
    st.markdown("""
        <div dir="rtl" style="direction: rtl; text-align: right; padding: 18px; border: 1px solid rgba(255,255,255,0.1); border-radius: 12px; margin-bottom: 15px; background-color: rgba(255,255,255,0.02);">
            <h4 style="font-size: 17px; font-weight: 700; color: #e06c75; margin-bottom: 10px;">🗑️ حذف العناصر: remove() مقابل pop()</h4>
        </div>
        """, unsafe_allow_html=True)

    st.code("""skills = {"Python", "SQL", "Power BI"}

# 1. حذف عنصر معين بـ remove() (ولو مش موجود بتطلع KeyError)
skills.remove("SQL")

# 2. حذف عنصر عشوائي بـ pop() (الـ Set غير مرتبة، فمتفترضش إنه آخر عنصر!)
skills.pop()""", language="python")

    st.markdown("""
        <div dir="rtl" style="direction: rtl; text-align: right; padding: 12px; border-radius: 8px; margin-bottom: 20px; background: rgba(255,255,255,0.03);">
            <p style="font-size: 13.5px; margin: 0;">
            🎮 <strong>سؤال سريع:</strong> لو عندك <code style="color: #e5c07b;" dir="ltr">skills = {"Python", "SQL", "Excel"}</code> وعايز تحذف "SQL" تحديداً، تستخدم إيه؟<br>
            ✅ <strong>الإجابة (A):</strong> <code style="color: #98c379;" dir="ltr">skills.remove("SQL")</code> لأن remove() بتحدد العنصر المطلوب بدقة.
            </p>
        </div>
        """, unsafe_allow_html=True)

    # مقارنة شاملة: List ولا Dictionary ولا Set؟
    st.markdown("""
        <div dir="rtl" style="direction: rtl; text-align: right; padding: 20px; border: 1px solid rgba(255,255,255,0.1); border-radius: 12px; background-color: rgba(255,255,255,0.02); margin-bottom: 20px;">
            <h3 style="font-size: 18px; font-weight: 700; margin-bottom: 15px;">🧠 مقارنة شاملة: أستخدم إيه ومتى؟</h3>
            <p style="font-size: 13.5px; opacity: 0.9; line-height: 1.7; margin-bottom: 0;">
            📋 <strong>List:</strong> لما يكون ترتيب العناصر مهم أو محتاج تعدل وتتعامل مع العناصر بالـ Index (<code style="color: #98c379;" dir="ltr">["Ahmed", "Sara", "Omar"]</code>).<br>
            🗂️ <strong>Dictionary:</strong> لما كل قيمة مرتبطة بـ Key وتعبر عن سمات لكيان واحد (<code style="color: #98c379;" dir="ltr">{"name": "Ahmed", "age": 22}</code>).<br>
            🧩 <strong>Set:</strong> لما يكون هدفك الأساسي التعامل مع قيم فريدة وفحص مجموعات العناصر بدون تكرار (<code style="color: #98c379;" dir="ltr">{"Ahmed", "Sara", "Omar"}</code>).
            </p>
        </div>
        """, unsafe_allow_html=True)

    # تطبيق عملي في Data Analysis (LinkedIn vs GitHub)
    st.markdown("""
        <div dir="rtl" style="direction: rtl; text-align: right; padding: 18px; border: 1px solid rgba(97, 175, 239, 0.3); border-radius: 12px; background-color: rgba(97, 175, 239, 0.04);">
            <h4 style="font-size: 16px; font-weight: 700; color: #61afef; margin-bottom: 8px;">💼 مثال حقيقي من Data Analysis</h4>
            <p style="font-size: 13.5px; opacity: 0.9; line-height: 1.6; margin-bottom: 10px;">
            تخيل عندك مستخدمين على منصتين:<br>
            <code style="color: #e5c07b;" dir="ltr">linkedin = {"Ahmed", "Sara", "Omar", "Ali"}</code><br>
            <code style="color: #e5c07b;" dir="ltr">github = {"Omar", "Ali", "Mona"}</code><br>
            • لمعرفة الناس الموجودة على LinkedIn ومش موجودة على GitHub: <code style="color: #98c379;" dir="ltr">linkedin.difference(github)</code> ➔ الناتج: <code style="color: #98c379;" dir="ltr">{"Ahmed", "Sara"}</code><br>
            • لمعرفة كل الأشخاص الموجودين على أي منصة (دَمج وظيفي): <code style="color: #98c379;" dir="ltr">linkedin.union(github)</code>
            </p>
            <p style="font-size: 13.5px; opacity: 0.9; line-height: 1.6; margin: 0;">
            وده بيوضحلك ليه عمليات مجموعات البيانات موجودة وأساسية في تحليل البيانات!
            </p>
        </div>
        """, unsafe_allow_html=True)


def render_python_lesson_7():
    # الهيدر الرئيسي للمحطة
    st.markdown("""
        <div dir="rtl" style="direction: rtl; text-align: right;">
            <h2 style="font-weight: 800; font-size: 22px; color: #fff; margin-bottom: 8px;">🧠 المحطة 7: Python Logic — إزاي نخلي البرنامج يفكر وياخد قرار؟</h2>
            <p style="opacity: 0.85; font-size: 14.5px; line-height: 1.7; margin-bottom: 20px;">
            لحد دلوقتي بايثون كانت بتنفذ الأوامر حرفياً زيمّا بنقولها. لكن تخيل إنك عايز البرنامج <strong>ياخد قرار بنفسه</strong> (زي: لو درجة الطالب أكبر من أو تساوي 50 يبقى ناجح، وإلا فراسب). هنا بندخل في عالم الـ Logic و Decision Making.
            </p>
        </div>
        """, unsafe_allow_html=True)

    # Comparison Operators
    st.markdown("""
        <div dir="rtl" style="direction: rtl; text-align: right; padding: 18px; border: 1px solid rgba(255,255,255,0.1); border-radius: 12px; margin-bottom: 15px; background-color: rgba(255,255,255,0.02);">
            <h4 style="font-size: 17px; font-weight: 700; color: #61afef; margin-bottom: 10px;">🔍 أول حاجة: Comparison Operators (المقارنات)</h4>
            <p style="font-size: 13.5px; opacity: 0.85; line-height: 1.6;">
            قبل ما بايثون تاخد قرار، لازم تعرف تقارن بين قيمتين وترجع نتيجة منطقية (<code style="color: #98c379;" dir="ltr">True</code> أو <code style="color: #e06c75;" dir="ltr">False</code>):
            </p>
        </div>
        """, unsafe_allow_html=True)

    st.code("""age = 21
print(age > 18)  # الناتج: True (لأن 21 فعلًا أكبر من 18)""", language="python")

    # جدول مختصر لعلامات المقارنة
    st.markdown("""
        <div dir="rtl" style="direction: rtl; text-align: right; padding: 15px; border-radius: 10px; background: rgba(255,255,255,0.02); border: 1px solid rgba(255,255,255,0.08); margin-bottom: 15px;">
            <p style="font-size: 13.5px; line-height: 1.8; margin: 0;">
            • <code style="color: #e5c07b;" dir="ltr">==</code> (يساوي) &nbsp;|&nbsp; 
            • <code style="color: #e5c07b;" dir="ltr">!=</code> (لا يساوي)<br>
            • <code style="color: #e5c07b;" dir="ltr">></code> (أكبر من) &nbsp;|&nbsp; 
            • <code style="color: #e5c07b;" dir="ltr"><</code> (أصغر من)<br>
            • <code style="color: #e5c07b;" dir="ltr">>=</code> (أكبر من أو يساوي) &nbsp;|&nbsp; 
            • <code style="color: #e5c07b;" dir="ltr"><=</code> (أصغر من أو يساوي)
            </p>
        </div>
        """, unsafe_allow_html=True)

    # تحذير الفرق بين = و ==
    st.markdown("""
        <div dir="rtl" style="direction: rtl; text-align: right; padding: 15px; border: 1px solid rgba(224, 108, 117, 0.3); border-radius: 10px; margin-bottom: 20px; background-color: rgba(224, 108, 117, 0.04);">
            <h4 style="font-size: 15px; font-weight: 700; color: #e06c75; margin-bottom: 6px;">⚠️ خلي بالك جدًا: الفرق بين = و ==</h4>
            <p style="font-size: 13.5px; opacity: 0.9; margin: 0;">
            • <code style="color: #61afef;" dir="ltr">=</code> دي Assignment (وضع قيمة في Variable مثل <code style="color: #61afef;" dir="ltr">score = 85</code>).<br>
            • <code style="color: #e5c07b;" dir="ltr">==</code> دي Comparison (مقارنة هل القيمة تساوي الأخرى مثل <code style="color: #e5c07b;" dir="ltr">score == 85</code>).
            </p>
        </div>
        """, unsafe_allow_html=True)

    # Logical Operators (and, or, not)
    st.markdown("""
        <div dir="rtl" style="direction: rtl; text-align: right; padding: 18px; border: 1px solid rgba(255,255,255,0.1); border-radius: 12px; margin-bottom: 15px; background-color: rgba(255,255,255,0.02);">
            <h4 style="font-size: 17px; font-weight: 700; color: #98c379; margin-bottom: 10px;">🧩 ربط الشروط: and، or، و not</h4>
        </div>
        """, unsafe_allow_html=True)

    st.code("""# 1. and (لازم كل الشروط تتحقق)
math = 80
python = 90
print(math >= 50 and python >= 50)  # True

# 2. or (كفاية شرط واحد يتحقق)
experience = 0
certificate = True
print(experience > 1 or certificate == True)  # True

# 3. not (عكس النتيجة)
is_student = True
print(not is_student)  # False""", language="python")

    # Algorithms & Decision Making
    st.markdown("""
        <div dir="rtl" style="direction: rtl; text-align: right; padding: 18px; border: 1px solid rgba(255,255,255,0.1); border-radius: 12px; margin-bottom: 15px; background-color: rgba(255,255,255,0.02);">
            <h4 style="font-size: 17px; font-weight: 700; color: #c678dd; margin-bottom: 10px;">🧭 Decision Making: الـ Algorithms و If Statements</h4>
            <p style="font-size: 13.5px; opacity: 0.85; line-height: 1.6;">
            الـ Algorithm هو مجموعة خطوات مرتبة لحل مشكلة. وباستخدام جمل الشروط (<code style="color: #e5c07b;" dir="ltr">if</code>, <code style="color: #e5c07b;" dir="ltr">elif</code>, <code style="color: #e5c07b;" dir="ltr">else</code>) بنحول الخطوات دي لكود ذكي:
            </p>
        </div>
        """, unsafe_allow_html=True)

    st.code("""score = 82

if score >= 90:
    print("Excellent")
elif score >= 75:
    print("Very Good")
elif score >= 50:
    print("Passed")
else:
    print("Failed")
# الناتج: Very Good (بايثون بتبدأ من فوق لأول شرط صح وتتوقف عنده)""", language="python")

    # تنبيه الـ Indentation والأخطاء الشائعة
    st.markdown("""
        <div dir="rtl" style="direction: rtl; text-align: right; padding: 15px; border: 1px solid rgba(229, 192, 123, 0.3); border-radius: 10px; margin-bottom: 20px; background-color: rgba(229, 192, 123, 0.04);">
            <h4 style="font-size: 15px; font-weight: 700; color: #e5c07b; margin-bottom: 6px;">⚠️ أشهر الأخطاء وأهمية الـ Indentation (المسافة البادئة)</h4>
            <p style="font-size: 13.5px; opacity: 0.9; line-height: 1.6; margin: 0;">
            1. استخدام <code style="color: #e06c75;" dir="ltr">=</code> بدل <code style="color: #e5c07b;" dir="ltr">==</code> في المقارنة.<br>
            2. نسيان النقطتين <code style="color: #e5c07b;" dir="ltr">:</code> في نهاية جملة الشرط.<br>
            3. مشكلة الـ Indentation: المسافة قبل الكود تحت الـ <code style="color: #e5c07b;" dir="ltr">if</code> مش مجرد شكل جمالي؛ دي اللي بتحدد الأكواد التابعة للشرط.
            </p>
        </div>
        """, unsafe_allow_html=True)

    # تطبيق عملي في Data Analysis
    st.markdown("""
        <div dir="rtl" style="direction: rtl; text-align: right; padding: 18px; border: 1px solid rgba(97, 175, 239, 0.3); border-radius: 12px; background-color: rgba(97, 175, 239, 0.04);">
            <h4 style="font-size: 16px; font-weight: 700; color: #61afef; margin-bottom: 8px;">💼 تطبيق عملي في Data Analysis</h4>
            <p style="font-size: 13.5px; opacity: 0.9; line-height: 1.6; margin-bottom: 10px;">
            تخيل تصنيف أداء الموظفين أو المبيعات:<br>
            <code style="color: #e5c07b;" dir="ltr">sales = 120000</code><br>
            <code style="color: #98c379;" dir="ltr">if sales >= 150000: print("Excellent")</code><br>
            <code style="color: #98c379;" dir="ltr">elif sales >= 100000: print("Good") ...</code>
            </p>
            <p style="font-size: 13.5px; opacity: 0.9; line-height: 1.6; margin: 0;">
            إحنا بنتعلم طريقة التفكير الشرطي دي مش بس لبرامج عادية، دي اللي هتستخدمها بعدين على آلاف أو ملايين الصفوف في تحليل البيانات باستخدام Pandas!
            </p>
        </div>
        """, unsafe_allow_html=True)


def render_python_lesson_8():
    # الهيدر الرئيسي للمحطة
    st.markdown("""
        <div dir="rtl" style="direction: rtl; text-align: right;">
            <h2 style="font-weight: 800; font-size: 22px; color: #fff; margin-bottom: 8px;">🔁 المحطة 8: While Loop — إزاي نخلي Python تكرر الشغل لوحدها؟</h2>
            <p style="opacity: 0.85; font-size: 14.5px; line-height: 1.7; margin-bottom: 20px;">
            تخيل إن عندك 50,000 عميل وعايز تطبع أسماءهم؛ هل هتكتب <code style="color: #61afef;" dir="ltr">print()</code> خمسين ألف مرة؟ طبعًا لأ! هنا بيجي مفهوم الـ <strong>Loop</strong> (الحلقات التكرارية) وبأشهر أنواعها: <code style="color: #e5c07b;" dir="ltr">while</code>.
            </p>
        </div>
        """, unsafe_allow_html=True)

    # يعني إيه while؟
    st.markdown("""
        <div dir="rtl" style="direction: rtl; text-align: right; padding: 18px; border: 1px solid rgba(255,255,255,0.1); border-radius: 12px; margin-bottom: 15px; background-color: rgba(255,255,255,0.02);">
            <h4 style="font-size: 17px; font-weight: 700; color: #98c379; margin-bottom: 10px;">🧠 يعني إيه while؟</h4>
            <p style="font-size: 13.5px; opacity: 0.85; line-height: 1.6;">
            كلمة while بمعناها البسيط: <strong>طول ما الشرط صحيح... كمل تكرار</strong>. وبايثون بتقييم الشرط في كل مرة قبل تنفيذ الكود جواها:
            </p>
        </div>
        """, unsafe_allow_html=True)

    st.code("""count = 1

while count <= 5:
    print(count)
    count += 1  # ضروري لتغيير قيمة الشرط

# الناتج: 1, 2, 3, 4, 5""", language="python")

    # تحذير الـ Infinite Loop
    st.markdown("""
        <div dir="rtl" style="direction: rtl; text-align: right; padding: 15px; border: 1px solid rgba(224, 108, 117, 0.3); border-radius: 10px; margin-bottom: 20px; background-color: rgba(224, 108, 117, 0.04);">
            <h4 style="font-size: 15px; font-weight: 700; color: #e06c75; margin-bottom: 6px;">⚠️ أهم حاجة في while: تجنب الـ Infinite Loop</h4>
            <p style="font-size: 13.5px; opacity: 0.9; line-height: 1.6; margin: 0;">
            لازم يكون فيه حاجة جوه الكود بتغير الشرط (زي <code style="color: #e06c75;" dir="ltr">count += 1</code>)؛ لو نسيتها، الشرط هيضل دايمًا True والبرنامج هيفضل شغال للأبد في ما يسمى بـ <strong style="color: #e06c75;">Infinite Loop</strong>.
            </p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("""
        <div dir="rtl" style="direction: rtl; text-align: right; padding: 12px; border-radius: 8px; margin-bottom: 20px; background: rgba(255,255,255,0.03);">
            <p style="font-size: 13.5px; margin: 0;">
            🎮 <strong>سؤال سريع:</strong> لو عندك <code style="color: #e5c07b;" dir="ltr">x = 1</code> وتنفذت الـ while loop لحد <code style="color: #e5c07b;" dir="ltr">x <= 3</code> مع <code style="color: #e5c07b;" dir="ltr">x += 1</code>، الناتج بيكون: <code style="color: #98c379;" dir="ltr">1, 2, 3</code>.
            </p>
        </div>
        """, unsafe_allow_html=True)

    # break و continue
    st.markdown("""
        <div dir="rtl" style="direction: rtl; text-align: right; padding: 18px; border: 1px solid rgba(255,255,255,0.1); border-radius: 12px; margin-bottom: 15px; background-color: rgba(255,255,255,0.02);">
            <h4 style="font-size: 17px; font-weight: 700; color: #61afef; margin-bottom: 10px;">🛑 التحكم في اللوب: break مقابل continue</h4>
            <p style="font-size: 13.5px; opacity: 0.85; line-height: 1.6; margin-bottom: 10px;">
            • <code style="color: #e06c75;" dir="ltr">break</code>: تنهي وتخرج من الـ Loop بالكامل فور تحقق الشرط.<br>
            • <code style="color: #e5c07b;" dir="ltr">continue</code>: بتتخطى التكرار الحالي (الدورة دي بس) وتنتقل للدورة اللي بعدها.
            </p>
        </div>
        """, unsafe_allow_html=True)

    st.code("""# مثال باستخدام break عند الوصول للقيمة 5
count = 1
while count <= 10:
    if count == 5:
        break
    print(count)
    count += 1
# الناتج: 1, 2, 3, 4 (وخرجت فوراً)

# مثال باستخدام continue لتخطى القيمة 3
c = 0
while c < 5:
    c += 1
    if c == 3:
        continue
    print(c)
# الناتج: 1, 2, 4, 5 (تم تخطي 3)""", language="python")

    # while ... else
    st.markdown("""
        <div dir="rtl" style="direction: rtl; text-align: right; padding: 18px; border: 1px solid rgba(255,255,255,0.1); border-radius: 12px; margin-bottom: 15px; background-color: rgba(255,255,255,0.02);">
            <h4 style="font-size: 17px; font-weight: 700; color: #c678dd; margin-bottom: 10px;">🔄 ميزة while ... else</h4>
            <p style="font-size: 13.5px; opacity: 0.85; line-height: 1.6; margin: 0;">
            جملة الـ <code style="color: #e5c07b;" dir="ltr">else</code> مع الـ while بتتنفذ لما اللوب تخلص بشكل طبيعي تماماً، لكن لو خرجنا منها باستخدام <code style="color: #e06c75;" dir="ltr">break</code> فالـ else مش هتتنفذ.
            </p>
        </div>
        """, unsafe_allow_html=True)

    # مثال شامل وتطبيق في Data Analysis
    st.markdown("""
        <div dir="rtl" style="direction: rtl; text-align: right; padding: 18px; border: 1px solid rgba(97, 175, 239, 0.3); border-radius: 12px; background-color: rgba(97, 175, 239, 0.04); margin-bottom: 15px;">
            <h4 style="font-size: 16px; font-weight: 700; color: #61afef; margin-bottom: 8px;">💼 مثال يجمع كل الأفكار (البحث في بيانات الدرجات)</h4>
            <p style="font-size: 13.5px; opacity: 0.9; line-height: 1.6; margin-bottom: 10px;">
            تخيل إنك بتدور على أول درجة أقل من 50 في القائمة لتوقيف البحث:
            </p>
        </div>
        """, unsafe_allow_html=True)

    st.code("""scores = [80, 75, 90, 45, 88]
index = 0

while index < len(scores):
    if scores[index] < 50:
        print("Found a failed score:", scores[index])
        break
    index += 1
# النتيجة: هتقف عند 45 وتطبع الرسالة""", language="python")

    # رأي من كواليس تحليل البيانات
    st.markdown("""
        <div dir="rtl" style="direction: rtl; text-align: right; padding: 18px; border: 1px solid rgba(229, 192, 123, 0.3); border-radius: 12px; background-color: rgba(229, 192, 123, 0.04);">
            <h4 style="font-size: 16px; font-weight: 700; color: #e5c07b; margin-bottom: 8px;">💡 رأي من كواليس Data Analysis</h4>
            <p style="font-size: 13.5px; opacity: 0.9; line-height: 1.6; margin: 0;">
            هل هستخدم <code style="color: #e5c07b;" dir="ltr">while</code> كتير في تحليل البيانات؟ الصراحة، مش بنفس أهمية الـ <code style="color: #e5c07b;" dir="ltr">for</code> ومكتبة <code style="color: #98c379;" dir="ltr">Pandas</code>. بس فهمها ضروري جداً علشان تستوعب <strong>طريقة التفكير البرمجي الأساسية، والـ Loops، والتحكم بالشروط (break/continue)</strong> قبل ما تدخل في الأدوات المتقدمة.
            </p>
        </div>
        """, unsafe_allow_html=True)

def render_python_lesson_9():
    # الهيدر الرئيسي للمحطة
    st.markdown("""
        <div dir="rtl" style="direction: rtl; text-align: right;">
            <h2 style="font-weight: 800; font-size: 22px; color: #fff; margin-bottom: 8px;">🔁 المحطة 9: For Loop — خلّي Python تعدّي على البيانات بدل ما تكرر الكود بنفسك</h2>
            <p style="opacity: 0.85; font-size: 14.5px; line-height: 1.7; margin-bottom: 20px;">
            لما يكون عندك 10,000 عنصر، مش هينفع تكتب <code style="color: #61afef;" dir="ltr">print()</code> لكل واحد! هنا بتجي الـ <strong>For Loop</strong> عشان تقول لبايثون: <em>"خدي كل عنصر من المجموعة، واعملي عليه نفس العملية."</em>
            </p>
        </div>
        """, unsafe_allow_html=True)

    # أساسيات الـ For Loop
    st.markdown("""
        <div dir="rtl" style="direction: rtl; text-align: right; padding: 18px; border: 1px solid rgba(255,255,255,0.1); border-radius: 12px; margin-bottom: 15px; background-color: rgba(255,255,255,0.02);">
            <h4 style="font-size: 17px; font-weight: 700; color: #98c379; margin-bottom: 10px;">🧠 يعني إيه For Loop؟</h4>
            <p style="font-size: 13.5px; opacity: 0.85; line-height: 1.6;">
            <code style="color: #e5c07b;" dir="ltr">for name in names:</code> معناها: لكل عنصر موجود في القائمة، حطّه مؤقتًا في متغير <code style="color: #61afef;" dir="ltr">name</code> ونفذ الكود تحته.
            </p>
        </div>
        """, unsafe_allow_html=True)

    st.code("""names = ["Ahmed", "Sara", "Omar", "Mona"]

for name in names:
    print(name)

# الناتج: Ahmed, Sara, Omar, Mona""", language="python")

    # Break & Continue
    st.markdown("""
        <div dir="rtl" style="direction: rtl; text-align: right; padding: 18px; border: 1px solid rgba(255,255,255,0.1); border-radius: 12px; margin-bottom: 15px; background-color: rgba(255,255,255,0.02);">
            <h4 style="font-size: 17px; font-weight: 700; color: #61afef; margin-bottom: 10px;">🛑 التحكم في اللوب: break مقابل continue</h4>
            <p style="font-size: 13.5px; opacity: 0.85; line-height: 1.6; margin-bottom: 10px;">
            • <code style="color: #e06c75;" dir="ltr">break</code>: توقف وتخرج فورًا من الـ Loop.<br>
            • <code style="color: #e5c07b;" dir="ltr">continue</code>: تتخطى العنصر الحالي وتكمل باقي العناصر.
            </p>
        </div>
        """, unsafe_allow_html=True)

    st.code("""# تطبيق عملي في تصفية الدرجات (استبعاد أقل من 50)
scores = [85, 90, 45, 78, 30, 95]

for score in scores:
    if score < 50:
        continue
    print(score)
# الناتج: 85, 90, 78, 95""", language="python")

    # For Loop مع Dictionary
    st.markdown("""
        <div dir="rtl" style="direction: rtl; text-align: right; padding: 18px; border: 1px solid rgba(255,255,255,0.1); border-radius: 12px; margin-bottom: 15px; background-color: rgba(255,255,255,0.02);">
            <h4 style="font-size: 17px; font-weight: 700; color: #c678dd; margin-bottom: 10px;">🗂️ For Loop مع Dictionary (الربط الأهم)</h4>
            <p style="font-size: 13.5px; opacity: 0.85; line-height: 1.6; margin-bottom: 10px;">
            الـ Dictionary لوحدها بترجع الـ <strong>Keys</strong>، لكن بنقدر نستخدم <code style="color: #e5c07b;" dir="ltr">.values()</code> أو <code style="color: #e5c07b;" dir="ltr">.items()</code> لاستخراج المفتاح والقيمة معًا:
            </p>
        </div>
        """, unsafe_allow_html=True)

    st.code("""student = {"name": "Omar", "age": 21, "grade": 90}

# استخراج الـ Keys والـ Values معًا باستخدام .items()
for key, value in student.items():
    print(key, value)""", language="python")

    # مثال عملي متقدم
    st.markdown("""
        <div dir="rtl" style="direction: rtl; text-align: right; padding: 18px; border: 1px solid rgba(97, 175, 239, 0.3); border-radius: 12px; background-color: rgba(97, 175, 239, 0.04); margin-bottom: 15px;">
            <h4 style="font-size: 16px; font-weight: 700; color: #61afef; margin-bottom: 8px;">💼 مثال عملي: تصفية المنتجات حسب السعر</h4>
            <p style="font-size: 13.5px; opacity: 0.9; line-height: 1.6; margin-bottom: 10px;">
            هنا جمعنا كذا مفهوم مع بعض (Dictionary + For Loop + items() + If Condition) بطريقة قريبة جدًا لشغل الـ Data Analysis:
            </p>
        </div>
        """, unsafe_allow_html=True)

    st.code("""products = {
    "Laptop": 25000,
    "Mouse": 500,
    "Keyboard": 1200
}

for product, price in products.items():
    if price > 1000:
        print(product, price)
# الناتج: Laptop 25000 و Keyboard 1200""", language="python")

    # تنبيه ذهني
    st.markdown("""
        <div dir="rtl" style="direction: rtl; text-align: right; padding: 15px; border: 1px solid rgba(229, 192, 123, 0.3); border-radius: 10px; background-color: rgba(229, 192, 123, 0.04);">
            <h4 style="font-size: 15px; font-weight: 700; color: #e5c07b; margin-bottom: 6px;">🧠 نقطة مهمة جداً في الفهم:</h4>
            <p style="font-size: 13.5px; opacity: 0.9; line-height: 1.6; margin: 0;">
            • متكتبش <code style="color: #e06c75;" dir="ltr">for key, value in product:</code> لأن الـ Dictionary وحدها بترجع المفاتيح بس، واستخدم دايمًا <code style="color: #e5c07b;" dir="ltr">.items()</code>.<br>
            • الـ For Loop مش مجرد "كرر عدد مرات"، هي <strong>مرور ذكي وتنقل بين عناصر البيانات</strong> (Iteration).
            </p>
        </div>
        """, unsafe_allow_html=True)

# =============================================================
# 🚧 دالة مؤقتة للمحطات الباقية
# =============================================================
def render_placeholder_lesson(lesson_num, lesson_name):
    st.markdown(f"""
        <div dir="rtl" style="direction: rtl; text-align: right; padding: 40px 20px; text-align: center;">
            <h3 style="color: #e5c07b; margin-bottom: 10px;">🚧 المحطة {lesson_num}: {lesson_name}</h3>
            <p style="opacity: 0.8; font-size: 14px;">هذه المحطة قيد التحضير والتنسيق ضمن الـ 25 محطة القادمة.. انتظروا المحتوى الاحترافي قريباً جداً! ✨</p>
        </div>
        """, unsafe_allow_html=True)
