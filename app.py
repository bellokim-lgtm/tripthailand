import streamlit as st
from datetime import date

# הגדרות עמוד
st.set_page_config(page_title="המדריך המלא - 2026", layout="centered")

# עיצוב קופסאות הלו"ז, המפה ותיקון זרימת הטקסט (CSS)
st.markdown("""
    <style>
    h1, h3, h2 { text-align: right; direction: rtl; font-family: 'Assistant', sans-serif; }
    
    /* תיקון מלא לסידור הטקסט, הסוגריים והשילוב של עברית ואנגלית */
    p, li, .tip-box { 
        text-align: right; 
        direction: rtl; 
        font-size: 16px; 
        line-height: 1.6;
        unicode-bidi: plaintext;
    }
    
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
    .tip-box {
        background-color: #fff3cd;
        color: #856404;
        padding: 10px;
        border-radius: 8px;
        margin-top: 10px;
        margin-bottom: 15px;
        font-weight: bold;
        border-right: 4px solid #ffeeba;
    }
    </style>
""", unsafe_allow_html=True)

# כותרת ראשית עם תאריכי הטיול
st.title("פוקט וקאו לאק | 20/05–30/05")

# קופסת מפה כללית בראש העמוד
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

# נתוני המסלול עטופים בגרשיים משולשים למניעת שגיאות סינטקס
itinerary = [
    {
        "stage": """תחנה 1: נחיתה והתאוששות""",
        "title": """חוף נייטון השקט והפסטורלי | Naithon Beach""",
        "date_display": f"📅 תאריך: {start_date.strftime('%d/%m/%Y')}",
        "description": """מלון מעולה שנמצא דקות ספורות משדה התעופה של פוקט. בחירה מושלמת ללילה הראשון כדי לנחות, לקבל צ'ק-אין מהיר, לנוח מהטיסה הארוכה וליהנות מחוף נייטון (Naithon Beach) שנחשב לאחד החופים השקטים והנקיים באי.""",
        "target_name": """Wyndham Garden Naithon Phuket""",
        "map_url": "https://www.google.com/maps/search/?api=1&query=Wyndham+Garden+Naithon+Phuket",
        "activities": [
            """הגעה מהירה מהשדה ומנוחה בריזורט החדש.""",
            """הליכה קצרה לשקיעה בחוף נייטון הפסטורלי."""
        ]
    },
    {
        "stage": """תחנה 2: קאו לאק - לינה מרכזית""",
        "title": """ריזורט ג'יי דבליו מריוט קאו לאק | JW Marriott Khao Lak""",
        "date_display": "📅 מהלך הטיול: 21/05 עד 28/05",
        "description": """ריזורט מפואר ברמה גבוהה מאוד המפורסם בזכות בריכת הלגונה הענקית שלו שנמתחת לאורך כל המלון, חדרים עם גישה ישירה למים וחוף חול לבן פרטי ושקט. מכאן תצאו לרוב האטרקציות בחלק המרכזי של החופשה.""",
        "target_name": """JW Marriott Khao Lak Resort & Spa""",
        "map_url": "https://www.google.com/maps/search/?api=1&query=JW+Marriott+Khao+Lak+Resort+Spa",
        "activities": [
            """פינוק במתחם הספא ובבריכות מהארוכות באסיה.""",
            """מנוחה ובטן-גב על קו החוף השליו של קאו לאק."""
        ]
    },
    {
        "stage": """תחנה 3: לב הטבע והג'ונגל""",
        "title": """שמורת הטבע הלאומית קאו סוק | Khao Sok National Park""",
        "date_display": "📅 מהלך הטיול: 21/05 עד 28/05",
        "description": """אחד מאתרי הטבע היפים ביותר בתאילנד. יער גשם עתיק, צוקי גיר עצומים המתנשאים מעל המים, ומגוון בעלי חיים. גולת הכותרת היא אגם צ'אורלאן שבו מומלץ לקחת שייט בסירה ארוכת זנב.""",
        "target_name": """Khao Sok National Park""",
        "map_url": "https://www.google.com/maps/search/?api=1&query=Khao+Sok+National+Park",
        "proximity_tip": """🚗 טיפ מרחק: קאו סוק נמצאת במרחק של כשעה וחצי נסיעה (לכיוון) ממלונות קאו לאק (כמו ה-JW Marriott). מומלץ לצאת מוקדם בבוקר כטיול יום ארוך או לשלב עם מעבר מנוחת הג'ונגל.""",
        "activities": [
            """שייט בין צוקי הגיר המפורסמים באגם צ'אורלאן.""",
            """טיול רגלי בג'ונגל וביקור במערות נטיפים נסתרות."""
        ]
    },
    {
        "stage": """תחנה 4: קאו לאק - אופציה ללינה חלופית 1""",
        "title": """ריזורט קאו לאק מרלין | Khaolak Merlin Resort""",
        "date_display": "📅 מהלך הטיול: 21/05 עד 28/05",
        "description": """ריזורט מדהים המעוצב ממש כמו ג'ונגל טרופי עשיר עם חיות בר, צמחייה עבותה ומפלים פנימיים, ומציע שילוב מושלם בין נוחות מודרנית לטבע פראי על שפת הים.""",
        "target_name": """Khaolak Merlin Resort""",
        "map_url": "https://www.google.com/maps/search/?api=1&query=Khaolak+Merlin+Resort",
        "activities": [
            """סיור בשבילי הטבע המרהיבים בתוך המלון.""",
            """שחייה בבריכות השונות המוקפות בצמחייה טרופית."""
        ]
    },
    {
        "stage": """תחנה 4: קאו לאק - אופציה ללינה חלופית 2""",
        "title": """מלון דה ליטל שור | The Little Shore Khao Lak""",
        "date_display": "📅 מהלך הטיול: 21/05 עד 28/05",
        "description": """מלון בוטיק יוקרתי, חדיש ומודרני המציע חווית אירוח אינטימית, שירות מוקפד ואישי, ועיצוב אדריכלי נקי ומרגיע מול רצועת החוף.""",
        "target_name": """The Little Shore Khao Lak by Katathani""",
        "map_url": "https://www.google.com/maps/search/?api=1&query=The+Little+Shore+Khao+Lak+by+Katathani",
        "activities": [
            """ליהנות מהשקט והפרטיות של מלון הבוטיק החדיש.""",
            """ארוחת ערב יוקרתית מול הנוף הפתוח של הים."""
        ]
    },
    {
        "stage": """תחנה 4: קאו לאק - אופציה ללינה חלופית 3""",
        "title": """ריזורט מורסאה קאו לאק | Moracea by Khao Lak""",
        "date_display": "📅 מהלך הטיול: 21/05 עד 28/05",
        "description": """מלון יפהפה הבנוי על צלע גבעה ירוקה הגולשת ישירות אל תוך חוף הים, ומציע בקתות עץ וחדרים באווירה תאילנדית קלאסית ואותנטית.""",
        "target_name": """Moracea by Khao Lak Resort""",
        "map_url": "https://www.google.com/maps/search/?api=1&query=Moracea+by+Khao+Lak+Resort",
        "activities": [
            """תצפית שקיעה מרהיבה מאזור המסעדה שעל צלע ההר.""",
            """הליכה רגועה ישירות מהחדר אל רצועת החוף הפרטית."""
        ]
    },
    {
        "stage": """תחנה 4: אופציה לטיול יום - בריכת האזמרגד""",
        "title": """בריכת האזמרגד | Emerald Pool""",
        "date_display": "📅 מהלך הטיול: 21/05 עד 28/05",
        "description": """בריכה טבעית מדהימה ביופייה הנובעת בלב שמורת טבע מוגנת ביער הגשם. המים הבהירים והצלולים מקבלים גוון ירוק-טורקיז מהפנט בגלל השתקפות המינרלים והטבע מסביב.""",
        "target_name": """Emerald Pool (Sa Morakot)""",
        "map_url": "https://www.google.com/maps/search/?api=1&query=Emerald+Pool+Sa+Morakot+Thailand",
        "proximity_tip": """⚠️ שימו לב למרחק: בריכת האזמרגד נמצאת באזור קראבי. המשמעות היא נסיעה ארוכה של כשעתיים וחצי עד שלוש שעות לכל כיוון מקאו לאק. מומלץ לעשות זאת רק אם אתם מוכנים ליום נסיעות שלם, או לשלב את זה ביום המעבר דרומה לפוקט!""",
        "activities": [
            """הליכה במסלול מסודר ופסטורלי בתוך יער הגשם המוביל אל הבריכה.""",
            """שחייה מרעננת במים הצלולים והחמימים של בריכת הטורקיז."""
        ]
    },
    {
        "stage": """תחנה 4: אטרקציית טבע בקאו לאק""",
        "title": """מפל סאי רונג | Sai Rung Waterfall""",
        "date_display": "📅 מהלך הטיול: 21/05 עד 28/05",
        "description": """מפל מים יפהפה, מרעננת ונגיש במיוחד בקאו לאק. המים נופלים מגובה אל תוך בריכה טבעית קסומה המוקפת בצמחייה טרופית עשירה, בה ניתן להשתכשך בכיף. המקום נוח מאוד להגעה ללא צורך בהליכה מאומצת.""",
        "target_name": """Sai Rung Waterfall""",
        "map_url": "https://www.google.com/maps/search/?api=1&query=Ton+Chong+Fa+Waterfall",
        "proximity_tip": """📍 טיפ מרחק: קרוב מאוד! מפל סאי רונג נמצא במרחק של פחות מ-15 דקות נסיעה מריזורט ה-JW Marriott. אידיאלי לעצירה ספונטנית וקלילה.""",
        "activities": [
            """רחצה מרעננת בבריכת המים הטבעית למרגלות המפל.""",
            """נהנים מהאווירה והטבע השקט מסביב."""
        ]
    },
    {
        "stage": """תחנה 4: אטרקציית טבע בקאו לאק""",
        "title": """מפל טון צ'ונג פה | Ton Chong Fa Waterfall""",
        "date_display": "📅 מהלך הטיול: 21/05 עד 28/05",
        "description": """מפל מרשים וגדול יותר השוכן בתוך שטח הפארק הלאומי. המפל מורכב מ-5 מפלסים מדהימים המסתתרים עמוק בתוך יער הגשם, ומציע חווית טיול קצת יותר הרפתקנית הכוללת הליכה קצרה בשבילי הג'ונגל הפראי.""",
        "target_name": """Ton Chong Fa Waterfall""",
        "map_url": "https://maps.app.goo.gl/KCwV8EVLu76GfWP6A1",
        "proximity_tip": """📍 טיפ מרחק: כ-25 דקות נסיעה מאזור המלונות המרכזי בקאו לאק. מומלץ לשלב נעלי הליכה נוחות אם תרצו לטפס בין המפלסים השונים.""",
        "activities": [
            """טיול הליכה קל בג'ונגל בין מפלסי המפל השונים.""",
            """תצפית על זרימת המים המרשימה ורחצה בבריכות הגבוהות."""
        ]
    },
    {
        "stage": """תחנה 4: שייט במפרץ האיים""",
        "title": """איי הונג | Koh Hong""",
        "date_display": "📅 מהלך הטיול: 21/05 עד 28/05",
        "description": """קבוצת איים חלומית ומפורסמת ביופייה, המהווה חלק מהפארק הלאומי של מחוז קראבי. האי המרכזי מציע לגונה פנימית נסתרת ומרהיבה אליה נכנסים דרך פתח צר בצוקים, לצד חוף עם חול לבן ורך ומים צלולים לחלוטין המושלמים לשנורקלינג.""",
        "target_name": """Koh Hong (Hong Islands)""",
        "map_url": "https://www.google.com/maps/search/?api=1&query=Ko+Lao+Bile",
        "proximity_tip": """🚤 טיפ מרחק: נקודת היציאה לשייט במפרץ פאנג נגה ובדרך לאיי הונג נמצאת במרחק של כ-45 דקות עד שעה נסיעה דרומית לקאו לאק. זוהי נקודה פנטסטית ליום שייט חוויתי ומלא בנופים בלתי נשכחים.""",
        "activities": [
            """שייט בסירה מהירה או סירת לונגטייל והגעה לחופים הלבנים של Koh Hong.""",
            """כניסה אל הלגונה הנסתרת והמדהימה בלב האי, חתירה בקיאקים ושנורקלינג עם דגים צבעוניים."""
        ]
    },
    {
        "stage": """תחנה 5: סיום יוקרתי ומפנק""",
        "title": """חוף קאטה נוי | Kata Noi Beach""",
        "date_display": f"📅 תאריכים: {end_start_date.strftime('%d/%m/%Y')} עד {end_date.strftime('%d/%m/%Y')}",
        "description": """הקטאטאני הוא אחד הריזורטים המבוקשים והמפנקים ביותר בדרום פוקט. הוא יושב על רצועת החוף המדהימה של קאטה נוי ומציע חווית חופש מושלמת, רגועה ויוקרתית לסגור איתה את הטיול.""",
        "target_name": """Katathani Phuket Beach Resort""",
        "map_url": "https://www.google.com/maps/search/?api=1&query=Katathani+Phuket+Beach+Resort",
        "activities": [
            """נופש בטן-גב מוחלט בבריכות הריזורט המתוחות לאורך קו החוף.""",
            """ארוחת ערב חגיגית מול השקיעה באחת ממסעדות האזור."""
        ]
    }
]

# הרצת הלו"ז והצגתו
for item in itinerary:
    st.markdown(f"""
    <div class="itinerary-card">
        <span class="stage-tag">{item['stage']}</span>
        <div class="date-badge">{item['date_display']}</div>
        <h3>📍 {item['title']}</h3>
        <p style="color: #444; text-align: right; direction: rtl; unicode-bidi: plaintext;">{item['description']}</p>
    </div>
    """, unsafe_allow_html=True)
    
    # הצגת טיפ המרחק/קרבה במידה וקיים
    if "proximity_tip" in item:
        st.markdown(f"""<div class="tip-box">{item['proximity_tip']}</div>""", unsafe_allow_html=True)
    
    st.markdown(f"**🎯 יעד ניווט:** {item['target_name']}")
    st.link_button("🧭 לחצי כאן לניווט והגעה למקום (Google Maps)", item['map_url'], type="primary")
    
    st.markdown("**🗺️ מה עושים כאן:**")
    for act in item['activities']:
        st.markdown(f"* {act}")
        
    st.write("---")
