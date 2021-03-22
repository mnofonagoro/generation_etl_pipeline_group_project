from connecting_to_db import create_db_connection
from trail import *



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
        branch_id = int("1")
        with connection.cursor() as cursor:
            for datetime, amt in zip(date_time_var, amount_var):
                sql = "INSERT INTO transaction (date_time, transaction_total, branch_id)  VALUES ('{}', '{}', {})".format(datetime, amt, branch_id) 
                cursor.execute(sql)
            connection.commit()
    except Exception as e:
        print(e) 
 
 
def insert_into_basket_table():
    try:
        product_and_transaction_list = basket_table(transaction_basket_list_dict)  
        connection = create_db_connection()
        with connection.cursor() as cursor:
            for row in product_and_transaction_list:
                sql = f"""INSERT INTO basket (product_id, transaction_id)
                    VALUES ('{row['product_id']}', '{row['transaction_id']}')"""   
                    
                cursor.execute(sql)
                connection.commit()
    except Exception as e:
        print(e)
        
              
# insert_into_product_table()
# insert_into_branch_table()
# insert_into_transaction_table()
# insert_into_basket_table()