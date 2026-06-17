import streamlit as st
from database import init_db, save_lead
from styles import MAIN_CSS, footer_html

st.set_page_config(
    page_title="Ariaans Assurantiën – Uw Verzekeringsadviseur in Zuid-Limburg",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="collapsed",
    menu_items={"Get help": None, "Report a bug": None, "About": None},
)

init_db()
st.markdown(MAIN_CSS, unsafe_allow_html=True)

# ── Hero ──────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero">
    <div class="hero-badge">⭐ 4.9/5 – 380+ beoordelingen in Zuid-Limburg</div>
    <h1>De slimste keuze voor<br>uw verzekering in<br><span>Zuid-Limburg</span></h1>
    <p>Wij besparen u gemiddeld <strong style="color:#68d391;">€ 312 per jaar</strong>
       door uw verzekeringen te vergelijken én persoonlijk te begeleiden –
       iets dat online vergelijkers nooit kunnen bieden.</p>
    <a href="/Offerte_Aanvragen" class="btn-primary">🚀 Bereken mijn besparing</a>
    <a href="/Contact" class="btn-secondary">📞 Gratis adviesgesprek</a>
</div>
""", unsafe_allow_html=True)

# ── Stats bar ─────────────────────────────────────────────────────────────────
st.markdown("""
<div class="stats-bar">
    <div class="stat-item">
        <div class="stat-number">25+</div>
        <div class="stat-label">Jaar ervaring</div>
    </div>
    <div class="stat-item">
        <div class="stat-number">4.200+</div>
        <div class="stat-label">Tevreden klanten</div>
    </div>
    <div class="stat-item">
        <div class="stat-number">€ 312</div>
        <div class="stat-label">Gem. besparing/jaar</div>
    </div>
    <div class="stat-item">
        <div class="stat-number">48u</div>
        <div class="stat-label">Reactietijd</div>
    </div>
    <div class="stat-item">
        <div class="stat-number">98%</div>
        <div class="stat-label">Klanttevredenheid</div>
    </div>
</div>
""", unsafe_allow_html=True)

# ── Waarom wij winnen van de concurrent ───────────────────────────────────────
st.markdown("""
<div class="section-header">
    <h2>Waarom klanten weggaan bij onze concurrenten</h2>
    <p>Wij hoorden het zelf: wat ontbreekt er bij andere verzekeraars in de regio?</p>
</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns([1, 1], gap="large")
with col1:
    st.markdown("""
    <div class="card">
        <h3 style="color:#c53030;">❌ Wat concurrenten fout doen</h3>
        <div class="usp-item">
            <span class="usp-check" style="color:#fc8181;">✗</span>
            <div class="usp-text">
                <strong>Weken wachten op een offerte</strong>
                <span>Klanten haken af – 67% verwacht binnen 24u reactie</span>
            </div>
        </div>
        <div class="usp-item">
            <span class="usp-check" style="color:#fc8181;">✗</span>
            <div class="usp-text">
                <strong>Geen transparante prijzen online</strong>
                <span>Bezoekers gaan weg zonder contact op te nemen</span>
            </div>
        </div>
        <div class="usp-item">
            <span class="usp-check" style="color:#fc8181;">✗</span>
            <div class="usp-text">
                <strong>Niet bereikbaar buiten kantooruren</strong>
                <span>45% van schademeldingen na 18:00u</span>
            </div>
        </div>
        <div class="usp-item">
            <span class="usp-check" style="color:#fc8181;">✗</span>
            <div class="usp-text">
                <strong>Generiek advies – geen lokale kennis</strong>
                <span>Zuid-Limburg heeft unieke risico's (hellingland, grensregio)</span>
            </div>
        </div>
        <div class="usp-item">
            <span class="usp-check" style="color:#fc8181;">✗</span>
            <div class="usp-text">
                <strong>Complexe voorwaarden, geen uitleg</strong>
                <span>Klanten ontdekken gaten in hun dekking pas bij schade</span>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card">
        <h3 style="color:#276749;">✅ Hoe Ariaans het oplost</h3>
        <div class="usp-item">
            <span class="usp-check">✓</span>
            <div class="usp-text">
                <strong>Offerte binnen 2 uur – direct online</strong>
                <span>Gebruik onze offertetool en ontvang dezelfde dag een voorstel</span>
            </div>
        </div>
        <div class="usp-item">
            <span class="usp-check">✓</span>
            <div class="usp-text">
                <strong>Transparante premie-indicatie direct op de site</strong>
                <span>Geen verrassingen – weet wat u betaalt vóór u belt</span>
            </div>
        </div>
        <div class="usp-item">
            <span class="usp-check">✓</span>
            <div class="usp-text">
                <strong>WhatsApp & avondservice tot 21:00u</strong>
                <span>Schade melden wanneer het u uitkomt</span>
            </div>
        </div>
        <div class="usp-item">
            <span class="usp-check">✓</span>
            <div class="usp-text">
                <strong>Specialist in de Limburgse markt</strong>
                <span>Kennis van lokale risico's en grensoverschrijdende situaties</span>
            </div>
        </div>
        <div class="usp-item">
            <span class="usp-check">✓</span>
            <div class="usp-text">
                <strong>Jaarlijkse gratis dekkingscheck</strong>
                <span>Wij signaleren gaten in uw dekking vóórdat er schade is</span>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ── Verzekeringen producten ────────────────────────────────────────────────────
st.markdown("""
<div class="section-header">
    <h2>Onze verzekeringen</h2>
    <p>Van auto tot bedrijf – alles voor particulieren en ondernemers in Zuid-Limburg</p>
</div>
""", unsafe_allow_html=True)

prod_cols = st.columns(3, gap="medium")
products = [
    ("🚗", "Autoverzekering", "WA, beperkt casco of allrisk – wij vergelijken 12 maatschappijen voor de laagste premie.", "v.a. € 48 / maand"),
    ("🏠", "Woonverzekering", "Inboedel + opstal. Speciaal tarief voor Limburgse woningen met berging en bijgebouwen.", "v.a. € 14 / maand"),
    ("❤️", "Zorgverzekering", "Basisverzekering + aanvullend. Wij vergelijken en regelen de overstap voor u.", "v.a. € 129 / maand"),
    ("💼", "Bedrijfsverzekering", "Aansprakelijkheid, inventaris, rechtsbijstand – op maat voor ZZP'ers en MKB.", "v.a. € 39 / maand"),
    ("✈️", "Reisverzekering", "Doorlopend of per reis – inclusief annuleringsverzekering.", "v.a. € 6 / maand"),
    ("🌿", "Levensverzekering", "Overlijdensrisico, uitvaartverzekering en pensioenadvies.", "Persoonlijk advies"),
]
for i, (icon, title, desc, price) in enumerate(products):
    with prod_cols[i % 3]:
        st.markdown(f"""
        <div class="card" style="margin-bottom:1.25rem;">
            <div class="card-icon">{icon}</div>
            <h3>{title}</h3>
            <p>{desc}</p>
            <div class="card-price">{price}</div>
        </div>
        """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)
col_cta1, col_cta2, col_cta3 = st.columns([1, 2, 1])
with col_cta2:
    st.page_link("pages/1_Verzekeringen.py", label="→ Bekijk alle verzekeringen & voorwaarden")

st.markdown("<br>", unsafe_allow_html=True)

# ── Snelle offerte aanvragen ───────────────────────────────────────────────────
st.markdown("""
<div class="section-header">
    <h2>Vrijblijvend offerte aanvragen</h2>
    <p>Binnen 2 uur telefonisch contact – garantie</p>
</div>
""", unsafe_allow_html=True)

with st.container():
    st.markdown('<div class="form-container">', unsafe_allow_html=True)
    col_f1, col_f2 = st.columns(2)
    with col_f1:
        naam = st.text_input("Uw naam *", placeholder="Jan Janssen")
        email = st.text_input("E-mailadres *", placeholder="jan@email.nl")
        telefoon = st.text_input("Telefoonnummer", placeholder="06 12 34 56 78")
    with col_f2:
        woonplaats = st.text_input("Woonplaats", placeholder="Maastricht")
        verzekering = st.selectbox("Welke verzekering? *", [
            "Selecteer...", "Autoverzekering", "Woonverzekering", "Zorgverzekering",
            "Bedrijfsverzekering", "Reisverzekering", "Levensverzekering", "Meerdere"
        ])
        bericht = st.text_area("Eventuele toelichting", placeholder="Bijv. huidige premie, dekking, bijzonderheden...", height=95)

    if st.button("🚀 Stuur mijn aanvraag – gratis & vrijblijvend", use_container_width=True):
        if not naam or not email or verzekering == "Selecteer...":
            st.error("Vul uw naam, e-mail en gewenste verzekering in.")
        else:
            save_lead(naam, email, telefoon, "", woonplaats, verzekering, bericht, "homepage_form")
            st.success("✅ Bedankt! Wij nemen binnen 2 uur contact met u op.")
            st.balloons()
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ── Testimonials ──────────────────────────────────────────────────────────────
st.markdown("""
<div class="section-header">
    <h2>Wat klanten zeggen</h2>
    <p>Meer dan 380 beoordelingen – gemiddeld 4.9 sterren</p>
</div>
""", unsafe_allow_html=True)

t_cols = st.columns(3, gap="medium")
testimonials = [
    ("\"Eindelijk een adviseur die gewoon uitlegt wat ik koop. Bespaard €280 op mijn auto- en woonverzekering samen.\"",
     "Petra V., Maastricht", "⭐⭐⭐⭐⭐"),
    ("\"Schade gemeld op zaterdagavond via WhatsApp – maandag al afgehandeld. Dat verwacht je niet!\"",
     "Remy K., Heerlen", "⭐⭐⭐⭐⭐"),
    ("\"Als ZZP'er had ik nooit goed nagedacht over aansprakelijkheid. Ariaans heeft alles perfect geregeld.\"",
     "Dorien M., Sittard", "⭐⭐⭐⭐⭐"),
]
for i, (text, author, stars) in enumerate(testimonials):
    with t_cols[i]:
        st.markdown(f"""
        <div class="testimonial">
            <div class="testimonial-stars">{stars}</div>
            <div class="testimonial-text">{text}</div>
            <div class="testimonial-author">— {author}</div>
        </div>
        """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ── Trust section ─────────────────────────────────────────────────────────────
col_t1, col_t2, col_t3 = st.columns([1, 2, 1])
with col_t2:
    st.markdown("""
    <div style="text-align:center; padding: 2rem; background: white; border-radius: 1rem;
                box-shadow: 0 4px 20px rgba(0,0,0,0.06);">
        <h3 style="color:#1a365d; font-size:1.4rem; margin-bottom:1rem;">
            Geregistreerd & gecertificeerd
        </h3>
        <div>
            <span class="trust-badge">🏛️ AFM Vergunning</span>
            <span class="trust-badge">⚖️ KiFiD Klachteninstituut</span>
            <span class="trust-badge">🔒 ISO 27001</span>
            <span class="trust-badge">🤝 Adfiz Lid</span>
            <span class="trust-badge">🏆 Top 10 Adviseur Limburg</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)
st.markdown(footer_html(), unsafe_allow_html=True)
