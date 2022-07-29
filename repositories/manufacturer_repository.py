from db.run_sql import run_sql

from models.manufacturer import Manufacturer
from models.product import Product

def save(manufacturer):
    sql = "INSERT INTO manufacturers (name, shipping_speed, status) VALUES (%s, %s, %s) RETURNING *"
    values = [manufacturer.name, manufacturer.shipping_speed, manufacturer.status]
    results = run_sql(sql, values)
    id = results[0]['id']
    manufacturer.id = id
    
    return manufacturer

def select_all():
    manufacturers = []

    sql = "SELECT * FROM manufacturers"
    results = run_sql(sql)

    for row in results:
        manufacturer = Manufacturer(row['name'], row['shipping_speed'], row['status'], row['id'])
        manufacturers.append(manufacturer)
    
    return manufacturers 

def select(id):
    manufacturer = None

    sql = "SELECT * FROM manufacturers WHERE id = %s"
    values=[id]
    results = run_sql(sql, values)

    if results:
        result = results[0]
        manufacturer = Manufacturer(result['name'], result['shipping_speed'], result['status'], result['id'])

    return manufacturer

def delete_all():
    sql = "DELETE FROM manufacturers"
    run_sql(sql)

def update(manufacturer):
    sql = "UPDATE manufacturers SET (name, shipping_speed, status) = (%s, %s, %s) WHERE id= %s"
    values = [manufacturer.name, manufacturer.shipping_speed, manufacturer.status, manufacturer.id]
    run_sql(sql,values)

