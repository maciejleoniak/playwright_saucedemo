def test_login_logout(page, base_url):
    page.goto(base_url)
    page.fill('[data-test="username"]', "standard_user")
    page.fill('[data-test="password"]', "secret_sauce")
    page.get_by_role("button", name="LOGIN").click()
    page.get_by_role("button", name="Open Menu").click()
    page.get_by_role("link", name="Logout").click()
    
    assert page.locator(".login_logo").is_visible()