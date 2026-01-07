
def test_firstplaywrite(playwright):
    browser = playwright.chromium.launch(headless= False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://rahulshettyacademy.com/")