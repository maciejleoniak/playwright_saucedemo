import re


def test_full_checkout_flow(page, base_url):

    page.goto(base_url)
    
    page.locator('[data-test="username"]').fill("standard_user")
    page.locator('[data-test="password"]').fill("secret_sauce")
    page.get_by_role("button", name="LOGIN").click()

    page.get_by_role("link", name="Sauce Labs Backpack").click()
    page.get_by_role("button", name="ADD TO CART").click()
    page.get_by_role("button", name="<- Back").click()

    page.locator("div").filter(has_text=re.compile(r"^\$9\.99ADD TO CART$")).get_by_role("button").click()

    page.get_by_role("link", name="2").click()
    page.get_by_role("link", name="CHECKOUT").click()

    page.locator('[data-test="firstName"]').fill("Swag")
    page.locator('[data-test="lastName"]').fill("Labs")
    page.locator('[data-test="postalCode"]').fill("007")

    page.get_by_role("button", name="CONTINUE").click()
    page.get_by_role("link", name="FINISH").click()

    assert page.get_by_role("heading", name="THANK YOU FOR YOUR ORDER").is_visible()
