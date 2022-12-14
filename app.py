from flask import Flask, render_template


from controllers.products_controller import products_blueprint
from controllers.manufacturers_controller import manufacturers_blueprint



app= Flask(__name__)

app.register_blueprint(products_blueprint)
app.register_blueprint(manufacturers_blueprint)




@app.route('/')
def home():
    return render_template('home.html')


if __name__ == '__main__':
    app.run(debug=True)