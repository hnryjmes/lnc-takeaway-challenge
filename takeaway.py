class Takeaway:

    def __init__(self):
        self.menu = {
                "Pizza": 1.0,
                "Falafel": 1.0
        }
        self.orders = []


    def list_menu_items(self):
        menu_string = ""
        for (item_name, item_price) in self.menu.items():
            menu_string += item_name + ": " + str(item_price) + ", "
        return menu_string

    def add(self, item, quantity=1):
        self.orders.append(
            {
                item: self.menu.get(item) * quantity
            }
        )
