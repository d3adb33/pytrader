from coinbase.rest import RESTClient
from json import dumps

api_key = "organizations/4f46bf15-0bba-438e-a11e-3563ba6164ff/apiKeys/4b84a802-8a3e-4090-b667-3d709caf7bbf"
api_secret = "-----BEGIN EC PRIVATE KEY-----\nMHcCAQEEIJxWiqhGBYyukYf/OBq+OvWY4dUbKVW59n67glM45JmXoAoGCCqGSM49\nAwEHoUQDQgAECoobOF4+Av9F+OoHAy6c87H/wasVOcAjlcqu7QjSEoBSxzs0pUko\nhMhb6og+H4eaLOYn9i1sFVCDV+sY/vJgEg==\n-----END EC PRIVATE KEY-----\n"

client = RESTClient(api_key=api_key, api_secret=api_secret)

#client = RESTClient()
accounts = client.get_accounts()
#print(dumps(accounts.to_dict(), indent=2))
product = client.get_product("BTC-USD")
print("Current BTC Price is: ", product.price)


