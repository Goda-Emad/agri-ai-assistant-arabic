<div align="center">

# مساعد الزراعة الذكي (نسخة عربية)

### مساعد زراعي مدعوم بالذكاء الاصطناعي

[![Python](https://img.shields.io/badge/Python-3.11%2B-3776AB?style=flat-square&logo=python&logoColor=white)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-3.1-000000?style=flat-square&logo=flask&logoColor=white)](https://flask.palletsprojects.com)
[![Groq](https://img.shields.io/badge/Groq-LLM-F55036?style=flat-square&logo=fastapi&logoColor=white)](https://console.groq.com)
[![License](https://img.shields.io/badge/License-MIT-22c55e?style=flat-square)](LICENSE)

مساعد زراعي ذكي مدعوم بالذكاء الاصطناعي، يساعد المزارعين في نصائح المحاصيل، مكافحة الآفات، صحة التربة، الطقس، والاستشارات الزراعية العامة — عن طريق النص، الصوت، وتحليل الصور.

</div>

---

## المميزات

| الميزة | الوصف |
|---------|-------------|
| محادثة نصية | اسأل أي سؤال زراعي واحصل على إجابة خبيرة |
| تشخيص الصور | ارفع صورة للمحصول ← الذكاء الاصطناعي يحدد الأمراض والآفات ونقص العناصر الغذائية |
| إدخال صوتي | تكلم مباشرة عن طريق Groq Whisper |
| إخراج صوتي | البوت يقرأ الإجابة بصوت عالٍ باستخدام Groq Orpheus TTS |
| ذاكرة المحادثة | يتذكر سياق المحادثة (Redis، مع نسخة احتياطية في الذاكرة المؤقتة) |
| تخزين مؤقت للتكلفة | توفير يصل إلى 50% عن طريق تخزين مؤقت للأجزاء المتكررة من الطلبات |
| وضع ليلي/نهاري | واجهة Glassmorphism مع تبديل بضغطة واحدة |
| متعدد اللغات | يرد بأكثر من لغة |

---

## التقنيات المستخدمة

| القسم | التقنية |
|---------|-------------|
| **الخلفية (Backend)** | Python 3.11+, Flask, Groq SDK |
| **الواجهة (Frontend)** | HTML5, CSS3 (Glassmorphism), jQuery |
| **نماذج اللغة** | `openai/gpt-oss-120b` (نصوص), `meta-llama/llama-4-scout-17b-16e-instruct` (صور) |
| **الصوت** | Groq Whisper `whisper-large-v3-turbo` (تحويل الصوت لنص), Groq Orpheus (تحويل النص لصوت) |
| **الذاكرة** | Redis (مع نسخة احتياطية تلقائية في الذاكرة) |
| **النشر** | Render, Docker, Gunicorn |

---

## البدء السريع

### المتطلبات الأساسية

- **Python 3.11+**
- **[مفتاح Groq API](https://console.groq.com/keys)** (متاح مجانًا)

### 1. تحميل المشروع وتثبيت المتطلبات

```bash
git clone https://github.com/Goda-Emad/agri-ai-assistant-arabic.git
cd agri-ai-assistant-arabic
pip install -r requirements.txt
```

### 2. الإعداد

```bash
copy .env.example .env
```

عدّل ملف `.env` وأضف مفتاح Groq API الخاص بك:

```env
GROQ_API_KEY=gsk_your_key_here
```

### 3. التشغيل

```bash
python run.py
```

افتح المتصفح على: **[http://127.0.0.1:5000](http://127.0.0.1:5000)**

---

## متغيرات البيئة (Environment Variables)

انسخ `.env.example` إلى `.env` واضبط القيم التالية:

| المتغير | مطلوب؟ | القيمة الافتراضية | الوصف |
|----------|:--------:|---------|-------------|
| `GROQ_API_KEY` | نعم | — | مفتاح Groq API الخاص بك ([احصل عليه هنا](https://console.groq.com/keys)) |
| `LLM_MODEL` | لا | `openai/gpt-oss-120b` | نموذج اللغة النصي |
| `LLM_VISION_MODEL` | لا | `meta-llama/llama-4-scout-17b-16e-instruct` | نموذج تحليل الصور |
| `LLM_TEMPERATURE` | لا | `0.3` | درجة عشوائية النموذج (0–2) |
| `LLM_MAX_TOKENS` | لا | `2048` | الحد الأقصى لطول الإجابة |
| `STT_MODEL` | لا | `whisper-large-v3-turbo` | نموذج تحويل الصوت إلى نص |
| `TTS_MODEL` | لا | — | نموذج تحويل النص إلى صوت |
| `TTS_VOICE` | لا | `autumn` | اسم الصوت المستخدم |
| `REDIS_HOST` | لا | `localhost` | عنوان Redis (اختياري — يعمل بدونه في الذاكرة) |
| `REDIS_PORT` | لا | `6379` | منفذ Redis |
| `REDIS_SSL` | لا | `false` | تفعيل SSL لـ Redis |
| `FLASK_SECRET_KEY` | نعم* | `dev-secret-key` | مفتاح جلسة Flask (*مطلوب في بيئة الإنتاج) |
| `FLASK_DEBUG` | لا | `true` | تفعيل وضع التصحيح |

---

## هيكل المشروع

```
agri-ai-assistant-arabic/
├── app/
│   ├── __init__.py             # App factory (create_app)
│   ├── config.py               # إعدادات مبنية على متغيرات البيئة
│   ├── routes/
│   │   ├── main.py             # الصفحة الرئيسية، robots.txt، sitemap
│   │   └── chat.py             # واجهة API للمحادثة (نص، صوت، صورة)
│   ├── services/
│   │   ├── llm_service.py      # نموذج اللغة + تحليل الصور + التخزين المؤقت
│   │   ├── memory_service.py   # Redis مع نسخة احتياطية في الذاكرة
│   │   ├── stt_service.py      # تحويل الصوت إلى نص
│   │   ├── tts_service.py      # تحويل النص إلى صوت
│   │   └── prompt_manager.py   # إدارة الـ system prompt
│   ├── static/
│   │   ├── css/style.css       # تصميم الواجهة (ليلي/نهاري)
│   │   ├── js/chat.js          # منطق المحادثة، رفع الصور، الصوت
│   │   └── images/             # الأيقونة
│   └── templates/
│       └── index.html          # القالب الرئيسي (SEO + JSON-LD)
├── Sample_image/                # صور توضيحية للـ README
├── llms.txt                     # إفصاح للزواحف الذكية
├── .env.example                 # نموذج متغيرات البيئة
├── gunicorn.conf.py             # إعدادات النشر
├── Dockerfile                   # ملف Docker
├── render.yaml                  # إعدادات النشر على Render
├── run.py                       # نقطة التشغيل الأساسية
├── pyproject.toml               # إعدادات المشروع
└── requirements.txt             # قائمة المكتبات المطلوبة
```

---

## النشر (Deployment)

### Render (الطريقة الموصى بها)

1. ارفع الكود على GitHub
2. اذهب إلى [render.com](https://render.com) ← **New** ← **Web Service**
3. اربط حساب GitHub الخاص بك بالريبو
4. Render هيكتشف تلقائيًا ملفات `render.yaml` و`Dockerfile`
5. أضف `GROQ_API_KEY` (والمتغيرات الأخرى) في لوحة تحكم Render
6. اضغط **Deploy**

### Docker

```bash
docker build -t agri-ai-assistant .
docker run -p 10000:10000 --env-file .env agri-ai-assistant
```

---

## مرجع الـ API

| الطريقة | المسار | الوصف |
|--------|----------|-------------|
| `GET` | `/` | واجهة المحادثة |
| `POST` | `/chat` | إرسال نص أو صورة أو صوت — يرجع إجابة الذكاء الاصطناعي |
| `POST` | `/chat/clear` | مسح سجل المحادثة |
| `GET` | `/health` | فحص حالة الخدمة (حالة Redis) |
| `GET` | `/robots.txt` | قواعد فهرسة محركات البحث |
| `GET` | `/sitemap.xml` | خريطة الموقع |
| `GET` | `/llms.txt` | إفصاح للزواحف الذكية |
| `GET` | `/.well-known/llms.txt` | إفصاح للزواحف الذكية (مسار بديل) |

---

## آلية العمل

```
المستخدم يرسل رسالة (نص / صورة / صوت)
        │
        ▼
┌─────────────────────────────────────────┐
│  خادم Flask                             │
│  ├── نص؟ ← نموذج اللغة (gpt-oss-120b)  │
│  ├── صورة؟ ← Llama 4 Scout (تحليل صور) │
│  └── صوت؟ ← تحويل لنص ← الرد ← تحويل لصوت │
│                                         │
│  الذاكرة: Redis (أو الذاكرة المؤقتة)     │
│  التخزين المؤقت: توفير تلقائي للتكلفة    │
└─────────────────────────────────────────┘
        │
        ▼
الرد بالنص + صوت اختياري
```

---

## الترخيص

مرخّص بموجب MIT License — راجع ملف [LICENSE](LICENSE)

---

<div align="center">

**تم التطوير بواسطة**

[Goda Emad](https://github.com/Goda-Emad) · [GitHub](https://github.com/Goda-Emad) · [LinkedIn](https://www.linkedin.com/in/goda-emad/)

</div>
