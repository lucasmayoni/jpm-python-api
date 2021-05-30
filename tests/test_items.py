def test_is_valid():
    pass


def test_status(client):
    rv = client.get('/items')
    assert rv.status_code == 200

