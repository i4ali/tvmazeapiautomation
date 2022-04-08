import pytest

def test_method_a(time_request, setup):
    print("running method a")

@pytest.mark.run(order=1)
def test_method_b(time_request, setup):
    print("running method b")



