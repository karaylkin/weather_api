from weather_api.weather import get_weather_data

def test_weather_data():
    api_key = "6c1d889aaf151880d51264b730e1e3eb"
    data = get_weather_data('London', api_key)
    assert isinstance(data, str)  
    assert 'Город:' in data or 'Error:' in data  

from weather_api.weather import get_weather_data


