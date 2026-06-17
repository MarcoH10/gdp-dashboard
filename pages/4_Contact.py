import streamlit as st
from database import init_db, save_lead, save_afspraak
from styles import MAIN_CSS, footer_html

st.set_page_config(
    page_title="Contact – Ariaans Assurantiën",
    page_icon="📞",
    layout="wide",
    initial_sidebar_state="collapsed",
    menu_items={"Get help": None, "Report a bug": None, "About": None},
)

init_db()
st.markdown(MAIN_CSS, unsafe_allow_html=True)

st.markdown("""
<div class="page-hero">
    <h1>📞 Contact & Afspraak</h1>
    <p>Bereikbaar via telefoon, WhatsApp, e-mail of gewoon langskomen</p>
</div>
""", unsafe_allow_html=True)

# ── Contactopties ─────────────────────────────────────────────────────────────
st.markdown("""
<div class="section-header">
    <h2>Hoe wilt u contact?</h2>
</div>
""", unsafe_allow_html=True)

c_cols = st.columns(4, gap="medium")
opties = [
    ("📞", "Bellen", "043 – 123 45 67", "Ma–Vr 8:30–17:30\nAvond ma/wo/do tot 21u"),
    ("💬", "WhatsApp", "06 – 12 34 56 78", "Stuur een bericht,\nwe reageren binnen 1u"),
    ("✉️", "E-mail", "info@ariaans-assurantien.nl", "Reactie binnen\n4 kantooruren"),
    ("📍", "Langskomen", "Vrijthof 12, Maastricht", "Op afspraak ook\nbuiten kantooruren"),
]
for i, (icon, titel, contact, info) in enumerate(opties):
    with c_cols[i]:
        st.markdown(f"""
        <div class="card" style="text-align:center;border-top:4px solid #3182ce;">
            <div style="font-size:2.5rem;margin-bottom:0.75rem;">{icon}</div>
            <h3 style="margin-bottom:0.25rem;">{titel}</h3>
            <div style="color:#3182ce;font-weight:700;font-size:0.9rem;margin-bottom:0.5rem;">{contact}</div>
            <div style="color:#718096;font-size:0.82rem;white-space:pre-line;">{info}</div>
        </div>
        """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ── Tabs: Afspraak / Contact / Schade ─────────────────────────────────────────
tab1, tab2, tab3 = st.tabs(["📅 Afspraak Inplannen", "📝 Contactformulier", "🚨 Schade Melden"])

with tab1:
    st.markdown("### Gratis adviesgesprek – op kantoor, bij u thuis of online")
    col_a1, col_a2 = st.columns(2, gap="large")
    with col_a1:
        a_naam = st.text_input("Uw naam *", key="a_naam", placeholder="Jan Janssen")
        a_email = st.text_input("E-mailadres *", key="a_email", placeholder="jan@email.nl")
        a_tel = st.text_input("Telefoonnummer *", key="a_tel", placeholder="06 12 34 56 78")
    with col_a2:
        a_datum = st.date_input("Gewenste datum *", key="a_datum")
        a_tijd = st.selectbox("Gewenste tijd *", [
            "08:30", "09:00", "09:30", "10:00", "10:30", "11:00", "11:30",
            "13:00", "13:30", "14:00", "14:30", "15:00", "15:30", "16:00",
            "16:30", "17:00", "Avond 18:00", "Avond 19:00", "Avond 20:00"
        ], key="a_tijd")
        a_soort = st.selectbox("Soort gesprek", [
            "Adviesgesprek nieuw klant",
            "Jaarlijkse dekkingscheck",
            "Schade bespreken",
            "Bedrijfsrisico-scan",
            "Online (Teams/Zoom)",
        ], key="a_soort")
        a_notities = st.text_area("Toelichting", key="a_notities",
                                  placeholder="Waar gaat het gesprek over? Uw huidige situatie...", height=80)

    if st.button("📅 Afspraak Inplannen – Bevestiging per e-mail", use_container_width=True, key="btn_afspraak"):
        if not a_naam or not a_email or not a_tel:
            st.error("Vul naam, e-mail en telefoonnummer in.")
        else:
            save_afspraak(a_naam, a_email, a_tel, str(a_datum), a_tijd, a_soort, a_notities)
            st.success(f"""
            ✅ **Afspraak aangevraagd!**

            Wij bevestigen uw afspraak op **{a_datum.strftime('%d %B %Y')} om {a_tijd}**
            via e-mail ({a_email}) en WhatsApp. Als het gewenste tijdstip niet beschikbaar is,
            nemen wij contact op om een alternatief te plannen.

            Tot ziens! 👋
            """)

with tab2:
    st.markdown("### Stel uw vraag of stuur een bericht")
    col_c1, col_c2 = st.columns(2, gap="large")
    with col_c1:
        c_naam = st.text_input("Uw naam *", key="c_naam", placeholder="Jan Janssen")
        c_email = st.text_input("E-mailadres *", key="c_email", placeholder="jan@email.nl")
        c_tel = st.text_input("Telefoonnummer", key="c_tel", placeholder="06 12 34 56 78 (optioneel)")
    with col_c2:
        c_onderwerp = st.selectbox("Onderwerp", [
            "Offerte aanvragen",
            "Vraag over bestaande polis",
            "Schade melden",
            "Klacht",
            "Samenwerking / verwijzing",
            "Anders",
        ], key="c_onderwerp")
        c_bericht = st.text_area("Uw bericht *", key="c_bericht",
                                 placeholder="Beschrijf uw vraag of situatie...", height=140)

    if st.button("✉️ Verstuur bericht – reactie binnen 4 uur", use_container_width=True, key="btn_contact"):
        if not c_naam or not c_email or not c_bericht:
            st.error("Vul naam, e-mail en bericht in.")
        else:
            save_lead(c_naam, c_email, c_tel, "", "", c_onderwerp, c_bericht, "contactformulier")
            st.success("✅ Uw bericht is ontvangen. Wij reageren binnen 4 kantooruren.")

with tab3:
    st.markdown("### 🚨 Schade melden – ook buiten kantooruren")
    st.info("""
    **Spoed? Bel direct: 043 – 123 45 67**
    Avond/weekend: WhatsApp 06 – 12 34 56 78

    Wij regelen de eerste opvang en zetten uw schademelding direct door naar uw maatschappij.
    """)

    col_s1, col_s2 = st.columns(2, gap="large")
    with col_s1:
        s_naam = st.text_input("Uw naam *", key="s_naam")
        s_email = st.text_input("E-mailadres *", key="s_email")
        s_tel = st.text_input("Telefoonnummer *", key="s_tel")
        s_polisnr = st.text_input("Polisnummer (indien bekend)", key="s_polisnr")
    with col_s2:
        s_type = st.selectbox("Type schade *", [
            "Auto-schade", "Brand", "Inbraak/diefstal", "Water/lekkage",
            "Storm", "Glasschade", "Persoonlijke schade", "Bedrijfsschade", "Anders"
        ], key="s_type")
        s_datum = st.date_input("Datum van schade *", key="s_datum")
        s_beschrijving = st.text_area("Beschrijf de schade *", key="s_beschrijving",
                                      placeholder="Wat is er gebeurd? Wat is de geschatte omvang?",
                                      height=100)

    if st.button("🚨 Verstuur Schademelding", use_container_width=True, key="btn_schade"):
        if not s_naam or not s_email or not s_tel or not s_beschrijving:
            st.error("Vul alle verplichte velden in.")
        else:
            bericht = f"SCHADEMELDING | Type: {s_type} | Datum: {s_datum} | {s_beschrijving}"
            if s_polisnr:
                bericht = f"Polisnr: {s_polisnr} | " + bericht
            save_lead(s_naam, s_email, s_tel, "", "", s_type, bericht, "schademelding")
            st.success("""
            ✅ **Schademelding ontvangen!**

            Wij nemen **binnen 1 uur** contact met u op om de schade verder te bespreken.
            Heeft u foto's? Stuur ze via WhatsApp naar **06 – 12 34 56 78**.
            """)

st.markdown("<br>", unsafe_allow_html=True)

# ── FAQ ────────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="section-header">
    <h2>Veelgestelde vragen</h2>
</div>
""", unsafe_allow_html=True)

with st.expander("Hoe snel ontvang ik een offerte?"):
    st.write("Wij garanderen contact binnen 2 uur op werkdagen. Een definitief voorstel ontvangt u dezelfde of volgende werkdag.")

with st.expander("Kost het advies iets?"):
    st.write("Nee. Een eerste adviesgesprek en offerte zijn altijd gratis en vrijblijvend. Wij verdienen onze provisie bij de verzekeringsmaatschappij – u betaalt daarvoor niet extra.")

with st.expander("Kan ik mijn bestaande verzekeringen laten controleren?"):
    st.write("Absoluut. Onze gratis dekkingscheck duurt 30 minuten en laat u precies zien of u goed verzekerd bent – en waar u eventueel te veel betaalt.")

with st.expander("Ik werk in België/Duitsland – kunnen jullie mij helpen?"):
    st.write("Ja! Wij zijn specialist in grensoverschrijdende situaties. Denk aan zorgverzekering, auto's met buitenlands kenteken, en aansprakelijkheid over de grens.")

with st.expander("Hoe meld ik een schade buiten kantooruren?"):
    st.write("Via WhatsApp op 06 – 12 34 56 78, ook 's avonds en in het weekend. Voor spoed is ons noodnummer 24/7 beschikbaar: 085 – 000 11 22.")

with st.expander("Bij welke maatschappijen zijn jullie tussenpersoon?"):
    st.write("Wij werken met meer dan 40 maatschappijen, waaronder Centraal Beheer, Nationale Nederlanden, Interpolis, AEGON, ASR, Allianz, Univé, Hema Verzekeringen, Ditzo en vele anderen.")

st.markdown("<br>", unsafe_allow_html=True)
st.markdown(footer_html(), unsafe_allow_html=True)
