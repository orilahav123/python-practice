import sqlite3

conn = sqlite3.connect(":memory:")
cur = conn.cursor()

cur.execute("""
CREATE TABLE bugs (
    id INTEGER,
    title TEXT,
    severity TEXT,
    status TEXT,
    days_open INTEGER
)
""")

bugs = [
    (1, "Double click shows missing name", "high", "fixed", 2),
    (2, "Login button not working on mobile", "high", "open", 5),
    (3, "Typo on homepage", "low", "open", 12),
    (4, "Wrong total in cart", "high", "open", 1),
    (5, "Logo blurry in dark mode", "low", "fixed", 7),
    (6, "Search ignores capital letters", "medium", "open", 3),
]
cur.executemany("INSERT INTO bugs VALUES (?, ?, ?, ?, ?)", bugs)


def run(query):
    print(query)
    for row in cur.execute(query):
        print(row)
    print()

run("SELECT * FROM bugs")
run("SELECT title FROM bugs")
run("SELECT status FROM bugs")
run("SELECT * FROM bugs WHERE severity = 'high'")
run("SELECT * FROM bugs WHERE status = 'open'")
run("SELECT * FROM bugs WHERE days_open >4")