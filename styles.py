MAIN_CSS = """
<style>
/* ── Imports ── */
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');

/* ── Base ── */
html, body, [class*="css"] {
    font-family: 'Inter', sans-serif !important;
}

.stApp {
    background: #f8fafc;
}

/* ── Hide Streamlit chrome ── */
#MainMenu { visibility: hidden; }
footer { visibility: hidden; }
header { visibility: hidden; }
.stDeployButton { display: none; }

/* ── Navigation bar ── */
.nav-bar {
    background: linear-gradient(135deg, #1a365d 0%, #2d5282 100%);
    padding: 0.75rem 2rem;
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin: -6rem -1rem 0 -1rem;
    box-shadow: 0 4px 20px rgba(0,0,0,0.15);
    position: sticky;
    top: 0;
    z-index: 999;
}

.nav-logo {
    color: white;
    font-size: 1.4rem;
    font-weight: 800;
    letter-spacing: -0.5px;
}

.nav-logo span {
    color: #68d391;
}

.nav-links a {
    color: rgba(255,255,255,0.85);
    text-decoration: none;
    margin-left: 1.5rem;
    font-size: 0.9rem;
    font-weight: 500;
    transition: color 0.2s;
}

.nav-links a:hover { color: #68d391; }

/* ── Hero section ── */
.hero {
    background: linear-gradient(135deg, #1a365d 0%, #2c5282 50%, #2b6cb0 100%);
    color: white;
    padding: 5rem 2rem;
    text-align: center;
    border-radius: 0 0 3rem 3rem;
    margin: 0 -1rem 3rem -1rem;
    position: relative;
    overflow: hidden;
}

.hero::before {
    content: '';
    position: absolute;
    top: -50%;
    left: -50%;
    width: 200%;
    height: 200%;
    background: radial-gradient(circle, rgba(104,211,145,0.1) 0%, transparent 60%);
    animation: pulse 4s ease-in-out infinite;
}

@keyframes pulse {
    0%, 100% { transform: scale(1); opacity: 0.5; }
    50% { transform: scale(1.1); opacity: 1; }
}

.hero-badge {
    display: inline-block;
    background: rgba(104,211,145,0.2);
    border: 1px solid rgba(104,211,145,0.4);
    color: #68d391;
    padding: 0.4rem 1.2rem;
    border-radius: 2rem;
    font-size: 0.85rem;
    font-weight: 600;
    margin-bottom: 1.5rem;
    letter-spacing: 0.5px;
}

.hero h1 {
    font-size: 3.2rem;
    font-weight: 800;
    line-height: 1.1;
    margin-bottom: 1.5rem;
    letter-spacing: -1px;
}

.hero h1 span { color: #68d391; }

.hero p {
    font-size: 1.25rem;
    opacity: 0.85;
    max-width: 600px;
    margin: 0 auto 2.5rem;
    line-height: 1.6;
}

/* ── Buttons ── */
.btn-primary {
    display: inline-block;
    background: linear-gradient(135deg, #38a169, #48bb78);
    color: white !important;
    padding: 1rem 2.5rem;
    border-radius: 0.75rem;
    font-size: 1.05rem;
    font-weight: 700;
    text-decoration: none !important;
    box-shadow: 0 8px 25px rgba(56,161,105,0.4);
    transition: all 0.3s ease;
    cursor: pointer;
    border: none;
}

.btn-primary:hover {
    transform: translateY(-2px);
    box-shadow: 0 12px 35px rgba(56,161,105,0.5);
}

.btn-secondary {
    display: inline-block;
    background: transparent;
    color: white !important;
    padding: 1rem 2.5rem;
    border-radius: 0.75rem;
    font-size: 1.05rem;
    font-weight: 600;
    border: 2px solid rgba(255,255,255,0.4);
    text-decoration: none !important;
    transition: all 0.3s ease;
    cursor: pointer;
    margin-left: 1rem;
}

.btn-secondary:hover {
    background: rgba(255,255,255,0.1);
    border-color: white;
}

/* ── Cards ── */
.card {
    background: white;
    border-radius: 1rem;
    padding: 1.75rem;
    box-shadow: 0 4px 20px rgba(0,0,0,0.06);
    border: 1px solid rgba(0,0,0,0.05);
    transition: transform 0.3s ease, box-shadow 0.3s ease;
    height: 100%;
}

.card:hover {
    transform: translateY(-4px);
    box-shadow: 0 12px 40px rgba(0,0,0,0.12);
}

.card-icon {
    font-size: 2.5rem;
    margin-bottom: 1rem;
}

.card h3 {
    font-size: 1.2rem;
    font-weight: 700;
    color: #1a365d;
    margin-bottom: 0.75rem;
}

.card p {
    color: #4a5568;
    font-size: 0.95rem;
    line-height: 1.6;
    margin-bottom: 0;
}

.card-price {
    font-size: 1.1rem;
    font-weight: 700;
    color: #38a169;
    margin-top: 0.75rem;
}

/* ── Section headers ── */
.section-header {
    text-align: center;
    margin-bottom: 2.5rem;
}

.section-header h2 {
    font-size: 2.2rem;
    font-weight: 800;
    color: #1a365d;
    margin-bottom: 0.75rem;
    letter-spacing: -0.5px;
}

.section-header p {
    color: #4a5568;
    font-size: 1.05rem;
    max-width: 540px;
    margin: 0 auto;
}

/* ── Stats bar ── */
.stats-bar {
    background: white;
    border-radius: 1rem;
    padding: 1.5rem 2rem;
    display: flex;
    justify-content: space-around;
    align-items: center;
    box-shadow: 0 4px 20px rgba(0,0,0,0.08);
    margin-bottom: 3rem;
}

.stat-item {
    text-align: center;
}

.stat-number {
    font-size: 2rem;
    font-weight: 800;
    color: #1a365d;
    line-height: 1;
}

.stat-label {
    font-size: 0.85rem;
    color: #718096;
    margin-top: 0.25rem;
}

/* ── USP list ── */
.usp-item {
    display: flex;
    align-items: flex-start;
    margin-bottom: 1rem;
}

.usp-check {
    color: #38a169;
    font-size: 1.2rem;
    margin-right: 0.75rem;
    flex-shrink: 0;
    margin-top: 0.1rem;
}

.usp-text strong {
    color: #1a365d;
    display: block;
    font-size: 0.95rem;
}

.usp-text span {
    color: #4a5568;
    font-size: 0.85rem;
}

/* ── Testimonials ── */
.testimonial {
    background: white;
    border-radius: 1rem;
    padding: 1.5rem;
    box-shadow: 0 4px 20px rgba(0,0,0,0.06);
    border-left: 4px solid #38a169;
}

.testimonial-text {
    font-style: italic;
    color: #2d3748;
    font-size: 0.95rem;
    line-height: 1.6;
    margin-bottom: 0.75rem;
}

.testimonial-author {
    font-weight: 700;
    color: #1a365d;
    font-size: 0.9rem;
}

.testimonial-stars {
    color: #f6ad55;
    font-size: 0.85rem;
}

/* ── Trust badges ── */
.trust-badge {
    display: inline-flex;
    align-items: center;
    background: #f0fff4;
    border: 1px solid #c6f6d5;
    border-radius: 0.5rem;
    padding: 0.5rem 1rem;
    margin: 0.25rem;
    font-size: 0.85rem;
    color: #276749;
    font-weight: 600;
}

/* ── Forms ── */
.form-container {
    background: white;
    border-radius: 1.25rem;
    padding: 2.5rem;
    box-shadow: 0 8px 40px rgba(0,0,0,0.1);
}

.form-container h2 {
    color: #1a365d;
    font-size: 1.6rem;
    font-weight: 800;
    margin-bottom: 0.5rem;
}

.form-container p {
    color: #718096;
    margin-bottom: 1.5rem;
}

/* ── Streamlit widget overrides ── */
.stTextInput > div > div > input,
.stSelectbox > div > div > div,
.stTextArea > div > div > textarea {
    border-radius: 0.6rem !important;
    border: 1.5px solid #e2e8f0 !important;
    font-family: 'Inter', sans-serif !important;
}

.stTextInput > div > div > input:focus,
.stTextArea > div > div > textarea:focus {
    border-color: #3182ce !important;
    box-shadow: 0 0 0 3px rgba(49,130,206,0.15) !important;
}

.stButton > button {
    background: linear-gradient(135deg, #2b6cb0, #3182ce) !important;
    color: white !important;
    font-weight: 700 !important;
    border: none !important;
    border-radius: 0.75rem !important;
    padding: 0.75rem 2rem !important;
    font-size: 1rem !important;
    font-family: 'Inter', sans-serif !important;
    box-shadow: 0 4px 15px rgba(43,108,176,0.3) !important;
    transition: all 0.3s ease !important;
}

.stButton > button:hover {
    background: linear-gradient(135deg, #1a365d, #2b6cb0) !important;
    box-shadow: 0 8px 25px rgba(43,108,176,0.4) !important;
    transform: translateY(-1px) !important;
}

/* ── Metric cards ── */
.metric-card {
    background: white;
    border-radius: 1rem;
    padding: 1.5rem;
    box-shadow: 0 4px 20px rgba(0,0,0,0.06);
    text-align: center;
    border-top: 4px solid #3182ce;
}

.metric-value {
    font-size: 2.5rem;
    font-weight: 800;
    color: #1a365d;
    line-height: 1;
}

.metric-label {
    font-size: 0.85rem;
    color: #718096;
    margin-top: 0.4rem;
    font-weight: 500;
}

.metric-delta {
    font-size: 0.8rem;
    color: #38a169;
    font-weight: 600;
    margin-top: 0.25rem;
}

/* ── Progress bar ── */
.progress-container {
    background: #edf2f7;
    border-radius: 1rem;
    height: 12px;
    overflow: hidden;
    margin-top: 0.5rem;
}

.progress-fill {
    background: linear-gradient(90deg, #38a169, #68d391);
    height: 100%;
    border-radius: 1rem;
    transition: width 0.8s ease;
}

/* ── Alert banners ── */
.alert-success {
    background: #f0fff4;
    border: 1px solid #9ae6b4;
    border-radius: 0.75rem;
    padding: 1rem 1.5rem;
    color: #276749;
    font-weight: 500;
    display: flex;
    align-items: center;
    gap: 0.75rem;
}

/* ── Footer ── */
.site-footer {
    background: #1a202c;
    color: #a0aec0;
    padding: 3rem 2rem 1.5rem;
    margin: 4rem -1rem -6rem -1rem;
    border-radius: 2rem 2rem 0 0;
}

.footer-grid {
    display: grid;
    grid-template-columns: 2fr 1fr 1fr 1fr;
    gap: 2rem;
    margin-bottom: 2rem;
}

.footer-brand {
    font-size: 1.3rem;
    font-weight: 800;
    color: white;
    margin-bottom: 0.75rem;
}

.footer-brand span { color: #68d391; }

.footer-desc {
    font-size: 0.85rem;
    line-height: 1.6;
    margin-bottom: 1rem;
}

.footer-heading {
    color: white;
    font-weight: 700;
    font-size: 0.9rem;
    margin-bottom: 0.75rem;
}

.footer-link {
    display: block;
    font-size: 0.85rem;
    color: #718096;
    margin-bottom: 0.4rem;
    text-decoration: none;
}

.footer-link:hover { color: #68d391; }

.footer-bottom {
    border-top: 1px solid #2d3748;
    padding-top: 1.25rem;
    font-size: 0.8rem;
    text-align: center;
}

/* ── Responsive ── */
@media (max-width: 768px) {
    .hero h1 { font-size: 2rem; }
    .hero { padding: 3rem 1rem; }
    .footer-grid { grid-template-columns: 1fr; }
}

/* ── Page sub-hero ── */
.page-hero {
    background: linear-gradient(135deg, #1a365d 0%, #2c5282 100%);
    color: white;
    padding: 3rem 2rem;
    border-radius: 0 0 2rem 2rem;
    margin: -4rem -1rem 3rem -1rem;
    text-align: center;
}

.page-hero h1 {
    font-size: 2.4rem;
    font-weight: 800;
    margin-bottom: 0.5rem;
}

.page-hero p {
    font-size: 1.1rem;
    opacity: 0.85;
}

/* ── Comparison table ── */
.compare-table {
    background: white;
    border-radius: 1rem;
    overflow: hidden;
    box-shadow: 0 4px 20px rgba(0,0,0,0.08);
}

.compare-row {
    display: grid;
    grid-template-columns: 2fr 1fr 1fr;
    padding: 0.9rem 1.5rem;
    border-bottom: 1px solid #f0f4f8;
    align-items: center;
}

.compare-row:first-child {
    background: #1a365d;
    color: white;
    font-weight: 700;
}

.compare-row:nth-child(even):not(:first-child) {
    background: #f8fafc;
}

.check { color: #38a169; font-weight: 700; }
.cross { color: #fc8181; }

/* ── Offerte calculator ── */
.price-display {
    background: linear-gradient(135deg, #1a365d, #2b6cb0);
    color: white;
    border-radius: 1rem;
    padding: 2rem;
    text-align: center;
}

.price-display .from {
    font-size: 0.9rem;
    opacity: 0.75;
    margin-bottom: 0.25rem;
}

.price-display .amount {
    font-size: 3rem;
    font-weight: 800;
    line-height: 1;
}

.price-display .period {
    font-size: 0.9rem;
    opacity: 0.75;
    margin-top: 0.25rem;
}

/* ── Status badges ── */
.badge {
    display: inline-block;
    padding: 0.2rem 0.75rem;
    border-radius: 2rem;
    font-size: 0.75rem;
    font-weight: 600;
}

.badge-new { background: #ebf8ff; color: #2b6cb0; }
.badge-progress { background: #fffbeb; color: #b7791f; }
.badge-done { background: #f0fff4; color: #276749; }
.badge-lost { background: #fff5f5; color: #c53030; }
</style>
"""


def nav_html(active="home"):
    pages = [
        ("home", "Home", "Ariaans_Assurantiën"),
        ("verzekeringen", "Verzekeringen", "Verzekeringen"),
        ("offerte", "Offerte", "Offerte_Aanvragen"),
        ("contact", "Contact", "Contact"),
    ]
    links = ""
    for key, label, page in pages:
        cls = 'style="color:#68d391;"' if key == active else ''
        links += f'<a href="/{page}" {cls}>{label}</a>'
    return f"""
    <div class="nav-bar">
        <div class="nav-logo">Ariaans<span>Assurantiën</span></div>
        <div class="nav-links">{links}</div>
    </div>
    """


def footer_html():
    return """
    <div class="site-footer">
        <div class="footer-grid">
            <div>
                <div class="footer-brand">Ariaans<span>Assurantiën</span></div>
                <div class="footer-desc">
                    Uw lokale verzekeringsadviseur in Zuid-Limburg. Al meer dan 25 jaar
                    betrouwbaar en persoonlijk advies voor particulieren en ondernemers.
                </div>
                <div>
                    <span class="trust-badge">🏛️ AFM Geregistreerd</span>
                    <span class="trust-badge">⚖️ KiFiD Aangesloten</span>
                </div>
            </div>
            <div>
                <div class="footer-heading">Verzekeringen</div>
                <a class="footer-link" href="#">Autoverzekering</a>
                <a class="footer-link" href="#">Woonverzekering</a>
                <a class="footer-link" href="#">Zorgverzekering</a>
                <a class="footer-link" href="#">Levensverzekering</a>
                <a class="footer-link" href="#">Bedrijfsverzekering</a>
                <a class="footer-link" href="#">Reisverzekering</a>
            </div>
            <div>
                <div class="footer-heading">Bedrijf</div>
                <a class="footer-link" href="#">Over Ons</a>
                <a class="footer-link" href="#">Ons Team</a>
                <a class="footer-link" href="#">Reviews</a>
                <a class="footer-link" href="#">Vacatures</a>
                <a class="footer-link" href="#">Nieuws</a>
            </div>
            <div>
                <div class="footer-heading">Contact</div>
                <a class="footer-link" href="#">📍 Maastricht & Heerlen</a>
                <a class="footer-link" href="#">📞 043 - 123 45 67</a>
                <a class="footer-link" href="#">✉️ info@ariaans-assurantien.nl</a>
                <a class="footer-link" href="#">🕐 Ma–Vr 8:30–17:30</a>
            </div>
        </div>
        <div class="footer-bottom">
            © 2025 Ariaans Assurantiën B.V. · KvK 12345678 · AFM 12345678 ·
            <a class="footer-link" style="display:inline;" href="#">Privacybeleid</a> ·
            <a class="footer-link" style="display:inline;" href="#">Klachten</a>
        </div>
    </div>
    """
