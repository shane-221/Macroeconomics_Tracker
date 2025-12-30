import requests

url ="https://www.imf.org/external/datamapper/api/v1/NGDP_RPCH"
try:
    response =  requests.get(url = url)
except Exception as e:
    print(f"There is an error {e}")
finally:
    data = response.json()


