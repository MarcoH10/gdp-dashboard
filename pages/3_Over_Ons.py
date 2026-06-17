import streamlit as st
from styles import MAIN_CSS, footer_html
from database import init_db

st.set_page_config(
    page_title="Over Ons – Ariaans Assurantiën",
    page_icon="🏢",
    layout="wide",
    initial_sidebar_state="collapsed",
    menu_items={"Get help": None, "Report a bug": None, "About": None},
)

init_db()
st.markdown(MAIN_CSS, unsafe_allow_html=True)

st.markdown("""
<div class="page-hero">
    <h1>🏢 Over Ariaans Assurantiën</h1>
    <p>25 jaar lang het vertrouwde adres voor verzekeringen in Zuid-Limburg</p>
</div>
""", unsafe_allow_html=True)

# ── Ons verhaal ───────────────────────────────────────────────────────────────
col_story, col_img = st.columns([3, 2], gap="large")
with col_story:
    st.markdown("""
    <div class="card">
        <h3>Ons verhaal</h3>
        <p>Ariaans Assurantiën is in 1999 opgericht door <strong>Arian Habets</strong>
        vanuit de overtuiging dat verzekeren persoonlijk en transparant kan én moet zijn.
        Wat begon als een eenmanszaak in Maastricht is uitgegroeid tot een adviesbureau
        met twee vestigingen – Maastricht en Heerlen – en een team van acht gepassioneerde
        adviseurs.</p>
        <br>
        <p>In 25 jaar hebben wij meer dan <strong>4.200 particulieren en ondernemers</strong>
        in Zuid-Limburg geholpen de juiste verzekering te vinden. Wij zijn trots op onze
        gemiddelde beoordeling van <strong>4.9 sterren</strong> en onze 98% klanttevredenheidscore.</p>
        <br>
        <p>Ons geheim? Wij verkopen geen producten, wij geven <em>advies</em>. Het beste
        advies voor ú – niet het product met de hoogste commissie.</p>
    </div>
    """, unsafe_allow_html=True)
with col_img:
    st.markdown("""
    <div style="background:linear-gradient(135deg,#1a365d,#2b6cb0);border-radius:1rem;
                padding:3rem;text-align:center;color:white;height:100%;
                display:flex;flex-direction:column;justify-content:center;">
        <div style="font-size:4rem;margin-bottom:1rem;">🏛️</div>
        <div style="font-size:2.5rem;font-weight:800;">25</div>
        <div style="font-size:1rem;opacity:0.8;margin-bottom:1.5rem;">jaar ervaring</div>
        <div style="font-size:2.5rem;font-weight:800;">4.200+</div>
        <div style="font-size:1rem;opacity:0.8;margin-bottom:1.5rem;">tevreden klanten</div>
        <div style="font-size:2.5rem;font-weight:800;">2</div>
        <div style="font-size:1rem;opacity:0.8;">vestigingen in Zuid-Limburg</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ── Ons team ──────────────────────────────────────────────────────────────────
st.markdown("""
<div class="section-header">
    <h2>Ons team</h2>
    <p>Acht gecertificeerde adviseurs met gezamenlijk 120 jaar ervaring</p>
</div>
""", unsafe_allow_html=True)

team = [
    ("👨‍💼", "Arian Habets", "Directeur & Oprichter", "WFT Basis, WFT Schade, WFT Leven, WFT Pensioen", "Maastricht"),
    ("👩‍💼", "Monique Lemmens", "Senior Adviseur", "WFT Basis, WFT Schade, WFT Inkomen", "Maastricht"),
    ("👨‍💼", "Kevin Theunissen", "Bedrijfsadviseur", "WFT Basis, WFT Schade, WFT Zakelijk", "Heerlen"),
    ("👩‍💼", "Sandra Kreijns", "Zorgspecialist & Grenswerkers", "WFT Basis, WFT Zorg, Grenswerker Cert.", "Maastricht"),
]

t_cols = st.columns(4, gap="medium")
for i, (icon, naam, rol, certs, kantoor) in enumerate(team):
    with t_cols[i]:
        st.markdown(f"""
        <div class="card" style="text-align:center;">
            <div style="font-size:3rem;margin-bottom:0.75rem;">{icon}</div>
            <h3 style="margin-bottom:0.25rem;">{naam}</h3>
            <div style="color:#3182ce;font-size:0.85rem;font-weight:600;margin-bottom:0.75rem;">{rol}</div>
            <div style="font-size:0.78rem;color:#718096;margin-bottom:0.5rem;">{certs}</div>
            <div style="font-size:0.8rem;color:#4a5568;">📍 {kantoor}</div>
        </div>
        """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ── Onze waarden ──────────────────────────────────────────────────────────────
st.markdown("""
<div class="section-header">
    <h2>Onze kernwaarden</h2>
</div>
""", unsafe_allow_html=True)

val_cols = st.columns(4, gap="medium")
waarden = [
    ("🔍", "Transparantie", "Geen verborgen kosten of commissiemotieven. Wij leggen altijd uit wat u koopt en waarom."),
    ("🤝", "Persoonlijk", "Elke klant heeft een vaste adviseur. Geen callcenter, maar een mens die u kent."),
    ("⚡", "Snel", "Wij respecteren uw tijd. Offerte binnen 2 uur, schade dezelfde dag opgepakt."),
    ("🌍", "Lokaal", "Wij zijn van Zuid-Limburg. Wij kennen de regio, de risico's en onze klanten persoonlijk."),
]
for i, (icon, titel, tekst) in enumerate(waarden):
    with val_cols[i]:
        st.markdown(f"""
        <div class="card" style="text-align:center;border-top:4px solid #3182ce;">
            <div style="font-size:2rem;margin-bottom:0.75rem;">{icon}</div>
            <h3>{titel}</h3>
            <p>{tekst}</p>
        </div>
        """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ── Vestigingen ───────────────────────────────────────────────────────────────
st.markdown("""
<div class="section-header">
    <h2>Onze vestigingen</h2>
    <p>Altijd dichtbij – of kom gewoon langs</p>
</div>
""", unsafe_allow_html=True)

v_col1, v_col2 = st.columns(2, gap="large")
with v_col1:
    st.markdown("""
    <div class="card">
        <h3>📍 Maastricht (Hoofdkantoor)</h3>
        <p>
            <strong>Adres:</strong> Vrijthof 12, 6211 LE Maastricht<br>
            <strong>Telefoon:</strong> 043 – 123 45 67<br>
            <strong>E-mail:</strong> maastricht@ariaans-assurantien.nl<br><br>
            <strong>Openingstijden:</strong><br>
            Maandag t/m vrijdag: 8:30 – 17:30<br>
            Zaterdag: 09:00 – 13:00 (op afspraak)<br>
            Avondservice: ma, wo, do tot 21:00 (WhatsApp)<br><br>
            <strong>Parkeren:</strong> Gratis in Parking Vrijthof (2u)
        </p>
    </div>
    """, unsafe_allow_html=True)
with v_col2:
    st.markdown("""
    <div class="card">
        <h3>📍 Heerlen</h3>
        <p>
            <strong>Adres:</strong> Oranje Nassaustraat 8, 6411 AM Heerlen<br>
            <strong>Telefoon:</strong> 045 – 987 65 43<br>
            <strong>E-mail:</strong> heerlen@ariaans-assurantien.nl<br><br>
            <strong>Openingstijden:</strong><br>
            Maandag t/m vrijdag: 8:30 – 17:30<br>
            Zaterdag: gesloten<br>
            Avondservice: di, vr tot 21:00 (WhatsApp)<br><br>
            <strong>Parkeren:</strong> Gratis parkeergarage achter het pand
        </p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ── Certificeringen ───────────────────────────────────────────────────────────
st.markdown("""
<div style="background:white;border-radius:1rem;padding:2rem;text-align:center;
            box-shadow:0 4px 20px rgba(0,0,0,0.06);margin-bottom:2rem;">
    <h3 style="color:#1a365d;margin-bottom:1rem;">Certificeringen & lidmaatschappen</h3>
    <div>
        <span class="trust-badge">🏛️ AFM Vergunning nr. 12345678</span>
        <span class="trust-badge">⚖️ KiFiD Aangesloten</span>
        <span class="trust-badge">🤝 Adfiz Lid</span>
        <span class="trust-badge">🔒 ISO 27001 Gecertificeerd</span>
        <span class="trust-badge">🏆 Top 10 Adviseur Limburg 2024</span>
        <span class="trust-badge">📜 DNB Geregistreerd</span>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)
st.markdown(footer_html(), unsafe_allow_html=True)
