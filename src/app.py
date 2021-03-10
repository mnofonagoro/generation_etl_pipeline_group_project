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
                data.append(row)
    except Exception as error:
        print("An error occurred: " + str(error))
    return data
extract_and_remove_sensitive_data()

for i in extract_and_remove_sensitive_data():
    print(i)