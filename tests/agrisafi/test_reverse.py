import sys 
sys.path.append("packages/agrisafi/reverse")
import reverse

def test_reverse():
    res = reverse.reverse({"input": "test"})
    assert res["output"] == "tset"

    res = reverse.reverse({})
    assert res["output"] == "Plese provide some input"
