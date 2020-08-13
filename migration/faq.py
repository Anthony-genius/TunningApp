import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode

try:
    connection = mysql.connector.connect(host='74.220.219.97',
                                         database='ibridge5_yectuning',
                                         user='ibridge5_igor',
                                         password='developer')
    mySql_insert_query = """INSERT INTO software_faq (id, question, answer) 
                           VALUES 
                           # Alfa Romeo / 147
                           ('1bfd201c171123a5236d8a10647ba6a0', 'What is chiptuning and how does it work ?', 'Every injection engine is equipped with a computer-ECU (Electronic Control Unit) that controls the ignition, injection and air-fuel ratio. This ECU (computerchip) contains all necessary operating settings for the engine. We rewrite the data on this chip so that the engine benifits from an individually optimized operating program.'),
                           ('1bfd201c171123a5236d8a10647ba601', 'What are the consequences for the factory warranty?', ' The chiptuning is completely invisible for the dealers and there is no reason why the warranty would expire. We may also at any time undo the remap so there is no trace of it. Most brands dont mind well-executed chiptuning as it does not have harmful effects on the car. There are even brands that sell tunings themselves.'),
                           ('1bfd201c171123a5236d8a10647ba602', 'Are there consequences for the insurance ?', 'Most insurance companies calculate their fees on the price of the vehicle, driver age, the sportiness of the car, but not the horsepower.'),
                           ('1bfd201c171123a5236d8a10647ba603', 'Are there consequences for the road taxes ?', 'No. The road tax is calculated on the tax horsepower and not on price.'),
                           ('1bfd201c171123a5236d8a10647ba604', 'How long does the chiptuning process take ?', 'After an appointment is made, we work on the car for about 2-3 hours, (note that some cars take longer) We individually adjust each car and often it takes several times before the result is perfect. We return the car when we are satisfied about the result, it should be perfect. Our customers are always welcome to stay and see what happens to the car.'),
                           ('1bfd201c171123a5236d8a10647ba605', 'Why does every car needs custom software and has to be tested on a decent dyno ?', 'Each engine is different, each injector is different, each turbo is different... Mass production = fairly large manufacturing tolerances. It just takes too much time and money to individually develop each engine. Because the manufacturers make those engines with positive and negative tolerances, they must also provide large margins in the software! If we take a look at them individually we can deliver a highly secure way a lot of horsepower and torque gain. Tuners that work with a standard tuning program dont get their extra horsepower not from fine-tuning, but simply from a greatly increased boost pressure, which of course is certainly not good for engine life! People sometimes ask how is it that tuner X has the same horsepower as tuner Y, but costs only half. Well the answer is simple, its just a different tuning, which has the same horsepower, yes, but the difference lies in the reliability, drivability, fuel consumption etc. Cheap is in this case more expensive!'),
                           ('1bfd201c171123a5236d8a10647ba606', 'What are the disadvantages of chiptuning ?', 'This may sound strange, but if you do it well, there are none !'),
                           ('1bfd201c171123a5236d8a10647ba607', 'Is chiptuning harmful for my motor ?', 'Our stage 1 remap is developed in a certain way that we always remain within the safety limits of the current car. A stage 1 is 100 reliable and we guarantee the same lifespan for this engine.'),
                           ('1bfd201c171123a5236d8a10647ba608', 'What if the car gets a software update ?', 'With newer cars it is possible they receive an update. If this happens you can rechedule and we remap the car based on the new software, ofcourse... Free of charge.'),
                           ('1bfd201c171123a5236d8a10647ba609', 'What is the difference between chiptuning and a power box ?', 'A powerbox is a small module that is connected onto the cars wiring system. By remapping the car we optimalise the software on the eeprom (chip). A powerbox just alters the value send at the engine ECU. In fact your "cheating" the chip. This isnt the correct way to tune a car and holds several dangers... that is why we dont sell it and you shouldnt as well :)')"""

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

