def split_price(price):
    price_zl = price // 100
    price_gr = price % 100

    return (price_zl, price_gr)


def get_description(name, price):
    zl, gr = split_price(price)

    return f'Price of {name} is {zl}.{gr:02}'


def print_description(name, price):
    description = get_description(name, price)
    print(description)


def get_product():
    name = input('Enter product name: ')
    price = input('Enter product price: ')

    return (name, int(price))


def get_total_price(receipt):
    total_value = 0
    for name, price in receipt:
        total_value += price

    return total_value


def format_price(price):
    zl, gr = split_price(price)

    return f'{zl}.{gr:02}'


def print_receipt(date, receipt):
    print(date)

    current_position = 1
    for name, price in receipt:
        price = format_price(price)
        print(f'{current_position:2}. {name:19} {price:>6}')
        current_position += 1

    print('-' * 30)

    total_value = get_total_price(receipt)
    formatted_value = format_price(total_value)
    print(f'TOTAL: {formatted_value:>23}')


receipt = [
    ('Bananas', 499),
    ('Oranges', 803),
    ('Milk', 315)
]

print_receipt('2021-03-22', receipt)
