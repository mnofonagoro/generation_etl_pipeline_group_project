# from connecting_to_db import create_db_connection

# When I opened up my container, my IP address had changed, so this is the code to check it:
# docker inspect team-3-project_devcontainer_postgres_1 | grep IPAddress

# connection = create_db_connection() 


def create_product_table(connection):
    try:
        with connection.cursor() as cursor:
            sql = '''
            CREATE TABLE IF NOT EXISTS product(
                        product_id INT IDENTITY(1,1) PRIMARY KEY,
                        product_name VARCHAR(100) NOT NULL,
                        product_size VARCHAR(100) NOT NULL,
                        product_price FLOAT
                        )'''
            cursor.execute(sql)
            connection.commit() 
    except Exception as e:
        print(e)     

def create_branch_table(connection):
    try:
        with connection.cursor() as cursor:
            sql = '''CREATE TABLE IF NOT EXISTS branch(
                        branch_id INT IDENTITY(1,1) PRIMARY KEY,
                        branch_location VARCHAR(100) NOT NULL
                        )'''
            cursor.execute(sql)
            connection.commit()
    except Exception as e:
        print(e)

def create_transaction_table(connection):
    try:
        with connection.cursor() as cursor:
            sql = '''CREATE TABLE IF NOT EXISTS transaction(
                        transaction_id INT IDENTITY(1,1) PRIMARY KEY,
                        date_time VARCHAR(100) NOT NULL,
                        transaction_total FLOAT NOT NULL,
                        branch_id INT,
                        CONSTRAINT fk_branch FOREIGN KEY(branch_id) REFERENCES branch(branch_id)
                        )'''
            cursor.execute(sql)
            connection.commit()
    except Exception as e:
        print(e)

def create_basket_table(connection):
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

# def close_connection():
#     return connection.close()


def create_all_tables(con):
    create_product_table(con)
    create_branch_table(con)
    create_transaction_table(con)
    create_basket_table(con)