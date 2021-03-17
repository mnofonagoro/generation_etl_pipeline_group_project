from connecting_to_db import create_db_connection
import csv

list_of_orders = []

list_of_orders_with_index = []

def extract_and_remove_sensitive_data():
        
    data = [] 
    
    print("Extracting...")
    try:
        with open('/workspace/2021-02-23-isle-of-wight.csv', 'r') as file:
            fieldnames=['date_time','location','full_name','order','payment_type','amount','card_details']
            source_file = csv.DictReader(file, fieldnames = fieldnames, delimiter=',')
            next(source_file) #ignore the header row
            for row in source_file:
                row = dict(row)
                if 'card_details' in row:
                    del row['card_details']
                if 'full_name' in row:
                    del row['full_name']
                if 'payment_type' in row:
                    del row['payment_type']
                data.append(row)
            # print("Successfully Extracted")
    except Exception as error:
        print("An error occurred: " + str(error))
    return data

def products_from_orders(data):
    # print(data[-1])
    # list_of_orders = []
    products_ordered = []
    for d in data:
        items = d['order']
        single_order = items.split(",")
        total = len(single_order)
        n = 0
        my_order = []
        # print(single_order)
        # print(my_order)
        while n < total:                
            product_name = single_order[(n+1)]     
            product_price = single_order[(n+2)]   
            product_size = single_order[(n)]                       
            if product_size == '':
                product_size = 'Standard'
            new_product = { 'product_name': product_name,
                            'product_size': product_size,
                            'product_price':product_price
                            }
            products_ordered.append(new_product)
            # 'order' is now a list of product dictionaries
            
            my_order.append(new_product)
            d['order'] = my_order
            # print(new_product)
            n += 3
            list_of_orders.append(my_order)
    # print(list_of_orders)        
    return products_ordered

def list_of_orders_indexed():
    count = 1
    for order in list_of_orders:
        # print(order)
        for dicct in order:
            dicct["id"] = count
            # print(dicct)
            # int(list_of_orders.index(order)) 
        count += 1
        list_of_orders_with_index.append(order)
    return list_of_orders_with_index


data = extract_and_remove_sensitive_data()
products = products_from_orders(data)
list_of_orders_indexed()




connection = create_db_connection()


transaction_1 = {"Hot chocolate" : "Large",
                 "Chai latte": "Large",
                 "Hot chocolate": "Large"}
transaction_2 = {"Latte": "Large"}
transaction_3 = {"Frappes - Coffee": "Standard",
                 "Cortado": "Standard", 
                 "Glass of milk": "Standard", 
                 "Speciality Tea - Camomile": "Standard", 
                 "Speciality Tea - Camomile": "Standard"}

list_of_transactions = []

list_of_transactions.append(transaction_1)
list_of_transactions.append(transaction_2)
list_of_transactions.append(transaction_3)


# dictionarylst = {1:"Hot chocolate",
#                  2: 'Chai latte', 
#                  3:'Latte', 
#                  4:'Frappes - Coffee',
#                  5:'Cortado'}

# def replace(ltransaction_1, dictionarylst):
#     for k,v in enumerate(transaction_1):
#         if v in dictionarylst:
#             transaction_1[k] = dictionarylst[v]
#     return transaction_1


# print(replace(list_of_transactions, dictionarylst))


# def replace(list_of_transactions, dictionary):
#     return [dictionarylst.get(item, item) for item in list_of_transactions]

# print(replace(list_of_transactions,dictionarylst))



# dictionarycleaned = {}

# def match_pattern(list_of_transactions,value):
#     new_list = []
#     for text in value:
#         # temp variable hold latest updated text
#         temp = text
#         for word in list_of_transactions:
#             if word in text:
#                 # replace text string with whitespace if word in text
#                 temp = temp.replace(word,"")
#         new_list.append(temp)
#     return new_list
    
    
# for k,v in dictionarylst.items():

#     dictionarycleaned[k] = match_pattern(list_of_transactions, v)

# print(dictionarycleaned)

# print(match_pattern(list_of_transactions,value))









# print(list_of_transactions)

## Extracting all products and their ids from the products table into a temporary data structure 
# replace the name from my list_of _transactions with the corresponding numbers from the joint_2 list below 

product_id_list = []
try:
        with connection.cursor() as cursor:
            sql = "SELECT product_id FROM product"    
            cursor.execute(sql)
            my_result = cursor.fetchall()
            for id in my_result:
                product_id_list.append(id[0])
except Exception as e:
    print(e)         

# print(product_id_list)

product_name_list = []
try:
        with connection.cursor() as cursor:
            sql = "SELECT product_name FROM product"    
            cursor.execute(sql)
            my_result_2 = cursor.fetchall()
            for name in my_result_2:
                product_name_list.append(name[0])
except Exception as e:
    print(e)      

# print(product_name_list)

product_size_list = []
try:
        with connection.cursor() as cursor:
            sql = "SELECT product_size FROM product"    
            cursor.execute(sql)
            my_result_3 = cursor.fetchall()
            for size in my_result_3:
                product_size_list.append(size[0])
except Exception as e:
    print(e)     





joint_three = (list(zip(product_id_list, product_name_list, product_size_list)))


# def workkkkk():
#     for tuple in joint_three:
#         for index in tuple:
#             for i in list_of_transactions:
#                 if index[1] and index[2] == i.items():
#                 pass

# b_dict = {x['name']: x for x in b}
# for item in a:
#     if item['name'] in b_dict:
#         f(b_dict['name']) 
#     else:
#         pass  # whatever



# print(joint_three)

print("\n")
print("\n")
print("\n")
print("\n")

print(list_of_orders_with_index[0])

orders_and_products = []
for items in list_of_orders:
    for dicct in items:
        a = dicct["id"]
        b = dicct["product_name"]
        c = dicct["product_size"]
        # print(dicct)
        for elem in joint_three:
            if elem[0] == a and elem[1] == b and elem[2] == c:
                orders_and_products.append(dict(zip(a,elem[0])))

# print(orders_and_products)
# print(list_of_transactions)

