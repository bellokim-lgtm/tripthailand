import streamlit as st
import pandas as pd
from datetime import date
import random

# הגדרות עמוד
st.set_page_config(page_title="תאילנד המדריך המלא - 2026", layout="centered")

# עיצוב CSS מותאם ל-RTL
st.markdown("""
    <style>
    .stButton button { width: 100%; border-radius: 12px; height: 3.5em; background-color: #008080; color: white; }
    h1, h3, h2 { text-align: right; direction: rtl; font-family: 'Assistant', sans-serif; }
    p, li { text-align: right; direction: rtl; font-size: 16px; }
    .countdown-container {
        background: linear-gradient(135deg, #fdfcfb 0%, #e2d1c3 100%);
        padding: 25px;
        border-radius: 20px;
        text-align: center;
        margin-bottom: 25px;
        direction: rtl;
        border: 2px dashed #008080;
    }
    .section-header {
        background-color: #008080;
        color: white;
        padding: 10px;
        border-radius: 8px;
        text-align: right;
        direction: rtl;
        margin-top: 15px;
        margin-bottom: 15px;
    }
    .itinerary-card {
        background-color: #f9f9f9;
        padding: 15px;
        border-radius: 10px;
        border-right: 5px solid #008080;
        margin-bottom: 15px;
        direction: rtl;
        text-align: right;
    }
    </style>
""", unsafe_allow_html=True)

# כותרת ראשית של האפליקציה
st.title("🇹🇭 לו\"ז הטיול המדויק שלך לתאילנד")

# רשימת המיקומים והאטרקציות המדויקת מצילומי המסך שלך
itinerary = [
    {
        "stage": "שלב 1: הגעה ונחיתה רכה",
        "title": "צפון פוקט (Naithon Beach)",
        "accommodation": "Wyndham Garden Naithon Phuket (לילה ראשון)",
        "activities": [
            "נחיתה בפוקט והגעה מהירה למלון בצפון האי.",
            "מנוחה, התאוששות מהטיסה ובילוי רגוע בחוף נייטון השקט."
        ]
    },
    {
        "stage": "שלב 2: שייט במפרץ",
        "title": "מפרץ פאנג נגה ואיי קראבי",
        "accommodation": "יציאה מאזור פוקט / פאנג נגה",
        "activities": [
            "טיול יום ושייט בסירה (Longtail Boat / Speedboat) במפרץ פאנג נגה המפורסם.",
            "ביקור וסיור באיים המרהיבים שסימנת: האי קו לאו בילה (Ko Lao Bile / אזור אי קו הונג) וסביבתו."
        ]
    },
    {
        "stage": "שלב 3: מעבר לחבל קאו לאק",
        "title": "טבע, מפלים וריזורטים בקאו לאק (Khao Lak)",
        "accommodation": "בחירה בין המלונות שסימנת: Khaolak Merlin Resort / JW Marriott Khao Lak / The Little Shore / Moracea by Khao Lak Resort",
        "activities": [
            "מעבר צפונה אל עבר חבל קאו לאק היפה והירוק.",
            "ביקור במפלי המים המרעננים ששמרת ברשימה: מפל סאי רונג (Sai Rung Waterfall) ומפל טון צ'ונג פה (Ton Chong Fa Waterfall).",
            "הנאה ופינוק בריזורטים המפוארים שעל רצועת החוף של קאו לאק."
        ]
    },
    {
        "stage": "שלב 4: לב הטבע הפראי",
        "title": "שמורת הטבע קאו סוק",
        "accommodation": "לינה בשמורה (בתי עץ או בקתות צפות על האגם)",
        "activities": [
            "טיול וסיור בשמורת הטבע הלאומית קאו סוק (Khao Sok National Park).",
            "שייט בסירה ארוכת זנב בין צוקי הגיר העצומים באגם צ'אורלאן (Cheow Lan Lake) וסיור בג'ונגל."
        ]
    },
    {
        "stage": "שלב 5: סיום מפנק בדרום האי",
        "title": "דרום פוקט (Kata Noi Beach)",
        "accommodation": "Katathani Phuket Beach Resort (2 לילות אחרונים)",
        "activities": [
            "חזרה לפוקט ישירות לריזורט המפנק בדרום האי בחוף קאטה נוי.",
            "יומיים של בטן-גב, בריכות, שקיעות מרהיבות וסגירה מושלמת לטיול."
        ]
    }
]

# הרצת הלו"ז והצגתו באפליקציה באמצעות כרטיסיות מעוצבות
for item in itinerary:
    st.markdown(f"""
    <div class="itinerary-card">
        <span style="color: #008080; font-weight: bold; font-size: 14px;">{item['stage']}</span>
        <h3 style="margin-top: 5px; margin-bottom: 10px;">📍 {item['title']}</h3>
        <p>🏨 <b>מקום לינה / נקודות ציון:</b> {item['accommodation']}</p>
        <p>🗺️ <b>מה בתוכנית:</b></p>
        <ul style="list-style-type: circle; padding-right: 20px; margin-top: 5px;">
            {"".join([f"<li>{act}</li>" for act in item['activities']])}
        </ul>
    </div>
    """, unsafe_allow_html=True)
