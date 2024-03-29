# Short'ner

![preview](preview.gif)

URL shortener written using Python's FastAPI framework, Vue.js and UIKit. The FastAPI framework uses SQLAlchemy for ORM. Data is persisted in Postgresql.

The app is available at https://url-shortener-take-home.herokuapp.com.

## Dev

Install the Python dependencies

```python
pip install -r requirements.txt
```

Run the app server with hot reload

```python
uvicorn shortener.main:app --reload  
```

## Tests

To run the unit tests, run

```python
python -m pytest
```

## Design

A URL hash consists of 9 digits, which are separated by 3 dashes, with the hope that the hashes are more readable.

We use digits-only hash because we don't think there will be high traffic from this app 🙂.
