import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode

try:
    connection = mysql.connector.connect(host='74.220.219.97',
                                         database='ibridge5_yectuning',
                                         user='ibridge5_igor',
                                         password='developer')
    mySql_insert_query = """INSERT INTO product_carengine (id, year_name, engine_name, engine_type, engine_status, eco_torque_origin, eco_torque_difference, eco_estimated_fuel_reduction, eco_price, eco_description, stage1_torque_origin, stage1_torque_difference, stage1_power_origin, stage1_power_difference, stage1_price, stage1_description, stage2_torque_origin, stage2_torque_difference, stage2_power_origin, stage2_power_difference, stage2_price, stage2_description, dsg_torque_origin, dsg_torque_difference, model_id) 
                           VALUES
                           ('bafd201c7194d81236d8a106234a600a', '2001 > 2005', '2.0 TS', 'gas', Null, 172, 20, 6, 360, Null, 150, 15, 172, 20, 460, Null, Null, Null, Null, Null, Null, Null, Null, Null, 'bafd201c17674d81236d8a10647ba64c')"""
    cursor = connection.cursor()
    cursor.execute(mySql_insert_query)
    connection.commit()
    print(cursor.rowcount, "Record inserted successfully into Engine table")
    cursor.close()

except mysql.connector.Error as error:
    print("Failed to insert record into Engine table {}".format(error))

finally:
    if (connection.is_connected()):
        connection.close()
        print("MySQL connection is closed")
