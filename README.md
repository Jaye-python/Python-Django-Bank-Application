# Python-Django-Bank-Application
This is an API-based Django app built using Django Rest Framework. You can register a new user, create bank accounts, make deposists and withdrawals and view your transactions using API endpoints.

# Python Django Bank App
## API Schema and requirements to consume the API is available on http://127.0.0.1:8000/docs/


### Logic to be implemented:
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
2. Create new folder/directory
```
mkdir hackernews
```
3. Navigate into this new folder
```
cd hackernews
```
4. Create new Python Virtual environment
```
python3 -m venv ./venv
```
5. Activate this new virtual environment
```
source venv/bin/activate
```
6. Clone this git repo
```
git clone https://github.com/Jaye-python/hackernewsapi.git
```
7. Move into the hackernewsapi folder 
```
cd hackernewsapi
```
8. Install dependencies
```
pip install -r requirements.txt
```
9. Launch
```
python manage.py runserver
```
10. To run the Celery workers used to seed the DB (Celery must have been installed and started)
```
celery -A hackernews worker -l info
```
11. To run the Celery Beat workers to sync the DB every 5 minutes
```
celery -A hackernews beat -l info
```

