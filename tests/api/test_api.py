from playwright.sync_api import sync_playwright
from utilities.api_utils import generate_random_user, register_user, login_user, get_profile

def test_user_flow():
    name, email, password = generate_random_user()

    print("\nGenerated User:")
    print("Name:", name)
    print("Email:", email)
    print("Password:", password)

    with sync_playwright() as p:
        request_context = p.request.new_context()

        # Register
        reg_response = register_user(request_context, name, email, password)
        print("Register Response:", reg_response)

        # Login
        token = login_user(request_context, email, password)
        print("Login Token:", token)

        # Profile
        profile_response = get_profile(request_context, token)
        print("Profile Response:", profile_response)
