# start small - break it down 

# what are those objects - shopping create_server
# what are their attributes - cart dictionary for item and qty
# what are the piece of functionality - add/delete/show/quit
# what do they act on? - user input


# start simple:
# prevent you from being overwhlemed
# prevent errors

# add functionality piece by piece and resr as you go 

class ShoppingCart():
    def __init__(self):
        self.cart = {}
    
    def show_items(self):
        if self.cart == {}:
            print('your cart is empty')
        else:
            for item in self.cart:
                print(f'you have {self.cart[item]} {item}')

    def add_items(self):
        item = input("what would you like to add? ")
        amount = int(input("how many would you like to add?"))
        if item in self.cart:
            self.cart[item] += amount
        else:
            self.cart[item] = amount 

    def delete_items(self):
        item = input("what would you like to delete?")
        if item.lower() in self.cart:
            del self.cart[item]
        else:
            print('that item isnt in your cart')
    




class UI():
    def __init__(self, shopping_cart):
        self.cart = shopping_cart

def run_program(self):
        while True:
            action = input("would you like to add, delete, show or quit? ")
            if action.lower() == "show":
                self.cart.show_items()
            elif action.lower() == "add":
                self.cart.add_items()
            elif action.lower() == "delete":
                self.cart.delete_item()
            elif action.lower() == "quit":
                self.cart.show_items()
                break
            else:
                print('invalid input, try again please')



my_cart = ShoppingCart()
ui = UI(my_cart)
ui.run_program()