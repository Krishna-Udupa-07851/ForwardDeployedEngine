import pytest
from pydantic import ValidationError
from parse import parse_answer


def test_good_answer():
    result = parse_answer('{"category": "billing", "priority": 5}')
    assert result.category == "billing"


def test_rejected():
    with pytest.raises(ValidationError):
        parse_answer("Human review needed")

@pytest.mark.parametrize("answer", [
    '{"category": "sales", "priority": 4}',
    '{"category": "billing", "priority": 9}',
    '{"category": "billing"}',
    '{"category": "billing", "priority": 0}',
    '{"category": "billing", "priority": "high"}',
    '{"category": "billing", "priority": "4"}',
])
def test_bad_values_are_rejected(answer):
    with pytest.raises(ValidationError):
        parse_answer(answer)