import re
from playwright.sync_api import Page, expect
import pytest
from playwright.sync_api import Playwright, APIRequestContext, sync_playwright



def test_register(page: Page): 

    page.goto("https://practice.expandtesting.com/notes/app/register")
    page.get_by_test_id("register-email").click()
    page.get_by_test_id("register-email").fill("devnerdqa113@yopmail.com")
    page.get_by_test_id("register-email").press("Tab")
    page.get_by_test_id("register-password").click()
    page.get_by_test_id("register-password").fill("Usa@12345")
    page.get_by_test_id("register-name").click()
    page.get_by_test_id("register-name").fill("Devnerdqa101")
    page.get_by_test_id("register-confirm-password").click()
    page.get_by_test_id("register-confirm-password").fill("Usa@12345")
    page.get_by_test_id("register-submit").click()
    # page.get_by_text("User account created").click()
    page.get_by_test_id("login-view").click()



