# from connecting_to_db import create_db_connection 
from src.sql_script import create_all_tables
from src.trail import *
from src.sql_script import *
from datetime import datetime
import psycopg2
import os
import copy

dbname = os.environ["DB"]
host = os.environ["HOST"]
port = os.environ["PORT"]
user = os.environ["DB_USER"]
password = os.environ["PASSWORD"]
connection = psycopg2.connect(dbname=dbname, host=host,
                           port=port, user=user, password=password)
                           
print(connection)
                           
def insert_into_product_table(list_not_duplicated_var, connection):
    newest_products_list = [] # populated with anything not already in the DB

    try:
        with connection.cursor() as cursor:
         
            cursor.execute('SELECT * FROM product')
            
            pre_existing_products = cursor.fetchall() #temporary structure for SELECT * results
            
            for product in list_not_duplicated_var:
                pre_existing = False
                for value in pre_existing_products:
                    if product["product_name"] == value[1] and product["product_size"] == value[2]:
                        pre_existing = True
                        break
                if pre_existing == False:
                    newest_products_list.append(product)
            
            for row in newest_products_list:
                cursor.execute("INSERT INTO product (product_name, product_size, product_price) VALUES (%s, %s, %s)",(row['product_name'], row['product_size'], row['product_price']))
                connection.commit()
    except Exception as e:
        print("exception!!", e)
        
        
def insert_into_branch_table(branch_location_w_par, connection):
    branch_locations = branch_location_w_par
    # print(branch_locations)
    newest_branch_list = []
    try:
        # connection = create_db_connection()
        with connection.cursor() as cursor:
            
            cursor.execute('SELECT * FROM branch')
            
            pre_existing_branch = cursor.fetchall()
            
            print(pre_existing_branch)
            
            for branch in branch_locations:
                pre_existing1 = False
                print(branch)
                for value in pre_existing_branch:
                    # print(branch["branch_location"])
                    print("did it work")
                    print(branch, value[1])
                    if branch == value[1]:
                        pre_existing1 = True
                        print("found location match: breaking loop")
                        break
                if pre_existing1 == False:
                    print("no location match: appending to branch list", branch)
                    newest_branch_list.append(branch)
                    
            
            for item in newest_branch_list:
                # print(item)
                # val = item
                # sql = f"INSERT INTO branch (branch_location) VALUES ('{val}')"
                cursor.execute("INSERT INTO branch (branch_location) VALUES (%s)", [item])
                connection.commit()
    except Exception as e:
        print(e)
        
        
def insert_into_transaction_table(corrected_branch_id, our_data, connection):
    try:
        amount_var = amount(our_data)
        date_time_var = date_time(our_data)
        # connection = create_db_connection()
        branch_id = corrected_branch_id['branch_id']  
        with connection.cursor() as cursor:
            for datetime, amt in zip(date_time_var, amount_var):
                sql = "INSERT INTO transaction (date_time, transaction_total, branch_id)  VALUES ('{}', '{}', {})".format(datetime, amt, branch_id) 
                cursor.execute(sql)
            connection.commit()
    except Exception as e:
        print(e) 
        
        
def insert_into_basket_table(product_and_transaction_ids_var, connection):
    try:
        product_and_transaction_list = product_and_transaction_ids_var
        # connection = create_db_connection()
        with connection.cursor() as cursor:
            for row in product_and_transaction_list:
                sql = f"""INSERT INTO basket (product_id, transaction_id)
                    VALUES ('{row['product_id']}', '{row['transaction_id']}')"""   
                cursor.execute(sql)
                connection.commit()
    except Exception as e:
        print(e)
        
# re-establish conn func
def run_loading(file, connection=connection):
    
    connection_open = connection.closed == 0
    if connection_open:
        pass
    else:
        connection = psycopg2.connect(dbname=dbname, host=host,
                                   port=port, user=user, password=password)
        
    
    create_all_tables(connection)
    # create_product_table(con)
    # create_branch_table(con)
    # create_transaction_table(con)
    # create_basket_table(con)
    # close_connection()
    print("Your tables have been created successfully")
    # global data
    
    our_data = extract_and_remove_sensitive_data(file)
    # print("no1")
    # global list_of_all_products
    
    list_of_all_products_var = cleaning(our_data)
    # print("no2")
    # list_of_all = cleaning(our_data)
    # list_of_all = products_from_orders(our_data)
    # global list_not_duplicated
    
    list_not_duplicated_var = list_no_duplicates(list_of_all_products_var)
    # print(list_not_duplicates_var)
    # print("no3") 
    #list_not_duplicated = list_no_duplicates(list_of_all)
    # global list_of_orders_with_branch
    
    list_of_orders_with_branch_var = adding_branch(list_of_all_products_var, our_data)
    # print("no1")
    # global list_of_orders_with_transac_id
    
    # print("before going through list of orders indexed", list_of_all_products_var[0])
    list_of_orders_with_transac_id_var = list_of_orders_indexed(list_of_all_products_var)
    # print("after", list_of_all_products_var[0]) # this keeps changing after being passed as a param in other funcs. deep copy these??
    #print("after going through list of orders indexed", list_of_orders_with_transac_id_var[0])
    
    # print("no4")
    # print(list_of_orders_with_transac_id_var[:10])
    # print(list_not_duplicated_var)
    
    insert_into_product_table(list_not_duplicated_var, connection)
    # print("do we have transaction ids HERE??", list_of_orders_with_transac_id_var[0])
    
    insert_into_branch_table(branch_location(our_data), connection)
    
    # this only works if the products table is created and populated as it depend on it to fetch the tuples.
    # global joint_two 
    print("Starting join branches", datetime.now())
    joint_two = zipping_branch_stuff()
    # print("no7")
    #global joint_three
    joint_three = zipping_product_stuff()
    print("finishing join branches", datetime.now())
    # print("no8")
    #global branch_id_loc
    print("Starting branch id location conversion", datetime.now())
    branch_id_loc = convert_branch_tuple_to_dict(joint_two)
    # print("no9")
    #global corrected_branch_id 
    corrected_branch_id_var = branch_id_transaction(branch_id_loc, list_of_orders_with_branch_var)
    # print("no10")
    #global unique_prod_id_name_size
    print("start unique product id names", datetime.now())
    unique_prod_id_name_size = convert_tuple_to_dict(joint_three)
    # print("no11")
    # global product_and_transaction_ids
    # print("before going into basket table", list_of_orders_with_transac_id_var[0])
    
    product_and_transaction_ids_var = basket_table(unique_prod_id_name_size, list_of_orders_with_transac_id_var)
    # print("no12")
    print("inserting into transaction table", datetime.now())
    insert_into_transaction_table(corrected_branch_id_var, our_data, connection)
    # print("no13")
    print("inserting into basket table", datetime.now())
    insert_into_basket_table(product_and_transaction_ids_var, connection)
    print("finished inserting into basket table", datetime.now())
    # print("no14")
    
    connection.close()
#     print(corrected_branch_id_var)

# file = open('/workspace/chesterfield_23-03-2021_09-00-00.csv')
# run_loading(file)