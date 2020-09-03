import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode

try:
    connection = mysql.connector.connect(host='74.220.219.97',
                                         database='ibridge5_yectuning',
                                         user='ibridge5_igor',
                                         password='developer')
    mySql_insert_query = """INSERT INTO product_carbrand (id, brand_name, banner_image) 
                           VALUES 
                           ('93074f3d589445959ecff7672b9c3016', 'Alfa Romeo', 'images/banner/alfa_romeo.jpg'),
                           ('23a12f1f6398436695f4aeb026678784', 'Alpina', 'images/banner/alpina.jpg'),
                           ('88bcaaab7b49442eb70627edbcc5842a', 'Alpine', 'images/banner/alpine.jpg'),
                           ('06f10b52b07e43c2aa7cc1e368b63179', 'Ariel', 'images/banner/ariel.jpg'),
                           ('09b38439ef43400aa16c477bc37e1f03', 'Astonmartin', 'images/banner/alfa_romeo.jpg'),
                           ('ed28908577614ee0b918bb4bed22dd89', 'Audi', 'images/banner/audi.jpg'),
                           ('8e42635a37bc4bb5996352df7d658f0b', 'Bentley', 'images/banner/bentley.jpg'),
                           ('0c10b9c3b4724e1bbf093d98e2fa4dd5', 'BMW', 'images/banner/bmw.jpg'),
                           ('40d03605cb3440109561cb1a14d95c22', 'Borgward', 'images/banner/borgward.jpg'),
                           ('ec8246119ceb4ce4bc3735ee1cac8370', 'Bugatti', 'images/banner/bugatti.jpg'),
                           ('a967f0dc39b64de7acd623d2e3122c41', 'Buick', 'images/banner/buick.jpg'),
                           ('7db42ad303694768aa268c345dd8f0b7', 'Cadillac', 'images/banner/cadillac.jpg'),
                           ('9331827af515427f92a412e47917f8da', 'Chevrolet', 'images/banner/chevloret.jpg'),
                           ('d02e919af0d4406faca32982ccfbd9de', 'Chrysler', 'images/banner/chrysler.jpg'),
                           ('e45caa26644045f3948836acdb4d62ba', 'Citroen', 'images/banner/citroen.jpg'),
                           ('ec3b259e6b8f414b807ea21590971a37', 'Cupra', 'images/banner/cupra.jpg'),
                           ('7a1cfff351cc42ef983ab17efc6f4a81', 'Dacia', 'images/banner/dacia.jpg'),
                           ('c36c8e366e21466db9d6746fa4ecc382', 'Daewoo', 'images/banner/daewoo.jpg'),
                           ('a8a48fd885f54be5a59ffe6e4fff9e52', 'Dodge', 'images/banner/dodge.jpg'),
                           ('df200fb1410944429478483843da6435', 'DS', 'images/banner/ds.jpg'),
                           ('a8a43ba9c6f6407bba5bdcb097ae6b85', 'Ferrari', 'images/banner/ferrari.jpg'),
                           ('a9bb6d1f63804cb08a9b40a691ffe263', 'Fiat', 'images/banner/fiat.jpg'),
                           ('b2b15e576e0b461faedd136af4f86a46', 'Ford', 'images/banner/ford.jpg'),
                           ('bc9cefbe9e204f10a071b39ed0ec7b0d', 'Geely', 'images/banner/geely.jpg'),
                           ('84f0cb5e4a6e4972aeee2d7a527423ae', 'GMW', 'images/banner/gwm.jpg'),
                           ('02bafdc72ec84a7a9de84485be0fb853', 'Holden', 'images/banner/holden.jpg'),
                           ('fd575ecfbcf74ac5ae4e7c4512787af9', 'Honda', 'images/banner/honda.jpg'),
                           ('633a7563f8c14a069431a935bf3746b2', 'Hyndai', 'images/banner/hyundai.jpg'),
                           ('24af1c6ef5dc4f8c9e734faaa699f511', 'Infiniti', 'images/banner/infiniti.jpg'),
                           ('33ad5e41389e4d4594faa5f2bbcdec28', 'Isuzu', 'images/banner/isuzu.jpg'),
                           ('22e7f6e58230420bb40ddcc16c791166', 'Iveco', 'images/banner/iveco.jpg'),
                           ('5d84739a2dee46c38e1cf6c62a1e8e2e', 'JAC', 'images/banner/jac.jpg'),
                           ('17b5dc48766e4c4bab2618ca8d712249', 'Jaguar', 'images/banner/jaguar.jpg'),
                           ('c8b729926a1c41eba9c813cb0b08d550', 'Jeep', 'images/banner/jeep.jpg'),
                           ('d6ba254800e24721b5d5caf0662f35cb', 'Kia', 'images/banner/kia.jpg'),
                           ('37a2176d52af45169fa3c0dc1db50829', 'KTM', 'images/banner/ktm.jpg'),
                           ('15a2ce25143f4432b98eb1e062fc9753', 'Lamborghini', 'images/banner/lancia.jpg'),
                           ('851bf403c56145e7b1a87ab095ecdda4', 'Lancia', 'images/banner/lancia.jpg'),
                           ('9e5f8896965447e19e3a95cfe1389b5e', 'Landrover', 'images/banner/landrover.jpg'),
                           ('b1509b52ec9343628f2fc58ad9e047bc', 'Lexus', 'images/banner/lexus.jpg'),
                           ('56b384969bee4083946bd953a2eaa69e', 'Lincoln', 'images/banner/lincoln.jpg'),
                           ('9103b1d8523f403a82da2bda4559cbd3', 'Lotus', 'images/banner/lotus.jpg'),
                           ('590a4d60e14a49da8b3ecc2479d40a3d', 'Mahindra', 'images/banner/mahindra.jpg'),
                           ('b16bf4a9f66a48b5a2db8f34bfabe32f', 'Man', 'images/banner/man.jpg'),
                           ('17613d4511b74eb4a9e36e87f29ccf01', 'Maserati', 'images/banner/maserati.jpg'),
                           ('e25b333531ce4b1b8c3fc6bae325d735', 'Mazda', 'images/banner/mazda.jpg'),
                           ('cf2a98951e7145469cc62d871346af25', 'Mclaren', 'images/banner/mc.jpg'),
                           ('c4c036d1d544461aa725b51bd6e73c5f', 'Mercedes', 'images/banner/mercedes.jpg'),
                           ('7a7521138b00472e9fe8d2a1d88e58c5', 'Mg', 'images/banner/mg.jpg'),
                           ('2e7fe1d774e14446892c221b9df19179', 'Mini', 'images/banner/mini.jpg'),
                           ('0f8e3900be7d4f9c86b68b8a21b1d3c4', 'Mitsubishi', 'images/banner/mitsubishi.jpg'),
                           ('31b981d9bc6349159ba44ebccc3f073b', 'Nissan', 'images/banner/nissan.jpg'),
                           ('1bc9f4b0d7d5495ba8076befdd512ce1', 'Opel', 'images/banner/opel.jpg'),
                           ('7531e96c15474d56af4e6342f8aea14b', 'Pagani', 'images/banner/pagani.jpg'),
                           ('309c22d39acb4fe4aa068dba7d26dc0f', 'Peugeot', 'images/banner/peugeot.jpg'),
                           ('c48c9aead3504799851a669a79e0116b', 'PGO', 'images/banner/pgo.jpg'),
                           ('1fd0065cebcd4f1ebb07f83bffc7bba3', 'Piaggio', 'images/banner/piaggio.jpg'),
                           ('60f296cb7c4c436c834428c662563d13', 'Porsche', 'images/banner/porsche.jpg'),
                           ('5f07d4327222489b8fe7979db007caa1', 'Renault', 'images/banner/renault.jpg'),
                           ('a25d8b25853245f291abbe514d498c18', 'Rollsroyce', 'images/banner/rolls_royce.jpg'),
                           ('ba35df8393c44c8585c47fb41e653629', 'Saab', 'images/banner/saab.jpg'),
                           ('01ed8267cdff43a1ac008e6c2b1ecebc', 'Samsung', 'images/banner/samsung.jpg'),
                           ('ea6d2e705424436791b8d170d55a5146', 'Scion', 'images/banner/scion.jpg'),
                           ('fd52132940fa469784b038a80e4ff33a', 'Seat', 'images/banner/seat.jpg'),
                           ('ffd984e3d3f94bcb8fa75bd84c3f4222', 'Skoda', 'images/banner/skoda.jpg'),
                           ('7765e98edbbd4b15960ddabd31336cbf', 'Smart', 'images/banner/smart.jpg'),
                           ('ae5a8e98340c4cf08066949332930ae6', 'Ssangyong', 'images/banner/ssangyong.jpg'),
                           ('9c1605b89c8b4915b2d4e46b14df10f6', 'Subaru', 'images/banner/subaru.jpg'),
                           ('52faa11f5ec54ce5838cf97f2e3f134d', 'Suzuki', 'images/banner/suzuki.jpg'),
                           ('e05326a5c2e74a9e8a0a757dc2e72819', 'Tata', 'images/banner/tata.jpg'),
                           ('147f4e90de1d436bb5a841d349f903cf', 'Toyota', 'images/banner/toyota.jpg'),
                           ('53615136027145acb6e1c93790c14099', 'Volkswagen', 'images/banner/volkswagen.jpg'),
                           ('dcec2ab3d56748c4ae59257d8a54cc7a', 'Volvo', 'images/banner/volvo.jpg'),
                           ('d1ab1c27aba54fb58d1afaa504318da2', 'Westfield', 'images/banner/westfield.jpg'),
                           ('395fb48f48f04800a7e904713bfe0e44', 'Wiesmann', 'images/banner/wiesmann.jpg')"""

    cursor = connection.cursor()
    cursor.execute(mySql_insert_query)
    connection.commit()
    print(cursor.rowcount, "Record inserted successfully into CarBrand table")
    cursor.close()

except mysql.connector.Error as error:
    print("Failed to insert record into CarBrand table {}".format(error))

finally:
    if (connection.is_connected()):
        connection.close()
        print("MySQL connection is closed")

