import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode

try:
    connection = mysql.connector.connect(host='74.220.219.97',
                                         database='ibridge5_yectuning',
                                         user='ibridge5_igor',
                                         password='developer')
    mySql_insert_query = """INSERT INTO software_tiktoklink (id, name, link, imgsrc) 
                           VALUES 
                           ('1bfd2ab2771123a5236d8a10647ba6a0', 'Tiktok1', 'https://tiktok.com', 'https://tiktok.com'),
                           ('1bfd2ab2771123a5236d8a10647ba601', 'Tiktok2', 'https://tiktok.com', 'https://tiktok.com'),
                           ('1bfd2ab2771123a5236d8a10647ba602', 'Tiktok3', 'https://tiktok.com', 'https://tiktok.com'),
                           ('1bfd2ab2771123a5236d8a10647ba609', 'Tiktok4', 'https://tiktok.com', 'https://tiktok.com')"""

    cursor = connection.cursor()
    cursor.execute(mySql_insert_query)
    connection.commit()
    print(cursor.rowcount, "Record inserted successfully into FAQ table")
    cursor.close()

except mysql.connector.Error as error:
    print("Failed to insert record into FAQ table {}".format(error))

finally:
    if (connection.is_connected()):
        connection.close()
        print("MySQL connection is closed")

