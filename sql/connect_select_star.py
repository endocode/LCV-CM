#!/usr/bin/python
import psycopg2
import pandas as pd
import numpy as np

from config import config

def postgresql_to_dataframe(conn, select_query, column_names):
    """
    Tranform a SELECT query into a pandas dataframe
    """
    cursor = conn.cursor()
    try:
        cursor.execute(select_query)
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error: %s" % error)
        cursor.close()
        return 1

    # Naturally we get a list of tupples
    tupples = cursor.fetchall()
    cursor.close()

    # We just need to turn it into a pandas dataframe
    df = pd.DataFrame(tupples, columns=column_names)
    return df

def connect(license_list_cleaned):
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # read connection parameters
        params = config()
        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)
        # duplicating the list to compare items, and before adding License field
        column_names_list = license_list_cleaned
        # Here you can add the license_list_cleaned list, + the License column, <-- basterebbe aggiungerlo alla lista, prima di passarlo alla funzione postgresql_to_dataframe()
        # in order to have in the DataFrame only the column required <--- wrong supposition, column_names refers to the whole table.
        # must be another method to extract a data subset
        column_names_list.insert(0,'License')
        for columns in column_names_list:
             print(columns)

        column_names=["License", "Classpath exception to GPL 2.0 or later", "GPL 2.0 or later", "Apache 2.0", "GPL 3.0"]
        #Execute the "SELECT *" query
        df = postgresql_to_dataframe(conn, "select * from validationmatrix", column_names)
        df=df.set_index('License')
        print('\nDataFrame with column as index\n',df)
        print('############################')

        license_list_cleaned = license_list_cleaned_to_compare

        for license in license_list_cleaned:
            for license_to_compare in license_list_cleaned_to_compare:
                comparison = df.loc[license,license_to_compare]
                if comparison == "0" :
                    print(license+" is not compatible with "+license_to_compare)
                # print(comparison)

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')


if __name__ == '__main__':
    connect()
