class Product:

    def __init__(self, name, description, size, stock_quantity, buying_cost, selling_price, manufacturer, id = None, ):
        self.name = name
        self.description = description
        self.size = size
        self.stock_quantity = stock_quantity
        self.buying_cost = buying_cost
        self.selling_price = selling_price
        self.manufacturer = manufacturer
        self.id = id
    
    def markup(self):
        markup = round((self.selling_price - self.buying_cost)/ self.buying_cost * 100)
        return markup
