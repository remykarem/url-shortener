# URL Shortener

URL shortener is available at http://whispering-hamlet-28439.herokuapp.com/.

## Dev

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
