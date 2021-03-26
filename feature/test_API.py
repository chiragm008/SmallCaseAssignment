import requests
import pytest
from endpoint.EndPointFactory import EndPoint


def test_books():
    response = requests.get(EndPoint.BASE_URI_API)
    print("\nStatus Code = ", response.status_code)
    print("Request URL = ", response.url)

    data = response.json()
    #print(data)

    da1 = data['books'][0]['isbn']
    da2 = data['books'][0]['title']
    da3 = data['books'][0]['subTitle']
    da4 = data['books'][0]['author']
    da5 = data['books'][0]['publish_date']
    da6 = data['books'][0]['publisher']
    da7 = data['books'][0]['pages']
    da8 = data['books'][0]['description']
    da9 = data['books'][0]['website']

    assert da1 == EndPoint.isbn and type(da1) == str
    assert da2 == EndPoint.title and type(da2) == str
    assert da3 == EndPoint.subTitle and type(da3) == str
    assert da4 == EndPoint.author and type(da4) == str
    assert da5 == EndPoint.publish_date and type(da5) == str
    assert da6 == EndPoint.publisher and type(da6) == str
    assert da7 == EndPoint.pages and type(da7) == int
    assert da8 == EndPoint.description and type(da8) == str
    assert da9 == EndPoint.website and type(da9) == str
