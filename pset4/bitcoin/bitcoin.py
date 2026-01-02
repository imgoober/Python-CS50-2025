import requests
import json
import sys


if len(sys.argv) > 2:
    print("Missing command-line argument")
elif len(sys.argv) < 2:
    print("Too many arguments")
try:
    n = float(sys.argv[1])
except ValueError:
    print("Command-line argument is not a number.")
    sys.exit(1)

try:
    bitcoin_url = "https://rest.coincap.io/v3/assets/bitcoin?apiKey=cc232c20f5d258cf70d154ce7a9f0906abdb0fc11d2a6d9e5d3d1fe6377c6dc8"
    #headers = {"Authorization" : "Bearer = cc232c20f5d258cf70d154ce7a9f0906abdb0fc11d2a6d9e5d3d1fe6377c6dc8"}
    response = requests.get(bitcoin_url)
    result = response.json()
    #print(result)
    if "data" in result and "priceUsd" in result["data"]:
        price = float(result["data"]["priceUsd"])
        amount = n * price
        print(f"${amount:,.4f}")
    else:
        print("Missing data")
        sys.exit(1)
except requests.RequestException:
    print("RequestException")
    sys.exit(1)


