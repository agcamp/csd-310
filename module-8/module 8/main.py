# Aaron Camp
# Module 8
# 7/6/24

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

cursor = db.cursor()

# function used to print results
def show_films(cursor, title):
    cursor.execute("SELECT film_name AS Name, "
                   "film_director AS Director  , "
                   "genre_name AS Genre,"
                   " studio_name AS 'Studio Name' "
                   "FROM film "
                   "INNER JOIN genre ON film.genre_id=genre.genre_id "
                   "INNER JOIN studio ON film.studio_id=studio.studio_id ")

    films = cursor.fetchall()
    print("\n -- {} --".format(title))

    for film in films:
        print("Film Name: {}\nDirector: {}\nGenre Name: {}\nStudio Name: {}\n".format(film[0], film[1], film[2], film[3]))


show_films(cursor, "DISPLAYING FILMS")

# Insert Speed into film table
cursor.execute("INSERT INTO film (film_name, film_director, genre_id, studio_id, film_runtime, film_releaseDate)"
                    "VALUES ('Speed ', 'Jan de Bont', 3, 1, 116, '1994'); " )

show_films(cursor, "DISPLAYING FILMS AFTER INSERT")


# update Alien genre to horror
cursor.execute("UPDATE film "
               "SET genre_id = 1 "
               "WHERE film_name= 'Alien'")

show_films(cursor, "DISPLAYING FILMS AFTER UPDATE- Changed Alien to Horror")

# delete gladiator from film table
cursor.execute("DELETE FROM film "
               "WHERE film_name= 'Gladiator' ")
show_films(cursor, "DISPLAYING FILMS AFTER DELETE")

