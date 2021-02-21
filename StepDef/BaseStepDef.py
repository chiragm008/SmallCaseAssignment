from requests.exceptions import HTTPError
from requests.exceptions import Timeout

def pretty_print_request(request):
    print( '\n{}\n{}\n\n{}\n\n{}\n'.format(
    '-----------Request----------->',
    request.method + ' ' + request.url,
    '\n'.join('{}: {}'.format(k, v) for k, v in request.headers.items()),
    request.body)
    )

def pretty_print_response(response):
    print('\n{}\n{}\n\n{}\n\n{}\n'.format(
    '<-----------Response-----------',
    'Status code:' + str(response.status_code),
    '\n'.join('{}: {}'.format(k, v) for k, v in response.headers.items()),
    response.text)
    )

def PrintData(response):
    try:
        response.raise_for_status()
    except HTTPError:
        print(f"Http Error occurred", HTTPError)
    except Exception:
        print(f"Exception has occurred", Exception)
    except Timeout:
        print("The request timed out")
    else:
        print("Login Success")

        print("Response Code is:", response.status_code)
        print("Response Text is:", response.text)
        assert response.status_code == 200
        pretty_print_request(response.request)
        pretty_print_response(response)
