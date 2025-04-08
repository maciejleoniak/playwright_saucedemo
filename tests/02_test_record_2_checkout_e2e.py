import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.saucedemo.com/v1/")
    page.locator("#login_button_container").click()
    page.locator("[data-test=\"username\"]").click()
    page.locator("[data-test=\"username\"]").fill("standard_user")
    page.locator("[data-test=\"password\"]").click()
    page.locator("[data-test=\"password\"]").fill("secret_sauce")
    page.get_by_role("button", name="LOGIN").click()
    page.get_by_role("button", name="Open Menu").click()
    page.get_by_role("link", name="Logout").click()
    page.locator(".login_logo").click()
    page.locator("[data-test=\"username\"]").click()
    page.locator("[data-test=\"username\"]").fill("standard_user")
    page.locator("[data-test=\"password\"]").click()
    page.locator("[data-test=\"password\"]").fill("secret_sauce")
    page.get_by_role("button", name="LOGIN").click()
    page.get_by_role("link", name="Sauce Labs Backpack").click()
    page.get_by_role("button", name="ADD TO CART").click()
    page.get_by_role("button", name="<- Back").click()
    page.locator("div").filter(has_text=re.compile(r"^\$9\.99ADD TO CART$")).get_by_role("button").click()
    page.get_by_role("link", name="2").click()
    page.get_by_role("link", name="CHECKOUT").click()
    page.locator("[data-test=\"firstName\"]").click()
    page.locator("[data-test=\"firstName\"]").fill("Swag")
    page.locator("[data-test=\"firstName\"]").press("Tab")
    page.locator("[data-test=\"lastName\"]").fill("Labs")
    page.locator("[data-test=\"lastName\"]").press("Tab")
    page.locator("[data-test=\"postalCode\"]").fill("007")
    page.get_by_role("button", name="CONTINUE").click()
    page.get_by_role("link", name="FINISH").click()
    page.get_by_role("heading", name="THANK YOU FOR YOUR ORDER").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
