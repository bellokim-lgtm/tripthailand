import streamlit as st
import pandas as pd
from datetime import date
import random

# הגדרות עמוד
st.set_page_config(page_title="תאילנד המדריך המלא - 2026", layout="centered")

# עיצוב CSS מותאם ל-RTL עם כפתורים וקישורים ברורים
st.markdown("""
    <style>
    .stButton button { width: 100%; border-radius: 12px; height: 3.5em; background-color: #008080; color: white; }
    h1, h3, h2 { text-align: right; direction: rtl; font-family: 'Assistant', sans-serif; }
    p, li { text-align: right; direction: rtl; font-size: 16px; }
    .itinerary-card {
        background-color: #f9f9f9;
        padding: 20px;
        border-radius: 10px;
        border-right: 6px solid #008080;
        margin-bottom: 20px;
        direction: rtl;
        text-align: right;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }
    .map-link {
        display: inline-block;
        background-color: #e6f2f2;
        color: #008080;
        padding: 5px 12px;
        border-radius: 6px;
        text-decoration: none;
        font-weight: bold;
        margin-top: 5px;
        margin-bottom: 10px;
    }
    .map-link:hover {
        background-color: #008080;
        color: white;
    }
    </style>
""", unsafe_allow_html=True)

# כותרת ראשית של האפליקציה
st.title("🇹🇭 מסלול הטיול המדויק שלך - פוקט והסביבה")
st.write("לחצי על הקישורים בכל שלב כדי לפתוח את המיקום המדויק בגוגל מאפס.")

# רשימת המיקומים, האטרקציות, הקישורים וההסברים המלאים מהמפה שלך
itinerary = [
    {
        "stage": "תחנה 1: נחיתה והתאוששות (צפון פוקט)",
        "title": "חוף נייטון השקט והפסטורלי",
        "hotel": "Wyndham Garden Naithon Phuket (לילה ראשון)",
        "hotel_link": "https://www.google.com/maps/search/?api=1&query=Wyndham+Garden+Naithon+Phuket",
        "description": "מלון מעולה שנמצא דקות ספורות משדה התעופה של פוקט. בחירה מושלמת ללילה הראשון כדי לנחות, לקבל צ'ק-אין מהיר, לנוח מהטיסה הארוכה וליהנות מחוף נייטון (Naithon Beach) שנחשב לאחד החופים השקטים, הנקיים והפחות עמוסים באי.",
        "activities": [
            "הגעה מהירה מהשדה ומנוחה בריזורט החדש.",
            "הליכה קצרה לשקיעה בחוף נייטון הנסתר והיפה."
        ],
        "attraction": "",
        "attraction_link": ""
    },
    {
        "stage": "תחנה 2: לב הטבע והג'ונגל (הכי בצפון המסלול)",
        "title": "שמורת הטבע הלאומית קאו סוק (Khao Sok)",
        "hotel": "לינה בבקתות ג'ונגל או בריזורט צף על האגם",
        "hotel_link": "https://www.google.com/maps/search/?api=1&query=Khao+Sok+National+Park",
        "description": "אחד מאתרי הטבע היפים ביותר בתאילנד. שמורת טבע פראית עם יער גשם עתיק, צוקי גיר עצומים המתנשאים מעל המים, ומגוון עצום של בעלי חיים. גולת הכותרת היא אגם צ'אורלאן (Cheow Lan Lake) שבו מומלץ לקחת שייט בסירה ארוכת זנב מסורתית.",
        "activities": [
            "שייט בין צוקי הגיר המפורסמים באגם צ'אורלאן הנוצר מסכר רג'אפרבה.",
            "טיול רגלי בג'ונגל, ביקור במערות נטיפים נסתרות ותצפיות נוף מדהימות."
        ],
        "attraction": "שמורת קאו סוק במפה",
        "attraction_link": "https://www.google.com/maps/search/?api=1&query=Khao+Sok+National+Park"
    },
    {
        "stage": "תחנה 3: חבל קאו לאק - חופים, מפלים וריזורטים",
        "title": "קאו לאק (Khao Lak) והמפלים בסביבה",
        "hotel": "ריזורטים לבחירה: JW Marriott / Khaolak Merlin / The Little Shore / Moracea",
        "hotel_link": "https://www.google.com/maps/search/?api=1&query=Khao+Lak+Resorts",
        "description": "אזור חוף רגוע ויוקרתי שנמצא צפונית לפוקט. קאו לאק מפורסמת ברצועות חוף אינסופיות, אווירה שלווה וקרבה לטבע ומפלי מים מהממים בתוך היער.",
        "activities": [
            "ביקור במפל סאי רונג (Sai Rung Waterfall) - מפל נגיש ויפהפה שנופל לבריכה טבעית לרחצה מרעננת.",
            "ביקור במפל טון צ'ונג פה (Ton Chong Fa Waterfall) - מפל בעל 5 מפלסים בתוך הג'ונגל, מעולה לחובבי הליכה בטבע.",
            "פינוק ובטן-גב באחד הריזורטים המטורפים ששמרת (כמו ה-JW Marriott המפורסם בזכות הבריכה הענקית שלו)."
        ],
        "attraction": "מפל סאי רונג במפה",
        "attraction_link": "https://www.google.com/maps/search/?api=1&query=Sai+Rung+Waterfall+Khao+Lak"
    },
    {
        "stage": "תחנה 4: שייט במפרץ האיים (מרכז)",
        "title": "מפרץ פאנג נגה ואיי קוטה / קו הונג",
        "accommodation": "יציאה לשייט יומי מודרך (Phuket / Phang Nga Pier)",
        "hotel_link": "",
        "description": "המפרץ המפורסם ששוכן בין פוקט לקראבי, מלא במאות איי גיר קטנים שיוצאים מתוך המים הירוקים. ברשימה שלך מופיע האי קו לאו בילה (Ko Lao Bile), המוכר יותר כחלק מאי קו הונג (Ko Hong) - אי חלום עם לגונה פנימית מדהימה שניתן להיכנס אליה רק בסירה, וחוף חול לבן מושלם לשנורקלינג.",
        "activities": [
            "שייט בסירה מהירה או סירת ארוכת-זנב בין איי המפרץ.",
            "חתירה בקיאקים בלגונה הנסתרת של קו הונג (Ko Lao Bile) ושחייה במים הצלולים."
        ],
        "attraction": "האי קו לאו בילה (Ko Lao Bile / Ko Hong) במפה",
        "attraction_link": "https://www.google.com/maps/search/?api=1&query=Ko+Lao+Bile+Ko+Hong"
    },
    {
        "stage": "תחנה 5: סיום יוקרתי ומפנק (דרום פוקט)",
        "title": "חוף קאטה נוי (Kata Noi)",
        "hotel": "Katathani Phuket Beach Resort (2 לילות אחרונים)",
        "hotel_link": "https://www.google.com/maps/search/?api=1&query=Katathani+Phuket+Beach+Resort",
        "description": "הקטאטאני הוא אחד הריזורטים המבוקשים והמפנקים ביותר בדרום פוקט. הוא יושב באופן כמעט בלעדי על רצועת החוף המדהימה של קאטה נוי (חוף עם חול רך ומים שקטים יחסית). המלון מציע המון בריכות, מסעדות מעולות, שירות ברמה הגבוהה ביותר ואווירת חופש מושלמת לסגור איתה את הטיול.",
        "activities": [
            "נופש בטן-גב מוחלט בבריכות הריזורט המתוחות לאורך קו החוף.",
            "ארוחת ערב חגיגית מול השקיעה באחת ממסעדות המלון או מסעדות דגים מקומיות באזור קאטה."
        ],
        "attraction": "",
        "attraction_link": ""
    }
]

# הרצת הלו"ז והצגתו באפליקציה באמצעות כרטיסיות מעוצבות
for item in itinerary:
    st.markdown(f"""
    <div class="itinerary-card">
        <span style="color: #008080; font-weight: bold; font-size: 14px;">{item['stage']}</span>
        <h3 style="margin-top: 5px; margin-bottom: 5px;">📍 {item['title']}</h3>
        <p style="margin-top: 5px; color: #555;">{item['description']}</p>
        
        <p style="margin-bottom: 5px;">🏨 <b>מלון/לינה:</b> {item['hotel']}</p>
        {f'<a href="{item["hotel_link"]}" target="_blank" class="map-link">📍 לחצי כאן למיקום המלון במפה</a>' if item['hotel_link'] else ''}
        
        {f'<p style="margin-top: 10px; margin-bottom: 5px;">🗺️ <b>אטרקציה מרכזית ששמרת:</b> {item["attraction"]}</p>' if item['attraction'] else ''}
        {f'<a href="{item["attraction_link"]}" target="_blank" class="map-link">🧭 לחצי כאן למיקום האטרקציה במפה</a>' if item['attraction_link'] else ''}
        
        <p style="margin-top: 10px; margin-bottom: 5px;">📝 <b>פעילויות מומלצות:</b></p>
        <ul style="list-style-type: circle; padding-right: 20px; margin-top: 5px;">
            {"".join([f"<li>{act}</li>" for act in item['activities']])}
        </ul>
    </div>
    """, unsafe_allow_html=True)
