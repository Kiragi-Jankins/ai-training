import csv

with open('prices.csv', encoding='utf-8') as file:
    rdr = csv.DictReader(file, delimiter=';')
    best_product = None
    for shop in rdr:
        for product in shop:
            if product == 'Магазин':
                continue
            price = int(shop[product])
            shop_name = shop['Магазин']
            cur_product = (price, product, shop_name)
            if best_product is None or cur_product < best_product:
                best_product = cur_product
    print(f'{best_product[1]}: {best_product[2]}')