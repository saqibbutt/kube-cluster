import sqlite3

connection = sqlite3.connect('database.sqlite3')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO jokes (url, value) VALUES (?, ?)", ('https://api.chucknorris.io/jokes/HoTV5-2JT4ymvEuav18leg','When Chuck Norris says he is Sorry, its not for what he has done, but for what he is about to do.'))

cur.execute("INSERT INTO jokes (url, value) VALUES (?, ?)", ('https://api.chucknorris.io/jokes/QKdvc3ugQPWucoDoBe0s3A','Despite millions of fan letters, Chuck Norris regretfully says that his schedule is simply too full to kill Nickelback anytime soon.'))


cur.execute("INSERT INTO jokes (url, value) VALUES (?, ?)", ('https://api.chucknorris.io/jokes/iNmA3fofScqorFXWo3g0MQ','Chuck Norris once loaned the dinosaurs money. They never payed him back.'))


cur.execute("INSERT INTO jokes (url, value) VALUES (?, ?)", ('https://api.chucknorris.io/jokes/KxfE_gtiQkezfXmKStwWIg','One time Chuck Norris stared a man to death.'))


connection.commit()
connection.close()