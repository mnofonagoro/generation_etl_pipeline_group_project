import csv
import os
# from connecting_to_db import create_db_connection 
import psycopg2

dbname = os.environ["DB"]
host = os.environ["HOST"]
port = os.environ["PORT"]
user = os.environ["DB_USER"]
password = os.environ["PASSWORD"]

connection = psycopg2.connect(dbname=dbname, host=host,
                           port=port, user=user, password=password)

# connection = create_db_connection()  

def clear(): return os.system('cls' if os.name == 'nt' else 'clear')

#file = open('/workspace/birmingham_23-03-2021_09-00-00.csv')

def extract_and_remove_sensitive_data(file):
    data = [] 
    try:
        fieldnames=['date_time','location','full_name','order','amount','payment_type','card_details']

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


def cleaning(data):
    products = []
    for d in data:
        order_info = (d['order'])
        # print(order_info)
        per_order = order_info.split(",")
        # print(per_order)
        products_of_transcation = []
        products.append(products_of_transcation)
        products_of_transcation.clear()
        
        for i in per_order:
            i = i.rsplit("-",1)
            # print(i)           
            p = i[0]  
            # print(p)
            pns = p.split()[1:]  
            # print(pns)
            product_name = " ".join(pns)
            # print(product_name)
            
            product_price_old = i[1] 
            product_price = product_price_old.replace(" ","")
             
            product_size = i[0].split()[0]
            # print(product_size)

            new_product = { 'product_name': product_name,
                            'product_size': product_size,
                            'product_price':product_price
                            }
            products_of_transcation.append(new_product)
            # print(new_product)

    return products


def list_no_duplicates(list_of_all_products):
    list_not_duplicated = []
    for p in list_of_all_products:
        for tr in p: 
            if tr not in list_not_duplicated:
                list_not_duplicated.append(tr)
            else:
                pass  
    return list_not_duplicated


def list_of_orders_indexed(list_of_all_products):
    list_of_orders_with_transac_id = []
    count = 0
    for order in list_of_all_products:
        count += 1
        for dicct in order:
            dicct["transaction_id"] = count
        list_of_orders_with_transac_id.append(order)
    return list_of_orders_with_transac_id

def adding_branch(list_of_all_products, data):
    list_of_orders_with_branch = []
    for d in data:
        for order in list_of_all_products:
            for one in order:
                one["branch_location"] = d['location']
            list_of_orders_with_branch.append(order)
    return list_of_orders_with_branch



## Extracting all products and their ids from the products table into a temporary data structure 
# this only works if the products is created and populated 

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

def get_branch_id_db():
    branch_id_list = []
    try:
            with connection.cursor() as cursor:
                sql = "SELECT branch_id FROM branch"    
                cursor.execute(sql)
                my_result_b = cursor.fetchall()
                for id in my_result_b:
                    branch_id_list.append(id[0])
    except Exception as e:
        print(e)         
    return branch_id_list

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

def get_branch_name_db():
    branch_name_list = []
    try:
            with connection.cursor() as cursor:
                sql = "SELECT branch_location FROM branch"    
                cursor.execute(sql)
                my_result_2b = cursor.fetchall()
                for name in my_result_2b:
                   branch_name_list.append(name[0])
    except Exception as e:
        print(e)    
    return  branch_name_list

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

def zipping_branch_stuff():
    joint_two = (list(zip(get_branch_id_db(), get_branch_name_db())))
    return joint_two

def convert_tuple_to_dict(joint_three):
    unique_prod_id_name_size = []

    for j in joint_three:
        new_productss = {'product_id': j[0],
                        'product_name': j[1],
                        'product_size':j[2]
                        }
        unique_prod_id_name_size.append(new_productss)
    return unique_prod_id_name_size
 
def convert_branch_tuple_to_dict(joint_two):
    branch_id_loc = []

    for j in joint_two:
        new_productss = {'branch_id': j[0],
                        'branch_location': j[1]
                        
                        }
        branch_id_loc.append(new_productss)
    return branch_id_loc  

def branch_id_transaction(branch_id_loc, list_of_orders_with_branch):
    corrected_branch_id = []
    for it in list_of_orders_with_branch:
        for d in it:
            for b in branch_id_loc:
                if d["branch_location"] == b["branch_location"]:
                    branch = { 'branch_id': b["branch_id"]
                                         }
                    corrected_branch_id.append(branch)
    return branch


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
        date_time = date_time.replace("/", "-")
        if len(date_time) >16:
            date_time = date_time[:-3]
        else:
            pass
 
        date_time_list.append(date_time)
        
    return date_time_list


def branch_location(data):
    branch_location_list = []
    branch_location_list_unique = []
    for item in data:
        # print(item)
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
    # connection = create_db_connection()            
    data = extract_and_remove_sensitive_data(file)
    
    list_of_all_products = cleaning(data)
    # print(list_of_all_products)
    
    list_not_duplicated = list_no_duplicates(list_of_all_products)
    # print(list_not_duplicated)
    
    list_of_orders_with_branch = adding_branch(list_of_all_products, data)
    
    list_of_orders_with_transac_id = list_of_orders_indexed(list_of_all_products)
    # print(list_of_orders_with_transac_id)

    # # this only works if the products is created and populated
    joint_three = zipping_product_stuff()
    
    ## this only works if the the branch table is created and populated
    joint_two = zipping_branch_stuff()
    
    ## This is to enter branch_id in transaction table
    branch_id_loc = convert_branch_tuple_to_dict(joint_two)
    
    corrected_branch_id = branch_id_transaction(branch_id_loc, list_of_orders_with_branch)
    # trans_branch_id = corrected_branch_id['branch_id']
    # print(trans_branch_id)
    
    ## Used to load into basket table
    unique_prod_id_name_size = convert_tuple_to_dict(joint_three)
    # print(unique_prod_id_name_size)
    
    product_and_transaction_ids = basket_table(unique_prod_id_name_size, list_of_orders_with_transac_id)
    
    
    # print(list_not_duplicated)
    # print(date_time(data)[:5])