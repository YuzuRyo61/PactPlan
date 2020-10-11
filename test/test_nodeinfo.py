from fastapi.testclient import TestClient

from pactplan import PP_APP

client = TestClient(PP_APP)


def test_nodeinfo():
    response = client.get("/nodeinfo/2.0")
    assert response.status_code == 200
