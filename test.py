from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://www.amazon.in")

    page.fill("#twotabsearchtextbox", "iPhone")
    page.press("#twotabsearchtextbox", "Enter")
    page.wait_for_selector(".s-main-slot")

    with context.expect_page() as new_page_info:
        page.locator(".s-main-slot .s-result-item h2 a").first.click()
    product_page = new_page_info.value

    product_page.wait_for_load_state()

    price1 = None
    for sel in ["#priceblock_ourprice", "#priceblock_dealprice", ".a-price .a-offscreen"]:
        if product_page.locator(sel).count() > 0:
            price1 = product_page.locator(sel).first.text_content()
            break

    print("iPhone Price:", price1)

    if product_page.locator("#add-to-cart-button").count() > 0:
        product_page.click("#add-to-cart-button")

    page.goto("https://www.amazon.in")

    page.fill("#twotabsearchtextbox", "Samsung Galaxy")
    page.press("#twotabsearchtextbox", "Enter")
    page.wait_for_selector(".s-main-slot")

    with context.expect_page() as new_page_info2:
        page.locator(".s-main-slot .s-result-item h2 a").first.click()
    product_page2 = new_page_info2.value

    product_page2.wait_for_load_state()

    price2 = None
    for sel in ["#priceblock_ourprice", "#priceblock_dealprice", ".a-price .a-offscreen"]:
        if product_page2.locator(sel).count() > 0:
            price2 = product_page2.locator(sel).first.text_content()
            break

    print("Galaxy Price:", price2)

    if product_page2.locator("#add-to-cart-button").count() > 0:
        product_page2.click("#add-to-cart-button")

    browser.close()