from weather import get_temperature


def test_tel_aviv_temperature_is_reasonable():
    temp = get_temperature(32.08, 34.78)
    assert -50 < temp < 60


def test_invalid_location_returns_none():
    temp = get_temperature(200, 34.78)
    assert temp is None