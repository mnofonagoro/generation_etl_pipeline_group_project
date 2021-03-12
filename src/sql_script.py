import psycopg2

# When I opened up my container, my IP address had changed, so this is the code to check it:
# docker inspect team-3-project_devcontainer_postgres_1 | grep IPAddress

def create_payment_method_table():
    try:
        with psycopg2.connect(database="team-3-group-project", user="root", password="password", host="172.18.0.2", port="5432") as connection:
            with connection.cursor() as cursor:
                sql = '''CREATE TABLE IF NOT EXISTS payment_method(
                            payment_id SERIAL PRIMARY KEY, 
                            payment_type VARCHAR(10) NOT NULL
                            );
                        INSERT INTO payment_method(payment_type)
                        VALUES('cash'), ('card'), ('other')'''
                cursor.execute(sql)
                connection.commit()
    except Exception as e:
        print(e)
                

def create_pii_table():
    try:
        with psycopg2.connect(database="team-3-group-project", user="root", password="password", host="172.18.0.2", port="5432") as connection:
            with connection.cursor() as cursor:
                sql = '''CREATE TABLE IF NOT EXISTS PII(
                            customer_id SERIAL PRIMARY KEY,
                            first_name VARCHAR(100) NOT NULL,
                            last_name VARCHAR(100) NOT NULL
                            )'''
                cursor.execute(sql)
                connection.commit()
    except Exception as e:
        print(e)

def create_product_size_table():
    try:
        with psycopg2.connect(database="team-3-group-project", user="root", password="password", host="172.18.0.2", port="5432") as connection:
            with connection.cursor() as cursor:
                sql = '''CREATE TABLE IF NOT EXISTS product_size(
                            product_size_id SERIAL PRIMARY KEY,
                            product_size VARCHAR(50) NOT NULL
                            );
                            INSERT INTO product_size(product_size)
                            VALUES('standard'), ('regular'), ('large')'''
                cursor.execute(sql)        
                connection.commit()
    except Exception as e:
        print(e)

def create_products_table():
    try:
        with psycopg2.connect(database="team-3-group-project", user="root", password="password", host="172.18.0.2", port="5432") as connection:
            with connection.cursor() as cursor:
                sql = '''CREATE TABLE IF NOT EXISTS products(
                            product_id SERIAL PRIMARY KEY,
                            product_name VARCHAR(100) NOT NULL,
                            product_size_id INT,
                            product_price FLOAT,
                            CONSTRAINT fk_product_size FOREIGN KEY(product_size_id) REFERENCES product_size(product_size_id)
                            )'''
                cursor.execute(sql)
                connection.commit() 
    except Exception as e:
        print(e)     

def create_branch_table():
    try:
        with psycopg2.connect(database="team-3-group-project", user="root", password="password", host="172.18.0.2", port="5432") as connection:
            with connection.cursor() as cursor:
                sql = '''CREATE TABLE IF NOT EXISTS branch(
                            branch_id SERIAL PRIMARY KEY,
                            branch_location VARCHAR(100) NOT NULL,
                            branch_address VARCHAR(100) NOT NULL
                            )'''
                cursor.execute(sql)
                connection.commit()
    except Exception as e:
        print(e)

def create_sales_data_table():
    try:
        with psycopg2.connect(database="team-3-group-project", user="root", password="password", host="172.18.0.2", port="5432") as connection:
            with connection.cursor() as cursor:
                sql = '''CREATE TABLE IF NOT EXISTS isle_of_wight_sales_data(
                            order_id SERIAL PRIMARY KEY,
                            date_time TIMESTAMP,
                            customer_id INT,
                            product_id INT,
                            order_amount FLOAT NOT NULL,
                            payment_id INT,
                            CONSTRAINT fk_customer FOREIGN KEY(customer_id) REFERENCES PII(customer_id),
                            CONSTRAINT fk_product_id FOREIGN KEY(product_id) REFERENCES products(product_id),
                            CONSTRAINT fk_payment_method FOREIGN KEY(payment_id) REFERENCES payment_method(payment_id)
                            )'''
                cursor.execute(sql)
                connection.commit()
    except Exception as e:
        print(e)


create_payment_method_table()
create_pii_table()
create_product_size_table()
create_products_table()
create_branch_table()
create_sales_data_table()
print("Your tables have been created successfully")
