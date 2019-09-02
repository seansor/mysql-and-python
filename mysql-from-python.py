import os
import datetime
import pymysql

#Get useranme from Cloud9 workspace
# (Modify this variable if running on another environment)
username = os.getenv('C9_USER')

#Connect to the database
connection = pymysql.connect(host='localhost',
                            user=username,
                            password='',
                            db='Chinook')

try:
    #Run a query
    with connection.cursor() as cursor:
        list_of_names = ['fred', 'Fred']
        # Prepare a string with the same number of placeholders as is in
        # list_of_names
        format_strings = ','.join(['%s']*len(list_of_names))
        cursor.execute("DELETE FROM Friends WHERE name in ({});".format(format_strings), list_of_names)
        connection.commit()
        # Note that the above will still display a warning (not error) if the
        # table already exists
finally:
    #Close the connection, regardless of whether the above was successful
    connection.close()