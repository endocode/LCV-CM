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
        cursor = conn.cursor()
        #SQL query
        postgreSQL_select_Query = "select * from validationmatrix"
        cursor.execute(postgreSQL_select_Query)
        row = cursor.fetchone()
        while row is not None:
          print(row)
          row = cursor.fetchone()


        # postgreSQL_Matching_Query = "select * from validationmatrix where \"License\" is %s"
        #booleanAssociation = True

        # print("Fetching first row")
        # cur.execute(postgreSQL_select_Query)
        # record = cur.fetchone()
        # print(record)
        # print("Fetching second row")
        # record = cur.fetchone()
        # print(record)
        # print("Fetching third row")
        # record = cur.fetchone()
        # print(record)

        # print("################### SQL Query #########################")
        # for license in license_list_cleaned:
        #     # license=str(license)
        #     print(license)
        #     cur.execute(postgreSQL_Matching_Query,(str(license)))
        #

        # close the communication with the PostgreSQL
        cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')


if __name__ == '__main__':
    connect()
