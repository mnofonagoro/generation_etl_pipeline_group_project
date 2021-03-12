## Schema: The information about the structure of the database and how things relate to each other

# Before storing our data we must design a schema for it so that we can create it in our database.

## User Story

> **As a** product owner
> **I want to** agree on the design of the schema
> **So that** the data is easy to query


## Table: <branch_id> sales data => data from 1 store

order_id|date_time|customer_id|order_amount|payment_method_id|
        |         |           |            |                 |
        |         |           |            |                 |
        |         |           |            |                 |


## Table: Per transaction?

product_id|
          |
          |
          |


## Table : Branch ID

branch_id|branch_location|branch_address|
         |               |              |
         |               |              |
         |               |              |


## Table: Products

product_id|product_name|product_size_id|product_price|
          |            |               |             |
          |            |               |             |
          |            |               |             |

enum data type
## Table: Products size >> not nessecary

product_size_id|product_size|
1              |standard    | 
2              |regular     |
3              |large       |


## Table: PII

customer_id|first_name|last_name|


## Table: Payment method

payment_method_id|payment_type
1                | cash
2                | card
3                | other



