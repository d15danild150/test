import psycopg2
import re


def check_email_validity():
    conn = psycopg2.connect('postgresql://postgres:parkour2013@localhost:5432/demotest')
    conn.autocommit = True
    cur = conn.cursor()

    cur.execute("SELECT email FROM demo2_order")
    emails = cur.fetchall()

    for email in emails:
        email = email[0]
        if re.match(r'^[A-Z0-9]+@[A-Z0-9]+\.[A-Z0-9]+$', email, re.IGNORECASE) and not re.search(r'[\[\]<>\'"]', email):
            print(f"{email}: 1")
        else:
            print(f"{email}: 0")

    conn.close()


check_email_validity()
