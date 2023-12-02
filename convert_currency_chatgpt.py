import json
import requests

payload = {}
headers = {"apikey": "6Hm25XXamrWza0StHe1WaFZNhWpXnzEP"}
base_url = "https://api.apilayer.com/fixer/"

def make_request(endpoint, params=None):
    """
    Make an API request to the specified endpoint.

    Parameters:
    - endpoint (str): The API endpoint to request.
    - params (dict): Optional parameters to include in the request.

    Returns:
    - dict or None: The JSON response if successful, or None on failure.
    """
    url = base_url + endpoint
    response = requests.get(url, headers=headers, params=params)

    try:
        response.raise_for_status()
        return response.json()

    except requests.exceptions.RequestException as e:
        print(f"Error making API request to {url}: {e}")

    except json.JSONDecodeError as e:
        print(f"Error decoding JSON response: {e}")

    return None

def get_currency_symbols():
    """
    Get the currency symbols using the 'symbols' endpoint.

    Returns:
    - dict or None: The currency symbols if successful, or None on failure.
    """
    endpoint = "symbols"
    return make_request(endpoint)

def convert_currency(from_currency, to_currency, amount):
    """
    Convert currency using the 'convert' endpoint.

    Parameters:
    - from_currency (str): The currency to convert from.
    - to_currency (str): The currency to convert to.
    - amount (float): The amount to convert.

    Returns:
    - float or None: The conversion result if successful, or None on failure.
    """
    params = {"to": to_currency, "from": from_currency, "amount": amount}
    endpoint = "convert"
    result = make_request(endpoint, params)

    if result:
        return result.get("result")

    return None

# Example usage
print(get_currency_symbols())

from_currency = input("Enter the currency you want to convert from: ")
to_currency = input("Enter the currency you want to convert to: ")
amount = float(input("Enter amount: "))

result = convert_currency(from_currency, to_currency, amount)

if result is not None:
    print("Conversion Result:", result)
else:
    print("Conversion failed.")
