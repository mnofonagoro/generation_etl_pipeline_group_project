from connecting_to_db import create_db_connection
from transform import *

data = extract_and_remove_sensitive_data()
products = products_from_orders(data)
# products_list_no_duplicates(products)

def insert_into_product_table():
    products_list_unique = products_list_no_duplicates(products)
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
        with connection.cursor() as cursor:
            for datetime, amt in zip(date_time_var, amount_var):
                sql = f"INSERT INTO transaction (date_time, transaction_total) VALUES ('{datetime}', '{amt}')"
                cursor.execute(sql)
            connection.commit()
    except Exception as e:
        print(e)
        
     
def insert_into_basket_table():
    try:
          
        connection = create_db_connection()
        with connection.cursor() as cursor:
            sql = f"INSERT INTO basket (product_id, transaction_id) VALUES ('{x}', '{y}')"
            cursor.execute(sql)
        connection.commit()
    except Exception as e:
        print(e)
        
        
        
insert_into_product_table()
insert_into_branch_table()
insert_into_transaction_table()