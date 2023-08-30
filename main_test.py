import pytest
import math
import requests

url = "https://reqres.in/api"

def test_main_api():
	response = requests.request("GET",url +"/users?page=2")
	res = response.json()
	assert response.status_code == 200

def test_single_user():
	response = requests.request("GET",url +"/users/2")
	res = response.json()
	assert res["data"]['email'] == 'janet.weaver@reqres.in'
	assert response.status_code == 200

def test_invalid_user():
	response = requests.request("GET",url + "/users/23")
	assert response.status_code == 404

def test_resource():
	response = requests.request("GET",url + "/unknown")
	assert response.status_code == 200

def test_single_resource():
	response = requests.request("GET",url+"/unknown/2")
	res = response.json()
	assert res["data"]["name"] == "fuchsia rose"
	assert response.status_code == 200

def test_unknown_resource():
	response = requests.request("GET",url+"/unknown/23")
	assert response.status_code == 404

	
	 



