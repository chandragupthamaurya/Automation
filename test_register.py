import pytest
import requests

url = "https://reqres.in/api"

def test_register_success():
	data  = {
	"email": "eve.holt@reqres.in",
    "password": "pistol"
    }
	response = requests.request("POST",url+'/api/register',data = data)
	print(response.content)
	assert response.status_code == 201
	

def test_register_without_password():
	data  = {
	"email": "eve.holt@reqres.in",
	"password": None
    }
	response = requests.request("POST",url+'/api/register',data = data)
	assert response.status_code == 400

def test_register_without_email():
	data  = {
	"email":None,
	"password": "new123",
    }
	response = requests.request("POST",url+'/api/register',data = data)
	assert response.status_code == 400

def test_register_without_credential():
	data  = {
	"email":None,
	"password": None,
    }
	response = requests.request("POST",url+'/api/register',data = data)
	assert response.status_code == 400

def test_login():
	data  = {
	"email": "eve.holt@reqres.in",
    "password": "cityslicka",
    }
	response = requests.request("POST",url+'/api/login',data = data)
	assert response.status_code == 201
	print(response.content)

def test_login_without_email():
	data  = {
	"email": "",
    "password": "cityslicka",
    }
	response = requests.request("POST",url+'/api/login',data = data)
	assert response.status_code == 400

def test_login_without_password():
	data  = {
	"email": "eve.holt@reqres.in",
    "password": "",
    }
	response = requests.request("POST",url+'/api/login',data = data)
	assert response.status_code == 400