import sqlite3, argparse

def init_series_table(db_path="series_state.db"):
    conn = sqlite3.connect(db_path)
    conn.execute("""CREATE TABLE IF NOT EXISTS series_episodes(
        series TEXT, ep_num INTEGER, title TEXT, notes TEXT,
        PRIMARY KEY(series, ep_num))""")
    conn.commit()
    return conn

def next_episode(conn, series):
    row = conn.execute(
        "SELECT MAX(ep_num) FROM series_episodes WHERE series=?",
        (series,)).fetchone()
    return (row[0] or 0) + 1

def add_episode(conn, series, title, notes):
    ep = next_episode(conn, series)
    conn.execute("INSERT INTO series_episodes VALUES (?,?,?,?)",
                 (series, ep, title, notes))
    conn.commit()
    return ep

if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--buildseries")
    p.add_argument("--title")
    p.add_argument("--notes", default="")
    args = p.parse_args()
    conn = init_series_table()
    ep = add_episode(conn, args.buildseries, args.title, args.notes)
    print(f"Recorded episode {ep} of {args.buildseries}")
