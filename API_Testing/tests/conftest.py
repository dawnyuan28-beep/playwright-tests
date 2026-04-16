
import pytest

@pytest.fixture
def context(browser):
    context = browser.new_context(
        locale="en-US",
        extra_http_headers={
            "Accept-Language": "en-US,en;q=0.9"
        }
    )
    yield context
    context.close()


@pytest.fixture
def page(context):
    page = context.new_page()

    page.add_init_script("""
        localStorage.setItem('memos-locale', 'en');
    """)

    return page