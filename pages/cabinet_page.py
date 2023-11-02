from data import *
from helpers import BasePage
from locators import CabinetLocators


class PersonalCabinetPage(BasePage, CabinetLocators):

    def open(self):
        self.driver.get(CABINET_PAGE_URL)

    def click_on_personal_data(self):
        self.click_on(self.PERSONAL_DATA)

    def fill_surname(self, surname):
        self.fill(self.USER_SURNAME, surname)

    def fill_name(self, name):
        self.fill(self.USER_NAME, name)

    def fill_lastname(self, lastname):
        self.fill(self.USER_LASTNAME, lastname)

    def fill_birthday(self, birthday):
        self.fill(self.USER_BIRTHDAY, birthday)

    def fill_personal_data(self, user):
        self.fill_surname(user['surname'])
        self.fill_name(user['name'])
        self.fill_lastname(user['lastname'])
        self.fill_birthday(user['birthday'])

    def choose_female_gender(self):
        self.select_radio_button(self.FEMALE_GENDER)

    def save_personal_data(self):
        self.click_on(self.SAVE_PERSONAL_BUTTON)

    def click_on_personal_account(self):
        self.click_on(self.ACCOUNT_LOCATOR)

    def assert_saved_personal_data(self, user):
        self.assert_text_in_element(self.SAVED_DATA, user['saved_data'])

    def click_on_my_subscribes(self):
        self.click_on(self.MY_SUBSCRIBES)

    def check_regular_mailing(self):
        self.check_checkbox(self.REGULAR_MAIING)

    def uncheck_regular_mailing(self):
        self.uncheck_checkbox(self.REGULAR_MAIING)

    def check_policy_agree(self):
        self.check_checkbox(self.POLICY_AGREE)

    def save_subscribes(self):
        self.click_on(self.SAVE_SUBSCRIBES)

    def click_on_sub_ok_button(self):
        self.click_on(self.SUB_OK_BUTTON)

    def assert_subscribes_saved_changes(self):
        self.assert_element_is_present(self.SUBSCRIBES_SAVED_CHANGES)



    def click_on_my_shop_button(self):
        self.click_on(self.MY_SHOP)

    def select_shop(self):
        self.scroll_down()
        self.click_on(self.FAVORITE_SHOP_TO_CHOOSE)

    def assert_if_favorite_shop_is_selected(self):
        self.assert_element_is_not_present(self.FAVORITE_SHOP)

    def delete_favorite_shop(self):
        self.click_on(self.DELETE_FAVORITE_SHOP_BUTTON)

    def assert_if_favorite_shop_is_deleted(self):
        self.assert_element_is_not_present(self.FAVORITE_SHOP)

    def click_on_delivery_address(self):
        self.click_on(self.DELIVERY_ADDRESS)

    def click_on_address_form(self):
        self.click_on(self.ADD_ADDRESS_FORM)

    def fill_city(self, city):
        self.fill(self.CITY_TO_FILL, city)
        self.click_on(self.SELECT_CITY)

    def fill_street(self, street):
        self.fill(self.STREET_TO_FILL, street)
        self.click_on(self.SELECT_STREET)

    def fill_house_number(self, house):
        self.fill(self.HOUSE_TO_FILL, house)

    def fill_apartment_number(self, apartment):
        self.fill(self.APARTMENT_TO_FILL, apartment)

    def fill_delivery_address_form(self, user):
        self.fill_city(user['city'])
        self.fill_street(user['street'])
        self.fill_house_number(user['house'])
        self.fill_apartment_number(user['apartment'])

    def set_address_to_default(self):
        self.check_checkbox(self.SET_TO_DEFAULT_ADDRESS_CHECKBOX)

    def save_address_settings(self):
        self.click_on(self.SAVE_ADDRESS_BUTTON)

    def assert_added_address(self):
        self.assert_element_is_present(self.ADDRESS_IS_PRESENT)

    def delete_address(self):
        self.click_on(self.DELETE_ADDRESS)

    def confirm_delete_address(self):
        self.click_on(self.CONFIRM_DELETE)

    def assert_if_address_is_deleted(self):
        self.assert_element_is_not_present(self.FAVORITE_SHOP)





