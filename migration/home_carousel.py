import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode

try:
    connection = mysql.connector.connect(host='74.220.219.97',
                                         database='ibridge5_yectuning',
                                         user='ibridge5_igor',
                                         password='developer')
    mySql_insert_query = """INSERT INTO software_topcarouseinhome (id, name, image) 
                           VALUES 
                           # Alfa Romeo / 147
                           ('1bfd2ab2771123a5236d8a10647ba6a0', 'Carousel Image 1', 'images/home/car_1.jpg'),
                           ('1bfd2ab2771123a5236d8a10647ba601', 'Carousel Image 2', 'images/home/car_2.jpg'),
                           ('1bfd2ab2771123a5236d8a10647ba602', 'Carousel Image 3', 'images/home/car_3.jpg'),
                           ('1bfd2ab2771123a5236d8a10647ba603', 'Carousel Image 4', 'images/home/car_4.jpg'),
                           ('1bfd2ab2771123a5236d8a10647ba604', 'Carousel Image 5', 'images/home/car_5.jpg'),
                           ('1bfd2ab2771123a5236d8a10647ba605', 'Carousel Image 6', 'images/home/car_6.jpg'),
                           ('1bfd2ab2771123a5236d8a10647ba606', 'Carousel Image 7', 'images/home/car_7.jpg'),
                           ('1bfd2ab2771123a5236d8a10647ba607', 'Carousel Image 8', 'images/home/car_8.jpg'),
                           ('1bfd2ab2771123a5236d8a10647ba608', 'Carousel Image 9', 'images/home/car_9.jpg'),
                           ('1bfd2ab2771123a5236d8a10647ba609', 'Carousel Image 10', 'images/home/car_10.jpg'),
                           ('1bfd2ab2771123a5236d8a10647ba60a', 'Carousel Image 11', 'images/home/car_11.jpg'),
                           ('1bfd2ab2771123a5236d8a10647ba60b', 'Carousel Image 12', 'images/home/car_12.jpg'),
                           ('1bfd2ab2771123a5236d8a10647ba60c', 'Carousel Image 13', 'images/home/car_13.jpg')"""

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

