from milk import ThePriceOfMilk

import pickle


if __name__ == "__main__":
    print("The class still works within the current code (of course)")
    price = ThePriceOfMilk(3, 99)
    price.tell_me_the_price()
    print()

    print("I can still load the pickle")
    with open("../price.pkl", "rb") as f:
        loaded_price = pickle.load(f)
    print()

    print("But it doesn't work")
    loaded_price.tell_me_the_price()
    print()
