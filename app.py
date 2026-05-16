import streamlit as st

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
    </style>
""", unsafe_allow_html=True)

# כותרת ראשית מעודכנת ומקוצרת
st.title("פוקט וקאו לאק")

# נתוני המסלול המדויקים
itinerary = [
    {
        "stage": "תחנה 1: נחיתה והתאוששות (צפון פוקט)",
        "title": "חוף נייטון השקט והפסטורלי",
        "description": "מלון מעולה שנמצא דקות ספורות משדה התעופה של פוקט. בחירה מושלמת ללילה הראשון כדי לנחות, לקבל צ'ק-אין מהיר, לנוח מהטיסה הארוכה וליהנות מחוף נייטון (Naithon Beach) השקט והנקי.",
        "target_name": "Wyndham Garden Naithon Phuket",
        "map_search_query": "Wyndham+Garden+Naithon+Phuket",
        "activities": [
            "הגעה מהירה מהשדה ומנוחה בריזורט החדש.",
            "הליכה קצרה לשקיעה בחוף נייטון הפסטורלי."
        ]
    },
    {
        "stage": "תחנה 2: לב הטבע והג'ונגל (הכי בצפון המסלול)",
        "title": "שמורת הטבע הלאומית קאו סוק (Khao Sok)",
        "description": "אחד מאתרי הטבע היפים ביותר בתאילנד. יער גשם עתיק, צוקי גיר עצומים המתנשאים מעל המים, ומגוון בעלי חיים. גולת הכותרת היא אגם צ'אורלאן שבו מומלץ לקחת שייט בסירה ארוכת זנב.",
        "target_name": "Khao Sok National Park",
        "map_search_query": "Khao+Sok+National+Park",
        "activities": [
            "שייט בין צוקי הגיר המפורסמים באגם צ'אורלאן.",
            "טיול רגלי בג'ונגל וביקור במערות נטיפים נסתרות."
        ]
    },
    {
        "stage": "תחנה 3: חבל קאו לאק - חופים, מפלים וריזורטים",
        "title": "קאו לאק (Khao Lak) והמפלים בסביבה",
        "description": "אזור חוף רגוע ויוקרתי שנמצא צפונית לפוקט. קאו לאק מפורסמת ברצועות חוף אינסופיות, אווירה שלווה, ומפלי מים מהממים בתוך היער כמו סאי רונג וטון צ'ונג פה.",
        "target_name": "קאו לאק (JW Marriott / Merlin / Little Shore / Moracea)",
        "map_search_query": "Khao+Lak",
        "activities": [
            "רחצה מרעננת במפל סאי רונג (Sai Rung Waterfall) הנגיש והיפה.",
            "טיול הליכה בטבע בין 5 המפלסים של מפל טון צ'ונג פה (Ton Chong Fa Waterfall).",
            "בטן-גב ופינוק בריזורטים המפוארים ששמרת על קו החוף."
        ]
    },
    {
        "stage": "תחנה 4: שייט במפרץ האיים (מרכז)",
        "title": "מפרץ פאנג נגה ואיי קוטה (Ko Lao Bile)",
        "description": "המפרץ המפורסם השוכן בין פוקט לקראבי, מלא במאות איי גיר קטנים היוצאים מתוך המים. ברשימה שלך מופיע האי קו לאו בילה, המוכר כחלק מאי קו הונג (Ko Hong) - אי חלומי עם לגונה פנימית מדהימה.",
        "target_name": "Ko Lao Bile (Ko Hong)",
        "map_search_query": "Ko+Lao+Bile",
        "activities": [
            "שייט בסירה מהירה או סירת לונגטייל בין איי המפרץ והאיים ששמרת.",
            "חתירה בקיאקים בלגונה הנסתרת של קו הונג ושחייה במים הצלולים."
        ]
    },
    {
        "stage": "תחנה 5: סיום יוקרתי ומפנק (דרום פוקט)",
        "title": "חוף קאטה נוי (Kata Noi Beach)",
        "description": "הקטאטאני הוא אחד הריזורטים המבוקשים והמפנקים ביותר בדרום פוקט. הוא יושב על רצועת החוף המדהימה של קאטה נוי (חוף עם חול רך ומים שקטים) ומציע חווית חופש מושלמת לסגור איתה את הטיול.",
        "target_name": "Katathani Phuket Beach Resort",
        "map_search_query": "Katathani+Phuket+Beach+Resort",
        "activities": [
            "נופש בטן-גב מוחלט בבריכות הריזורט המתוחות לאורך קו החוף.",
            "ארוחת ערב חגיגית מול השקיעה באחת ממסעדות הדגים המקומיות באזור קאטה."
        ]
    }
]

# הרצת הלו"ז והצגתו
for item in itinerary:
    st.markdown(f"""
    <div class="itinerary-card">
        <span class="stage-tag">{item['stage']}</span>
        <h3>📍 {item['title']}</h3>
        <p style="color: #444;">{item['description']}</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown(f"**🎯 יעד ניווט:** {item['target_name']}")
    
    # כפתור הניווט הייעודי של Streamlit
    navigation_url = f"https://www.google.com/maps/search/?api=1&query={item['map_search_query']}"
    st.link_button("🧭 לחצי כאן לניווט והגעה למקום (Google Maps)", navigation_url, type="primary")
    
    st.markdown("**🗺️ מה עושים כאן:**")
    for act in item['activities']:
        st.markdown(f"* {act}")
        
    st.write("---")
