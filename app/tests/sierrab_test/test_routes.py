

def test_investor_success(client):
    reply = client.get('/investors')
    assert reply.status_code == 200

def test_index_content(client):
    response = client.get('/')
    assert b'our mission is to showcase the wealth' in response.data