# from crypt import methods
import pdb
from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.product import Product
import repositories.product_repository as product_repository
import repositories.manufacturer_repository as manufacturer_repository

products_blueprint = Blueprint("/products", __name__)

@products_blueprint.route('/products')
def products():
    products = product_repository.select_all()
    return render_template('/index.html', all_products = products)

@products_blueprint.route('/products/new')
def new_product():
    manufacturer = manufacturer_repository.select_all()
    return render_template('/products/new.html', all_manufacturers = manufacturer)

@products_blueprint.route('/products', methods = ['POST'])
def add_product():
    name = request.form['name']
    description = request.form['description']
    size = request.form['size']
    stock_quantity = request.form['stock_quantity']
    buying_cost = request.form['buying_cost']
    selling_price = request.form['selling_price']
    manufacturer_id = request.form['manufacturer_id']
    manufacturer = manufacturer_repository.select(manufacturer_id)
    product = Product(name, description, size, stock_quantity, buying_cost, selling_price, manufacturer)
    product_repository.save(product)
    return redirect('/products')

@products_blueprint.route("/products/<id>")
def view_product(id):
    product = product_repository.select(id)
    return render_template('/products/view.html', product = product)


