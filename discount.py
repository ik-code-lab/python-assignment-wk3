price = float(input("enter the price:"))
discount_percent = int(input("enter the percentage:"))
def calculate_discount(price, discount_percent):
    if discount_percent >=20:
        discount_percent = discount_percent / 100
        discount = discount_percent * price
        new_price = price - discount
        print(f"the discount is {discount_percentage}, and new price now is{new_price}, thanks for shopping with us")
    else:
        print(f"the percentage {discount_percent}, is too low. the {price} is the original price, thanks for shopping with us")
        calculate_discount(price, discount_percent)