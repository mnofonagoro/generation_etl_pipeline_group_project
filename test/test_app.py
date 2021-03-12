from io import StringIO
from src import app
import csv   


def test_extract_and_remove_sensitive_data():
    expected = {'date_time': '2021-02-23 17:59:04', 'location': 'Isle of Wight', 'full_name': 'Stanley Cordano', 'order': ',Frappes - Coffee,2.75,,Speciality Tea - Darjeeling,1.3,,Smoothies - Berry Beautiful,2.0,Large,Latte,2.45', 'payment_type': 'CASH', 'amount': '8.50'}
    actual = app.extract_and_remove_sensitive_data()[-1]

    assert expected == actual