from src.connecting_to_db import create_db_connection

connection = create_db_connection()

from src.sql_script import *

create_product_table()
create_branch_table()
create_transaction_table()
create_basket_table()
close_connection()

print("Your tables have been created successfully")

from src.trail import *

# connection = create_db_connection()             
data = extract_and_remove_sensitive_data()
list_of_all = products_from_orders(data)
list_not_duplicated = list_no_duplicates(list_of_all)
list_of_orders_indexed(list_of_all)
list_of_orders_with_transac_id = list_of_orders_indexed(list_of_all)
joint_three = zipping_product_stuff()
transaction_basket_list_dict = convert_tuple_to_dict(joint_three)

from src.loading import *

insert_into_product_table()
insert_into_branch_table()
insert_into_transaction_table()
insert_into_basket_table()


