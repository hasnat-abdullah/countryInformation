Country Information
----------------------
This is a web apps made by Django framework (python), an Assignment project provided by a well known company.<br>
Country related information will be pulled from a 3rd party API and store to DB. It will be provided by REST API & template too. Functional programming concept and Unit Testing is applied here.

### Currently latest branch is ```dev_hasnat```

API's documentation
-------------------
```djangourlpath
http://127.0.0.1:8000/api/v1/docs/
```
or
https://docs.google.com/document/d/1m_l0LnUDy70Ig1X1apNolJZ6E9nzQBGxb7ExkzCGpas/edit?usp=sharing

Steps: [setup dev environment]
---------------------
#### _For Ubuntu_:

### 1. Clone repo
`$ git clone `

### 2. Checkout to latest branch
`$ git checkout dev_hasnat`

### 3. Create `virtualenv` and activate `venv`
`$ virtualenv -p python3 .venv` <br />
`$ source .venv/bin/activate`

### 4. Install dependencies for project
`$ pip install -r requirements.txt`

### 5. Copy `.env.example` file to `.env`
### 6. Create a PostgreSQL database according to `.env.example`

### 7. Migrate, create superuser
`$ python manage.py migrate`<br />
`$ python manage.py createsuperuser`

### 8. Populate data from 3rd party API to DB
`$ python manage.py populate_data`

### 9. Run project
`$ python manage.py runserver`
## :wink: happy coding :wink: