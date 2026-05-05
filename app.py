import streamlit as st
import pandas as pd
from datetime import date
import random

# הגדרות עמוד
st.set_page_config(page_title="תאילנד 2026 - המדריך המלא", layout="centered")

# עיצוב CSS
st.markdown("""
    <style>
    .stButton button { width: 100%; border-radius: 12px; height: 3.5em; background-color: #008080; color: white; font-weight: bold; border: none; }
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
        padding: 5px 15px;
        border-radius: 8px;
        margin-top: 15px;
        display: inline-block;
    }
    .info-card {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 15px;
        border-right: 8px solid #008080;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        direction: rtl;
        text-align: right;
    }
    </style>
    """, unsafe_allow_html=True)

# --- ספירה לאחור ---
target_date = date(2026, 5, 20)
days_left = (target_date - date.today()).days
st.markdown(f"""
    <div class="countdown-container">
        <span style="font-size: 40px; font-weight: 900; color: #008080;">{max(0, days_left)} ימים</span><br>
        <span style="font-size: 18px;">עד שהדרכון מקבל חותמת של חופש! ✈️</span>
    </div>
""", unsafe_allow_html=True)

# --- בסיס נתונים מורחב ---
data = [
    {
        "תאריך": "20/05",
        "מקום": "JW Marriott Khao Lak",
        "פעילות": "נחיתה והתאקלמות",
        "על המלון": "ריזורט 5 כוכבים מפואר עם הבריכה הארוכה ביותר בדרום מזרח אסיה (יותר מ-2 קילומטר של בריכה!). המלון מעוצב בסגנון תאילנדי קלאסי עם המון פינות חמד.",
        "מה עושים": "אחרי הנחיתה ב-11:25 ואיסוף הרכב, ניסע צפונה לקאו לאק (כשעה ורבע נסיעה). היום מוקדש למנוחה, סיבוב בבריכה האינסופית של המלון וארוחת ערב ראשונה מול הים.",
        "כתובת": "41/12 Moo 3, Khuk Khak, Takuapa",
        "ניווט": "https://www.google.com/maps/search/?api=1&query=JW+Marriott+Khao+Lak+Resort"
    },
    {
        "תאריך": "21/05",
        "מקום": "מפל Sai Rung",
        "פעילות": "מפל הקשת בענן",
        "על המלון": "ממשיכים לילה שני ב-JW Marriott. מומלץ לנצל את ארוחת הבוקר המפורסמת שלהם.",
        "מה עושים": "נסיעה קצרה של 10 דקות מהמלון למפל קליל ונגיש. המפל נופל לבריכה רדודה שאפשר להשתכשך בה. המקום מוקף בצמחייה טרופית ויש מסעדות קטנות בקרבת מקום לנשנוש צהריים.",
        "כתובת": "Khuekkhak, Takua Pa District",
        "ניווט": "https://www.google.com/maps/search/?api=1&query=Sai+Rung+Waterfall+Khao+Lak"
    },
    {
        "תאריך": "22/05",
        "מקום": "מפל Ton Chong Fa",
        "פעילות": "טיול ג'ונגל ומפלים",
        "על המלון": "לילה אחרון ב-JW Marriott - זמן טוב למסאז' במלון או בדוכנים שעל החוף.",
        "מה עושים": "מפל מרשים בעל 5 מפלסים. המסלול עובר בתוך הג'ונגל. בדרגה הראשונה יש בריכה טבעית עם 'דגי פדיקור' שידגדגו לכם ברגליים. הליכה מעט יותר מאתגרת מהיום הקודם אבל מתאימה למשפחות.",
        "כתובת": "Takua Pa District, Phang-nga",
        "ניווט": "https://www.google.com/maps/search/?api=1&query=Ton+Chong+Fa+Waterfall"
    },
    {
        "תאריך": "23/05",
        "מקום": "La Flora Khao Lak",
        "פעילות": "מרכז צבי הים וחוף באנג ניאנג",
        "על המלון": "מלון מודרני במיקום מעולה בלב אזור באנג ניאנג. קרוב מאוד לשוק הלילה ולמסעדות. העיצוב נקי והבריכות גולשות לחוף.",
        "מה עושים": "נוסעים לבסיס חיל הים (Thap Lamu) לבקר במרכז שיקום צבי הים. רואים צבים בכל הגדלים. אחר כך צ'ק-אין במלון החדש וסיבוב ערב בשוק הלילה של באנג ניאנג (שוק תוסס עם אוכל רחוב ומזכרות).",
        "כתובת": "59/1 Moo 5, Khuk Khak",
        "ניווט": "https://www.google.com/maps/search/?api=1&query=La+Flora+Khao+Lak"
    },
    {
        "תאריך": "24/05",
        "מקום": "Phang Nga Bay",
        "פעילות": "שייט קיאקים במפרץ פאנג נגה",
        "על המלון": "לילה שני ב-La Flora. מומלץ לצאת בערב למסעדות המעולות שנמצאות במרחק הליכה קצר מהמלון.",
        "מה עושים": "יום שיא! שייט בין צוקי גיר ענקיים שיוצאים מהמים. נכנסים עם קיאקים (יש מדריך שחותר) לתוך מערות נטיפים ולגונות נסתרות. כולל ביקור ב'אי של ג'יימס בונד'. יום מלא בחוויות וצילומים.",
        "כתובת": "Ao Phang Nga National Park",
        "ניווט": "https://www.google.com/maps/search/?api=1&query=Ao+Phang+Nga+National+Park+Pier"
    },
    {
        "תאריך": "25/05",
        "מקום": "Moracea by Khao Lak",
        "פעילות": "רוגע בחוף Nang Thong",
        "על המלון": "מלון מרהיב הבנוי על צלע גבעה שיורדת עד לים. חדרים עם נוף פנורמי ואווירה רומנטית ושקטה יותר.",
        "מה עושים": "מעבר לחוף 'החולות הזהובים'. זה יום להוריד הילוך, ליהנות מהשקיעות המטורפות של חוף נאנג ת'ונג, ולטייל בערב ברחוב הראשי של קאו לאק סנטר (קניות וברים).",
        "כתובת": "26/20 M.7, Khuk Khak",
        "ניווט": "https://www.google.com/maps/search/?api=1&query=Moracea+by+Khao+Lak+Resort"
    },
    {
        "תאריך": "28/05",
        "מקום": "Khaolak Merlin Resort",
        "פעילות": "לינה בתוך שמורת טבע",
        "על המלון": "חוויה ייחודית! המלון מרגיש כמו גן בוטני ענק. יש בו נחלים, עצים עתיקים וחיות בר (סנאים, לטאות כוח) שמסתובבות חופשי. ידידותי מאוד למשפחות.",
        "מה עושים": "יום של 'ג'ונגל לייט'. נהנים מהמתקנים המדהימים של המלון, הבריכות שמשתלבות בטבע, ואולי טיול פילים (אתי) שנמצא בקרבת מקום.",
        "כתובת": "7/7 Moo 2, Lam Kaen",
        "ניווט": "https://www.google.com/maps/search/?api=1&query=Khaolak+Merlin+Resort"
    },
    {
        "תאריך": "29/05",
        "מקום": "Andamanda & Katathani",
        "פעילות": "פארק מים ומעבר לפוקט",
        "על המלון": "Katathani - ריזורט ענק על חוף Kata Noi המבודד. המלון הכי מבוקש למשפחות בזכות מתקני הילדים והקרבה לחוף שקט ונקי.",
        "מה עושים": "מתחילים את הבוקר באקשן בפארק המים Andamanda (הכי גדול בפוקט!). משם נסיעה דרומה לצ'ק-אין ב-Katathani. בערב - ארוחה מול הגלים.",
        "כתובת": "14 Kata Noi Rd, Karon, Phuket",
        "ניווט": "https://www.google.com/maps/search/?api=1&query=Katathani+Phuket+Beach+Resort"
    },
    {
        "תאריך": "30/05",
        "מקום": "Central Phuket & טיסה",
        "פעילות": "שופינג ופרידה מתאילנד",
        "על המלון": "צ'ק-אאוט מ-Katathani (אפשר להשאיר מזוודות בשמירת חפצים).",
        "מה עושים": "יום שופינג מרוכז ב-Central Phuket Floresta. כל המותגים, קומת אוכל עצומה ואקווריום. משם נסיעה של שעה לשדה התעופה לטיסה של 22:30. לא לשכוח להגיע לשדה 3 שעות לפני!",
        "כתובת": "Vichitsongkram Rd, Phuket",
        "ניווט": "https://www.google.com/maps/search/?api=1&query=Central+Phuket+Floresta"
    }
]

df = pd.DataFrame(data)

# --- תצוגת האפליקציה ---
st.title("🗺️ תאילנד 2026: המדריך המשפחתי")

mode = st.radio("בחר תצוגה:", ["היום הנוכחי", "הלו\"ז המלא"], horizontal=True)

if mode == "היום הנוכחי":
    selected_date = st.selectbox("לאיזה יום תרצו לראות פירוט?", df["תאריך"].tolist())
    row = df[df["תאריך"] == selected_date].iloc[0]
    
    st.markdown(f"### 📍 {row['מקום']}")
    
    st.markdown('<div class="section-header">🏨 על המלון</div>', unsafe_allow_html=True)
    st.write(row['על המלון'])
    
    st.markdown('<div class="section-header">🛶 מה עושים היום?</div>', unsafe_allow_html=True)
    st.write(row['מה עושים'])
    
    st.markdown("---")
    st.code(f"כתובת: {row['כתובת']}")
    st.link_button("🚗 נווט ליעד", row['ניווט'])

else:
    for _, row in df.iterrows():
        with st.expander(f"📅 {row['תאריך']} - {row['מקום']}"):
            st.markdown("**🏨 המלון:** " + row['על המלון'])
            st.markdown("**🛶 הפעילות:** " + row['מה עושים'])
            st.link_button(f"ניווט ל-{row['מקום']}", row['ניווט'])

st.markdown("---")
st.markdown("<p style='text-align: center; color: #888;'>חופשה מהנה! אל תשכחו לשתות המון שייק מנגו 🥭</p>", unsafe_allow_html=True)
