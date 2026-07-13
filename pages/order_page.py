from datetime import date, timedelta

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class OrderPage(BasePage):
    NAME_INPUT = (By.XPATH, "//input[@placeholder='* Имя']")
    LAST_NAME_INPUT = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS_INPUT = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_INPUT = (By.XPATH, "//input[@placeholder='* Станция метро']")
    PHONE_INPUT = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, "//button[contains(., 'Далее')]")
    DATE_INPUT = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    RENTAL_PERIOD_DROPDOWN = (By.CLASS_NAME, "Dropdown-control")
    RENTAL_OPTION = (By.XPATH, "//div[@class='Dropdown-option' and text()='сутки']")
    BLACK_COLOR = (By.ID, "black")
    COMMENT_INPUT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    ORDER_BUTTON = (By.XPATH, "//button[contains(., 'Заказать')]")
    CONFIRM_ORDER_BUTTON = (By.XPATH, "//button[contains(., 'Да')]")
    SUCCESS_MESSAGE = (By.XPATH, "//*[contains(text(), 'Заказ оформлен')]")

    def fill_customer_form(self, name, last_name, address, metro, phone):
        self.fill_input(self.NAME_INPUT, name)
        self.fill_input(self.LAST_NAME_INPUT, last_name)
        self.fill_input(self.ADDRESS_INPUT, address)
        self.select_metro(metro)
        self.fill_input(self.PHONE_INPUT, phone)

    def select_metro(self, metro):
        self.click(self.METRO_INPUT)
        self.fill_input(self.METRO_INPUT, metro)
        option = self.wait.until(EC.element_to_be_clickable((By.XPATH, f"//div[contains(@class, 'Order_Text') and contains(., '{metro}')]")))
        option.click()

    def continue_to_next_step(self):
        self.click(self.NEXT_BUTTON)

    def fill_delivery_details(self):
        delivery_date = (date.today() + timedelta(days=1)).strftime("%d.%m.%Y")
        self.fill_input(self.DATE_INPUT, delivery_date)
        self.driver.find_element(By.TAG_NAME, "body").send_keys(Keys.ESCAPE)
        self.click(self.RENTAL_PERIOD_DROPDOWN)
        self.click(self.RENTAL_OPTION)
        self.click(self.BLACK_COLOR)
        self.fill_input(self.COMMENT_INPUT, "Тестовый заказ")

    def confirm_order(self):
        buttons = self.driver.find_elements(*self.ORDER_BUTTON)
        buttons[-1].click()
        self.click(self.CONFIRM_ORDER_BUTTON)

    def is_success_message_displayed(self):
        return self.wait.until(EC.visibility_of_element_located(self.SUCCESS_MESSAGE)).is_displayed()
