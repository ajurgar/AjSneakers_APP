import pdb
from models.product import Product
from models.manufacturer import Manufacturer

import repositories.manufacturer_repository as manufacturer_repository
import repositories.product_repository as product_repository


manufacturer_repository.delete_all()

manufacturer1 = Manufacturer("Nike", "Fast Shipping")
manufacturer_repository.save(manufacturer1)
manufacturer1_db = manufacturer_repository.select(manufacturer1.id)
print(manufacturer1_db.__dict__)

manufacturer2 = Manufacturer("New Balance", "Standard")
manufacturer_repository.save(manufacturer2)


product1 = Product("Nike Cortez", "Navy/White", 4, 90, 135, manufacturer1)
product_repository.save(product1)
# manufacturer_repository.select(3)

manufacturer1.name = "Adidas"
manufacturer1.shipping_speed = "Standard"

manufacturer_repository.update(manufacturer1)

manufacturer1_db = manufacturer_repository.select(manufacturer1.id)

print(manufacturer1_db.__dict__)