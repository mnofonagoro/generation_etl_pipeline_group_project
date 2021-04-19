from io import StringIO
from src import trail
import csv    

def test_extract_and_remove_sensitive_data():
    expected = {'date_time': '2021-02-23 17:59:04', 'location': 'Isle of Wight', 'order': ',Frappes - Coffee,2.75,,Speciality Tea - Darjeeling,1.3,,Smoothies - Berry Beautiful,2.0,Large,Latte,2.45', 'amount': '8.50'}
    actual = trail.extract_and_remove_sensitive_data()[-1]
    assert expected == actual

def test_products_from_orders():
    mock_orders = [{'date_time': '2021-02-23 17:59:04', 'location': 'Isle of Wight', 'order': ',Frappes - Coffee,2.75,,Speciality Tea - Darjeeling,1.3,,Smoothies - Berry Beautiful,2.0,Large,Latte,2.45', 'amount': '8.50'}]
    expected = [[{'product_name': 'Frappes - Coffee', 'product_price': '2.75', 'product_size': 'Standard'}, {'product_name': 'Speciality Tea - Darjeeling', 'product_size': 'Standard', 'product_price': '1.3'}, {'product_name': 'Smoothies - Berry Beautiful', 'product_size': 'Standard', 'product_price': '2.0'}, {'product_name': 'Latte', 'product_price': '2.45', 'product_size': 'Large'}]]
    actual = trail.products_from_orders(mock_orders)
    
    assert expected == actual
      
def test_list_no_duplicatess():
    mock_products = [[{'product_name': 'Hot chocolate', 'product_size': 'Large', 'product_price': '2.9'}, {'product_name': 'Hot chocolate', 'product_size': 'Large', 'product_price': '2.9'}, {'product_name': 'Chai latte', 'product_size': 'Large', 'product_price': '2.6'}, {'product_name': 'Latte', 'product_size': 'Large', 'product_price': '2.45'}]]
    expected = [{'product_name': 'Hot chocolate', 'product_size': 'Large', 'product_price': '2.9'}, {'product_name': 'Chai latte', 'product_size': 'Large', 'product_price': '2.6'}, {'product_name': 'Latte', 'product_size': 'Large', 'product_price': '2.45'}]
    actual = trail.list_no_duplicates(mock_products)
    assert actual == expected

def test_date_time():
   
   mock_products = [{'date_time': '2021-02-23 09:00:48', 'location': 'Isle of Wight', 'order': 'Large,Hot chocolate,2.9,Large,Chai latte,2.6,Large,Hot chocolate,2.9', 'amount': '8.40'}, {'date_time': '2021-02-23 09:01:45', 'location': 'Isle of Wight', 'order': 'Large,Latte,2.45', 'amount': '2.45'}, {'date_time': '2021-02-23 09:02:27', 'location': 'Isle of Wight', 'order': ',Frappes - Coffee,2.75,,Cortado,2.05,,Glass of milk,0.7,,Speciality Tea - Camomile,1.3,,Speciality Tea - Camomile,1.3', 'amount': '8.10'}]
   expected = ['2021-02-23 09:00:48', '2021-02-23 09:01:45', '2021-02-23 09:02:27'] 
   actual = trail.date_time(mock_products)
   assert actual == expected
   
def test_amount():
   mock_products = [{'date_time': '2021-02-23 09:00:48', 'location': 'Isle of Wight', 'order': 'Large,Hot chocolate,2.9,Large,Chai latte,2.6,Large,Hot chocolate,2.9', 'amount': '8.40'}, {'date_time': '2021-02-23 09:01:45', 'location': 'Isle of Wight', 'order': 'Large,Latte,2.45', 'amount': '2.45'}, {'date_time': '2021-02-23 09:02:27', 'location': 'Isle of Wight', 'order': ',Frappes - Coffee,2.75,,Cortado,2.05,,Glass of milk,0.7,,Speciality Tea - Camomile,1.3,,Speciality Tea - Camomile,1.3', 'amount': '8.10'}]
   expected = ['8.40', '2.45', '8.10']
   actual = trail.amount(mock_products)
   assert actual == expected
   
def test_branch_location():
   mock_products = [{'date_time': '2021-02-23 09:00:48', 'location': 'Isle of Wight', 'order': 'Large,Hot chocolate,2.9,Large,Chai latte,2.6,Large,Hot chocolate,2.9', 'amount': '8.40'}, {'date_time': '2021-02-23 09:01:45', 'location': 'Isle of Wight', 'order': 'Large,Latte,2.45', 'amount': '2.45'}, {'date_time': '2021-02-23 09:02:27', 'location': 'Isle of Wight', 'order': ',Frappes - Coffee,2.75,,Cortado,2.05,,Glass of milk,0.7,,Speciality Tea - Camomile,1.3,,Speciality Tea - Camomile,1.3', 'amount': '8.10'}]
   expected = {'Isle of Wight'}
   actual = trail.branch_location(mock_products)
   assert actual == expected

def test_list_of_orders_indexed(): 
   mock_products = [[{'product_name': 'Hot chocolate', 'product_size': 'Large', 'product_price': '2.9'}, {'product_name': 'Chai latte', 'product_size': 'Large', 'product_price': '2.6'}, {'product_name': 'Hot chocolate', 'product_size': 'Large', 'product_price': '2.9'}], [{'product_name': 'Latte', 'product_size': 'Large', 'product_price': '2.45'}]]
   expected = [[{'product_name': 'Hot chocolate', 'product_size': 'Large', 'product_price': '2.9', 'transaction_id': 1}, {'product_name': 'Chai latte', 'product_size': 'Large', 'product_price': '2.6', 'transaction_id': 1}, {'product_name': 'Hot chocolate', 'product_size': 'Large', 'product_price': '2.9', 'transaction_id': 1}], [{'product_name': 'Latte', 'product_size': 'Large', 'product_price': '2.45', 'transaction_id': 2}]]
   actual = trail.list_of_orders_indexed(mock_products)
   assert actual == expected
  

