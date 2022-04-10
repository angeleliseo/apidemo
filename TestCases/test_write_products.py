import pytest
import requests, json

BASE_URL = "http://localhost:8000"
#json file request
file = open(r"./TestCases/TestData/add_product_request.json")
payload = json.load(file)


def test_add_prodcts_http_response():
  test_url = f"{BASE_URL}/products/create"
  req = requests.post(test_url, data=json.dumps(payload))
  response_body = req.json()
  print(response_body)
  assert req.status_code == 200
  remove_data(response_body["pk"])

def test_add_prodcts_content_response():
  test_url = f"{BASE_URL}/products/create"
  req = requests.post(test_url, data=json.dumps(payload))
  response_body = req.json()
  print(response_body)
  assert isinstance(response_body["pk"], str) == True
  assert response_body["name"] == "Development services"
  remove_data(response_body["pk"])

def remove_data(pk: str):
  test_url = f"{BASE_URL}/products/{pk}"
  req = requests.delete(test_url)
  assert req.status_code == 200, "Error deleting the product"
  req = requests.get(test_url)
  assert req.status_code == 500, "Product is yet being listed after deleting it"