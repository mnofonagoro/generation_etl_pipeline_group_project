## Schema: The information about the structure of the database and how things relate to each other

# Before storing our data we must design a schema for it so that we can create it in our database.

## User Story

> **As a** product owner
> **I want to** agree on the design of the schema
> **So that** the data is easy to query


## Table: transaction

transaction_id|date_time|transaction_total|branch_id|
              |         |                 |         |                
              |         |                 |         |                
              |         |                 |         |                 


## Table: basket

basket_id |product_id|transaction_id|
          |          |              |
          |          |              |
          |          |              |


## Table : Branch 

branch_id|branch_location|
         |               |
         |               |
         |               |


## Table: Products

product_id|product_name|product_size|product_price|
          |            |            |             |
          |            |            |             |
          |            |            |             |

