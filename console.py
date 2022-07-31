import pdb
from models.product import Product
from models.manufacturer import Manufacturer

import repositories.manufacturer_repository as manufacturer_repository
import repositories.product_repository as product_repository

product_repository.delete_all()
manufacturer_repository.delete_all()

manufacturer1 = Manufacturer("Nike", "Fast Shipping")
manufacturer_repository.save(manufacturer1)


manufacturer2 = Manufacturer("New Balance", "Standard")
manufacturer_repository.save(manufacturer2)

manufacturer3 = Manufacturer("Adidas", "Standard")
manufacturer_repository.save(manufacturer3)

manufacturer4 = Manufacturer("Asics", "Fast Shipping")
manufacturer_repository.save(manufacturer4)


product1 = Product("Nike Cortez", "Navy/White", 7, 4, 90, 135, manufacturer1)
product_repository.save(product1)

product2 = Product("Air Jordan 3", "University Red/White", 8, 4, 90, 135, manufacturer1)
product_repository.save(product2)

product3 = Product("Air Jordan 1", "Royal Blue", 4, 0, 149, 210, manufacturer1)
product_repository.save(product3)

product4 = Product("Air Force 1 Low", "Triple White", 7, 15, 90, 140, manufacturer1)
product_repository.save(product4)

product5 = Product("Yeezy 350 V2", "Cinder", 9, 2, 180, 220, manufacturer3)
product_repository.save(product5)

product6 = Product("Yeezy Slides", "Bone", 6, 8, 70, 130, manufacturer3)
product_repository.save(product6)

product7 = Product("New Balance 2002R", "Protection Pack/Green", 7, 12, 130, 180, manufacturer2)
product_repository.save(product7)

product8 = Product("New Balance 900V3", "Marvel Head/ Grey", 10, 0, 200, 260, manufacturer2)
product_repository.save(product8)








# product2.name = "Trainer"

# product_repository.update(product2)

# show1= product_repository.select(product2.id)

# print(show1.__dict__)



# manufacturer_repository.select(3)

# manufacturer1.name = "Adidas"
# manufacturer1.shipping_speed = "Standard"

# manufacturer_repository.update(manufacturer1)

# manufacturer1_db = manufacturer_repository.select(manufacturer1.id)

# print(manufacturer1_db.__dict__)