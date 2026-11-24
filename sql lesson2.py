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


run("SELECT COUNT(*) FROM bugs")

cur.execute("INSERT INTO bugs VALUES (7, 'Page loads slowly', 'medium', 'open', 0)")
run("SELECT COUNT(*) FROM bugs")

cur.execute("INSERT INTO bugs VALUES (8, 'Button text is cut off', 'low', 'open', 4)")
run("SELECT * FROM bugs WHERE id = 8")


cur.execute("DELETE FROM bugs WHERE id = 5")
run("SELECT COUNT(*) FROM bugs")

run("SELECT * FROM bugs WHERE id = 5")

cur.execute("INSERT INTO bugs VALUES (8, 'Button text is cut off', 'low', 'open', 4)")

cur.execute("UPDATE bugs SET status = 'fixed' WHERE id = 8")
run("SELECT * FROM bugs WHERE id = 8")