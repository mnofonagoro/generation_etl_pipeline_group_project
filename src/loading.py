from connecting_to_db import create_db_connection
from trail import *
from sql_script import *


def insert_into_product_table(list_not_duplicated_par):
    products_list_unique = list_not_duplicated_par
    try:
        connection = create_db_connection()
        with connection.cursor() as cursor:
            for row in products_list_unique:
                sql = f"""INSERT INTO product (product_name, product_size, product_price)
                VALUES ('{row['product_name']}', '{row['product_size']}', '{row['product_price']}')"""
                
                cursor.execute(sql)
                connection.commit() 
  
    except Exception as e:
        print(e)
    
    
def insert_into_branch_table(branch_location_w_par):
    branch_locations = branch_location_w_par
    try:
        connection = create_db_connection()
        with connection.cursor() as cursor:
            
            for item in branch_locations:
                val = item
                sql = f"INSERT INTO branch (branch_location) VALUES ('{val}')"
                cursor.execute(sql)
                connection.commit()
    except Exception as e:
        print(e)
             
        
def insert_into_transaction_table(corrected_branch_id, our_data):
    try:
        amount_var = amount(our_data)
        date_time_var = date_time(our_data)
        connection = create_db_connection()
        branch_id = corrected_branch_id['branch_id']  
        with connection.cursor() as cursor:
            for datetime, amt in zip(date_time_var, amount_var):
                sql = "INSERT INTO transaction (date_time, transaction_total, branch_id)  VALUES ('{}', '{}', {})".format(datetime, amt, branch_id) 
                cursor.execute(sql)
            connection.commit()
    except Exception as e:
        print(e) 
 
 
def insert_into_basket_table(product_and_transaction_ids_var):
    try:
        product_and_transaction_list = product_and_transaction_ids_var
        connection = create_db_connection()
        with connection.cursor() as cursor:
            for row in product_and_transaction_list:
                sql = f"""INSERT INTO basket (product_id, transaction_id)
                    VALUES ('{row['product_id']}', '{row['transaction_id']}')"""   
                    
                cursor.execute(sql)
                connection.commit()
    except Exception as e:
        print(e)
        
def run_loading(file):
    create_product_table()
    create_branch_table()
    create_transaction_table()
    create_basket_table()
    close_connection()
    print("Your tables have been created successfully")
    
    # global data
    our_data = extract_and_remove_sensitive_data(file)
    # global list_of_all_products
    list_of_all_products_var = cleaning(our_data)
    # list_of_all = cleaning(our_data)
    # list_of_all = products_from_orders(our_data)
    # global list_not_duplicated
    list_not_duplicated_var = list_no_duplicates(list_of_all_products_var)
    #list_not_duplicated = list_no_duplicates(list_of_all)
    # global list_of_orders_with_branch
    list_of_orders_with_branch_var = adding_branch(list_of_all_products_var, our_data)
    # global list_of_orders_with_transac_id
    list_of_orders_with_transac_id_var = list_of_orders_indexed(list_of_all_products_var)
    # print(list_of_orders_with_transac_id_var[:10])
    insert_into_product_table(list_not_duplicated_var)
    insert_into_branch_table(branch_location(our_data))
    
    # this only works if the products table is created and populated as it depend on it to fetch the tuples.
    # global joint_two 
    joint_two = zipping_branch_stuff()
    #global joint_three
    joint_three = zipping_product_stuff()
    #global branch_id_loc
    branch_id_loc = convert_branch_tuple_to_dict(joint_two)
    #global corrected_branch_id 
    corrected_branch_id_var = branch_id_transaction(branch_id_loc, list_of_orders_with_branch_var)
    #global unique_prod_id_name_size
    unique_prod_id_name_size = convert_tuple_to_dict(joint_three)
    # global product_and_transaction_ids
    product_and_transaction_ids_var = basket_table(unique_prod_id_name_size, list_of_orders_with_transac_id_var)

    insert_into_transaction_table(corrected_branch_id_var, our_data)
    insert_into_basket_table(product_and_transaction_ids_var)
    
