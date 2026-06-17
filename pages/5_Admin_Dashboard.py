import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, date
from database import init_db, get_leads, get_offertes, get_afspraken, get_statistieken, update_lead_status
from styles import MAIN_CSS

st.set_page_config(
    page_title="Admin CRM – Ariaans Assurantiën",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed",
    menu_items={"Get help": None, "Report a bug": None, "About": None},
)

init_db()
st.markdown(MAIN_CSS, unsafe_allow_html=True)

# ── Eenvoudige toegangsbeveiliging ────────────────────────────────────────────
if "admin_ok" not in st.session_state:
    st.session_state.admin_ok = False

if not st.session_state.admin_ok:
    st.markdown("""
    <div style="max-width:400px;margin:4rem auto;">
        <div style="background:white;border-radius:1.25rem;padding:2.5rem;
                    box-shadow:0 8px 40px rgba(0,0,0,0.12);text-align:center;">
            <div style="font-size:3rem;margin-bottom:1rem;">🔐</div>
            <h2 style="color:#1a365d;margin-bottom:0.5rem;">Admin Toegang</h2>
            <p style="color:#718096;margin-bottom:1.5rem;">Alleen voor Ariaans medewerkers</p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    col_l, col_m, col_r = st.columns([1, 2, 1])
    with col_m:
        wachtwoord = st.text_input("Wachtwoord", type="password", key="admin_pw")
        if st.button("Inloggen", use_container_width=True):
            if wachtwoord == "ariaans2025":
                st.session_state.admin_ok = True
                st.rerun()
            else:
                st.error("Onjuist wachtwoord.")
    st.stop()

# ── Dashboard header ───────────────────────────────────────────────────────────
col_h1, col_h2 = st.columns([3, 1])
with col_h1:
    st.markdown("""
    <h1 style="color:#1a365d;font-size:2rem;font-weight:800;margin-bottom:0.25rem;">
        📊 CRM Dashboard – Ariaans Assurantiën
    </h1>
    <p style="color:#718096;">Leadbeheer · Offertes · Afspraken · Conversie-analyse</p>
    """, unsafe_allow_html=True)
with col_h2:
    if st.button("🚪 Uitloggen"):
        st.session_state.admin_ok = False
        st.rerun()

st.divider()

# ── Live statistieken ─────────────────────────────────────────────────────────
stats = get_statistieken()
now = datetime.now()
maand_naam = now.strftime("%B %Y").capitalize()

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-value">{stats['totaal_leads']}</div>
        <div class="metric-label">Totaal Leads</div>
        <div class="metric-delta">Alle tijd</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="metric-card" style="border-top-color:#f6ad55;">
        <div class="metric-value" style="color:#b7791f;">{stats['nieuwe_leads']}</div>
        <div class="metric-label">Nieuwe Leads</div>
        <div class="metric-delta">Actie vereist</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
    <div class="metric-card" style="border-top-color:#38a169;">
        <div class="metric-value" style="color:#276749;">{stats['klanten_geworden']}</div>
        <div class="metric-label">Nieuwe Klanten</div>
        <div class="metric-delta">Doel: 50/maand</div>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown(f"""
    <div class="metric-card" style="border-top-color:#805ad5;">
        <div class="metric-value" style="color:#553c9a;">{stats['conversie_ratio']}%</div>
        <div class="metric-label">Conversieratio</div>
        <div class="metric-delta">Lead → Klant</div>
    </div>
    """, unsafe_allow_html=True)

with col5:
    st.markdown(f"""
    <div class="metric-card" style="border-top-color:#ed8936;">
        <div class="metric-value" style="color:#c05621;">{stats['afspraken']}</div>
        <div class="metric-label">Afspraken</div>
        <div class="metric-delta">Gepland</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ── Maanddoel voortgang ────────────────────────────────────────────────────────
leads_dm = [r for r in get_leads() if r["aangemaakt_op"].startswith(now.strftime("%Y-%m"))]
klanten_dm = [r for r in leads_dm if r["status"] == "klant_geworden"]
doel = 50
gerealiseerd = len(klanten_dm)
pct = min(int(gerealiseerd / doel * 100), 100)
rest = max(doel - gerealiseerd, 0)

col_doel, col_leads_m = st.columns([2, 3], gap="large")
with col_doel:
    st.markdown(f"""
    <div style="background:white;border-radius:1rem;padding:1.5rem;
                box-shadow:0 4px 20px rgba(0,0,0,0.06);">
        <h3 style="color:#1a365d;font-size:1.1rem;margin-bottom:1rem;">
            🎯 Maanddoel – {maand_naam}
        </h3>
        <div style="display:flex;justify-content:space-between;margin-bottom:0.5rem;">
            <span style="font-weight:600;color:#2d3748;">{gerealiseerd} nieuwe klanten</span>
            <span style="color:#718096;">Doel: {doel}</span>
        </div>
        <div class="progress-container">
            <div class="progress-fill" style="width:{pct}%;"></div>
        </div>
        <div style="margin-top:0.75rem;font-size:0.85rem;color:#718096;">
            Nog <strong>{rest}</strong> klanten nodig voor het maanddoel.
            Leads deze maand: <strong>{len(leads_dm)}</strong>
        </div>
        <div style="margin-top:1rem;padding:0.75rem;background:#f0fff4;border-radius:0.5rem;
                    font-size:0.85rem;color:#276749;">
            💡 <strong>Tip:</strong> Bel vandaag de {stats['nieuwe_leads']} onbehandelde leads –
            gemiddeld zet 35% over naar klant bij eerste contact.
        </div>
    </div>
    """, unsafe_allow_html=True)

with col_leads_m:
    leads_per_maand = stats["leads_per_maand"][::-1]
    if leads_per_maand:
        df_lpm = pd.DataFrame(leads_per_maand)
        df_lpm["maand_label"] = df_lpm["maand"].apply(
            lambda m: datetime.strptime(m, "%Y-%m").strftime("%b '%y")
        )
        fig = px.bar(df_lpm, x="maand_label", y="aantal",
                     title="Leads per maand",
                     color_discrete_sequence=["#3182ce"],
                     labels={"maand_label": "Maand", "aantal": "Aantal leads"})
        fig.add_hline(y=50, line_dash="dash", line_color="#38a169",
                      annotation_text="Doel (50)", annotation_position="top right")
        fig.update_layout(
            plot_bgcolor="white", paper_bgcolor="white",
            font_family="Inter", title_font_size=14,
            margin=dict(l=0, r=0, t=40, b=0), height=220
        )
        st.plotly_chart(fig, use_container_width=True)

st.markdown("<br>", unsafe_allow_html=True)

# ── Tabs: Leads / Offertes / Afspraken / Analyse ──────────────────────────────
tab_leads, tab_offertes, tab_afspraken, tab_analyse = st.tabs([
    "📋 Leads Beheer", "📄 Offertes", "📅 Afspraken", "📈 Analyse"
])

with tab_leads:
    col_filter1, col_filter2, col_filter3 = st.columns([2, 2, 1])
    with col_filter1:
        filter_status = st.selectbox("Filter op status", [
            "Alle", "nieuw", "in_behandeling", "offerte_verstuurd",
            "klant_geworden", "niet_geinteresseerd"
        ])
    with col_filter2:
        filter_type = st.selectbox("Filter op verzekering", [
            "Alle", "Autoverzekering", "Woonverzekering", "Zorgverzekering",
            "Bedrijfsverzekering", "Reisverzekering", "Levensverzekering", "Meerdere"
        ])
    with col_filter3:
        st.markdown("<br>", unsafe_allow_html=True)
        refresh = st.button("🔄 Verversen")

    leads = get_leads(status=None if filter_status == "Alle" else filter_status)

    if filter_type != "Alle":
        leads = [l for l in leads if l["verzekering_type"] == filter_type]

    if not leads:
        st.info("Geen leads gevonden met de huidige filters.")
    else:
        df_leads = pd.DataFrame(leads)
        st.markdown(f"**{len(df_leads)} leads gevonden**")

        status_kleuren = {
            "nieuw": "🔵",
            "in_behandeling": "🟡",
            "offerte_verstuurd": "🟠",
            "klant_geworden": "🟢",
            "niet_geinteresseerd": "🔴",
        }

        for _, row in df_leads.iterrows():
            with st.expander(
                f"{status_kleuren.get(row['status'], '⚪')} {row['naam']} – "
                f"{row['verzekering_type']} – {row['woonplaats']} – "
                f"{row['aangemaakt_op'][:16]}"
            ):
                col_info, col_actions = st.columns([3, 2])
                with col_info:
                    st.markdown(f"""
                    **Naam:** {row['naam']}
                    **E-mail:** {row['email']}
                    **Telefoon:** {row['telefoon'] or '–'}
                    **Postcode:** {row['postcode'] or '–'} {row['woonplaats'] or ''}
                    **Verzekering:** {row['verzekering_type']}
                    **Bron:** {row['bron']}
                    **Bericht:** {row['bericht'] or '–'}
                    **Aangemaakt:** {row['aangemaakt_op']}
                    """)
                with col_actions:
                    nieuwe_status = st.selectbox(
                        "Status wijzigen",
                        ["nieuw", "in_behandeling", "offerte_verstuurd",
                         "klant_geworden", "niet_geinteresseerd"],
                        index=["nieuw", "in_behandeling", "offerte_verstuurd",
                               "klant_geworden", "niet_geinteresseerd"].index(row["status"]),
                        key=f"status_{row['id']}"
                    )
                    if st.button("Opslaan", key=f"save_{row['id']}"):
                        update_lead_status(row["id"], nieuwe_status)
                        st.success(f"Status gewijzigd naar: {nieuwe_status}")
                        st.rerun()

                    st.markdown(f"""
                    <div style="margin-top:0.75rem;">
                        <a href="mailto:{row['email']}" style="display:inline-block;
                           background:#ebf8ff;color:#2b6cb0;padding:0.4rem 0.9rem;
                           border-radius:0.5rem;text-decoration:none;font-size:0.85rem;font-weight:600;
                           margin-right:0.5rem;">✉️ E-mail</a>
                        {'<a href="tel:' + str(row["telefoon"]) + '" style="display:inline-block;background:#f0fff4;color:#276749;padding:0.4rem 0.9rem;border-radius:0.5rem;text-decoration:none;font-size:0.85rem;font-weight:600;">📞 Bellen</a>' if row["telefoon"] else ""}
                    </div>
                    """, unsafe_allow_html=True)

with tab_offertes:
    offertes = get_offertes()
    if not offertes:
        st.info("Nog geen offerte-aanvragen.")
    else:
        df_off = pd.DataFrame(offertes)
        df_display = df_off[["naam", "email", "telefoon", "woonplaats",
                              "verzekering_type", "geschatte_premie_min",
                              "geschatte_premie_max", "status", "aangemaakt_op"]].copy()
        df_display.columns = ["Naam", "E-mail", "Telefoon", "Woonplaats",
                               "Verzekering", "Premie min (€)", "Premie max (€)",
                               "Status", "Aangemaakt"]
        df_display["Aangemaakt"] = df_display["Aangemaakt"].str[:16]
        st.dataframe(df_display, use_container_width=True, hide_index=True)

with tab_afspraken:
    afspraken = get_afspraken()
    if not afspraken:
        st.info("Nog geen afspraken.")
    else:
        df_afs = pd.DataFrame(afspraken)
        df_display = df_afs[["naam", "email", "telefoon", "gewenste_datum",
                              "gewenste_tijd", "onderwerp", "status", "aangemaakt_op"]].copy()
        df_display.columns = ["Naam", "E-mail", "Telefoon", "Datum", "Tijd",
                               "Onderwerp", "Status", "Aangevraagd"]
        df_display["Aangevraagd"] = df_display["Aangevraagd"].str[:16]
        st.dataframe(df_display, use_container_width=True, hide_index=True)

with tab_analyse:
    col_an1, col_an2 = st.columns(2, gap="large")

    with col_an1:
        leads_per_type = stats["leads_per_type"]
        if leads_per_type:
            df_lpt = pd.DataFrame(leads_per_type)
            fig_pie = px.pie(df_lpt, names="verzekering_type", values="aantal",
                             title="Leads per verzekering type",
                             color_discrete_sequence=px.colors.sequential.Blues_r)
            fig_pie.update_layout(
                font_family="Inter", paper_bgcolor="white",
                margin=dict(l=0, r=0, t=40, b=0), height=320
            )
            st.plotly_chart(fig_pie, use_container_width=True)

    with col_an2:
        all_leads = get_leads()
        if all_leads:
            df_all = pd.DataFrame(all_leads)
            status_counts = df_all["status"].value_counts()
            status_labels = {
                "nieuw": "Nieuw",
                "in_behandeling": "In behandeling",
                "offerte_verstuurd": "Offerte verstuurd",
                "klant_geworden": "Klant geworden",
                "niet_geinteresseerd": "Niet geinteresseerd",
            }
            status_colors = {
                "Nieuw": "#4299e1",
                "In behandeling": "#f6ad55",
                "Offerte verstuurd": "#ed8936",
                "Klant geworden": "#48bb78",
                "Niet geinteresseerd": "#fc8181",
            }
            df_funnel = pd.DataFrame({
                "status": [status_labels.get(s, s) for s in status_counts.index],
                "aantal": status_counts.values,
            })
            fig_funnel = px.bar(df_funnel, x="aantal", y="status", orientation="h",
                                title="Lead pipeline",
                                color="status",
                                color_discrete_map=status_colors)
            fig_funnel.update_layout(
                showlegend=False, font_family="Inter",
                paper_bgcolor="white", plot_bgcolor="white",
                margin=dict(l=0, r=0, t=40, b=0), height=320
            )
            st.plotly_chart(fig_funnel, use_container_width=True)

    # Leads per woonplaats
    all_leads = get_leads()
    if all_leads:
        df_all = pd.DataFrame(all_leads)
        if "woonplaats" in df_all.columns:
            df_plaatsen = df_all[df_all["woonplaats"].notna() & (df_all["woonplaats"] != "")]
            if not df_plaatsen.empty:
                plaatsen_counts = df_plaatsen["woonplaats"].value_counts().head(10).reset_index()
                plaatsen_counts.columns = ["Woonplaats", "Leads"]
                fig_plaatsen = px.bar(plaatsen_counts, x="Woonplaats", y="Leads",
                                      title="Top 10 woonplaatsen",
                                      color_discrete_sequence=["#3182ce"])
                fig_plaatsen.update_layout(
                    font_family="Inter", paper_bgcolor="white", plot_bgcolor="white",
                    margin=dict(l=0, r=0, t=40, b=0), height=280
                )
                st.plotly_chart(fig_plaatsen, use_container_width=True)

    # Tips om 50 klanten te halen
    st.markdown("""
    <div style="background:linear-gradient(135deg,#1a365d,#2b6cb0);color:white;
                border-radius:1rem;padding:2rem;margin-top:1rem;">
        <h3 style="color:#68d391;font-size:1.2rem;margin-bottom:1rem;">
            💡 Actieplan: 50 nieuwe klanten per maand
        </h3>
        <div style="display:grid;grid-template-columns:1fr 1fr;gap:1rem;font-size:0.9rem;">
            <div>
                <strong style="color:#68d391;">Week 1–2: Leads converteren</strong><br>
                • Bel alle nieuwe leads binnen 2 uur<br>
                • Stuur offertemail diezelfde dag<br>
                • Nabellen na 3 dagen
            </div>
            <div>
                <strong style="color:#68d391;">Week 3–4: Nieuwe leads genereren</strong><br>
                • Google My Business posts<br>
                • Facebook advertenties Zuid-Limburg<br>
                • Klanten vragen om verwijzingen
            </div>
            <div>
                <strong style="color:#68d391;">Maandelijks: Retentie</strong><br>
                • Dekkingscheck bestaande klanten<br>
                • Nieuwsbrief met tips en aanbiedingen<br>
                • Verjaardagscardjes sturen
            </div>
            <div>
                <strong style="color:#68d391;">SEO & vindbaarheid</strong><br>
                • Lokale zoekwoorden (bijv. "autoverzekering Maastricht")<br>
                • Google reviews verzamelen<br>
                • Blogposts over Limburgse verzekeringszaken
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# ── CSV export ────────────────────────────────────────────────────────────────
st.markdown("<br>", unsafe_allow_html=True)
st.divider()
col_exp1, col_exp2 = st.columns(2)
with col_exp1:
    all_leads_export = get_leads()
    if all_leads_export:
        df_export = pd.DataFrame(all_leads_export)
        csv_leads = df_export.to_csv(index=False).encode("utf-8")
        st.download_button(
            "⬇️ Download alle leads (CSV)",
            csv_leads,
            f"leads_{datetime.now().strftime('%Y%m%d')}.csv",
            "text/csv",
            use_container_width=True,
        )
with col_exp2:
    all_off_export = get_offertes()
    if all_off_export:
        df_off_exp = pd.DataFrame(all_off_export)
        csv_off = df_off_exp.to_csv(index=False).encode("utf-8")
        st.download_button(
            "⬇️ Download alle offertes (CSV)",
            csv_off,
            f"offertes_{datetime.now().strftime('%Y%m%d')}.csv",
            "text/csv",
            use_container_width=True,
        )
