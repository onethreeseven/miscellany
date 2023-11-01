class ThePriceOfMilk:
    # At some point before now, we changed the object's internal representation
    # Note that we didn't even change the external interface!
    def __init__(self, dollars, cents):
        self.price = dollars + cents * 0.01

    def tell_me_the_price(self):
        print(f"It's ${self.price:.2f}")
