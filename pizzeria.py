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

def order_request(order,pizza_options):
    request = input("Order")
    for request in pizza_options[0]["Name"]:
        order.append(request)

def pizza_preparation(order, pizza_prepare):
    if len(order) > 0 :
        for pizza in order:
            pizza_prepare.append(pizza)

def stock_manage(stock):
    for ingredients in stock:
        print(ingredients)

order_request(order,pizza_options)

pizza_preparation(order,pizza_prepare)

print(order)
print (pizza_prepare)

