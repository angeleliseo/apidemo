#from dataclasses import dataclass
from itertools import product
import string
from typing import Optional
from redis_om import get_redis_connection, HashModel
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

redis =  get_redis_connection(
  host="redis-14743.c289.us-west-1-2.ec2.cloud.redislabs.com",
  port=14743,
  password="JSUbhMh3vs8zNxyUX3hmeYExxjsTKt6E",
  decode_responses=True
)

app.add_middleware(
  CORSMiddleware,
  allow_origins = ["http://localhost:3000"],
  allow_methods = ["*"],
  allow_headers = ["*"]
)

class Product(HashModel):
  name: str
  price: float
  quantity: int

  class Meta:
    database = redis

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/products")
def all_products():
    return [format(pk) for pk in Product.all_pks()]

def format(pk: str):
  product = Product.get(pk)

  return {
    "id": product.pk,
    "name": product.name,
    "price": product.price,
    "quantity": product.quantity
  }

@app.post("/products/create")
def add_products(product: Product):
    return product.save()

@app.get("/products/{pk}")
def get_product(pk: str):
  return Product.get(pk)

@app.delete("/products/{pk}")
def delete_product(pk: str):
  return Product.delete(pk)
