import csv
import os
from connecting_to_db import create_db_connection

connection = create_db_connection()  

def clear(): return os.system('cls' if os.name == 'nt' else 'clear')

file = open('/workspace/2021-02-23-isle-of-wight.csv')

def extract_and_remove_sensitive_data(file):   
    data = [] 
    try:
            fieldnames=['date_time','location','full_name','order','payment_type','amount','card_details']
            source_file = csv.DictReader(file, fieldnames = fieldnames, delimiter=',')
            # next(source_file) #ignore the header row 
            
            
            for row in source_file:
                row = dict(row)
                if 'card_details' in row:
                    del row['card_details']
                if 'full_name' in row:
                    del row['full_name']
                if 'payment_type' in row:
                    del row['payment_type']
                data.append(row)
    except Exception as error:
        print("An error occurred: " + str(error))
    return data


def products_from_orders(data):
    list_of_all = []
    products_ordered = []
    for d in data:
        items = d['order']
        single_order = items.split(",")

        total = len(single_order)

        n = 0
        my_order = []
        products_of_transcation = []
        list_of_all.append(products_of_transcation)
        products_of_transcation.clear()


        while n < total:                
            product_size = single_order[(n)]                       
            product_name = single_order[(n+1)]     
            product_price = single_order[(n+2)]   
            if product_size == '':
                product_size = 'Standard'
            new_product = { 'product_name': product_name,
                            'product_size': product_size,
                            'product_price':product_price
                            }
            products_of_transcation.append(new_product)
            n += 3
                  
    return list_of_all


def list_no_duplicates(list_of_all):
    list_not_duplicated = []
    for p in list_of_all:
        for tr in p: 
            if tr not in list_not_duplicated:
                list_not_duplicated.append(tr)
            else:
                pass  
    return list_not_duplicated


def list_of_orders_indexed(list_of_all):
    list_of_orders_with_transac_id = []
    count = 0
    for order in list_of_all:
        count += 1
        for dicct in order:
            dicct["transaction_id"] = count
        list_of_orders_with_transac_id.append(order)
    return list_of_orders_with_transac_id

## Extracting all products and their ids from the products table into a temporary data structure 
# this only works if the products table is created and populated 

def get_product_id_db():
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
    return product_id_list

def get_product_name_db():
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
    return product_name_list  

def get_product_size_db():
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
    return product_size_list     

def zipping_product_stuff():
    joint_three = (list(zip(get_product_id_db(), get_product_name_db(), get_product_size_db())))
    return joint_three

def convert_tuple_to_dict(joint_three):
    unique_prod_id_name_size = []

    for j in joint_three:
        new_productss = {'product_id': j[0],
                        'product_name': j[1],
                        'product_size':j[2]
                        }
        unique_prod_id_name_size.append(new_productss)
    return unique_prod_id_name_size
    
def basket_table(unique_prod_id_name_size, list_of_orders_with_transac_id):
    product_and_transaction_ids = []
    for i in list_of_orders_with_transac_id:
        for dicct in i:
            for x in unique_prod_id_name_size:
                if dicct["product_name"] == x["product_name"] and dicct["product_size"] == x["product_size"]:
                    unique_products = { 'product_id': x['product_id'],
                        'transaction_id': dicct['transaction_id']

                        }
                    product_and_transaction_ids.append(unique_products)
    return(product_and_transaction_ids)

def date_time(data):
    date_time_list = []
    
    for item in data:
        date_time = item['date_time']
        
        if len(date_time) >16:
            date_time = date_time[:-3]
        else:
            pass
 
        date_time_list.append(date_time)
        
    return date_time_list

# def date_time(data):
#     date_time_list = []
    
#     for item in data:
#         date_time = item['date_time']
#         date_time = date_time.replace("/", "-")
#         if len(date_time) >16:
#             date_time = date_time[:-3]
#         else:
#             pass
 
#         date_time_list.append(date_time)
        
#     return date_time_list


def branch_location(data):
    branch_location_list = []
    branch_location_list_unique = []
    for item in data:
        branch_location = item['location']
        branch_location_list.append(branch_location)
        branch_location_list_unique = set(branch_location_list)
    
    return branch_location_list_unique
      
def amount(data):
    amount_list = []
    
    for item in data:

        amount = item['amount']
        amount_list.append(amount)
        
    return amount_list



if __name__ == '__main__':
    connection = create_db_connection()            
    data = extract_and_remove_sensitive_data(file)
    list_of_all = products_from_orders(data)
    list_not_duplicated = list_no_duplicates(list_of_all)
    list_of_orders_with_transac_id = list_of_orders_indexed(list_of_all)

    # # this only works if the products is created and populated
    joint_three = zipping_product_stuff()
    unique_prod_id_name_size = convert_tuple_to_dict(joint_three)
    product_and_transaction_ids = basket_table(unique_prod_id_name_size, list_of_orders_with_transac_id)
    
