'''
Imagineu-vos que heu estat contractats per dissenyar el sistema de gestió d'una pizzeria. 
L'objectiu és desenvolupar un conjunt de funcions que permetin gestionar diferents tasques relacionades amb el funcionament de la pizzeria.
Això inclou la presa de comandes, la preparació de pizzes, la gestió de l'estoc d'ingredients i el processament dels pagaments.
Recordeu fer servir disseny top down, i mantenir un baix acoblament i una alta cohesió.

'''
order = []

pizza_prepare = []

stock = [{"Name":"Tomato", "Quantity":2},{"Name":"Cheese", "Quantity":3},{"Name":"Pepperoni", "Quantity":5}]

pizza_options = [{"Name":"Margarita", "Ingredients":["tomato", "cheese"],"Price":10},
                 {"Name":"Pepperoni", "Ingredients":["tomato", "cheese", "pepperoni"],"Price":12},]
count_pizza = 0

ticket = float(0)


def order_request(order,pizza_options, count_pizza):
    aproved = False
    request = input("Order: ")
    while aproved == False :
        if count_pizza < len(pizza_options):
            if request in pizza_options[count_pizza]["Name"]:
                order.append(pizza_options[count_pizza])
                aproved = True
            count_pizza = count_pizza + 1
        else:
            print("we doint have rthe piza you rquest")
            aproved = True


def pizza_preparation(order, pizza_prepare,stock):
    if len(order) > 0 :
        for pizza in order:
            pizza_prepare.append(pizza)
    for pizza in pizza_prepare:
        for ingredients in pizza["Ingredients"]:
            print("")
            #here we substract the ingredient  used to make the pizza to the stock

def stock_manage(stock):
    for ingredients in stock:
        print("")
            #here we're going to be able to add, consult or eliminate stock\
        
order_request(order,pizza_options,count_pizza)

pizza_preparation(order,pizza_prepare,stock)

for pizza in pizza_prepare:
    ticket = pizza_prepare[0]["Price"]

print(f"You requested the pizza {pizza_prepare[0]['Name']}, you have to pay {ticket}€")