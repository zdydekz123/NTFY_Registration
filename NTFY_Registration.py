from selenium import webdriver
import unittest
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

fbemail = "zdybek1997@onet.pl"
fbpassword = "Zdybcio199"

class NtfyRegistration(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('D:/chromedriver/chromedriver.exe')
        # 1. Wejdź na stronę "NTFY".
        self.driver.get('https://ntfy-vue.nidev.pl/')
        self.driver.maximize_window()
        self.driver.implicitly_wait(60)

    def tearDown(self):
        self.driver.quit()

    def testCheckTotalValueProducts(self):
        driver = self.driver
        # 2. Przejdź do nawigacji strony głównej i kliknij w button "Zaloguj się".
        sign_in_button = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, 'btn-login')))
        sign_in_button.click()

        # 3. Kliknij w przycisk "Zaloguj się przez Facebooka"

        fb_sign_in = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//a[@class='plg-ni_users_login-facebookBtn']")))
        fb_sign_in.click()

        # 4. Przejdz do nowego okna z logowaniem do Facebooka
        window_before = driver.window_handles[0]
        window_after = driver.window_handles[1]
        for handle in driver.window_handles:
            driver.switch_to.window(handle)

        # 5. W oknie logowania do serwisu FB wypełnij pola formularzu o adres e-mail i hasło
        input_email = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, 'email')))
        input_email.send_keys(fbemail)

        input_password = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, 'pass')))
        input_password.send_keys(fbpassword)

        # 6. Naciśnij w przycisk "Log In"
        log_in = driver.find_element_by_id('loginbutton')
        log_in.click()

        # UWAGA: SPRAWDZAMY REZULTAT!

        # Wyszukuje wszystkie błedy
        error_notices = driver.find_elements_by_xpath('//div[@id="error_box"]/div')

        # Pusta lista na widoczne błedy
        visible_error_notices = []

        # Przypisz wszystkie wyświetlone błedy do listy visible_error_notices
        for error in error_notices:
            if error.is_displayed():
                visible_error_notices.append(error)

        # Wyświetl błedy
        for errortype in visible_error_notices:
            print(errortype.get_attribute('innerHTML'))


        sleep(10)


if __name__ == '__main__':
    unittest.main(verbosity=2)