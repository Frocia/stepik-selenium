from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import time


# 1. Запускаем браузер
browser = webdriver.Chrome()

try:
    # 2. Открываем страницу
    browser.get("http://suninjuly.github.io/alert_accept.html")

    # 3. Нажимаем кнопку
    button = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button"))
    )
    button.click()

    # 4. Принимаем confirm
    WebDriverWait(browser, 10).until(EC.alert_is_present())
    alert = browser.switch_to.alert
    alert.accept()

    # 5. Ждём загрузки новой страницы
    time.sleep(1)

    # 6. Получаем число x
    x_element = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.ID, "input_value"))
    )

    x = int(x_element.text)

    # 7. Решаем капчу
    answer = math.log(abs(12 * math.sin(x)))

    print("x =", x)
    print("Ответ =", answer)

    # 8. Вводим ответ
    answer_input = browser.find_element(By.ID, "answer")
    answer_input.send_keys(str(answer))

    # 9. Нажимаем Submit
    button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    button.click()

    # 10. Ждём результат
    time.sleep(2)

    # 11. Получаем текст итогового alert
    WebDriverWait(browser, 10).until(EC.alert_is_present())
    result = browser.switch_to.alert.text

    print("Результат:", result)

    # Оставляем alert открытым
    # чтобы можно было увидеть число

    input("Нажмите Enter для закрытия браузера...")

finally:
    browser.quit()