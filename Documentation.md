## Create a new user via API
1. To create new users, you must specify `email`, `first_name`, `last_name` and `password`. You need `email` and `password` to login
2. To create new users via API using curl command, run
```
curl --data "email=newuser@pp.com&first_name=newuserfirstname&last_name=newuserfirstname&password=1234" http://127.0.0.1:8000/register/
```
## Create/Update a new bank account via API
1. To create a new bank account, you must specify the `id` of an existing customer and the `account_type` to be created
2. `account_type` must be either `savings` or `credit`
3. `credit` accounts can have negative values up to a limit of 20,000.00
4. `savings` accounts must always have a positive value of 50.00 or more
5. Curl command example:
```
curl --data "account_type=credit&user=1" http://127.0.0.1:8000/createbankaccountapi/
```
## Make deposits via API
1. To make deposits into an account, you must specify the `id` of an existing user, `id` of an existing bank account, `transaction_type` and `transaction_amount`
2. The two `id`s will be checked to see if they march an existing bank account or there will be an error raised
3. Curl command to create a deposit of 100 into savings account 1 owned by user with id 1
```
curl --data "transaction_type=deposit&transaction_amount=10000&account_type=1&user=1" http://127.0.0.1:8000/createtransactionapi/
```
Make withdrawals via API
All transactions need to be persisted.
One user can have multiple accounts of all types.
Implement an API endpoint that shows all accounts, balances, and the last 10 transactions, for the logged in USER.
Implement an Administrator view that can see accounts, balances, transactions for a specific user (by user ID).
Implement a simple report (CSV Download) that contains: a. All accounts b. Associated balances c. Associated Users
