def main():
    shopping_cart = [
        ["tooth paste", "q-tips", "milk"],
        ["milk", "candy", "apples"],
        ["paper", "pencils", "q-tips"]
    ]

    all_in_one = allInOne(shopping_cart)
    print("All items in one list without duplicates:")
    print(all_in_one)

    count_qtips = countQtips(shopping_cart)
    print("Total q-tips count:", count_qtips)


def allInOne(shopping_cart):
    all_items = []
    for cart in shopping_cart:
        for item in cart:
            if item not in all_items:
                all_items.append(item)
    return all_items


def countQtips(shopping_cart):
    total_qtips = 0
    for cart in shopping_cart:
        total_qtips += cart.count("q-tips")
    return total_qtips


main()