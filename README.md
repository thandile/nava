## Create and activate a new Python virtual environment 

`virtualenv -p python3 venv`

`source venv/bin/activate`
``

## Run the following commands in your venv
1. `pip install -r requirements.txt`
3. `python manage.py runserver`

## In your browser go to
```http://127.0.0.1:8000/phonebook_entry/```

You can `get`, `delete` and `put` new phonebook entries. 

Individual entries are accessed by their IDs e.g.

```http://127.0.0.1:8000/phonebook_entry/1/```


