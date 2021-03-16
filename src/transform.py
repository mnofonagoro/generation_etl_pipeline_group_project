import csv

def extract_and_remove_sensitive_data():
        
    data = [] 
    
    print("Extracting...")
    try:
        with open('/workspace/2021-02-23-isle-of-wight.csv', 'r') as file:
            fieldnames=['date_time','location','full_name','order','payment_type','amount','card_details']
            source_file = csv.DictReader(file, fieldnames = fieldnames, delimiter=',')
            next(source_file) #ignore the header row
            for row in source_file:
                row = dict(row)
                if 'card_details' in row:
                    del row['card_details']
                if 'full_name' in row:
                    del row['full_name']
                if 'payment_type' in row:
                    del row['payment_type']
                data.append(row)
            print("Successfully Extracted")
    except Exception as error:
        print("An error occurred: " + str(error))
    return data

def products_from_orders(data):
    # print(data[-1])
    products_ordered = []
    for d in data:
        items = d['order']
        single_order = items.split(",")
        total = len(single_order)
        n = 0
        my_order = []
        while n < total:                
            product_name = single_order[(n+1)]     
            product_price = single_order[(n+2)]   
            product_size = single_order[(n)]                       
            if product_size == '':
                product_size = 'Standard'
            new_product = { 'product_name': product_name,
                            'product_size': product_size,
                            'product_price':product_price}
            products_ordered.append(new_product)
            # 'order' is now a list of product dictionaries
            my_order.append(new_product)
            d['order'] = my_order
            n += 3
    return products_ordered


def products_list_no_duplicates(products):
    products_no_duplicates = []
    for product in products:
        if product in products_no_duplicates:
            pass
        else:
            products_no_duplicates.append(product)
    return products_no_duplicates


def date_time(data):
    date_time_list = []
    
    for item in data:
        date_time = item['date_time']
        date_time_list.append(date_time)
        
    return date_time_list

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

# branch_location(data)

if __name__ == '__main__':
    data = extract_and_remove_sensitive_data()
    products = products_from_orders(data)
    # print(products_list_no_duplicates(products))
    # products_list_no_duplicates(products)
    # extract_and_remove_sensitive_data()
    print(branch_location(data))   


