import os, requests as req
def test_reverse():
    url = os.environ.get("OPSDEV_HOST") + "/api/my/agrisafi/reverse"
    res = req.get(url, {"input": "test"}).json()
    assert res.get("output") == "tset"

    res = req.get(url, {}).json()
    assert res.get("output") == "Plese provide some input"
