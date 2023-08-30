import pytest
import requests

url = "https://reqres.in/api"

def test_create_user():
	data = {
    "name": "morpheus",
    "job": "leader"
	}
	response = requests.request("POST",url+"/users",data = data)
	assert response.status_code == 201

def test_create_user_without_name():
	data = {
    "job": "leader"
	}
	response = requests.request("POST",url+"/users",data = data)
	assert response.status_code == 400
def test_create_user_without_job():
	data = {
    "name": "morpheus",
	}
	response = requests.request("POST",url+"/users",data = data)
	assert response.status_code == 400

def test_create_user_without_variable():
	data = {
    
	}
	response = requests.request("POST",url+"/users",data = data)
	assert response.status_code == 400

def test_update_user():
	data = {
    "name": "morpheus",
    "job": "zion resident"
	}
	response = requests.request("PUT",url+"/users/2",data = data)
	assert response.status_code == 200
	print(response.content)

def test_update_user_patch():
	data = {
    "name": "morpheus",
    "job": "zion resident"
	}
	response = requests.request("PATCH",url+"/users/2",data = data)
	assert response.status_code == 201
	print(response.content) 


def test_delete_user():
	response = requests.delete(url+"/users/2")
	assert response.status_code == 204

def test_delete_nonexists_user():
	response = requests.delete(url+"/users/23")
	assert response.status_code == 400

