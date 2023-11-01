class ThePriceOfMilk:
    def __init__(self, dollars, cents):
        self.dollars = dollars
        self.cents = cents

    def tell_me_the_price(self):
        print(f"It's ${self.dollars}.{self.cents:02}")
