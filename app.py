import streamlit as st
import pandas as pd

# הגדרות עמוד
st.set_page_config(page_title="טיול משפחתי - תאילנד 2026", layout="centered")

# עיצוב CSS בסיסי להתאמה לנייד
st.markdown("""
    <style>
    .stButton button { width: 100%; border-radius: 10px; height: 3em; background-color: #008080; color: white; }
    .stDownloadButton button { width: 100%; }
    h1, h3 { text-align: right; direction: rtl; }
    p { text-align: right; direction: rtl; }
    .address-box { background-color: #f0f2f6; padding: 10px; border-radius: 5px; text-align: left; direction: ltr; font-size: 14px; }
    </style>
    """, unsafe_allow_html=True)

# נתוני הטיול
data = [
    {"תאריך": "20/05", "מקום": "JW Marriott Khao Lak", "פעילות": "נחיתה (11:25), איסוף רכב וצ'ק-אין", "כתובת": "41/12 Moo 3, Khuk Khak, Takuapa, Phang Nga", "ניווט": "https://www.google.com/maps/search/?api=1&query=JW+Marriott+Khao+Lak+Resort"},
    {"תאריך": "21/05", "מקום": "מפל Sai Rung + צבי ים", "פעילות": "טיול קל למפל וביקור במרכז הצבים", "כתובת": "Khuekkhak, Takua Pa District, Phang-nga", "ניווט": "https://www.google.com/maps/search/?api=1&query=Sai+Rung+Waterfall+Khao+Lak"},
    {"תאריך": "22/05", "מקום": "La Flora Khao Lak", "פעילות": "מפל Ton Chong Fa ומעבר מלון", "כתובת": "59/1 Moo 5, Khuk Khak, Takua Pa, Phang Nga", "ניווט": "https://www.google.com/maps/search/?api=1&query=La+Flora+Khao+Lak"},
    {"תאריך": "23/05", "מקום": "מרכז באנג ניאנג", "פעילות": "זמן חוף, בריכה ושוק מקומי (Bang Niang Market)", "כתובת": "Khuekkhak, Takua Pa District, Phang-nga", "ניווט": "https://www.google.com/maps/search/?api=1&query=Bang+Niang+Market"},
    {"תאריך": "24/05", "מקום": "נחל Kiang Koo", "פעילות": "שיט רפסודות במבוק רגוע בג'ונגל", "כתובת": "4/20 Moo 1, Kukkak, Takuapa, Phang Nga", "ניווט": "https://www.google.com/maps/search/?api=1&query=Komol+Corner+Bamboo+Rafting"},
    {"תאריך": "25/05", "מקום": "Moracea by Khao Lak", "פעילות": "מעבר מלון ובילוי בחוף Nang Thong", "כתובת": "26/20 M.7, Khuk Khak, Takuapa, Phang Nga", "ניווט": "https://www.google.com/maps/search/?api=1&query=Moracea+by+Khao+Lak+Resort"},
    {"תאריך": "26/05", "מקום": "שמורת Khao Lak-Lam Ru", "פעילות": "טיול רגלי קל (Eco-Trail) לחוף נסתר", "כתובת": "7/9 Moo 2, Thai Mueang, Phang-nga", "ניווט": "https://www.google.com/maps/search/?api=1&query=Khao+Lak+Lam+Ru+National+Park"},
    {"תאריך": "27/05", "מקום": "מרכז קאו לאק", "פעילות": "קניות, מסאז'ים וזמן חופשי", "כתובת": "Nang Thong, Khao Lak", "ניווט": "https://www.google.com/maps/search/?api=1&query=Nang+Thong+Beach+Khao+Lak"},
    {"תאריך": "28/05", "מקום": "Khaolak Merlin Resort", "פעילות": "מעבר מלון (לילה אחד) - 'ספארי' חיות בגני המלון", "כתובת": "7/7 Moo 2, Lam Kaen, Thai Mueang, Phang Nga", "ניווט": "https://www.google.com/maps/search/?api=1&query=Khaolak+Merlin+Resort"},
    {"תאריך": "29/05", "מקום": "פארק המים Andamanda", "פעילות": "מפל Lampi בדרך ומעבר לפוקט לפארק מים", "כתובת": "333, Kathu, Kathu District, Phuket", "ניווט": "https://www.google.com/maps/search/?api=1&query=Andamanda+Phuket"},
    {"תאריך": "30/05", "מקום": "העיר העתיקה + טיסה", "פעילות": "Old Town, קניון סנטרל וחזרה לשדה ב-20:00", "כתובת": "Vichitsongkram Rd, Wichit, Phuket", "ניווט": "https://www.google.com/maps/search/?api=1&query=Central+Phuket+Floresta"}
]

df = pd.DataFrame(data)

# כותרת האפליקציה
st.title("🌴 טיול משפחתי: פוקט & קאו לאק")
st.subheader("מאי 2026")

# בחירת מצב תצוגה
mode = st.radio("בחר תצוגה:", ["היום הנוכחי", "טיול מלא"], horizontal=True)

if mode == "היום הנוכחי":
    selected_date = st.selectbox("בחר תאריך:", df["תאריך"].tolist())
    day_info = df[df["תאריך"] == selected_date].iloc[0]
    
    st.markdown(f"### 📍 {day_info['מקום']}")
    st.write(f"**מה עושים:** {day_info['פעילות']}")
    
    st.markdown("**כתובת להעתקה:**")
    st.code(day_info['כתובת'], language="text")
    
    st.link_button("🚗 נווט עם Google Maps / Waze", day_info['ניווט'])

else:
    st.markdown("### 📋 המסלול המלא")
    for index, row in df.iterrows():
        with st.expander(f"{row['תאריך']} - {row['מקום']}"):
            st.write(f"**פעילות:** {row['פעילות']}")
            st.write(f"**כתובת:** {row['כתובת']}")
            st.link_button(f"נווט ל-{row['מקום']}", row['ניווט'])

# חתימה בתחתית
st.markdown("---")
st.markdown("<p style='text-align: center;'>חופשה מהנה! 🥥</p>", unsafe_allow_html=True)
