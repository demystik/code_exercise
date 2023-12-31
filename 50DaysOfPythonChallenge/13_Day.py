#!/usr/bin/python3

def your_var():
    #Ask for user input
    try:
        price = int(input('The price of the item:📦 '))
        vat = input('Your current vat:')
        if vat.find("%") > 0:
            vat = vat.replace("%", "")
        vat = int(vat)
    except ValueError:
        print("Please Enter correct values!🤝 \n")
        your_var()
    else:
        vat = price * vat / 100
        newPrice = vat + price
        # print("Your vat with price is: #{:.2f}".format(newPrice))
        print(f"Your vat with price is: #{newPrice:.2f}")

if __name__ == "__main__":
    your_var();