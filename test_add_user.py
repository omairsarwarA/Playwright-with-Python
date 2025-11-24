import re
from playwright.sync_api import Page, expect

def test_has_title(page: Page):
   
    page.goto("https://practice.expandtesting.com/notes/app")
    page.get_by_role("link", name="Login").click()
    page.get_by_test_id("login-email").click()
    page.get_by_test_id("login-email").fill("devnerdqa@yopmail.com")
    page.get_by_test_id("login-email").press("Tab")
    page.get_by_test_id("login-password").click()
    page.get_by_test_id("login-password").click()
    page.get_by_test_id("login-password").fill("Usa@12345")
    page.get_by_test_id("login-submit").click()
    page.get_by_test_id("add-new-note").click()
    page.get_by_test_id("note-category").select_option("Personal")
    page.get_by_test_id("note-title").click()
    page.get_by_test_id("note-title").fill("Test101")
    page.get_by_test_id("note-description").click()
    page.get_by_test_id("note-description").fill("Test101")
    page.get_by_test_id("note-submit").click()
    page.get_by_test_id("search-input").click()
    page.get_by_test_id("search-input").fill("Test101")
    page.get_by_test_id("search-btn").click()
    page.get_by_test_id("note-delete").click()
    page.get_by_test_id("note-delete-confirm").click()