class CatalogueLocators:

    LOWER_PRICE = '//*[@id="filter-price"]/div/div[1]/div/div[1]/input'
    HIGHER_PRICE = '//*[@id="filter-price"]/div/div[1]/div/div[2]/input'
    PRICE_RANGES = '//*[text()="Цена: от 500 до 1000 руб."]'
    INSTALLMENT_PAYMENT = '//div[4]/div/div/label/div[1]'
    INSTALLMENT_PAYMENT_SIGN = '//span[text()="Товары в рассрочку"]'
    DISCOUNT_GOODS = '//div[5]/div/div/label/div[1]'
    DISCOUNT_GOODS_SIGN = '//span[text()="Товары с уценкой"]'
    ACTIONS_FILTER = '//div[@data-target="#filter-actions"]'
    ALL_ACTIONS = '//*[@id="filter-actions"]/div/div[2]/div/label/div[1]'
    ALL_ACTIONS_SIGN = '//span[text()="Акции: ВСЕ акционные товары"]'
    XIAOMI_BRAND_CHECKBOX = '//*[@id="filter-692695"]/div/div[2]/div/label/div[1]'
    BRAND_SELECTED_SIGN = '//span[text()="Бренд: XIAOMI"]'
    SHOW_ALL_YEARS = '//*[@id="filter-726460"]/div/a/span[1]'
    YEAR_2023 = '//*[@id="filter-more-726460"]/div[2]/div/label/div[1]'
    YEAR_2023_SIGN = '//span[text()="Год выхода модели: 2023"]'
    SORT_DROPDOWN = '//div[2]/div/div/div[2]/div/button'
    VALUE_RATING = '//input[@value="rating"]'
    SORT_BY_RATING = '//span[text()="По рейтингу"]'
    CATALOGUE_CITY_LIST = '//span[@class="a-link city-link"]'
    CITY_OF_A_CLIENT_TO_SELECT = '//div[text()="Брест"]'
    FINAL_ACTUAL_CITY = '//span[text()="Бреста"]'
    ITEM_1 = '//button[@data-product_id="784765"]'
