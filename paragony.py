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
    product_prices = {
        'Bananas': 499,
        'Oranges': 1803,
        'Milk': 315,
        'Lollipop': 100,
        'Bread': 509
    }

    name = input('Enter product name: ')
    amount = input('Enter amount: ')

    return (name, int(amount) * product_prices.get(name, 0))


def get_total_price(receipt):
    total_value = 0
    for name, price in receipt:
        total_value += price

    return total_value


def format_price(price):
    zl, gr = split_price(price)

    return f'{zl}.{gr:02}'


def print_product(current_position, product):
    name, price = product
    price = format_price(price)
    tax_group = get_tax_group(name)
    print(f'{current_position:2}. {name:17} {price:>6} {tax_group}')


def print_receipt(date, receipt):
    if (not receipt):
        print('Receipt is empty!')
        return

    print(date)

    current_position = 1
    for product in receipt:
        print_product(current_position, product)
        current_position += 1

    print('-' * 30)

    total_tax_value = get_total_tax(receipt)
    formatted_value = format_price(total_tax_value)
    print(f'TAX: {formatted_value:>25}')

    total_value = get_total_price(receipt)
    formatted_value = format_price(total_value)
    print(f'TOTAL: {formatted_value:>23}')

    formatted_value = format_price(total_tax_value + total_value)
    print(f'TOTAL+TAX: {formatted_value:>19}')


def get_tax_group(product):
    tax_group_A = {'Milk', 'Bread'}
    tax_group_B = {'Bananas', 'Oranges'}

    if (product in tax_group_A):
        return 'A'
    elif (product in tax_group_B):
        return 'B'
    else:
        return 'E'


def get_total_tax(receipt):
    tax_values = {
        'A': 12,
        'B': 8,
        'E': 22,
    }

    total_value = 0
    for name, price in receipt:
        tax_group = get_tax_group(name)
        total_value += price * tax_values.get(tax_group)

    return round(total_value / 100)


receipt = [
    ('Bananas', 499),
    ('Oranges', 1803),
    ('Milk', 315),
    ('Lollipop', 100)
]

# receipt = []
# for i in range(6):
#     receipt.append(get_product())

print_receipt('2021-03-22', receipt)
