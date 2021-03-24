import csv
# file = open('/workspace/2021-02-23-isle-of-wight.csv')
# file = open('/workspace/birmingham_23-03-2021_09-00-00.csv')
# path = '/workspace/birmingham_23-03-2021_09-00-00.csv'
path = '/workspace/2021-02-23-isle-of-wight.csv'
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

for d in data_2:
    print(d)
    break


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

