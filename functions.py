available_parts = {1: 'T-Shirt',
2: 'Shorts',
3: 'Jeans',
4: 'Slacks',
5: 'Polos',
6: 'Button Down',
}

price_quantity = {'T-Shirt': {'price': 25, 'quantity' : 10},
'Shorts': {'price': 45, 'quantity': 8},
'Jeans': {'price': 85, 'quantity' : 6},
'Slacks': {'price': 100, 'quantity': 0},
'Polos': {'price': 35, 'quantity': 10},
'Button Down': {'price': 95, 'quantity' : 3}
}

   

def shopping_cart_calc():
    user_input = -1
    cost = 0
    
    while user_input != 0:
        if user_input in available_parts:
            chosen_part = available_parts[user_input]
            if price_quantity[chosen_part]['quantity'] > 0:
                print(f'Adding {chosen_part}')
                price_quantity[chosen_part]['quantity'] -= 1
                price = price_quantity[chosen_part]['price']
                cost += price
            else:
                print(f'{chosen_part} is out of stock.')
    
    
        else:
            print('Please type number to add to your shopping cart')
            print('Print 0 to finish shopping')
            for key, value in available_parts.items():
                print(f'{key}: {value}')
        print()
        try:
            user_input = int(input("> "))
        except ValueError as e:
            e = 'Invalid Input. Re-run program.'
            print(e)
            quit()

    print(f'Total Cost (plus tax) = $' + str(round((cost * 1.0825), 2)))

shopping_cart_calc()

if __name__ == '__main__':
    shopping_cart_calc()
