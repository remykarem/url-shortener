from shortener.schemas import hash_to_short, hasher

def test_hash_to_short():
    assert hash_to_short("645920113") == "645-920-113"

def test_hasher():
    raw = "example.com"
    url_hash = str(abs(hash(raw)))[:9]
    url_short = hash_to_short(url_hash)
    assert hasher(raw) == (url_hash, url_short)
