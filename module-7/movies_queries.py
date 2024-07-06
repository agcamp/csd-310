# Aaron Camp
# Module 7.2

# import mysql connector
import mysql.connector

from mysql.connector import errorcode
from mysql_test import config
# connect to database
try:
    db = mysql.connector.connect(**config)
    print("\n Database user {} connected to MySQL on host {} with database {}"
          .format(config["user"], config["host"], config["database"]))
    input("\n\n Press any key to continue...")

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)

# first query for displaying all fields in studio table
cursor = db.cursor()
cursor.execute("SELECT studio_id, studio_name "
               "FROM studio")
studio = cursor.fetchall()
print("--DISPLAYING Studio RECORDS--")
for studio in studio:

    print("Studio ID: {}\nStudio Name: {}\n".format(studio[0], studio[1]))

# second query displays data from genre table
cursor.execute("SELECT genre_id, genre_name "
               "FROM genre")
genre = cursor.fetchall()
print("--DISPLAYING Genre RECORDS--\n")
for genre in genre:
    print("Genre ID: {}\nGenre Name: {}\n".format(genre[0], genre[1]))

# pulls film name on runtime for films shorter than 2 hours
cursor.execute("SELECT film_name, film_runtime "
               "FROM film WHERE film_runtime < 120")
film = cursor.fetchall()
print("--DISPLAYING Short Film RECORDS--\n")
for film in film:
    print("Film Name: {}\nRuntime: {}\n".format(film[0], film[1]))

cursor.execute("SELECT film_name, film_director "
               "FROM film "
               "GROUP BY film_director, film_name "
               "ORDER BY film_director")

film = cursor.fetchall()
print("--DISPLAYING Director RECORDS--\n")
for film in film:
    print("Film Name: {}\nDirector: {}\n".format(film[0], film[1]))




