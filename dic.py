from prettytable import PrettyTable

def Calculate(product) :
    price = product['price']
    discount = product['discount']
    savedAmount = (price*discount/100)
    amount = price - savedAmount
    return {
        "amount": amount,
        "savedAmount": savedAmount
    }

def App() :
    products = [
        {
            "title" : "Sumsung Galxy",
            "price" : 9999,
            "discount" : 17,
            "curency" : "$"
        },
        {
            "title" : "MI Phones",
            "price" : 10000,
            "discount" : 11,
            "curency" : "$"
        },
        {
            "title" : "Moto edge",
            "price" : 20000,
            "discount" : 18,
            "curency" : "$"
        },
        {
            "title" : "Redmi MIUI",
            "price" : 12000,
            "discount" : 12,
            "curency" : "$"
        },
        {
            "title" : "Oppo",
            "price" : 23000,
            "discount" : 24,
            "curency" : "$"
        }
    ]
    table = PrettyTable()
    table.field_names = ['Title', 'Price', 'Discount', 'Curency', 'Payable Amount']
    for product in products:
        calc = Calculate(product)
        table.add_row([product['title'], product['price'], product['discount'], product['curency'], calc['amount']])
    print(table)
App()