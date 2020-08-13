import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode

try:
    connection = mysql.connector.connect(host='74.220.219.97',
                                         database='ibridge5_yectuning',
                                         user='ibridge5_igor',
                                         password='developer')
    mySql_insert_query = """INSERT INTO software_youtubelink (id, name, link, imgsrc) 
                           VALUES 
                           ('1b1284ec7a237c12236d8a10647ba6a0', '13 Jul, 2020  •  972 views', 'https://youtube.com/embed/oaIQ-g22c6I', 'https://i4.ytimg.com/vi/oaIQ-g22c6I/hqdefault.jpg'),
                           ('1b1284ec7a237c12236d8a10647ba601', '10 Jul, 2020  •  823 views', 'https://youtube.com/embed/WT-28czqt64', 'https://i4.ytimg.com/vi/WT-28czqt64/hqdefault.jpg'),
                           ('1b1284ec7a237c12236d8a10647ba602', '07 Jul, 2020  •  1576 views', 'https://youtube.com/embed/dYVxV46JQm4', 'https://i1.ytimg.com/vi/dYVxV46JQm4/hqdefault.jpg'),
                           ('1b1284ec7a237c12236d8a10647ba609', '03 Jul, 2020  •  1027 views', 'https://youtube.com/embed/FgEgr3pSH9I', 'https://i3.ytimg.com/vi/FgEgr3pSH9I/hqdefault.jpg'),
                           ('1b1284ec7a237c12236d8a10647ba60a', '29 Jun, 2020  •  991 views', 'https://youtube.com/embed/lDaYjKN00jk', 'https://i1.ytimg.com/vi/lDaYjKN00jk/hqdefault.jpg'),
                           ('1b1284ec7a237c12236d8a10647ba60b', '26 Jun, 2020  •  1402 views', 'https://youtube.com/embed/tku93-Odsrw', 'https://i1.ytimg.com/vi/tku93-Odsrw/hqdefault.jpg'),
                           ('1b1284ec7a237c12236d8a10647ba60c', '22 Jun, 2020  •  1221 views', 'https://youtube.com/embed/oaIQ-g22c6I', 'https://i4.ytimg.com/vi/oaIQ-g22c6I/hqdefault.jpg'),
                           ('1b1284ec7a237c12236d8a10647ba60d', '19 Jun, 2020  •  1594 views', 'https://youtube.com/embed/h2qhiovIz6g', 'https://i2.ytimg.com/vi/9YpJ-yxdQ3A/hqdefault.jpg'),
                           ('1b1284ec7a237c12236d8a10647ba60e', '16 Jun, 2020  •  2279 views', 'https://youtube.com/embed/lICiXjDk710', 'https://i1.ytimg.com/vi/h2qhiovIz6g/hqdefault.jpg'),
                           ('1b1284ec7a237c12236d8a10647ba611', '12 Jun, 2020  •  3353 views', 'https://youtube.com/embed/TjhQFcWE0oU', 'https://i1.ytimg.com/vi/lICiXjDk710/hqdefault.jpg'),
                           ('1b1284ec7a237c12236d8a10647ba612', '09 Jun, 2020  •  1785 views', 'https://youtube.com/embed/9iWucSiYdJA', 'https://i1.ytimg.com/vi/TjhQFcWE0oU/hqdefault.jpg'),
                           ('1b1284ec7a237c12236d8a10647ba613', '01 Jun, 2020  •  3574 views', 'https://youtube.com/embed/9iWucSiYdJA', 'https://i2.ytimg.com/vi/9iWucSiYdJA/hqdefault.jpg'),
                           ('1b1284ec7a237c12236d8a10647ba614', '29 May, 2020  •  1624 views', 'https://youtube.com/embed/kNa2_gi-UTA', 'https://i4.ytimg.com/vi/kNa2_gi-UTA/hqdefault.jpg'),
                           ('1b1284ec7a237c12236d8a10647ba615', '25 May, 2020  •  61227 views', 'https://youtube.com/embed/_vYyhuNLY8I', 'https://i4.ytimg.com/vi/_vYyhuNLY8I/hqdefault.jpg'),
                           ('1b1284ec7a237c12236d8a10647ba616', '22 May, 2020  •  1332 views', 'https://youtube.com/embed/Ir_PMPrXE3c', 'https://i2.ytimg.com/vi/Ir_PMPrXE3c/hqdefault.jpg')"""

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

