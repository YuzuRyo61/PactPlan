from fastapi.testclient import TestClient

from pactplan import PP_APP

client = TestClient(PP_APP)


def test_wk_nodeinfo():
    response = client.get("/.well-known/nodeinfo")
    assert response.status_code == 200
