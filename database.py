import sqlite3
import os
from datetime import datetime

DB_PATH = os.path.join(os.path.dirname(__file__), "data", "ariaans.db")


def get_connection():
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    conn = sqlite3.connect(DB_PATH, check_same_thread=False)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_connection()
    c = conn.cursor()
    c.executescript("""
        CREATE TABLE IF NOT EXISTS leads (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            naam TEXT NOT NULL,
            email TEXT NOT NULL,
            telefoon TEXT,
            postcode TEXT,
            woonplaats TEXT,
            verzekering_type TEXT,
            bericht TEXT,
            bron TEXT DEFAULT 'website',
            status TEXT DEFAULT 'nieuw',
            aangemaakt_op TEXT NOT NULL,
            bijgewerkt_op TEXT NOT NULL
        );

        CREATE TABLE IF NOT EXISTS offertes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            lead_id INTEGER,
            naam TEXT NOT NULL,
            email TEXT NOT NULL,
            telefoon TEXT,
            postcode TEXT,
            woonplaats TEXT,
            verzekering_type TEXT NOT NULL,
            details TEXT,
            geschatte_premie_min REAL,
            geschatte_premie_max REAL,
            status TEXT DEFAULT 'aangevraagd',
            aangemaakt_op TEXT NOT NULL,
            FOREIGN KEY (lead_id) REFERENCES leads(id)
        );

        CREATE TABLE IF NOT EXISTS afspraken (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            naam TEXT NOT NULL,
            email TEXT NOT NULL,
            telefoon TEXT NOT NULL,
            gewenste_datum TEXT,
            gewenste_tijd TEXT,
            onderwerp TEXT,
            notities TEXT,
            status TEXT DEFAULT 'gepland',
            aangemaakt_op TEXT NOT NULL
        );

        CREATE TABLE IF NOT EXISTS maand_doelen (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            jaar INTEGER NOT NULL,
            maand INTEGER NOT NULL,
            doel INTEGER DEFAULT 50,
            gerealiseerd INTEGER DEFAULT 0,
            UNIQUE(jaar, maand)
        );
    """)
    conn.commit()
    _seed_demo_data(conn)
    conn.close()


def _seed_demo_data(conn):
    c = conn.cursor()
    c.execute("SELECT COUNT(*) FROM leads")
    if c.fetchone()[0] > 0:
        return

    from random import randint, choice
    import calendar

    namen = [
        ("Jan", "Janssen"), ("Piet", "Peters"), ("Maria", "Meijers"),
        ("Loes", "Lemmens"), ("Kees", "Kreijns"), ("Anne", "Aerts"),
        ("Tom", "Theunissen"), ("Sandra", "Smeets"), ("Rob", "Rutten"),
        ("Linda", "Leclercq"), ("Mark", "Maessen"), ("Inge", "Iven"),
        ("Frank", "Franssen"), ("Carla", "Caubo"), ("Hans", "Habets"),
        ("Nicole", "Nelissen"), ("Wim", "Willems"), ("Anita", "Amkreutz"),
        ("Bert", "Bollen"), ("Els", "Eijssen"),
    ]
    types = ["Autoverzekering", "Woonverzekering", "Zorgverzekering",
             "Bedrijfsverzekering", "Levensverzekering", "Reisverzekering"]
    plaatsen = ["Maastricht", "Heerlen", "Sittard", "Geleen", "Valkenburg",
                "Kerkrade", "Brunssum", "Landgraaf", "Vaals", "Gulpen"]
    statussen = ["nieuw", "in_behandeling", "offerte_verstuurd", "klant_geworden", "niet_geinteresseerd"]

    now = datetime.now()
    leads_to_insert = []
    for i in range(47):
        naam = choice(namen)
        maand_offset = randint(0, 2)
        dag = randint(1, 28)
        maand = now.month - maand_offset
        jaar = now.year
        if maand <= 0:
            maand += 12
            jaar -= 1
        ts = f"{jaar}-{maand:02d}-{dag:02d} {randint(8,17):02d}:{randint(0,59):02d}:00"
        status = choice(statussen)
        leads_to_insert.append((
            f"{naam[0]} {naam[1]}",
            f"{naam[0].lower()}.{naam[1].lower()}@email.nl",
            f"06{randint(10000000,99999999)}",
            f"{randint(6200,6299)} {choice('ABCDEFGH')}{''.join([choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(1)])}",
            choice(plaatsen),
            choice(types),
            "",
            "website",
            status,
            ts,
            ts,
        ))

    c.executemany("""
        INSERT INTO leads (naam, email, telefoon, postcode, woonplaats, verzekering_type,
                           bericht, bron, status, aangemaakt_op, bijgewerkt_op)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, leads_to_insert)
    conn.commit()


def save_lead(naam, email, telefoon, postcode, woonplaats, verzekering_type, bericht, bron="website"):
    conn = get_connection()
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    conn.execute("""
        INSERT INTO leads (naam, email, telefoon, postcode, woonplaats, verzekering_type,
                           bericht, bron, status, aangemaakt_op, bijgewerkt_op)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, 'nieuw', ?, ?)
    """, (naam, email, telefoon, postcode, woonplaats, verzekering_type, bericht, bron, now, now))
    conn.commit()
    conn.close()


def save_offerte(naam, email, telefoon, postcode, woonplaats, verzekering_type, details,
                 premie_min, premie_max):
    conn = get_connection()
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor = conn.execute("""
        INSERT INTO leads (naam, email, telefoon, postcode, woonplaats, verzekering_type,
                           bericht, bron, status, aangemaakt_op, bijgewerkt_op)
        VALUES (?, ?, ?, ?, ?, ?, ?, 'offerte_tool', 'nieuw', ?, ?)
    """, (naam, email, telefoon, postcode, woonplaats, verzekering_type,
          f"Offerte aangevraagd: {details}", now, now))
    lead_id = cursor.lastrowid
    conn.execute("""
        INSERT INTO offertes (lead_id, naam, email, telefoon, postcode, woonplaats,
                              verzekering_type, details, geschatte_premie_min,
                              geschatte_premie_max, aangemaakt_op)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (lead_id, naam, email, telefoon, postcode, woonplaats, verzekering_type,
          details, premie_min, premie_max, now))
    conn.commit()
    conn.close()


def save_afspraak(naam, email, telefoon, datum, tijd, onderwerp, notities=""):
    conn = get_connection()
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    conn.execute("""
        INSERT INTO afspraken (naam, email, telefoon, gewenste_datum, gewenste_tijd,
                               onderwerp, notities, aangemaakt_op)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (naam, email, telefoon, datum, tijd, onderwerp, notities, now))
    conn.commit()
    conn.close()


def get_leads(status=None, limit=500):
    conn = get_connection()
    if status:
        rows = conn.execute(
            "SELECT * FROM leads WHERE status=? ORDER BY aangemaakt_op DESC LIMIT ?",
            (status, limit)
        ).fetchall()
    else:
        rows = conn.execute(
            "SELECT * FROM leads ORDER BY aangemaakt_op DESC LIMIT ?", (limit,)
        ).fetchall()
    conn.close()
    return [dict(r) for r in rows]


def get_offertes(limit=200):
    conn = get_connection()
    rows = conn.execute(
        "SELECT * FROM offertes ORDER BY aangemaakt_op DESC LIMIT ?", (limit,)
    ).fetchall()
    conn.close()
    return [dict(r) for r in rows]


def get_afspraken(limit=200):
    conn = get_connection()
    rows = conn.execute(
        "SELECT * FROM afspraken ORDER BY aangemaakt_op DESC LIMIT ?", (limit,)
    ).fetchall()
    conn.close()
    return [dict(r) for r in rows]


def update_lead_status(lead_id, nieuwe_status):
    conn = get_connection()
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    conn.execute(
        "UPDATE leads SET status=?, bijgewerkt_op=? WHERE id=?",
        (nieuwe_status, now, lead_id)
    )
    conn.commit()
    conn.close()


def get_statistieken():
    conn = get_connection()
    stats = {}
    stats["totaal_leads"] = conn.execute("SELECT COUNT(*) FROM leads").fetchone()[0]
    stats["nieuwe_leads"] = conn.execute(
        "SELECT COUNT(*) FROM leads WHERE status='nieuw'"
    ).fetchone()[0]
    stats["klanten_geworden"] = conn.execute(
        "SELECT COUNT(*) FROM leads WHERE status='klant_geworden'"
    ).fetchone()[0]
    stats["offertes_verstuurd"] = conn.execute(
        "SELECT COUNT(*) FROM leads WHERE status='offerte_verstuurd'"
    ).fetchone()[0]
    stats["afspraken"] = conn.execute("SELECT COUNT(*) FROM afspraken").fetchone()[0]

    # Leads per maand (laatste 6 maanden)
    rows = conn.execute("""
        SELECT strftime('%Y-%m', aangemaakt_op) as maand, COUNT(*) as aantal
        FROM leads
        GROUP BY maand
        ORDER BY maand DESC
        LIMIT 6
    """).fetchall()
    stats["leads_per_maand"] = [dict(r) for r in rows]

    # Leads per verzekering type
    rows = conn.execute("""
        SELECT verzekering_type, COUNT(*) as aantal
        FROM leads
        GROUP BY verzekering_type
        ORDER BY aantal DESC
    """).fetchall()
    stats["leads_per_type"] = [dict(r) for r in rows]

    # Conversie ratio
    totaal = stats["totaal_leads"] or 1
    stats["conversie_ratio"] = round(stats["klanten_geworden"] / totaal * 100, 1)

    conn.close()
    return stats
