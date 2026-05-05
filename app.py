import streamlit as st
import pandas as pd
from datetime import date
import random

# הגדרות עמוד
st.set_page_config(page_title="תאילנד 2026 - הספירה לאחור!", layout="centered")

# עיצוב CSS
st.markdown("""
    <style>
    .stButton button { width: 100%; border-radius: 12px; height: 3.5em; background-color: #008080; color: white; font-weight: bold; border: none; }
    h1, h3, h2 { text-align: right; direction: rtl; font-family: 'Assistant', sans-serif; }
    p, li { text-align: right; direction: rtl; font-size: 16px; }
    .countdown-container {
        background: linear-gradient(135deg, #fdfcfb 0%, #e2d1c3 100%);
        padding: 30px;
        border-radius: 25px;
        text-align: center;
        box-shadow: 0 10px 25px rgba(0,0,0,0.05);
        margin-bottom: 25px;
        direction: rtl;
        border: 2px dashed #008080;
    }
    .countdown-number { font-size: 55px; color: #008080; font-weight: 900; display: block; line-height: 1; }
    .funny-note { font-style: italic; color: #555; margin-top: 10px; font-size: 18px; }
    .details-box {
        background-color: #f0f7f9;
        padding: 15px;
        border-radius: 12px;
        border-right: 6px solid #008080;
        direction: rtl;
        text-align: right;
        margin-bottom: 12px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- לוגיקה לספירה לאחור ומשפטים מצחיקים ---
target_date = date(2026, 5, 20)
today = date.today()
days_left = (target_date - today).days

def get_funny_note(days):
    if days > 100:
        return random.choice([
            "זה מרגיש רחוק כמו הקינוח הבא שלי, אבל זה יגיע!",
            "זמן מצוין להתחיל להתאמן על אכילה עם מקלות.",
            "בינתיים תמשיכו לחלום על שייק מנגו, זה בחינם.",
            "אפשר כבר להתחיל לארוז? לא? אוקיי..."
        ])
    elif 30 < days <= 100:
        return random.choice([
            "זה הזמן לקנות קרם הגנה לפני שכולם נזכרים.",
            "הודעה רשמית: המזוודה בבוידעם מתחילה להתרגש.",
            "הקיבה שלכם כבר עושה הכנות נפשיות לאוכל חריף.",
            "תתחילו להיפרד מהחולצות הארוכות, הן לא באות איתנו."
        ])
    elif 10 < days <= 30:
        return random.choice([
            "מתחילים לחפש את הדרכונים בלחץ? עכשיו זה זמן טוב.",
            "זהו, רמת הריכוז בעבודה ירדה ל-0. אופסי.",
            "עוד מעט מחליפים את המזגן של המשרד בלחות של פוקט!",
            "האם כבר קניתם כפכפים חדשים או שאתם מחכים לרגע האחרון?"
        ])
    elif 0 < days <= 10:
        return random.choice([
            "זה לא תרגול! חוזר: זה לא תרגול! אורזים באמת!",
            "מצב נפשי: כבר בתוך השייק מנגו.",
            "מישהו ראה את המטען של המצלמה?!",
            "תחזיקו מעמד, תאילנד כבר מריחה אתכם."
        ])
    elif days == 0:
        return "✈️ יאללה למטוס! אל תשכחו את הילדות בטרמינל!"
    else:
        return "🏝️ אנחנו בתאילנד! נא לא להפריע, אני עסוק/ה בלהיות מאושר/ת."

# הצגת הספירה לאחור
st.markdown(f"""
    <div class="countdown-container">
        <span style="font-size: 20px; color: #666;">טבלת ייאוש (גרסת האקסטזה):</span>
        <span class="countdown-number">{max(0, days_left)} ימים</span>
        <p class="funny-note">"{get_funny_note(days_left)}"</p>
    </div>
""", unsafe_allow_html=True)

# --- נתוני הטיול ---
data = [
    {"תאריך": "20/05", "מקום": "JW Marriott Khao Lak", "פעילות": "נחיתה, איסוף רכב וצפונה לגן עדן!", "כתובת": "41/12 Moo 3, Khuk Khak, Takuapa", "ניווט": "https://www.google.com/maps/search/?api=1&query=JW+Marriott+Khao+Lak+Resort", "פירוט": ""},
    {"תאריך": "21/05", "מקום": "מפל Sai Rung", "פעילות": "מפל הקשת בענן - מרענן וקרוב.", "כתובת": "Khuekkhak, Takua Pa District", "ניווט": "https://www.google.com/maps/search/?api=1&query=Sai+Rung+Waterfall+Khao+Lak", "פירוט": ""},
    {"תאריך": "22/05", "מקום": "מפל Ton Chong Fa", "פעילות": "ג'ונגל ובריכות שחייה.", "כתובת": "Takua Pa District, Phang-nga", "ניווט": "https://www.google.com/maps/search/?api=1&query=Ton+Chong+Fa+Waterfall", "פירוט": "כניסה כ-200 באט."},
    {"תאריך": "23/05", "מקום": "La Flora & מרכז צבי הים", "פעילות": "צבים בבסיס חיל הים (להביא תעודה מזהה לשער!).", "כתובת": "Phang Nga Naval Base, Thai Mueang", "ניווט": "https://www.google.com/maps/search/?api=1&query=Sea+Turtle+Conservation+Center+Phang+Nga", "פירוט": ""},
    {"תאריך": "24/05", "מקום": "Phang Nga Bay", "פעילות": "שייט קיאקים בלגונות (לא חותרים לבד, אל דאגה).", "כתובת": "Ao Phang Nga National Park", "ניווט": "https://www.google.com/maps/search/?api=1&query=Ao+Phang+Nga+National+Park+Pier", "פירוט": ""},
    {"תאריך": "25/05", "מקום": "Moracea by Khao Lak", "פעילות": "מעבר למלון על הצוק בחוף Nang Thong.", "כתובת": "26/20 M.7, Khuk Khak", "ניווט": "https://www.google.com/maps/search/?api=1&query=Moracea+by+Khao+Lak+Resort", "פירוט": ""},
    {"תאריך": "28/05", "מקום": "Khaolak Merlin Resort", "פעילות": "לילה בג'ונגל - לחפש את לטאות הכוח בחצר!", "כתובת": "7/7 Moo 2, Lam Kaen", "ניווט": "https://www.google.com/maps/search/?api=1&query=Khaolak+Merlin+Resort", "פירוט": ""},
    {"תאריך": "29/05", "מקום": "Andamanda & Katathani", "פעילות": "פארק מים מטורף ומעבר לחוף קאטה נוי.", "כתובת": "14 Kata Noi Rd, Karon, Phuket", "ניווט": "https://www.google.com/maps/search/?api=1&query=Katathani+Phuket+Beach+Resort", "פירוט": ""},
    {"תאריך": "30/05", "מקום": "שופינג ב-Central Phuket", "פעילות": "מרוקנים את הקניון וטסים הביתה ב-22:30.", "כתובת": "Vichitsongkram Rd, Phuket", "ניווט": "https://www.google.com/maps/search/?api=1&query=Central+Phuket+Floresta", "פירוט": "טיפ: תשאירו מקום במזוודה למציאות!"}
]

df = pd.DataFrame(data)

# --- ממשק חיפוש ---
st.title("🗺️ המדריך המשפחתי לתאילנד")
search_query = st.text_input("חפשו משהו (מפל, שופינג, מלון)...")

if search_query:
    filtered_df = df[df['מקום'].str.contains(search_query, case=False, na=False) | df['פעילות'].str.contains(search_query, case=False, na=False)]
else:
    filtered_df = df

# הצגת נתונים
mode = st.radio("תצוגה:", ["היום הנוכחי", "כל הלו\"ז"], horizontal=True)

if mode == "היום הנוכחי" and not search_query:
    selected_date = st.selectbox("בחר תאריך:", df["תאריך"].tolist())
    day_info = df[df["תאריך"] == selected_date].iloc[0]
    st.markdown(f"### 📍 {day_info['מקום']}")
    st.write(f"**בלו\"ז:** {day_info['פעילות']}")
    st.code(day_info['כתובת'], language="text")
    st.link_button("🚗 יאללה נוסעים!", day_info['ניווט'])
else:
    for _, row in filtered_df.iterrows():
        with st.expander(f"{row['תאריך']} - {row['מקום']}"):
            st.write(f"**פעילות:** {row['פעילות']}")
            if row['פירוט']: st.info(row['פירוט'])
            st.code(row['כתובת'])
            st.link_button("ניווט", row['ניווט'])

st.markdown("---")
st.markdown("<p style='text-align: center;'>🇹🇭 קופון למי שקרא עד כאן: שייק בננה לוטי עלינו! (סתם, על אבא)</p>", unsafe_allow_html=True)
