import sqlite3 as lite


def create_database(database_path: str):
    # generate the database and drops if already created
    connection = lite.connect(database_path)
    with connection:
        cursor = connection.cursor()
        cursor.execute("drop table if exists words")
        ddl = "CREATE TABLE words(word TEXT PRIMARY KEY NOT NULL, usage_count INT DEFAULT 1 NOT NULL); "
        cursor.execute(ddl)
        ddl = "CREATE UNIQUE INDEX words_word_uindex ON words (word)"
        cursor.execute(ddl)
        # connection.close()


def save_words_to_database(database_path: str, words_list: list):
    # save the words to the database
    conn = lite.connect(database_path)
    with conn:
        cur = conn.cursor()
        for word in words_list:
            # check to see if world is already in there
            sql = "SELECT count(word) FROM words WHERE word='" + word + "'"
            cur.execute(sql)
            count = cur.fetchone()[0]
            if count > 0:
                sql = "UPDATE words SET usage_count = usage_count + 1 WHERE word = '" + word + "'"
            else:
                sql = "INSERT INTO words(word) VALUES ('" + word + "')"
            cur.execute(sql)
        print("Database save complete!")
    conn.close()
