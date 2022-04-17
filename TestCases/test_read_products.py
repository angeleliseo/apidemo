import pytest
import requests, jsonpath, json

file = open(r"./TestCases/TestData/env.json")
payload = json.load(file)
BASE_URL = payload["qa"]

def test_canary_http_status():
  test_endpoint = f"{BASE_URL}/"
  req = requests.get(test_endpoint)
  assert req.status_code == 200

def test_list_products_http_status():
  test_endpoint = f"{BASE_URL}/products"
  req = requests.get(test_endpoint)
  assert req.status_code == 200

def test_list_products_content():
  test_endpoint = f"{BASE_URL}/products"
  req = requests.get(test_endpoint)
  response_body = req.json()
  print(response_body)

  for product in response_body:
    res_id = product["id"]
    assert isinstance(res_id, str) == True
    assert res_id != ""

def test_get_product_http_status():
  test_endpoint = f"{BASE_URL}/products"
  req = requests.get(test_endpoint)
  response_body = req.json()
  assert len(response_body) > 0
  print(response_body[0])
  res_id = response_body[0]["id"]

  test_endpoint = f"{BASE_URL}/products/{res_id}"
  req = requests.get(test_endpoint)
  assert req.status_code == 200

def test_get_product_content():
  test_endpoint = f"{BASE_URL}/products"
  req = requests.get(test_endpoint)
  response_body = req.json()
  assert len(response_body) > 0, "There are not products to test"
  print(response_body[0])
  res_id = response_body[0]["id"]

  test_endpoint = f"{BASE_URL}/products/{res_id}"
  req = requests.get(test_endpoint)
  response_body = req.json()
  quantity = response_body["quantity"]
  assert isinstance(quantity, int) == True
  assert quantity > 0
