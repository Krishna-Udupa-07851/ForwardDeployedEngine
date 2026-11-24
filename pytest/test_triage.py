from triage import categorise


def test_charge_is_billing():
    assert categorise("I was charged twice for one order") == "billing"


def test_parcel_is_shipping():
    assert categorise("My parcel has not arrived") == "shipping"


def test_password_is_other():
    assert categorise("How do I change my password?") == "other"


def test_money_back_is_billing():
    assert categorise("I want my money back") == "billing"