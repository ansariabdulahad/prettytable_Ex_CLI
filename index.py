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
    product = {
        "title" : "Sumsung Galxy",
        "price" : 9999,
        "discount" : 17,
        "curency" : "$"
    }
    calc = Calculate(product)
    print("Product: ", product['title'])
    print("Price: ", product["curency"], product['price'], sep="")
    print("Discount: ", product["curency"], product['discount'], sep="")
    print("----------------------------------------------------------------")
    print("saved amount: ", product["curency"], calc['savedAmount'], sep="")
    print("Payable Amount: ", product['curency'], calc['amount'], sep="")
App()