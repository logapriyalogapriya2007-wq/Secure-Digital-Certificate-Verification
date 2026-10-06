import sqlite3

DATABASE = "certificates.db"


def connect():
    return sqlite3.connect(DATABASE)


def create_tables():
    con = connect()
    cur = con.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS certificates (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            certificate_id TEXT UNIQUE,
            student_name TEXT,
            course TEXT,
            issue_date TEXT,
            certificate_hash TEXT,
            blockchain_hash TEXT
        )
    """)

    con.commit()
    con.close()


def add_certificate(data):
    con = connect()
    cur = con.cursor()

    cur.execute("""
        INSERT INTO certificates
        (certificate_id, student_name, course, issue_date,
         certificate_hash, blockchain_hash)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (
        data["certificate_id"],
        data["student_name"],
        data["course"],
        data["issue_date"],
        data["certificate_hash"],
        data["blockchain_hash"]
    ))

    con.commit()
    con.close()


def get_certificate(certificate_id):
    con = connect()
    cur = con.cursor()

    cur.execute(
        "SELECT * FROM certificates WHERE certificate_id = ?",
        (certificate_id,)
    )

    result = cur.fetchone()
    con.close()

    return result


def get_all_certificates():
    con = connect()
    cur = con.cursor()

    cur.execute("SELECT * FROM certificates")

    result = cur.fetchall()
    con.close()

    return result