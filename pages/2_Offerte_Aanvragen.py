import streamlit as st
from database import init_db, save_offerte
from styles import MAIN_CSS, footer_html

st.set_page_config(
    page_title="Offerte Aanvragen – Ariaans Assurantiën",
    page_icon="📋",
    layout="wide",
    initial_sidebar_state="collapsed",
    menu_items={"Get help": None, "Report a bug": None, "About": None},
)

init_db()
st.markdown(MAIN_CSS, unsafe_allow_html=True)

st.markdown("""
<div class="page-hero">
    <h1>📋 Offerte Aanvragen</h1>
    <p>Gratis premie-indicatie in 2 minuten · Geen verplichtingen · Binnen 2 uur reactie</p>
</div>
""", unsafe_allow_html=True)

# ── Selecteer verzekering type ─────────────────────────────────────────────────
st.markdown("""
<div class="section-header">
    <h2>Stap 1 – Kies uw verzekering</h2>
    <p>Onze online calculator geeft direct een indicatie van uw premie</p>
</div>
""", unsafe_allow_html=True)

verzekering_type = st.selectbox(
    "Welke verzekering wilt u berekenen?",
    ["Autoverzekering", "Woonverzekering", "Zorgverzekering",
     "Bedrijfsverzekering", "Reisverzekering", "Levensverzekering"],
    key="offerte_type"
)

st.markdown("<br>", unsafe_allow_html=True)
st.markdown(f"""
<div class="section-header">
    <h2>Stap 2 – Uw {verzekering_type} details</h2>
</div>
""", unsafe_allow_html=True)

# ── Dynamische calculator per type ────────────────────────────────────────────
premie_min = 0.0
premie_max = 0.0
details_parts = []

col_form, col_result = st.columns([3, 2], gap="large")

with col_form:
    if verzekering_type == "Autoverzekering":
        bouwjaar = st.number_input("Bouwjaar auto", min_value=1980, max_value=2025, value=2018)
        merk = st.text_input("Merk & model", placeholder="bijv. Volkswagen Golf")
        dekking = st.selectbox("Gewenste dekking", ["WA", "WA + Beperkt Casco", "Allrisk"])
        leeftijd = st.number_input("Leeftijd bestuurder", min_value=18, max_value=80, value=40)
        schadevrij = st.slider("Schadevrije jaren", 0, 20, 8)
        km_jaar = st.selectbox("Km per jaar", ["< 10.000 km", "10.000 – 20.000 km", "> 20.000 km"])
        details_parts = [f"Auto: {merk} ({bouwjaar})", f"Dekking: {dekking}",
                         f"Leeftijd: {leeftijd}j", f"SF-jaren: {schadevrij}",
                         f"KM/jaar: {km_jaar}"]
        basis = 60 if dekking == "WA" else (85 if dekking == "WA + Beperkt Casco" else 120)
        korting = min(schadevrij * 2.5, 40)
        ouderkorting = 5 if 30 <= leeftijd <= 65 else 0
        premie_min = round(basis - korting - ouderkorting - 5, 0)
        premie_max = round(basis - korting - ouderkorting + 15, 0)

    elif verzekering_type == "Woonverzekering":
        type_woning = st.selectbox("Type woning", ["Appartement", "Tussenwoning", "Hoekwoning", "Vrijstaand", "Boerderij"])
        oppervlak = st.number_input("Woonoppervlak (m²)", min_value=30, max_value=500, value=100)
        inboedel_waarde = st.select_slider("Inboedelwaarde", options=[25000, 35000, 50000, 75000, 100000, 150000], value=50000)
        opstal = st.checkbox("Opstalverzekering toevoegen", value=True)
        glas = st.checkbox("Glasverzekering toevoegen", value=True)
        details_parts = [f"Woning: {type_woning} ({oppervlak}m²)",
                         f"Inboedel: €{inboedel_waarde:,}",
                         f"Opstal: {'ja' if opstal else 'nee'}"]
        basis_inboedel = inboedel_waarde / 4000
        basis_opstal = (oppervlak * 0.08) if opstal else 0
        basis_glas = 3 if glas else 0
        premie_min = round(basis_inboedel + basis_opstal + basis_glas - 2, 0)
        premie_max = round(basis_inboedel + basis_opstal + basis_glas + 5, 0)

    elif verzekering_type == "Zorgverzekering":
        polistype = st.selectbox("Type polis", ["Naturapolis (goedkoopst)", "Combinatiepolis", "Restitutiepolis (vrije keuze)"])
        eigen_risico = st.select_slider("Vrijwillig eigen risico", options=[0, 100, 200, 300, 400, 500], value=0)
        aanvullend = st.selectbox("Aanvullende verzekering", ["Geen", "Basis aanvullend", "Uitgebreid aanvullend", "Compleet"])
        tandverzekering = st.checkbox("Tandverzekering", value=False)
        details_parts = [f"Polis: {polistype}", f"Vrijwillig ER: €{eigen_risico}",
                         f"Aanvullend: {aanvullend}"]
        basis = 135 if "Natura" in polistype else (148 if "Combi" in polistype else 158)
        korting_er = eigen_risico * 0.08
        extra_aanv = {"Geen": 0, "Basis aanvullend": 12, "Uitgebreid aanvullend": 24, "Compleet": 38}[aanvullend]
        extra_tand = 15 if tandverzekering else 0
        premie_min = round(basis - korting_er + extra_aanv + extra_tand - 3, 0)
        premie_max = round(basis - korting_er + extra_aanv + extra_tand + 8, 0)

    elif verzekering_type == "Bedrijfsverzekering":
        type_bedrijf = st.selectbox("Type bedrijf", ["ZZP / Freelancer", "MKB (2–10 medewerkers)", "MKB (11–50 medewerkers)", "Groter bedrijf"])
        branche = st.selectbox("Branche", ["IT / Consultancy", "Bouw / Techniek", "Horeca", "Detailhandel", "Zorg", "Transport", "Overig"])
        omzet = st.select_slider("Jaaromzet", options=["< €50k", "€50k–€150k", "€150k–€500k", "> €500k"], value="€50k–€150k")
        avb = st.checkbox("Aansprakelijkheidsverzekering (AVB)", value=True)
        bav = st.checkbox("Beroepsaansprakelijkheid (BAV)", value=False)
        cyber = st.checkbox("Cyberverzekering", value=False)
        details_parts = [f"Bedrijf: {type_bedrijf}", f"Branche: {branche}", f"Omzet: {omzet}"]
        basis = {"ZZP / Freelancer": 39, "MKB (2–10 medewerkers)": 89, "MKB (11–50 medewerkers)": 189, "Groter bedrijf": 350}[type_bedrijf]
        extra = (30 if bav else 0) + (25 if cyber else 0)
        premie_min = round(basis + extra - 10, 0)
        premie_max = round(basis + extra + 30, 0)

    elif verzekering_type == "Reisverzekering":
        soort = st.selectbox("Soort verzekering", ["Doorlopend (heel jaar)", "Kortlopend (per reis)"])
        gezin = st.selectbox("Wie meeverzekeren?", ["Alleen ikzelf", "Ikzelf + partner", "Gezin (met kinderen)"])
        gebied = st.selectbox("Reisgebied", ["Europa", "Wereld excl. VS/Canada", "Wereld incl. VS/Canada"])
        annulering = st.checkbox("Annuleringsverzekering", value=True)
        details_parts = [f"Soort: {soort}", f"Personen: {gezin}", f"Gebied: {gebied}"]
        basis_pers = {"Alleen ikzelf": 4, "Ikzelf + partner": 6.5, "Gezin (met kinderen)": 9}[gezin]
        basis_gebied = {"Europa": 0, "Wereld excl. VS/Canada": 1.5, "Wereld incl. VS/Canada": 3}[gebied]
        kortlopend_factor = 0 if soort == "Doorlopend (heel jaar)" else -2
        annulering_extra = 4 if annulering else 0
        if soort == "Kortlopend (per reis)":
            premie_min = round(12 + basis_gebied + annulering_extra, 0)
            premie_max = round(25 + basis_gebied + annulering_extra, 0)
        else:
            premie_min = round(basis_pers + basis_gebied + annulering_extra - 1, 0)
            premie_max = round(basis_pers + basis_gebied + annulering_extra + 3, 0)

    else:  # Levensverzekering
        soort_leven = st.selectbox("Type", ["Overlijdensrisicoverzekering (ORV)", "Uitvaartverzekering", "Lijfrenteverzekering"])
        leeftijd_l = st.number_input("Uw leeftijd", min_value=18, max_value=75, value=40)
        roker = st.radio("Rookt u?", ["Nee", "Ja"], horizontal=True)
        verzekerd_bedrag = st.select_slider("Verzekerd bedrag", options=[50000, 100000, 150000, 200000, 300000, 500000], value=200000) if soort_leven == "Overlijdensrisicoverzekering (ORV)" else None
        details_parts = [f"Type: {soort_leven}", f"Leeftijd: {leeftijd_l}j",
                         f"Roker: {roker}"]
        if soort_leven == "Overlijdensrisicoverzekering (ORV)":
            basis = (verzekerd_bedrag / 10000) * (1.2 if leeftijd_l > 50 else 1.0) * (1.5 if roker == "Ja" else 1.0)
            premie_min = round(basis - 2, 2)
            premie_max = round(basis + 5, 2)
        elif soort_leven == "Uitvaartverzekering":
            premie_min = 12 if leeftijd_l < 40 else (18 if leeftijd_l < 55 else 28)
            premie_max = premie_min + 15
        else:
            premie_min = 50
            premie_max = 300

with col_result:
    st.markdown(f"""
    <div class="price-display">
        <div class="from">Uw indicatieve premie</div>
        <div class="amount">€ {int(premie_min)} – {int(premie_max)}</div>
        <div class="period">per maand</div>
    </div>
    <br>
    <div style="background:#fffbeb;border:1px solid #f6e05e;border-radius:0.75rem;padding:1rem;font-size:0.85rem;color:#744210;">
        ⚠️ <strong>Let op:</strong> Dit is een indicatie op basis van uw invoer.
        De definitieve premie bepalen wij samen na een persoonlijk gesprek,
        waarbij wij alle maatschappijen voor u vergelijken.
    </div>
    <br>
    <div style="background:#f0fff4;border:1px solid #9ae6b4;border-radius:0.75rem;padding:1rem;font-size:0.9rem;color:#276749;">
        ✅ <strong>Gemiddelde besparing bij overstap naar Ariaans:</strong><br>
        <span style="font-size:1.5rem;font-weight:800;">€ {int(premie_max * 0.15 * 12)} per jaar</span>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)
st.markdown("""
<div class="section-header">
    <h2>Stap 3 – Uw contactgegevens</h2>
    <p>Wij nemen binnen 2 uur contact op met een op maat gemaakt voorstel</p>
</div>
""", unsafe_allow_html=True)

with st.container():
    st.markdown('<div class="form-container">', unsafe_allow_html=True)
    col_c1, col_c2 = st.columns(2)
    with col_c1:
        o_naam = st.text_input("Uw naam *", key="o_naam", placeholder="Jan Janssen")
        o_email = st.text_input("E-mailadres *", key="o_email", placeholder="jan@email.nl")
        o_tel = st.text_input("Telefoonnummer *", key="o_tel", placeholder="06 12 34 56 78")
    with col_c2:
        o_postcode = st.text_input("Postcode", key="o_postcode", placeholder="6211 AB")
        o_plaats = st.text_input("Woonplaats", key="o_plaats", placeholder="Maastricht")
        o_extra = st.text_area("Extra toelichting", key="o_extra",
                               placeholder="Uw huidige premie, looptijd, bijzonderheden...",
                               height=95)

    akkoord = st.checkbox(
        "Ik ga akkoord dat Ariaans Assurantiën mijn gegevens gebruikt om contact op te nemen. "
        "Mijn gegevens worden niet aan derden verstrekt."
    )

    if st.button("✅ Verstuur mijn offerte-aanvraag – gratis & vrijblijvend", use_container_width=True):
        if not o_naam or not o_email or not o_tel:
            st.error("Vul uw naam, e-mailadres en telefoonnummer in.")
        elif not akkoord:
            st.error("Ga akkoord met de privacyverklaring om uw aanvraag te versturen.")
        else:
            details_str = " | ".join(details_parts)
            save_offerte(o_naam, o_email, o_tel, o_postcode, o_plaats,
                         verzekering_type, details_str, premie_min, premie_max)
            st.success(f"""
            ✅ **Uw aanvraag is ontvangen!**

            Wij bellen u **binnen 2 uur** op **{o_tel}** met een persoonlijk voorstel
            voor uw {verzekering_type}. Indicatie: **€ {int(premie_min)} – {int(premie_max)} / maand**.

            Ter bevestiging sturen wij ook een e-mail naar {o_email}.
            """)
            st.balloons()
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ── Garanties ─────────────────────────────────────────────────────────────────
g_cols = st.columns(3, gap="medium")
garanties = [
    ("⏱️", "2-uur garantie", "Geen reactie binnen 2 uur? Dan bieden wij u een extra korting van €25 op uw eerste premie."),
    ("🔒", "Geen verplichtingen", "Een offerte-aanvraag is altijd gratis en vrijblijvend. U beslist zelf of u overstapt."),
    ("🤝", "Persoonlijke adviseur", "U krijgt één vaste contactpersoon die uw dossier kent en altijd bereikbaar is."),
]
for i, (icon, title, text) in enumerate(garanties):
    with g_cols[i]:
        st.markdown(f"""
        <div class="card" style="text-align:center;">
            <div class="card-icon">{icon}</div>
            <h3>{title}</h3>
            <p>{text}</p>
        </div>
        """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)
st.markdown(footer_html(), unsafe_allow_html=True)
