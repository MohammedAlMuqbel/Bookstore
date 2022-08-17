import psycopg2



def my_library():
    conn=psycopg2.connect("dbname='db1' user='postgres' password='2013880011' host='localhost' port='5432'")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS books(book TEXT, author TEXT, year INTEGER)")
    conn.commit()
    conn.close()


def insert_books(book,author,year):
        conn=psycopg2.connect("dbname='db1' user='postgres' password='2013880011' host='localhost' port='5432'")
        cur=conn.cursor()
        cur.execute("INSERT INTO books VALUES(%s, %s, %s)", (book,author,year))
        conn.commit()
        conn.close()



def view():
    conn=psycopg2.connect("dbname='db1' user='postgres' password='2013880011' host='localhost' port='5432'")
    cur=conn.cursor()
    cur.execute("SELECT * FROM books")
    rows=cur.fetchall()
    conn.close()
    return rows


def delete (book):
    conn=psycopg2.connect("dbname='db1' user='postgres' password='2013880011' host='localhost' port='5432'")
    cur=conn.cursor()
    cur.execute("DELETE FROM books WHERE book=%s",(book,))
    conn.commit()
    conn.close()

def update (book,t):
    conn=psycopg2.connect("dbname='db1' user='postgres' password='2013880011' host='localhost' port='5432'")
    cur=conn.cursor()
    cur.execute("UPDATE  books SET book=%s WHERE book=%s",(t,book))
    conn.commit()
    conn.close()

my_library()
insert_books("5ra","Mohammed Odeh",2019)
#delete("5ra")
update("5ra","المخيلة")
print(view())
