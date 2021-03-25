from connecting_to_db import create_db_connection
from trail import *
from sql_script import *



def insert_into_product_table():
    products_list_unique = list_not_duplicated 
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
    
    
def insert_into_branch_table():
    branch_locations = branch_location(data)
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
             
        
def insert_into_transaction_table():
    try:
        amount_var = amount(data)
        date_time_var = date_time(data)
        connection = create_db_connection()
        branch_id = corrected_branch_id['branch_id']  
        with connection.cursor() as cursor:
            for datetime, amt in zip(date_time_var, amount_var):
                sql = "INSERT INTO transaction (date_time, transaction_total, branch_id)  VALUES ('{}', '{}', {})".format(datetime, amt, branch_id) 
                cursor.execute(sql)
            connection.commit()
    except Exception as e:
        print(e) 
 
 
def insert_into_basket_table():
    try:
        product_and_transaction_list = product_and_transaction_ids 
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
    
    global data
    data = extract_and_remove_sensitive_data(file) 
    global list_of_all_products
    list_of_all_products = cleaning(data)
    #list_of_all = cleaning(data)
    ## list_of_all = products_from_orders(data)
    global list_not_duplicated
    list_not_duplicated = list_no_duplicates(list_of_all_products)
    #list_not_duplicated = list_no_duplicates(list_of_all)
    
    global list_of_orders_with_branch
    list_of_orders_with_branch = adding_branch(list_of_all_products, data)
    
    global list_of_orders_with_transac_id
    list_of_orders_with_transac_id = list_of_orders_indexed(list_of_all_products)

    insert_into_product_table()

    insert_into_branch_table()
    
    # this only works if the products table is created and populated as it depend on it to fetch the tuples.
    
    global joint_two 
    joint_two = zipping_branch_stuff()
    
    global joint_three
    joint_three = zipping_product_stuff()
    
    global branch_id_loc
    branch_id_loc = convert_branch_tuple_to_dict(joint_two)
    
    global corrected_branch_id 
    corrected_branch_id = branch_id_transaction(branch_id_loc, list_of_orders_with_branch)
    
    global unique_prod_id_name_size
    unique_prod_id_name_size = convert_tuple_to_dict(joint_three)
   
    global product_and_transaction_ids
    product_and_transaction_ids = basket_table(unique_prod_id_name_size, list_of_orders_with_transac_id)


    insert_into_transaction_table()
    insert_into_basket_table()




