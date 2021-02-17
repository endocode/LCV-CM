#!/usr/bin/python
import psycopg2
from config import config

def connect(license_list_cleaned):
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # read connection parameters
        params = config()

        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)

        # create a cursor
        cur = conn.cursor()
        #SQL query
        #postgreSQL_select_Query = "select * from validationmatrix"
        postgreSQL_Matching_Query = "select * from validationmatrix where %s IS NOT NULL;"


	# execute a statement
        print('PostgreSQL database version:')
        cur.execute('SELECT version()')

        display the PostgreSQL database server version
        db_version = cur.fetchone()
        print(db_version)
        cur.execute(postgreSQL_select_Query)
        print("Selecting rows from validationmatrix table using cursor.fetchall")
        license_records = cur.fetchall()

        print("Print each row and it's columns values")
        for row in license_records:
           print("Id = ", row[0], )
           print("Model = ", row[1])
           print("Price  = ", row[2], "\n")
    #    booleanAssociation = True

        # print("################### SQL Query #########################")
        # for license in license_list_cleaned:
        #     license=str(license)
        #     print(license)
        #     cur.execute(postgreSQL_Matching_Query,(str(license)))

        # close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')


if __name__ == '__main__':
    connect()
