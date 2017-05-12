import sqlite3

#łączymy się z bazą - wcześniej stworzoną
conn = sqlite3.connect('first_db')

#tworzymy kursor
c = conn.cursor()

#wstawiamy dane do bazy
c.execute("INSERT INTO users VALUES ('Felek', 1)")

#zapisujemy dane w bazie
conn.commit()


# pobieranie danych
data = c.execute("SELECT * from users WHERE login='Felek';")
print(data)
print(type(data))
for row in data:
    print(row)
    print(type(row))
    for item in row:
        print('{}\t{}'.format(item, type(item)))

#zamykamy połączenie
conn.close()
