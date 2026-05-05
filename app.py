import streamlit as st
import pandas as pd
from datetime import date

# הגדרות עמוד
st.set_page_config(page_title="תאילנד 2026 - המשפחה טסה!", layout="centered")

# עיצוב CSS משודרג
st.markdown("""
    <style>
    .stButton button { width: 100%; border-radius: 12px; height: 3.5em; background-color: #008080; color: white; font-weight: bold; border: none; }
    h1, h3, h2 { text-align: right; direction: rtl; font-family: 'Assistant', sans-serif; }
    p, li { text-align: right; direction: rtl; font-size: 16px; }
    .countdown-container {
        background: linear-gradient(135deg, #ff9a9e 0%, #fad0c4 100%);
        padding: 25px;
        border-radius: 20px;
        text-align: center;
        box-shadow: 0 10px 20px rgba(0,0,0,0.1);
        margin-bottom: 25px;
        direction: rtl;
    }
    .countdown-number { font-size: 45px; color: #ff0055; font-weight: 900; display: block; }
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

# --- טבלת ייאוש מדליקה ---
target_date = date(2026, 5, 20)
today = date.today()
days_left = (target_date - today).days

if days_left > 0:
    st.markdown(f"""
        <div class="countdown-container">
            <span style="font-size: 20px;">תחזיקו חזק, זה כמעט כאן...</span>
            <span class="countdown-number">{days_left} ימים!</span>
            <span style="font-size: 18px; color: #444;">עד שנחליף את המזגן של הבית בבריזה של קאו לאק 🥥🍹</span>
            <br><br>
            <span style="font-size: 14px; font-style: italic;">#תאילנד2026 #לאיכוליםלחכות</span>
        </div>
    """, unsafe_allow_html=True)
elif days_left == 0:
    st.markdown("""<div class="countdown-container"><h2>✈️ צאו לדרך! השייק כבר מחכה לכם! 🥭</h2></div>""", unsafe_allow_html=True)
else:
    st.markdown("""<div class="countdown-container"><h2>🏝️ חיים את החלום! אל תשכחו למרוח קרם הגנה ☀️</h2></div>""", unsafe_allow_html=True)

# --- נתוני הטיול (סורין הוסר) ---
data = [
    {"תאריך": "20/05", "מקום": "JW Marriott Khao Lak", "פעילות": "נוחתים ב-11:25, אוספים את הרכב וטסים צפונה לגן עדן!", "כתובת": "41/12 Moo 3, Khuk Khak, Takuapa, Phang Nga", "ניווט": "https://www.google.com/maps/search/?api=1&query=JW+Marriott+Khao+Lak+Resort", "פירוט": ""},
    {"תאריך": "21/05", "מקום": "מפל Sai Rung", "פעילות": "קפיצה למפל הקשת בענן - קרוב, קליל ומרענן.", "כתובת": "Khuekkhak, Takua Pa District, Phang-nga", "ניווט": "https://www.google.com/maps/search/?api=1&query=Sai+Rung+Waterfall+Khao+Lak", "פירוט": ""},
    {"תאריך": "22/05", "מקום": "מפל Ton Chong Fa", "פעילות": "הליכה בג'ונגל ובריכות שחייה טבעיות.", "כתובת": "Takua Pa District, Phang-nga", "ניווט": "https://www.google.com/maps/search/?api=1&query=Ton+Chong+Fa+Waterfall", 
     "פירוט": "💰 כניסה: ~200 באט. הליכה של 10-30 דקות. יש בריכות שחייה ומדי פעם קופים בדרך! מושלם לחצי יום רגוע."},
    {"תאריך": "23/05", "מקום": "La Flora Khao Lak (צבי ים)", "פעילות": "עוברים מלון לבאנג ניאנג ומבקרים את הצבים בבסיס חיל הים.", "כתובת": "59/1 Moo 5, Khuk Khak, Takua Pa, Phang Nga", "ניווט": "https://www.google.com/maps/search/?api=1&query=La+Flora+Khao+Lak", "פירוט": ""},
    {"תאריך": "24/05", "מקום": "Phang Nga Bay (קיאקים)", "פעילות": "טיול חובה! שייט במערות ולגונות נסתרות.", "כתובת": "Ao Phang Nga National Park", "ניווט": "https://www.google.com/maps/search/?api=1&query=Ao+Phang+Nga+National+Park+Pier", 
     "פירוט": "שייט קיאקים בין צוקים. לא חותרים לבד - יש מדריך! בטוח ורגוע מאוד לילדות."},
    {"תאריך": "25/05", "מקום": "Moracea by Khao Lak", "פעילות": "מעבר למלון המרהיב על צלע הגבעה בחוף Nang Thong.", "כתובת": "26/20 M.7, Khuk Khak, Takuapa, Phang Nga", "ניווט": "https://www.google.com/maps/search/?api=1&query=Moracea+by+Khao+Lak+Resort", "פירוט": ""},
    {"תאריך": "28/05", "מקום": "Khaolak Merlin Resort", "פעילות": "לילה בג'ונגל - המלון הכי 'טבעי' שיש.", "כתובת": "7/7 Moo 2, Lam Kaen, Thai Mueang, Phang Nga", "ניווט": "https://www.google.com/maps/search/?api=1&query=Khaolak+Merlin+Resort", "פירוט": "שימו לב לסנאים וללטאות הכוח (הידידותיות!) בגני המלון."},
    {"תאריך": "29/05", "מקום": "פארק המים Andamanda", "פעילות": "מפל Lampi בדרך ומעבר לפוקט ליום של אקשן בתוך המים.", "כתובת": "333, Kathu, Kathu District, Phuket", "ניווט": "https://www.google.com/maps/search/?api=1&query=Andamanda+Phuket", "פירוט": ""},
    {"תאריך": "30/05", "מקום": "העיר העתיקה וטיסה", "פעילות": "סיבוב פרידה בפוקט טאון, קניות אחרונות וטיסה ב-22:30.", "כתובת": "Vichitsongkram Rd, Wichit, Phuket", "ניווט": "https://www.google.com/maps/search/?api=1&query=Central+Phuket+Floresta", "פירוט": ""}
]

df = pd.DataFrame(data)

# --- גוף האפליקציה ---
st.title("🔍 מצאו את היעד הבא שלכם")

search_query = st.text_input("חפשו מקום או פעילות...", "")

if search_query:
    filtered_df = df[df['מקום'].str.contains(search_query, case=False, na=False) | df['פעילות'].str.contains(search_query, case=False, na=False)]
else:
    filtered_df = df

mode = st.radio("תצוגה:", ["היום הנוכחי", "כל הטיול"], horizontal=True)

if mode == "היום הנוכחי" and not search_query:
    selected_date = st.selectbox("בחר תאריך:", df["תאריך"].tolist())
    day_info = df[df["תאריך"] == selected_date].iloc[0]
    st.markdown(f"### 📍 {day_info['מקום']}")
    st.write(f"**מה בלו\"ז:** {day_info['פעילות']}")
    if day_info['פירוט']:
        st.markdown(f'<div class="details-box">{day_info["פירוט"]}</div>', unsafe_allow_html=True)
    st.code(day_info['כתובת'], language="text")
    st.link_button("🚗 יאללה נוסעים! (ניווט)", day_info['ניווט'])

else:
    for index, row in filtered_df.iterrows():
        with st.expander(f"{row['תאריך']} - {row['מקום']}"):
            st.write(f"**פעילות:** {row['פעילות']}")
            if row['פירוט']:
                st.markdown(f'<div class="details-box">{row["פירוט"]}</div>', unsafe_allow_html=True)
            st.code(row['כתובת'], language="text")
            st.link_button(f"ניווט ל-{row['מקום']}", row['ניווט'])

st.markdown("---")
st.markdown("<p style='text-align: center;'>🇹🇭 שתהיה לנו החופשה הכי טובה בעולם! 🥥</p>", unsafe_allow_html=True)
