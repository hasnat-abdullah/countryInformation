Country Information
----------------------
This is a web apps made by Django framework (python), an Assignment project provided by a well known company.<br>
Country related information will be pulled from a 3rd party API and store to DB. It will be provided by REST API & template too. Functional programming concept and Unit Testing is applied here.

###Currently latest branch is ```dev_hasnat```

API's documentation
-------------------
```djangourlpath
http://127.0.0.1:8000/api/v1/docs/
```

##steps: [setup dev environment]<h3><span style="color: green">For Ubuntu:</span><h3>

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

### 7. Migrate, create superuser and run project
`$ python manage.py migrate`<br />
`$ python manage.py createsuperuser` \
`$ python manage.py runserver`



## :wink: happy coding :wink: