from connecting_to_db import create_db_connection

# When I opened up my container, my IP address had changed, so this is the code to check it:
# docker inspect team-3-project_devcontainer_postgres_1 | grep IPAddress

connection = create_db_connection()


def create_product_table():
    try:
        with connection.cursor() as cursor:
            sql = '''DROP TYPE IF EXISTS product_size;
            CREATE TYPE product_size AS ENUM 
                    ('Standard' , 'Regular' , 'Large');
            CREATE TABLE IF NOT EXISTS product(
                        product_id SERIAL PRIMARY KEY,
                        product_name VARCHAR(100) NOT NULL,
                        product_size product_size,
                        product_price FLOAT
                        )'''
            cursor.execute(sql)
            connection.commit() 
    except Exception as e:
        print(e)     

def create_branch_table():
    try:
        with connection.cursor() as cursor:
            sql = '''CREATE TABLE IF NOT EXISTS branch(
                        branch_id SERIAL PRIMARY KEY,
                        branch_location VARCHAR(100) NOT NULL
                        )'''
            cursor.execute(sql)
            connection.commit()
    except Exception as e:
        print(e)

def create_transaction_table():
    try:
        with connection.cursor() as cursor:
            sql = '''CREATE TABLE IF NOT EXISTS transaction(
                        transaction_id SERIAL PRIMARY KEY,
                        date_time TIMESTAMP NOT NULL,
                        transaction_total FLOAT NOT NULL,
                        branch_id INT,
                        CONSTRAINT fk_branch FOREIGN KEY(branch_id) REFERENCES branch(branch_id)
                        )'''
            cursor.execute(sql)
            connection.commit()
    except Exception as e:
        print(e)

def create_basket_table():
    try:
        with connection.cursor() as cursor:
            sql = '''CREATE TABLE IF NOT EXISTS basket(
                        product_id INT,
                        transaction_id INT,
                        CONSTRAINT fk_product_id FOREIGN KEY(product_id) REFERENCES product(product_id),
                        CONSTRAINT fk_transaction FOREIGN KEY(transaction_id) REFERENCES transaction(transaction_id)
                        )'''
            cursor.execute(sql)
            connection.commit()
    except Exception as e:
        print(e)

def close_connection():
    return connection.close()