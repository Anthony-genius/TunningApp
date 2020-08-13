import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode

try:
    connection = mysql.connector.connect(host='74.220.219.97',
                                         database='ibridge5_yectuning',
                                         user='ibridge5_igor',
                                         password='developer')
    mySql_insert_query = """INSERT INTO software_teamcarousel (id, name, imgsrc) 
                           VALUES 
                           ('1bfd2ab2771123a5236d8a10647ba6a0', 'Team Carousel Image 1', 'images/home/team/intro.png'),
                           ('1bfd2ab2771123a5236d8a10647ba601', 'Team Carousel Image 2', 'images/home/team/map.jpg'),
                           ('1bfd2ab2771123a5236d8a10647ba602', 'Team Carousel Image 3', 'images/home/team/streets.jpg'),
                           ('1bfd2ab2771123a5236d8a10647ba609', 'Team Carousel Image 4', 'images/home/team/team.jpg')"""

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

