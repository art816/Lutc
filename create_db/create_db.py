
import sqlite3 as lite

def create_db(date):

    # con = None
    # print(date[1])
    # print(len(date))
    # print(type(date[2]))
    str_date = []
    for n in date:
        str_date.append('{}'.format(n))
    # print('type(str_date) = ', type(str_date), '\n')
    # print('str_date = ', str_date, '\n')
    # date2=['1', '2', '3']
    con = lite.connect('test1.db')
    with con:

        cur = con.cursor()
        cur.execute("INSERT INTO Date VALUES(?, ?, ?)", str_date)
        # cur.
        con.commit()
    return 1

def look_db():
    con = lite.connect('test1.db')
    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM Date")
        data = cur.fetchall()
        for n in data:
            print(n, '\n')
        cur.execute("SELECT * FROM users")
        data = cur.fetchall()
        for n in data:
            print(n, '\n')

    return 1

