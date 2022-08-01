class Manufacturer:
    def __init__(self, name, shipping_speed, status = True, id = None, ):
        self.name = name
        self.shipping_speed = shipping_speed
        self.status = status
        self.id = id
    
    def deactivated(self):
        self.status = False
