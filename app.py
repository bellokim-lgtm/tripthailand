import streamlit as st
from datetime import date

# הגדרות עמוד
st.set_page_config(page_title="המדריך המלא - 2026", layout="centered")

# עיצוב קופסאות הלו"ז והמפה הכללית (CSS)
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
    .map-box {
        background-color: #e6f2f2;
        padding: 20px;
        border-radius: 12px;
        border: 2px dashed #008080;
        margin-bottom: 30px;
        direction: rtl;
        text-align: right;
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

# כותרת ראשית חדשה עם תאריכי הטיול
st.title("פוקט וקאו לאק | 20/05–30/05")

# קופסת מפה כללית עם כותרת מעודכנת
st.markdown("""
    <div class="map-box">
        <h3>🗺️ מפת המסלול המלאה שלכם</h3>
        <p>לנוחיותכם, ריכזנו את כל הנקודות, המלונות והאטרקציות של הטיול על גבי מפה אחת משותפת בגוגל מאפס.</p>
    </div>
""", unsafe_allow_html=True)
st.link_button("🌐 לחצו כאן לצפייה במפת הטיול המלאה", "https://www.google.com/maps/@8.3930358,99.4133095,9z/data=!4m6!1m2!10m1!1e1!11m2!2s8ZZz-WLQADbBj2BVs94Z9UkoKTzh0w!3e8?entry=ttu&g_ep=EgoyMDI2MDUxMy4wIKXMDSoASAFQAw%3D%3D", type="primary")
st.markdown("---")

# הגדרת תאריכים קבועים
start_date = date(2026, 5, 20)
end_start_date = date(2026, 5, 29)
end_date = date(2026, 5, 30)

# נתוני המסלול
itinerary = [
    {
        "stage": "תחנה 1: נחיתה והתאוששות",
        "title": "חוף נייטון השקט והפסטורלי",
        "date_display": f"📅 תאריך: {start_date.strftime('%d/%m/%Y')}",
        "description": "מלון מעולה שנמצא דקות ספורות משדה התעופה של פוקט. בחירה מושלמת ללילה הראשון כדי לנחות, לקבל צ'ק-אין מהיר, לנוח מהטיסה הארוכה וליהנות מחוף נייטון (Naithon Beach) השקט והנקי.",
        "target_name": "Wyndham Garden Naithon Phuket",
        "map_url": "https://www.google.com/maps/search/?api=1&query=Wyndham+Garden+Naithon+Phuket",
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
        "map_url": "https://www.google.com/maps/search/?api=1&query=JW+Marriott+Khao+Lak+Resort+Spa",
        "activities": [
            "פינוק מוחלט במתחם הספא והבריכות מהארוכות באסיה.",
            "מנוחה ובטן-גב על קו החוף השליו של קאו לאק."
        ]
    },
    {
        "stage": "תחנה 3: לב הטבע והג'ונגל",
        "title": "שמורת הטבע הלאומית קאו סוק",
        "date_display": "📅 מהלך הטיול: 21/05 עד 28/05",
        "description": "אחד מאתרי הטבע היפים ביותר בתאילנד. יער גשם עתיק, צוקי גיר עצומים המתנשאים מעל המים, ומגוון בעלי חיים. גולת הכותרת היא אגם צ'אורלאן שבו מומלץ לקחת שייט בסירה ארוכת זנב.",
        "target_name": "Khao Sok National Park",
        "map_url": "https://www.google.com/maps/search/?api=1&query=Khao+Sok+National+Park",
        "activities": [
            "שייט בין צוקי הגיר המפורסמים באגם צ'אורלאן.",
            "טיול רגלי בג'ונגל וביקור במערות נטיפים נסתרות."
        ]
    },
    {
        "stage": "תחנה 4: קאו לאק - אופציה ללינה חלופית 1",
        "title": "ריזורט קאו לאק מרלין",
        "date_display": "📅 מהלך הטיול: 21/05 עד 28/05",
        "description": "ריזורט מדהים המעוצב ממש כמו ג'ונגל טרופי עשיר עם חיות בר, צמחייה עבותה ומפלים פנימיים, ומציע שילוב מושלם בין נוחות ממודרנית לטבע פראי על שפת הים.",
        "target_name": "Khaolak Merlin Resort",
        "map_url": "https://www.google.com/maps/search/?api=1&query=Khaolak+Merlin+Resort",
        "activities": [
            "סיור בשבילי הטבע המרהיבים בתוך המלון.",
            "שחייה בבריכות השונות המוקפות בצמחייה טרופית."
        ]
    },
    {
        "stage": "תחנה 4: קאו לאק - אופציה ללינה חלופית 2",
        "title": "מלון דה ליטל שור",
        "date_display": "📅 מהלך הטיול: 21/05 עד 28/05",
        "description": "מלון בוטיק יוקרתי, חדיש וממודרני המציע חווית אירוח אינטימית, שירות מוקפד ואישי, ועיצוב אדריכלי נקי ומרגיע מול רצועת החוף.",
        "target_name": "The Little Shore Khao Lak by Katathani",
        "map_url": "https://www.google.com/maps/search/?api=1&query=The+Little+Shore+Khao+Lak+by+Katathani",
        "activities": [
            "ליהנות מהשקט והפרטיות של מלון הבוטיק החדיש.",
            "ארוחת ערב יוקרתית מול הנוף הפתוח של הים."
        ]
    },
    {
        "stage": "תחנה 4: קאו לאק - אופציה ללינה חלופית 3",
        "title": "ריזורט מורסאה קאו לאק",
        "date_display": "📅 מהלך הטיול: 21/05 עד 28/05",
        "description": "מלון יפהפה הבנוי על צלע גבעה ירוקה הגולשת ישירות אל תוך חוף הים, ומציע בקתות עץ וחדרים באווירה תאילנדית קלאסית ואותנטית.",
        "target_name": "Moracea by Khao Lak Resort",
        "map_url": "https://www.google.com/maps/search/?api=1&query=Moracea+by+Khao+Lak+Resort",
        "activities": [
            "תצפית שקיעה מרהיבה מאזור המסעדה שעל צלע ההר.",
            "הליכה רגועה ישירות מהחדר אל רצועת החוף הפרטית."
        ]
    },
    {
        "stage": "תחנה 4: אופציה לטיול יום - בריכת האזמרגד",
        "title": "בריכת האזמרגד (Emerald Pool / Sa Morakot)",
        "date_display": "📅 מהלך הטיול: 21/05 עד 28/05",
        "description": "בריכה טבעית מדהימה ביופייה הנובעת בלב שמורת טבע מוגנת ביער הגשם. המים הבהירים והצלולים מקבלים גוון ירוק-טורקיז (אזמרגד) מהפנט בגלל השתקפות המינרלים והטבע מסביב. מקום מושלם לחובבי טבע ושחייה מרעננת.",
        "target_name": "Emerald Pool (Sa Morakot)",
        "map_url": "https://www.google.com/maps/search/?api=1&query=Emerald+Pool+Sa+Morakot+Thailand",
        "activities": [
            "הליכה במסלול מסודר ופסטורלי בתוך יער הגשם המוביל אל הבריכה.",
            "שחייה מרעננת במים הצלולים והחמימים של בריכת הטורקיז הטבעית."
        ]
    },
    {
        "stage": "תחנה 4: אטרקציית טבע בקאו לאק",
        "title": "מפלי המים של קאו לאק",
        "date_display": "📅 מהלך הטיול: 21/05 עד 28/05",
        "description": "ביקור במפלי המים המפורסמים והמרעננים של החבל. מפל סאי רונג (Sai Rung) הוא מפל נגיש ויפהפה שנופל לבריכה טבעית, ומפל טון צ'ונג פה (Ton Chong Fa) מציע חמישה מפלסים מדהימים בלב היער.",
        "target_name": "Ton Chong Fa & Sai Rung Waterfalls",
        "map_url": "https://www.google.com/maps/search/?api=1&query=Ton+Chong+Fa+Waterfall",
        "activities": [
            "רחצה מרעננת בבריכת המים הטבעית למרגלות מפל סאי רונג.",
            "טיול הליכה קל בג'ונגל בין המפלסים של מפל טון צ'ונג פה."
        ]
    },
    {
        "stage": "תחנה 4: שייט במפרץ האיים",
        "title": "מפרץ פאנג נגה ואיי קוטה",
        "date_display": "📅 מהלך הטיול: 21/05 עד 28/05",
        "description": "המפרץ המפורסם השוכן בין פוקט לקראבי, מלא במאות איי גיר קטנים היוצאים מתוך המים. ברשימה שלך מופיע האי קו לאו בילה, המוכר כחלק מאי קו הונג (Ko Hong) - אי חלומי עם לגונה פנימית מדהימה.",
        "target_name": "Ko Lao Bile",
        "map_url": "https://www.google.com/maps/search/?api=1&query=Ko+Lao+Bile",
        "activities":
