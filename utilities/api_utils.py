import random
import string
from playwright.sync_api import sync_playwright

# ---------------------------
# Generate Random User Data
# ---------------------------
def generate_random_user():
    name = "user" + str(random.randint(1000, 9999))
    email = "user" + str(random.randint(1000, 9999)) + "@yopmail.com"
    password = "Pass@" + "".join(random.choices(string.ascii_letters + string.digits, k=6))
    return name, email, password

# ---------------------------
# API Helpers
# ---------------------------
def register_user(request_context, name, email, password):
    response = request_context.post(
        "https://practice.expandtesting.com/notes/api/users/register",
        data={
            "name": name,
            "email": email,
            "password": password
        }
    )
    assert response.status == 201
    return response.json()

def login_user(request_context, email, password):
    response = request_context.post(
        "https://practice.expandtesting.com/notes/api/users/login",
        data={
            "email": email,
            "password": password
        }
    )
    assert response.status == 200
    return response.json()["data"]["token"]

def get_profile(request_context, token):
    response = request_context.get(
        "https://practice.expandtesting.com/notes/api/users/profile",
        headers={"x-auth-token": token}
    )
    assert response.status == 200
    return response.json()
