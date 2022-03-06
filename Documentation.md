# Architecture
There are 3 models:
1. `CustomUser` model to create and manage users
2. `BankAccount` model for bank account details. Fields are : `Account Type` which has two options: `savings` & `credit`; `Account Balance` and a foreign key field to `CustomUser` model `User`. When deposits and withdrawals are made, the `Account Balance` is updated with latest balance after calculations
3. `Transaction` model with details of transactions carried out and the type of transaction: `deposit` or `withdrawal`. This model has foreign key relationship to both `CustomUser` and `BankAccount` models
4. When creating bank accounts, `User ID` must be provided so it will link back to an existing user
5. When creating a transaction, the `User ID` and `Bank Account ID` must be provided. These two parameters will be used to check if there is a bank account on record before any transaction will be allowed


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
5. `Create bank account` curl command example:
```
curl --data "account_type=credit&user=1" http://127.0.0.1:8000/createbankaccountapi/
```
6. `Update bank account` curl command example (Only account type can be updated via API, `account balance` have to be updated via a transaction in order to have proper records):
```
curl -X PUT -d "account_type=savings&user=11" http://127.0.0.1:8000/bankaccountupdate/1/
```

## Make deposits and withdrawals via API
1. To make deposits into an account, you must specify the `id` of an existing user, `id` of an existing bank account, `transaction_type` and `transaction_amount`
2. The two `id`s will be checked to see if they march an existing bank account or there will be an error raised
3. `transaction_type` can either be `deposit` or `withdrawal`
4. Curl command to create a deposit of 10000 into an account with id 1 owned by user with id 1
```
curl --data "transaction_type=deposit&transaction_amount=10000&account_type=1&user=1" http://127.0.0.1:8000/createtransactionapi/
```
5. Curl command to make a withdrawal of 500 from an account with id 6 owned by user with id 1
```
curl --data "transaction_type=withdrawal&transaction_amount=500&account_type=6&user=1" http://127.0.0.1:8000/createtransactionapi/
```
## All transactions are persisted with an sqlite3 db which is auto-created after running migrations
## Implement an API endpoint that shows all accounts, balances, and the last 10 transactions, for the logged in USER
1. `email` and `password` are required to login
2. URL to login
```
http://127.0.0.1:8000/viewuseraccount/
```
3. See bank account drill down
```
http://127.0.0.1:8000/viewbankaccountuser/
```
## Implement an Administrator view that can see accounts, balances, transactions for a specific user (by user ID)
1. Below URL shows info for user with id 1
```
http://127.0.0.1:8000/adminviewuser/1/
```
2. Django admin url has also been configured for this purpose
```
http://127.0.0.1:8000/admin/
```

## Implement a simple report (CSV Download) that contains: a. All accounts b. Associated balances c. Associated Users
1. Download reports from url:
```
http://127.0.0.1:8000/downloadbankaccounts/
```

#### To check the API documentation, visit http://127.0.0.1:8000/docs/
