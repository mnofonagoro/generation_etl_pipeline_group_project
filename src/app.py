import csv

data = []      
def extract_and_remove_sensitive_data():
    print("Extracting...")
    try:
        with open('/workspace/2021-02-23-isle-of-wight.csv', 'r') as file:
            source_file = csv.DictReader(file, fieldnames=['date_time','location','full_name','order','payment_type','amount','card_details'], delimiter=',')
            next(source_file) #ignore the header row
            for row in source_file:
                data.append((row['date_time'], row['location'], row['full_name'], row['order'], row['payment_type'], row['amount']))
    except Exception as error:
        print("An error occurred: " + str(error))

    return data

extract_and_remove_sensitive_data()

for i in data:
    print(i)




