import streamlit as st
from datetime import date, timedelta

# הגדרות עמוד
st.set_page_config(page_title="המדריך המלא - 2026", layout="centered")

# עיצוב קופסאות הלו"ז (CSS)
st.markdown("""
    <style>
    h1, h3, h2 { text-align: right; direction: rtl; font-family: 'Assistant', sans-serif; }
    p, li { text-align: right; direction: rtl; font-size: 16px; line-height: 1.6; }
    .itinerary-card {
        background-color: #f9f9f9;
        padding: 20px;
        border-radius: 12px;
        border-right: 6px solid #008080;
        margin-bottom: 25px;
        direction: rtl;
        text-align: right;
        box-shadow: 0 2px 5px rgba(0,0,0,0.05);
    }
    .stage-tag {
        color: #008080;
        font-weight: bold;
        font-size: 14px;
        display: block;
        margin-bottom: 5px;
    }
    .date-badge {
        background-color: #008080;
        color: white;
        padding: 3px 10px;
        border-radius: 20px;
        font-size: 14px;
        font-weight: bold;
        display: inline-block;
        margin-bottom: 10px;
        direction: rtl;
    }
    </style>
""", unsafe_allow_html=True)

# כותרת ראשית
st.title("פוקט וקאו לאק")

# הגרת תאריכים קבועים
start_date = date(2026, 5, 20)
end_start_date = date(2026, 5, 29)
end_date = date(2026, 5, 31)

# נתוני המסלול המעודכנים - JW Marriott עבר לתחנה 2
itinerary = [
    {
        "stage": "תחנה 1: נחיתה והתאוששות",
        "title": "חוף נייטון השקט והפסטורלי",
        "date_display": f"📅 תאריך: {start_date.strftime('%d/%m/%Y')}",
        "description": "מלון מעולה שנמצא דקות ספורות משדה התעופה של פוקט. בחירה מושלמת ללילה הראשון כדי לנחות, לקבל צ'ק-אין מהיר, לנוח מהטיסה הארוכה וליהנות מחוף נייטון (Naithon Beach) השקט והנקי.",
        "target_name": "Wyndham Garden Naithon Phuket",
        "map_url": "https://maps.app.goo.gl/rfE7SNGKhybjRCzq5",
        "activities": [
            "הגעה מהירה מהשדה ומנוחה בריזורט החדש.",
            "הליכה קצרה לשקיעה בחוף נייטון הפסטורלי."
        ]
    },
    {
        "stage": "תחנה 2: קאו לאק - לינה מרכזית",
        "title": "ריזורט ג'יי דבליו מריוט קאו לאק",
        "date_display": "📅 מהלך הטיול: 21/05 עד 28/05",
        "description": "ריזורט מפואר ברמה גבוהה מאוד המפורסם בזכות בריכת הלגונה הענקית שלו שנמתחת לאורך כל המלון, חדרים עם גישה ישירה למים וחוף חול לבן פרטי ושקט.",
        "target_name": "JW Marriott Khao Lak Resort & Spa",
        "map_url": "https://maps.app.goo.gl/tBoZytwm1nnnQoxD8",
        "activities": [
            "פינוק מוחלט במתחם הספא והבריכות מהארוכות באסיה.",
            "מנוחה ובטן-גב על קו החוף השליו של קאו לאק."
        ]
    },
    {
        "stage": "תחנה 3: לב הטבע והג'ונגל",
        "title": "שמורת הטבע הלאומית קאו סוק (Khao Sok)",
        "date_display": "📅 מהלך הטיול: 21/05 עד 28/05",
        "description": "אחד מאתרי הטבע היפים ביותר בתאילנד. יער גשם עתיק, צוקי גיר עצומים המתנשאים מעל המים, ומגוון בעלי חיים. גולת הכותרת היא אגם צ'אורלאן שבו מומלץ לקחת שייט בסירה ארוכת זנב.",
        "target_name": "Khao Sok National Park",
        "map_url": "https://maps.app.goo.gl/KCwV8EVLu76GfWP6A",
        "activities": [
            "שייט בין צוקי הגיר המפורסמים באגם צ'אורלאן.",
            "טיול רגלי בג'ונגל וביקור במערות נטיפים נסתרות."
        ]
    },
    {
        "stage": "תחנה 4: קאו לאק - אופציה ללינה חלופית 1",
        "title": "ריזורט קאו לאק מרלין",
        "date_display": "📅 מהלך הטיול: 21/05 עד 28/05",
        "description": "ריזורט מדהים המעוצב ממש כמו ג'ונגל טרופי עשיר עם חיות בר, צמחייה עבותה ומפלים פנימיים, ומציע שילוב מושלם בין נוחות מודרנית לטבע פראי על שפת הים.",
        "target_name": "Khaolak Merlin Resort",
        "map_url": "https://maps.app.goo.gl/ffQjwsQhaZ4S7Be26",
        "activities": [
            "סיור בשבילי הטבע המרהיבים בתוך המלון.",
            "שחייה בבריכות השונות המוקפות בצמחייה טרופית."
        ]
    },
    {
        "stage": "תחנה 4: קאו לאק -
