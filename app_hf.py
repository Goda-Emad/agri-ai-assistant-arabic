import subprocess
import os
import streamlit as st

# 1. تشغيل سيرفر Flask الخاص بمشروعك كعملية خلفية (Background Process)
# المنصة في هجينج فيس تمرر المنفذ تلقائياً في متغير البيئة PORT، وإذا لم يوجد نستخدم 7860
port = os.environ.get("PORT", "7860")

st.write("جاري تشغيل مساعد الزراعة الذكي...")

# تشغيل ملف run.py الخاص بمشروعك وتوجيهه للمنفذ المطلوب
subprocess.Popen(["python", "run.py", "--host", "0.0.0.0", "--port", port])

# 2. عرض واجهة الـ Flask داخل صفحة الـ Streamlit باستخدام Iframe
st.components.v1.iframe(f"http://127.0.0.1:{port}", height=800, scrolling=True)
