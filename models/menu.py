class Menu:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __repr__(self):
        return f"<Menu(id={self.id}, name={self.name})>"

class MenuItem:
    def __init__(self, id, name, price, menu_id):
        self.id = id
        self.name = name
        self.price = price
        self.menu_id = menu_id

    def __repr__(self):
        return f"<MenuItem(id={self.id}, name={self.name}, price=${self.price}, menu_id={self.menu_id})>"
