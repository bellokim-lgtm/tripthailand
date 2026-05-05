import streamlit as st
import pandas as pd
from datetime import date

# הגדרות עמוד
st.set_page_config(page_title="תאילנד 2026 - Katathani Vibes", layout="centered")

# עיצוב CSS
st.markdown("""
    <style>
    .stButton button { width: 100%; border-radius: 12px; height: 3.5em; background-color: #008080; color: white; font-weight: bold; border: none; }
    h1, h3, h2 { text-align: right; direction: rtl; font-family: 'Assistant', sans-serif; }
    p, li { text-align: right; direction: rtl; font-size: 16px; }
    .countdown-container {
        background: linear-gradient(135deg, #fbc2eb 0%, #a6c1ee 100%);
        padding: 20px;
        border-radius: 20px;
        text-align: center;
        margin-bottom: 25px;
        direction: rtl;
    }
    .details-box {
        background-color: #f0f7f9;
        padding: 15px;
        border-radius: 12px;
        border-right: 6px solid #008080;
        direction: rtl;
        text-align: right;
        margin-bottom: 12px;
    }
    .hotel-box {
        background-color: #fff9db;
        padding: 15px;
        border-radius: 12px;
        border-right: 6px solid #fcc419;
        direction: rtl;
        text-align: right;
    }
    </style>
    """, unsafe_allow_html=True)

# --- טבלת ייאוש ---
days_left = (date(2026, 5, 20) - date.today()).days
st.markdown(f'<div class="countdown-container"><h3>🏝️ עוד {days_left} ימים להתפנקות ב-Katathani!</h3></div>', unsafe_allow_html=True)

# --- נתוני הטיול המעודכנים ---
data = [
    {"תאריך": "20/05", "מקום": "JW Marriott Khao Lak", "פעילות": "נחיתה, איסוף רכב ונסיעה למלון הראשון.", "כתובת": "41/12 Moo 3, Khuk Khak, Takuapa", "ניווט": "https://www.google.com/maps/search/?api=1&query=JW+Marriott+Khao+Lak+Resort", "פירוט": ""},
    {"תאריך": "21/05", "מקום": "מפל Sai Rung", "פעילות": "מפל הקשת בענן - קליל ומרענן.", "כתובת": "Khuekkhak, Takua Pa District", "ניווט": "https://www.google.com/maps/search/?api=1&query=Sai+Rung+Waterfall+Khao+Lak", "פירוט": ""},
    {"תאריך": "22/05", "מקום": "מפל Ton Chong Fa", "פעילות": "ג'ונגל ובריכות שחייה טבעיות.", "כתובת": "Takua Pa District, Phang-nga", "ניווט": "https://www.google.com/maps/search/?api=1&query=Ton+Chong+Fa+Waterfall", "פירוט": "כניסה כ-200 באט. הליכה קלה ובריכות מים."},
    {"תאריך": "23/05", "מקום": "La Flora & מרכז צבי הים", "פעילות": "מעבר מלון וביקור בצבים בבסיס חיל הים.", "כתובת": "Phang Nga Naval Base, Thai Mueang", "ניווט": "https://www.google.com/maps/search/?api=1&query=Sea+Turtle+Conservation+Center+Phang+Nga", "פירוט": "נמצא בתוך בסיס חיל הים (Thap Lamu). להציג תעודה בשער."},
    {"תאריך": "24/05", "מקום": "Phang Nga Bay (קיאקים)", "פעילות": "שייט במערות ולגונות נסתרות.", "כתובת": "Ao Phang Nga National Park", "ניווט": "https://www.google.com/maps/search/?api=1&query=Ao+Phang+Nga+National+Park+Pier", "פירוט": "טיול חובה! בטוח ורגוע לילדים."},
    {"תאריך": "25/05", "מקום": "Moracea by Khao Lak", "פעילות": "מעבר למלון בחוף Nang Thong.", "כתובת": "26/20 M.7, Khuk Khak", "ניווט": "https://www.google.com/maps/search/?api=1&query=Moracea+by+Khao+Lak+Resort", "פירוט": ""},
    {"תאריך": "28/05", "מקום": "Khaolak Merlin Resort", "פעילות": "לילה בג'ונגל עם סנאים ולטאות כוח.", "כתובת": "7/7 Moo 2, Lam Kaen", "ניווט": "https://www.google.com/maps/search/?api=1&query=Khaolak+Merlin+Resort", "פירוט": ""},
    {"תאריך": "29/05", "מקום": "Andamanda & Katathani Phuket", "פעילות": "יום פארק מים ומעבר למלון המפנק בחוף קאטה נוי.", "כתובת": "14 Kata Noi Rd, Karon, Phuket", "ניווט": "https://www.google.com/maps/search/?api=1&query=Katathani+Phuket+Beach+Resort", 
     "פירוט": """
**🏨 Katathani Phuket Beach Resort:**
* המלון יושב על חוף **Kata Noi** - מהחופים היפים והשקטים בפוקט.
* בערב מומלץ לאכול באזור קאטה או להישאר במלון שיש בו המון מסעדות מעולות.
"""},
    {"תאריך": "30/05", "מקום": "שופינג - Central Phuket", "פעילות": "צ'ק אאוט, קניות ב-Central Phuket וטיסה ב-22:30.", "כתובת": "Vichitsongkram Rd, Phuket", "ניווט": "https://www.google.com/maps/search/?api=1&query=Central+Phuket+Floresta", "פירוט": "לא לשכוח VAT Refund! נסיעה מהקניון לשדה התעופה לוקחת כ-45-60 דקות."}
]

df = pd.DataFrame(data)

# --- גוף האפליקציה ---
st.title("🔍 לאן נוסעים היום?")
search_query = st.text_input("חפשו מקום או מילה (למשל: מלון, שופינג, מפל)...", "")

if search_query:
    filtered_df = df[df['מקום'].str.contains(search_query, case=False, na=False) | df['פעילות'].str.contains(search_query, case=False, na=False)]
else:
    filtered_df = df

mode = st.radio("תצוגה:", ["היום הנוכחי", "כל הטיול"], horizontal=True)

if mode == "היום הנוכחי" and not search_query:
    selected_date = st.selectbox("בחר תאריך:", df["תאריך"].tolist(), index=len(df)-2)
    day_info = df[df["תאריך"] == selected_date].iloc[0]
    st.markdown(f"### 📍 {day_info['מקום']}")
    st.write(f"**מה בתוכנית:** {day_info['פעילות']}")
    if day_info['פירוט']:
        st.markdown(f'<div class="details-box">{day_info["פירוט"]}</div>', unsafe_allow_html=True)
    st.code(day_info['כתובת'], language="text")
    st.link_button("🚗 נווט למקום", day_info['ניווט'])

else:
    for index, row in filtered_df.iterrows():
        box_style = "hotel-box" if "Katathani" in row['מקום'] else "details-box"
        with st.expander(f"{row['תאריך']} - {row['מקום']}"):
            st.write(f"**פעילות:** {row['פעילות']}")
            if row['פירוט']:
                st.markdown(f'<div class="{box_style}">{row["פירוט"]}</div>', unsafe_allow_html=True)
            st.code(row['כתובת'], language="text")
            st.link_button(f"ניווט ל-{row['מקום']}", row['ניווט'])

st.markdown("---")
st.markdown("<p style='text-align: center;'>✨ סיומת מושלמת לטיול מושלם! ✨</p>", unsafe_allow_html=True)
