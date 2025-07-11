To install Fast Api :pip install fastapi
To install uvicorn server:pip install uvicorn
To run server : python -m uvicorn main:app --reload
Default server: http://127.0.0.1:8000

For sql:pip install fastapi uvicorn sqlalchemy pymysql
URL = 'mysql+pymysql://root:root@localhost/schema_name'

To create virtual env:python -m venv env_name 
to enter virtual env:env\Scripts\activate.bat

To use mongodb: python -m pip install "pymongo[srv]" 
and add connection url in config.py mongodb://localhost:27017/

For JWT token authentications:
>pip install python-multipart
>pip install python-jose[cryptography]
>pip install passlib[bcrypt]
