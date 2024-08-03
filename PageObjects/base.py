import allure
from playwright.sync_api import Page, TimeoutError, Response
from Data.environment import host


class Base:
    def __init__(self, page: Page):
        self.page = page

    @allure.step
    def open(self, uri) -> Response | None:
        return self.page.goto(f"{host.get_base_url()}{uri}", wait_until='domcontentloaded')

    @allure.step
    def click(self, locator: str) -> None:
        self.page.click(locator)

    @allure.step
    def input(self, locator: str, data: str) -> None:
        self.page.locator(locator).fill(data)

    def get_items_lists(self, locator: str):
        items = self.page.locator(locator).all_inner_texts()
        i = sorted(items)
        return i
