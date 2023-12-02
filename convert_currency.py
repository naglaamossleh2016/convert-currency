import json
import requests
payload = {}
headers= {
  "apikey": "6Hm25XXamrWza0StHe1WaFZNhWpXnzEP"
}
def get_currency_symbols():
    url = "https://api.apilayer.com/fixer/symbols"
    response = requests.request("GET", url, headers=headers, data = payload)
    status_code = response.status_code
    if(status_code==200):
        result = response.text
        return result
    else:
        print("Try again")

def convert_currency():
    from_currency=input("Enter the currency you want to convert from: ")
    to_currency=input("Enter currency you want to convert to: ")
    amount=float(input("Enter amount:"))
    url = f"https://api.apilayer.com/fixer/convert?to={to_currency}&from={from_currency}&amount={amount}"
    response = requests.request("GET", url, headers=headers, data = payload)
    
    status_code = response.status_code
    if(status_code==200):
        try:
            # result = response.text
            # return result
            result = json.loads(response.text)
            return result.get("result")
        except json.JSONDecodeError as e:
            print("Error decoding JSON:", e)
    else:
        print(f"Failed to fetch data. Status code: {status_code}")
    
print(get_currency_symbols())
result = convert_currency()
print("Conversion Result:", result)      