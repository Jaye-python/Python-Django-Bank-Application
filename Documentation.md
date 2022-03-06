## Create a new user via API
1. To create new users, you must specify `email`, `first_name`, `last_name` and `password`. You need `email` and `password` to login
2. To create new users via API using curl command, run
```
curl --data "email=newuser@pp.com&first_name=newuserfirstname&last_name=newuserfirstname&password=1234" http://127.0.0.1:8000/register/
```
Create/Update a new bank account via API
Bank account to be one of either SAVINGS, or CREDIT
CREDIT account can have negative values up to a limit of 20,000.00.
SAVINGS account to always have a positive value of 50.00 or more.
Make deposits via API
Make withdrawals via API
All transactions need to be persisted.
One user can have multiple accounts of all types.
Implement an API endpoint that shows all accounts, balances, and the last 10 transactions, for the logged in USER.
Implement an Administrator view that can see accounts, balances, transactions for a specific user (by user ID).
Implement a simple report (CSV Download) that contains: a. All accounts b. Associated balances c. Associated Users
