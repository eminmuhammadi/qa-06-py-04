class ProductsPage:
    def __init__(self, page):
        self.page = page
        self.title_heading = page.locator('[data-test="title"]')

    def visit(self):
        self.page.goto("https://www.saucedemo.com/inventory.html")