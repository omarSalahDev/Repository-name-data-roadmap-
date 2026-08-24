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
    # 📚 جدول المحطات والدرس (هنا تقدر تضيف أو تعدل بسهولة أي وقت)
    # -------------------------------------------------------------
    lessons_registry = {
        "المحطة 1: قبل ما نبدأ + أول برنامج print()": render_python_lesson_1,
        "المحطة 2: المتغيرات وأنواع البيانات (Variables & Types)": lambda: render_placeholder_lesson(2, "المتغيرات وأنواع البيانات"),
        "المحطة 3: العمليات الحسابية والمنطقية": lambda: render_placeholder_lesson(3, "العمليات الحسابية والمنطقية"),
        "المحطة 4: الشروط والتحكم (If Statements)": lambda: render_placeholder_lesson(4, "الشروط والتحكم"),
        "المحطة 5: الحلقات التكرارية (Loops: For & While)": lambda: render_placeholder_lesson(5, "الحلقات التكرارية"),
        # يمكنك إضافة باقي الـ 25 محطة هنا بنفس الطريقة بسهولة تامة مستقبلاً!
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
# 🚀 تفاصيل المحطة الأولى (المنشور الأول بالكامل ومظبوط RTL)
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
# 🚧 دالة مؤقتة للمحطات القادمة (حتى يتم ملؤها تباعاً)
# =============================================================
def render_placeholder_lesson(lesson_num, lesson_name):
    st.markdown(f"""
        <div dir="rtl" style="direction: rtl; text-align: right; padding: 40px 20px; text-align: center;">
            <h3 style="color: #e5c07b; margin-bottom: 10px;">🚧 المحطة {lesson_num}: {lesson_name}</h3>
            <p style="opacity: 0.8; font-size: 14px;">هذه المحطة قيد التحضير والتنسيق ضمن الـ 25 محطة القادمة.. انتظروا المحتوى الاحترافي قريباً جداً! ✨</p>
        </div>
        """, unsafe_allow_html=True)
