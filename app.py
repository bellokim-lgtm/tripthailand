import streamlit as st
import pandas as pd
from datetime import date

# הגדרות עמוד
st.set_page_config(page_title="טיול משפחתי - תאילנד 2026", layout="centered")

# עיצוב CSS
st.markdown("""
    <style>
    .stButton button { width: 100%; border-radius: 10px; height: 3em; background-color: #008080; color: white; }
    h1, h3, h2 { text-align: right; direction: rtl; }
    p, li { text-align: right; direction: rtl; }
    .countdown-box {
        background: linear-gradient(90deg, #1cb5e0 0%, #000851 100%);
        padding: 20px;
        border-radius: 15px;
        text-align: center;
        color: white;
        font-weight: bold;
        margin-bottom: 20px;
    }
    .details-box {
        background-color: #f1f8f9;
        padding: 15px;
        border-radius: 10px;
        border-right: 5px solid #008080;
        direction: rtl;
        text-align: right;
        margin-bottom: 10px;
    }
    /* התאמת תיבת החיפוש ליישור לימין */
    div[data-testid="stTextInput"] {
        direction: rtl;
        text-align: right;
    }
    </style>
    """, unsafe_allow_html=True)

# --- חישוב טבלת ייאוש ---
target_date = date(2026, 5, 20)
today = date.today()
days_left = (target_date - today).days

if days_left > 0:
    st.markdown(f'<div class="countdown-box"><h2 style="margin:0; color:white;">⏳ רק עוד {days_left} ימים לטיול!</h2></div>', unsafe_allow_html=True)
elif days_left == 0:
    st.markdown('<div class="countdown-box"><h2>✈️ טסים היום!</h2></div>', unsafe_allow_html=True)
else:
    st.markdown('<div class="countdown-box"><h2>🏝️ מבלים בתאילנד!</h2></div>', unsafe_allow_html=True)

# --- נתוני הטיול ---
data = [
    {"תאריך": "20/05", "מקום": "JW Marriott Khao Lak", "פעילות": "נחיתה ב-11:25, איסוף רכב ונסיעה לקאו לאק.", "כתובת": "41/12 Moo 3, Khuk Khak, Takuapa, Phang Nga", "ניווט": "https://www.google.com/maps/search/?api=1&query=JW+Marriott+Khao+Lak+Resort", "פירוט": ""},
    {"תאריך": "21/05", "מקום": "מפל Sai Rung / איי סורין Surin", "פעילות": "יום טבע ושנורקלינג (בכפוף למצב הים).", "כתובת": "Nam Khem Pier", "ניווט": "https://www.google.com/maps/search/?api=1&query=Baan+Nam+Khem+Pier", "פירוט": ""},
    {"תאריך": "22/05", "מקום": "מפל Ton Chong Fa Waterfall", "פעילות": "טיול ג'ונגל ובריכות שחייה טבעיות.", "כתובת": "Takua Pa District, Phang-nga", "ניווט": "https://www.google.com/maps/search/?api=1&query=Ton+Chong+Fa+Waterfall", 
     "פירוט": "מסלול קל יחסית, בריכות שחייה, עלות כ-200 באט."},
    {"תאריך": "23/05", "מקום": "La Flora Khao Lak (צבי ים)", "פעילות": "מעבר מלון לבאנג ניאנג וביקור במרכז צבי הים.", "כתובת": "59/1 Moo 5, Khuk Khak, Takua Pa, Phang Nga", "ניווט": "https://www.google.com/maps/search/?api=1&query=La+Flora+Khao+Lak", "פירוט": ""},
    {"תאריך": "24/05", "מקום": "Phang Nga Bay (קיאקים)", "פעילות": "שייט קיאקים בין צוקי גיר ומערות Hong.", "כתובת": "Ao Phang Nga National Park", "ניווט": "https://www.google.com/maps/search/?api=1&query=Ao+Phang+Nga+National+Park+Pier", 
     "פירוט": "שייט בין לגונות, מערות וצוקים. כולל מדריך חותר."},
    {"תאריך": "25/05", "מקום": "Moracea by Khao Lak", "פעילות": "מעבר מלון לחוף Nang Thong.", "כתובת": "26/20 M.7, Khuk Khak, Takuapa, Phang Nga", "ניווט": "https://www.google.com/maps/search/?api=1&query=Moracea+by+Khao+Lak+Resort", "פירוט": ""},
    {"תאריך": "28/05", "מקום": "Khaolak Merlin Resort", "פעילות": "לילה בג'ונגל - חיות בר בגני המלון.", "כתובת": "7/7 Moo 2, Lam Kaen, Thai Mueang, Phang Nga", "ניווט": "https://www.google.com/maps/search/?api=1&query=Khaolak+Merlin+Resort", "פירוט": ""},
    {"תאריך": "29/05", "מקום": "פארק המים Andamanda", "פעילות": "מפל Lampi בדרך ומעבר לפוקט לפארק מים.", "כתובת": "333, Kathu, Kathu District, Phuket", "ניווט": "https://www.google.com/maps/search/?api=1&query=Andamanda+Phuket", "פירוט": ""},
    {"תאריך": "30/05", "מקום": "עיר עתיקה Old Town Phuket", "פעילות": "סיור בעיר העתיקה וטיסה ב-22:30.", "כתובת": "Vichitsongkram Rd, Wichit, Phuket", "ניווט": "https://www.google.com/maps/search/?api=1&query=Central+Phuket+Floresta", "פירוט": ""}
]

df = pd.DataFrame(data)

# --- גוף האפליקציה ---
st.title("🔍 חיפוש אתרים בטיול")

# הוספת תיבת חיפוש
search_query = st.text_input("חפשו אתר (למשל: מפל, מלון, קיאקים...)", "")

# סינון הנתונים לפי החיפוש
if search_query:
    filtered_df = df[
        df['מקום'].str.contains(search_query, case=False, na=False) | 
        df['פעילות'].str.contains(search_query, case=False, na=False) |
        df['פירוט'].str.contains(search_query, case=False, na=False)
    ]
else:
    filtered_df = df

# בחירת מצב תצוגה
mode = st.radio("תצוגה:", ["היום הנוכחי", "טיול מלא / תוצאות חיפוש"], horizontal=True)

if mode == "היום הנוכחי" and not search_query:
    selected_date = st.selectbox("בחר תאריך:", df["תאריך"].tolist())
    day_info = df[df["תאריך"] == selected_date].iloc[0]
    
    st.markdown(f"### 📍 {day_info['מקום']}")
    st.write(f"**מה בתוכנית:** {day_info['פעילות']}")
    if day_info['פירוט']:
        st.markdown(f'<div class="details-box">{day_info["פירוט"]}</div>', unsafe_allow_html=True)
    st.code(day_info['כתובת'], language="text")
    st.link_button("🚗 פתח ניווט", day_info['ניווט'])

else:
    if search_query:
        st.write(f"נמצאו {len(filtered_df)} תוצאות עבור '{search_query}':")
    
    for index, row in filtered_df.iterrows():
        with st.expander(f"{row['תאריך']} - {row['מקום']}"):
            st.write(f"**תוכנית:** {row['פעילות']}")
            if row['פירוט']:
                st.markdown(f'<div class="details-box">{row["פירוט"]}</div>', unsafe_allow_html=True)
            st.code(row['כתובת'], language="text")
            st.link_button(f"ניווט ל-{row['מקום']}", row['ניווט'])

st.markdown("---")
st.markdown("<p style='text-align: center;'>🇹🇭 חופשה מהנה! 🥥</p>", unsafe_allow_html=True)
