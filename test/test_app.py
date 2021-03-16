from io import StringIO
from src import transform
import csv   

def test_extract_and_remove_sensitive_data():
    expected = {'date_time': '2021-02-23 17:59:04', 'location': 'Isle of Wight', 'order': ',Frappes - Coffee,2.75,,Speciality Tea - Darjeeling,1.3,,Smoothies - Berry Beautiful,2.0,Large,Latte,2.45', 'amount': '8.50'}
    actual = transform.extract_and_remove_sensitive_data()[-1]
    assert expected == actual


def test_products_from_orders():
    mock_orders = [{'date_time': '2021-02-23 17:59:04', 'location': 'Isle of Wight', 'order': ',Frappes - Coffee,2.75,,Speciality Tea - Darjeeling,1.3,,Smoothies - Berry Beautiful,2.0,Large,Latte,2.45', 'amount': '8.50'}]
    expected = [{'product_name': 'Frappes - Coffee', 'product_size': 'Standard', 'product_price': '2.75'}, {'product_name': 'Speciality Tea - Darjeeling', 'product_size': 'Standard', 'product_price': '1.3'}, {'product_name': 'Smoothies - Berry Beautiful', 'product_size': 'Standard', 'product_price': '2.0'}, {'product_name': 'Latte', 'product_size': 'Large', 'product_price': '2.45'}]
    actual = transform.products_from_orders(mock_orders)
    
    assert expected == actual
    
    
def test_remove_duplicate_products():
    mock_products = [{'product_name': 'Hot chocolate', 'product_size': 'Large', 'product_price': '2.9'}, {'product_name': 'Hot chocolate', 'product_size': 'Large', 'product_price': '2.9'}, {'product_name': 'Chai latte', 'product_size': 'Large', 'product_price': '2.6'}, {'product_name': 'Latte', 'product_size': 'Large', 'product_price': '2.45'}]
    expected = [{'product_name': 'Hot chocolate', 'product_size': 'Large', 'product_price': '2.9'}, {'product_name': 'Chai latte', 'product_size': 'Large', 'product_price': '2.6'}, {'product_name': 'Latte', 'product_size': 'Large', 'product_price': '2.45'}]
    actual = transform.products_list_no_duplicates(mock_products)
    assert actual == expected