def stock_availability(*args):
    stock = [item for item in args[0]]
    if args[1] == 'delivery':
        items_to_add = args[2:]
        for item in items_to_add:
            stock.append(item)
    elif args[1] == 'sell':
        if len(args) > 2:
            if type(args[2]) == int:
                stock = stock[args[2]:]
            elif len(args) > 2:
                items_for_sell = args[2:]
                for item in items_for_sell:
                    if item in stock:
                        while item in stock:
                            stock.remove(item)
        else:
            stock = stock[1:]
    return stock