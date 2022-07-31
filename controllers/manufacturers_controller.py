from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.manufacturer import Manufacturer
import repositories.manufacturer_repository as manufacturer_repository
import repositories.product_repository as product_repository

manufacturers_blueprint = Blueprint("manufacturers", __name__)

@manufacturers_blueprint.route('/manufacturers')
def manufacturers():
    manufacturers = manufacturer_repository.select_all()
    return render_template('manufacturers/index.html', all_manufacturers = manufacturers)

@manufacturers_blueprint.route('/manufacturers/new')
def new_manufacturer():
    return render_template('manufacturers/new.html')

@manufacturers_blueprint.route('/manufacturers', methods=['POST'])
def add_manufacturer():
    name = request.form['name']
    shipping_speed = request.form['shipping_speed']
    status = request.form['status']
    
    new_manufacturer = Manufacturer(name, shipping_speed, status)
    manufacturer_repository.save(new_manufacturer)
    return redirect('/manufacturers')

@manufacturers_blueprint.route('/manufacturers/<id>')
def view_manufacturer(id):
    manufacturer = manufacturer_repository.select(id)
    products_assigned = product_repository.select_all_with_manufacturer_id(id)
    return render_template('manufacturers/view.html', manufacturer = manufacturer, products = products_assigned)

@manufacturers_blueprint.route('/manufacturers/<id>/delete', methods=['POST'])
def delete(id):
    manufacturer_repository.delete(id)
    return redirect('/manufacturers')

@manufacturers_blueprint.route('/manufacturers/<id>/edit')
def get_edit_form(id):
    manufacturer_to_update = manufacturer_repository.select(id)
    return render_template('manufacturers/edit.html', manufacturer = manufacturer_to_update)

@manufacturers_blueprint.route('/manufacturers/<id>', methods=['POST'])
def update(id):
    name = request.form['name']
    shipping_speed = request.form['shipping_speed']
    status = request.form['status']
    manufacturer_to_update = Manufacturer(name, shipping_speed, status, id)
    manufacturer_repository.update(manufacturer_to_update)
    return redirect('/manufacturers/' + id)