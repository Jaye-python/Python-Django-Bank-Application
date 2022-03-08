# Python-Django-Bank-Application
This is an API-based Django app built using Django Rest Framework. You can register a new user, create bank accounts, make deposists and withdrawals and view your transactions using API endpoints.

#### Video Demo: https://youtu.be/qheQ96NYeqE


### Logic implemented:
1. Create a new user via API.
2. Create/Update a new bank account via API
3. Bank account to be one of either SAVINGS, or CREDIT
4. CREDIT account can have negative values up to a limit of 20,000.00.
5. SAVINGS account to always have a positive value of 50.00 or more.
6. Make deposits via API
7. Make withdrawals via API
8. All transactions need to be persisted.
9. One user can have multiple accounts of all types.
10. Implement an API endpoint that shows all accounts, balances, and the last 10 transactions, for the logged in USER.
11. Implement an Administrator view that can see accounts, balances, transactions for a specific user (by user ID).
12. Implement a simple report (CSV Download) that contains:
  a. All accounts
  b. Associated balances
  c. Associated Users


### To launch this app on your system:
1. Navigate to your desktop
```
cd Desktop
```
2. Create new Python Virtual environment
```
python3 -m venv ./venv
```
3. Activate this new virtual environment
```
source venv/bin/activate
```
4. Clone this git repo
```
git clone https://github.com/Jaye-python/Python-Django-Bank-Application.git
```
5. Move into the Python-Django-Bank-Application folder 
```
cd Python-Django-Bank-Application
```
6. Install dependencies
```
pip install -r requirements.txt
```
7. Make migrations (this will auto-create an sqlite3 database for this app. You may interact with the database if you wish)
```
python manage.py makemigrations
```
8. Migrate
```
python manage.py migrate
```
9. Launch
```
python manage.py runserver
```
10. **Open a new terminal while server is still running** and navigate back to the virtual environment created in No. 2 (in this new terminal)
```
cd ..
```
11. Now activate the virtual environment created in No. 2 in this new terminal
```
source venv/bin/activate
```
12. . Move back into the Python-Django-Bank-Application folder 
```
cd Python-Django-Bank-Application
```
13. In this same new terminal, run custom management command below to create 5 new user accounts (while server is still running)
```
python manage.py create_users
```
14. In this same new terminal, run custom management commands below (one after the other) to create bank accounts for these new users (while server is still running)
```
python manage.py create_savings_accounts
python manage.py create_credit_accounts
```
15. In this same terminal, run custom management command below to make deposits into the bank accounts for these new users (while server is still running)
```
python manage.py make_deposit
```
16. In this same terminal, run custom management command below to make withdrawals from the bank accounts of these new users (while server is still running)
```
python manage.py make_withdrawal
```
17. In this same terminal, run custom management command below to run tests (while server is still running)
```
python manage.py test
```
18. In this same terminal, create superuser account
```
python manage.py createsuperuser
```
19. To check the API documentation, visit http://127.0.0.1:8000/docs/
20. See documentation in the `Documentation.md` file included in this repo

