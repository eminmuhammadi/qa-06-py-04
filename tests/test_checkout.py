import pytest

# README !!
# https://playwright.dev/python/docs/api/class-page
# https://playwright.dev/python/docs/api/class-locator
# https://playwright.dev/python/docs/api/class-locator#locator-get-by-role

# py -m pytest -v --browser chromium --headed -q --tracing=on --video=on --html=reports/report.html --tags homework --slowmo 800
@pytest.mark.tags("homework")
def test_users_should_be_able_to_checkout(page):
    pass # Add your steps here
