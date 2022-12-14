import requests
producturl="http://google.com/"

res = requests.get(producturl, timeout=5)
print(res.status_code)