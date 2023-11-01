from milk import ThePriceOfMilk

import pickle


if __name__ == "__main__":
    print("I can create an object and (of course) it works")
    price = ThePriceOfMilk(2, 99)
    price.tell_me_the_price()

    print("Pickle the object")
    with open("../price.pkl", "wb") as f:
        pickle.dump(price, f)

    print("Let's load the object just to prove that it works")
    with open("../price.pkl", "rb") as f:
        loaded_price = pickle.load(f)
    loaded_price.tell_me_the_price()
