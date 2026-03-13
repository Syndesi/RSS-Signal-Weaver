import json
import pytest

from rsssignalweaver.type import Demo


@pytest.mark.parametrize(
    "payload",
    [
        """
        {
            "type": "demo",
            "name": "alpha",
            "value": 1
        }
        """,
        """
        {
            "type": "demo",
            "name": "beta",
            "value": 42
        }
        """,
        """
        {
            "type": "demo",
            "name": "gamma",
            "value": 999
        }
        """
    ],
)
def test_demo_parsing(payload: str):
    data = json.loads(payload)

    obj = Demo.model_validate(data)

    assert obj.type == "demo"
    assert isinstance(obj.name, str)
    assert isinstance(obj.value, int)
