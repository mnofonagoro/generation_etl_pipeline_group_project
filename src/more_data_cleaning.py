import csv
# file = open('/workspace/2021-02-23-isle-of-wight.csv') 
# file = open('/workspace/birmingham_23-03-2021_09-00-00.csv')
path = '/workspace/birmingham_23-03-2021_09-00-00.csv'
# path = '/workspace/2021-02-23-isle-of-wight.csv'
file = open('{}'.format(path))

def extract_and_remove_sensitive_data(file):
    data = [] 
    try:
        if path == '/workspace/2021-02-23-isle-of-wight.csv' :
            fieldnames=['date_time','location','full_name','order','payment_type','amount','card_details']
        else:
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
        # print("Successfully Extracted")
    except Exception as error:
        print("An error occurred: " + str(error))
    return data

data_2 = (extract_and_remove_sensitive_data(file))

def cleaning(data_2):
    products = []
    for d in data_2:
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
            
            product_price = i[1] 
            product_price =product_price.replace(" ","")
             
            product_size = i[0].split()[0]
            # print(product_size)

            new_product = { 'product_name': product_name,
                            'product_size': product_size,
                            'product_price':product_price
                            }
            products_of_transcation.append(new_product)
            # print(new_product)

    return products

# products = cleaning(data_2)
# print(products)
# print(len(products))


def list_no_duplicates2(products):
    list_not_duplicated2 = []
    for p in products:
        for tr in p:
            if tr not in list_not_duplicated2:
                list_not_duplicated2.append(tr)
 
    return list_not_duplicated2

# list_not_duplicated2 = list_no_duplicates2(products)
# print(list_not_duplicated2)
# print(len(list_not_duplicated2))

def list_of_orders_indexed(list_of_all_2):
    list_of_orders_with_transac_id = []
    count = 0
    for order in list_of_all_2:
        count += 1
        for dicct in order:
            dicct["transaction_id"] = count
        list_of_orders_with_transac_id.append(order)
    return list_of_orders_with_transac_id

list_of_all_2 = cleaning(data_2)

print(list_of_orders_indexed(list_of_all_2))

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