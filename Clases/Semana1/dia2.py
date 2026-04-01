#prices = ['10','12','25','30'] #.16%
#a = .16
#final_prices = []
#for i in prices:
    #tax = round(int(i) + (int(i)*a))
    #final_prices.append(tax)
#print(final_prices)


productlist = [
    {
        'product_name':'ManZana',
        'price': 10.5
    },
    {
        'product_name':'peRa',
        'price': 11     
    },
    {
        'product_name':'piÑa',
        'price': None      
    },
    {
        'product_name':'uVa',
        'price': '???'      
    }
]




def standarize(prices):
    for i in prices:
        price = i['price']
        name = i['product_name']
        i['product_name'] = name.lower()

        if isinstance(price,int):
            pass
        elif price is None:
            try:
                #print('a')
                i['price'] = int(input(f'Ingresa un precio ENTERO para tu producto {name}: '))
            except:
                print("Te dije entero wei >:(")
        elif isinstance(price,str):
            try:
                respuesta =input(f"tu producto tiene texto por precio el texto es: {price.lower()}, quieres comvertirlo a entero? y/n ")
                if respuesta == 'y':
                    try:
                        i['price'] = int(price)
                    except:
                        print("No era numero tio >:( ")
                        costo = int(input("Ingresa un costo entero "))
                        i['price'] = costo
                elif respuesta == 'n':
                    costo = int(input("Ingresa un costo entero "))
                    i['price'] = costo    
            except:
                print("Respuesta no valida")
        elif isinstance(price,float):
            i['price'] = round(price)
    return prices
    
a = standarize(productlist)






    


