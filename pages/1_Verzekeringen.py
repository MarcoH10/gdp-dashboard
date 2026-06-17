import streamlit as st
from styles import MAIN_CSS, footer_html
from database import init_db

st.set_page_config(
    page_title="Verzekeringen – Ariaans Assurantiën",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="collapsed",
    menu_items={"Get help": None, "Report a bug": None, "About": None},
)

init_db()
st.markdown(MAIN_CSS, unsafe_allow_html=True)

st.markdown("""
<div class="page-hero">
    <h1>🛡️ Onze Verzekeringen</h1>
    <p>Transparante voorwaarden · Eerlijke premies · Lokaal advies in Zuid-Limburg</p>
</div>
""", unsafe_allow_html=True)

# ── Waarom vergelijken niet genoeg is ─────────────────────────────────────────
st.markdown("""
<div class="section-header">
    <h2>Waarom online vergelijken niet genoeg is</h2>
    <p>Vergelijkingssites laten maximaal 30% van de markt zien. Wij vergelijken 40+ maatschappijen – ook exclusieve aanbieders.</p>
</div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3, gap="medium")
with col1:
    st.markdown("""
    <div class="card" style="border-top: 4px solid #3182ce;">
        <div style="font-size:2rem;margin-bottom:0.75rem;">🔍</div>
        <h3>40+ Maatschappijen</h3>
        <p>Wij vergelijken bij meer aanbieders dan welke site ook – inclusief regionale en exclusieve aanbieders.</p>
    </div>""", unsafe_allow_html=True)
with col2:
    st.markdown("""
    <div class="card" style="border-top: 4px solid #38a169;">
        <div style="font-size:2rem;margin-bottom:0.75rem;">🤝</div>
        <h3>Persoonlijk Advies</h3>
        <p>Een algoritme snapt uw situatie niet. Wij wel. Uw gezin, uw bedrijf, uw risico – uw maatwerkoplossing.</p>
    </div>""", unsafe_allow_html=True)
with col3:
    st.markdown("""
    <div class="card" style="border-top: 4px solid #805ad5;">
        <div style="font-size:2rem;margin-bottom:0.75rem;">📋</div>
        <h3>Jaarlijkse Check</h3>
        <p>Uw situatie verandert – uw verzekeringen moeten meegroeien. Wij checken elk jaar of u nog optimaal verzekerd bent.</p>
    </div>""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ── Product tabbladen ──────────────────────────────────────────────────────────
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "🚗 Auto", "🏠 Wonen", "❤️ Zorg", "💼 Bedrijf", "✈️ Reis", "🌿 Leven"
])

with tab1:
    col_a, col_b = st.columns([3, 2], gap="large")
    with col_a:
        st.markdown("### 🚗 Autoverzekering")
        st.markdown("""
        **Drie dekkingsniveaus – wij adviseren welke bij uw auto past:**

        | Dekking | WA | Beperkt Casco | Allrisk |
        |---|---|---|---|
        | Schade aan anderen | ✅ | ✅ | ✅ |
        | Brand & diefstal | ❌ | ✅ | ✅ |
        | Storm & overstroming | ❌ | ✅ | ✅ |
        | Eigen schuld schade | ❌ | ❌ | ✅ |
        | Inzittendenverzekering | ➕ optie | ➕ optie | ➕ optie |
        | Rechtsbijstand | ➕ optie | ➕ optie | ➕ optie |

        **Speciaal voor Zuid-Limburg:**
        - Grensoverschrijdend rijden (B, D) zonder meerkosten
        - Camperverzekering & oldtimers
        - Elektrisch rijden – laagste premie in de regio
        """)
    with col_b:
        st.markdown("""
        <div class="price-display">
            <div class="from">Premie-indicatie</div>
            <div class="amount">€ 48</div>
            <div class="period">per maand (WA)</div>
        </div>
        <br>
        <div class="card">
            <strong>Gemiddelde besparing bij overstap:</strong><br>
            <span style="font-size:1.8rem;font-weight:800;color:#38a169;">€ 187 / jaar</span><br>
            <small style="color:#718096;">Gebaseerd op 2024 klantgegevens</small>
        </div>
        """, unsafe_allow_html=True)
        if st.button("🚀 Offerte Autoverzekering", use_container_width=True, key="btn_auto"):
            st.switch_page("pages/2_Offerte_Aanvragen.py")

with tab2:
    col_a, col_b = st.columns([3, 2], gap="large")
    with col_a:
        st.markdown("### 🏠 Woonverzekering")
        st.markdown("""
        **Combineer inboedel + opstal en bespaar tot 15%:**

        **Inboedelverzekering** – dekt uw spullen bij:
        - Brand, blikseminslag, explosie
        - Storm, water, regen
        - Inbraak en diefstal
        - Aansprakelijkheid (optioneel)

        **Opstalverzekering** – beschermt uw woning bij:
        - Structurele schade (storm, brand)
        - Lekkage en vorstschade
        - Eigen glasverzekering inbegrepen

        **Limburgse bijzonderheden:**
        Woning op helling, boerderij of monumentaal pand?
        Wij hebben hiervoor speciaal maatwerk.
        """)
    with col_b:
        st.markdown("""
        <div class="price-display">
            <div class="from">Combinatie inboedel + opstal</div>
            <div class="amount">€ 24</div>
            <div class="period">per maand</div>
        </div>
        <br>
        <div class="card">
            <strong>Gratis dekkingscheck:</strong><br>
            Wij controleren of uw inboedelwaarde nog klopt.<br>
            <small style="color:#718096;">70% van Nederlanders is onderverzekerd!</small>
        </div>
        """, unsafe_allow_html=True)
        if st.button("🚀 Offerte Woonverzekering", use_container_width=True, key="btn_woon"):
            st.switch_page("pages/2_Offerte_Aanvragen.py")

with tab3:
    col_a, col_b = st.columns([3, 2], gap="large")
    with col_a:
        st.markdown("### ❤️ Zorgverzekering")
        st.markdown("""
        **Zorgverzekering – elk jaar opnieuw de beste keuze:**

        Wij vergelijken jaarlijks (november/december) alle zorgverzekeraars
        voor u en adviseren welke het beste bij uw gebruik past.

        **Basisverzekering:**
        - Naturapolis vs. restitutiepolis – wij leggen het verschil uit
        - Eigen risico: € 385 (verplicht) – wil u vrijwillig meer nemen?

        **Aanvullende verzekering:**
        - Tandzorg (60%, 75%, 100% vergoeding)
        - Fysiotherapie (1–18 behandelingen)
        - Brillen en lenzen
        - Alternatieve geneeskunde

        **Grenswerkers en expats:**
        Wij zijn specialist in zorg voor grenswerkers (B/D).
        """)
    with col_b:
        st.markdown("""
        <div class="price-display">
            <div class="from">Basisverzekering v.a.</div>
            <div class="amount">€ 129</div>
            <div class="period">per maand</div>
        </div>
        <br>
        <div class="card">
            <strong>Overstapservice gratis:</strong><br>
            Wij regelen de hele overstap voor u – van opzegging tot nieuwe polis.<br>
            <small style="color:#718096;">Deadline overstap: 31 december</small>
        </div>
        """, unsafe_allow_html=True)
        if st.button("🚀 Zorgadvies aanvragen", use_container_width=True, key="btn_zorg"):
            st.switch_page("pages/2_Offerte_Aanvragen.py")

with tab4:
    col_a, col_b = st.columns([3, 2], gap="large")
    with col_a:
        st.markdown("### 💼 Bedrijfsverzekering")
        st.markdown("""
        **Voor ZZP'ers, MKB en grote bedrijven in Zuid-Limburg:**

        **Verzekeringspakket op maat:**
        - **Bedrijfsaansprakelijkheid (AVB)** – beschermt u als iemand schade lijdt
        - **Beroepsaansprakelijkheid (BAV)** – voor fouten in uw dienstverlening
        - **Inventaris & goederen** – spullen, machines, voorraad
        - **Bedrijfsschade** – omzetdervings bij brand of ramp
        - **Rechtsbijstand** – juridisch advies en procesbegeleiding
        - **Cyber** – steeds belangrijker voor elk bedrijf
        - **Bestuurdersaansprakelijkheid (D&O)** – voor directeuren

        **Wij werken met:**
        Horeca, bouw, zorg, detailhandel, IT, transport en meer.
        """)
    with col_b:
        st.markdown("""
        <div class="price-display">
            <div class="from">ZZP-pakket v.a.</div>
            <div class="amount">€ 39</div>
            <div class="period">per maand</div>
        </div>
        <br>
        <div class="card">
            <strong>Gratis bedrijfsrisico-scan:</strong><br>
            Wij analyseren uw risico's in 30 minuten.<br>
            <small style="color:#718096;">Beschikbaar op ons kantoor of online</small>
        </div>
        """, unsafe_allow_html=True)
        if st.button("🚀 Bedrijfsadvies aanvragen", use_container_width=True, key="btn_bedrijf"):
            st.switch_page("pages/2_Offerte_Aanvragen.py")

with tab5:
    col_a, col_b = st.columns([3, 2], gap="large")
    with col_a:
        st.markdown("### ✈️ Reisverzekering")
        st.markdown("""
        **Zorgeloos op reis – ook voor grensoverschrijdend werk:**

        **Doorlopende reisverzekering (aanbevolen):**
        - Onbeperkt reizen per jaar
        - Annulering inbegrepen (optie)
        - Medische kosten wereldwijd
        - Repatriëring

        **Kortlopende reisverzekering:**
        - Per vakantie of zakenreis
        - Europa of werelddekking
        - Kostbaar bezit meeverzekeren

        **Speciaal voor grenswerkers:**
        Woon u in Nederland maar werkt u in België of Duitsland?
        Wij kennen de valkuilen.
        """)
    with col_b:
        st.markdown("""
        <div class="price-display">
            <div class="from">Doorlopend v.a.</div>
            <div class="amount">€ 6</div>
            <div class="period">per maand (gezin)</div>
        </div>
        <br>
        <div class="card">
            <strong>Tip:</strong><br>
            Een doorlopende verzekering is al voordeliger bij 2+ reizen per jaar.<br>
            <small style="color:#718096;">Inclusief wintersporten optie</small>
        </div>
        """, unsafe_allow_html=True)
        if st.button("🚀 Reis-offerte aanvragen", use_container_width=True, key="btn_reis"):
            st.switch_page("pages/2_Offerte_Aanvragen.py")

with tab6:
    col_a, col_b = st.columns([3, 2], gap="large")
    with col_a:
        st.markdown("### 🌿 Levensverzekering & Pensioen")
        st.markdown("""
        **Zekerheid voor uzelf en uw dierbaren:**

        **Overlijdensrisicoverzekering (ORV):**
        - Hypotheek afdekken bij overlijden partner
        - Uitkering voor uw kinderen
        - Aflossingsvrij of annuïtair

        **Uitvaartverzekering:**
        - Natura of kapitaal
        - Wij vergelijken alle uitvaartverzekeraars

        **Pensioenadvies:**
        - ZZP-pensioen (lijfrente, banksparen)
        - Pensioenanalyse bij werkgeverswissel
        - Pensioenkloof in kaart brengen

        **Vermogensopbouw:**
        - Beleggen voor later
        - Studiespaarverzekering voor kinderen
        """)
    with col_b:
        st.markdown("""
        <div class="price-display">
            <div class="from">ORV v.a.</div>
            <div class="amount">€ 12</div>
            <div class="period">per maand</div>
        </div>
        <br>
        <div class="card">
            <strong>Persoonlijk gesprek:</strong><br>
            Levensverzekering is maatwerk. Wij nemen de tijd voor een gratis gesprek.<br>
            <small style="color:#718096;">Op kantoor, bij u thuis of online</small>
        </div>
        """, unsafe_allow_html=True)
        if st.button("🚀 Levensadvies aanvragen", use_container_width=True, key="btn_leven"):
            st.switch_page("pages/2_Offerte_Aanvragen.py")

st.markdown("<br>", unsafe_allow_html=True)

# ── Vergelijkingstabel Ariaans vs concurrenten ────────────────────────────────
st.markdown("""
<div class="section-header">
    <h2>Ariaans vs. de concurrentie</h2>
    <p>Bekijk objectief wat ons onderscheidt van andere adviseurs en online platforms</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="compare-table">
    <div class="compare-row">
        <div>Dienst / kenmerk</div>
        <div>Ariaans Assurantiën</div>
        <div>Andere kantoren / online</div>
    </div>
    <div class="compare-row">
        <div>Offerte binnen 2 uur</div>
        <div class="check">✓ Gegarandeerd</div>
        <div class="cross">✗ Vaak 3–5 werkdagen</div>
    </div>
    <div class="compare-row">
        <div>40+ maatschappijen vergelijken</div>
        <div class="check">✓ Altijd</div>
        <div class="cross">✗ Gemiddeld 5–10</div>
    </div>
    <div class="compare-row">
        <div>Avondservice (tot 21u)</div>
        <div class="check">✓ Ja</div>
        <div class="cross">✗ Nee</div>
    </div>
    <div class="compare-row">
        <div>WhatsApp contact</div>
        <div class="check">✓ Ja</div>
        <div class="cross">✗ Zelden</div>
    </div>
    <div class="compare-row">
        <div>Gratis jaarlijkse dekkingscheck</div>
        <div class="check">✓ Inbegrepen</div>
        <div class="cross">✗ Niet standaard</div>
    </div>
    <div class="compare-row">
        <div>Specialist grenswerkers (B/D)</div>
        <div class="check">✓ Ja</div>
        <div class="cross">✗ Nee</div>
    </div>
    <div class="compare-row">
        <div>Lokaal kantoor Zuid-Limburg</div>
        <div class="check">✓ Maastricht & Heerlen</div>
        <div class="cross">✗ Vaak centraal/online only</div>
    </div>
    <div class="compare-row">
        <div>Transparante premie-indicatie</div>
        <div class="check">✓ Direct op de site</div>
        <div class="cross">✗ Alleen na contact</div>
    </div>
    <div class="compare-row">
        <div>KiFiD klachteninstituut</div>
        <div class="check">✓ Aangesloten</div>
        <div class="cross">~ Niet altijd</div>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)
col_btn1, col_btn2, col_btn3 = st.columns([1, 2, 1])
with col_btn2:
    if st.button("🚀 Gratis vergelijking aanvragen – geen verplichtingen", use_container_width=True):
        st.switch_page("pages/2_Offerte_Aanvragen.py")

st.markdown("<br>", unsafe_allow_html=True)
st.markdown(footer_html(), unsafe_allow_html=True)
