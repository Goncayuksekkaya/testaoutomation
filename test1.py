from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
import unittest

####-Kullanıcı adı ve şifre alanları boş geçildiğinde uyarı mesajı olarak "Epic sadface: Username is required" gösterilmelidir.

 
class Test_class(unittest.TestCase): # yeni bir class oluşturduk

    def gonca_test1(self):  # yeni bir method oluşturduk

        driver = webdriver.Chrome() # chrome browser açmak için driver değişkenine eşitledik

        driver.get("https://www.saucedemo.com/") # gideceğimiz adresi belirttik

        driver.maximize_window() # chrome penceresini tüm ekranı kaplayacak şekilde büyüttük

        sleep(1) # 1 saniye bekledik

        loginButton = driver.find_element(By.ID,"login-button") # websitesi üzerinde id değeri login-button olan butonu selenium metodu ile bulduk ve değişkene atadık

        loginButton.click() # bulduğumuz elementte tıklama metodunu çalıştırdık

        sleep(1) # 1 saniye bekledik

        error_message = driver.find_element(By.CLASS_NAME,"error-message-container").text # websitesi üzerinde class değeri error-message-container olan metni selenium metodu ile bulduk metin bilgisini .text ile aldık ve değişkene atadık

        expected_message = "Epic sadface: Username is required" # ekranda beklediğimiz yazıyı değişkene atadık

        self.assertEqual(error_message,expected_message,"Beklenen mesajla ekrandaki mesaj uyumlu değil!") # ekrandaki mesaj ile beklediğimiz mesajı karşılaştırdık. Eğer aynı değilse konsola Beklenen mesajla ekrandaki mesaj uyumlu değil! mesajını yazdırdık.
        print("1. test başarılı!")

###-Sadece şifre alanı boş geçildiğinde uyarı mesajı olarak "Epic sadface: Password is required" gösterilmelidir.

    def gonca_test2(self):  # yeni bir method oluşturduk

        driver = webdriver.Chrome() # chrome browser açmak için driver değişkenine eşitledik

        driver.get("https://www.saucedemo.com/") # gideceğimiz adresi belirttik

        driver.maximize_window() # chrome penceresini tüm ekranı kaplayacak şekilde büyüttük

        sleep(1) # 1 saniye bekledik

        fill_username = driver.find_element(By.ID,"user-name") # websitesi üzerinde id değeri user-name olan textbox'ı selenium metodu ile bulduk ve değişkene atadık

        fill_username.send_keys("standard_user") # websitesi üzerinde bulduğumuz username textbox'a standart_user değerini yazdık

        sleep(1) # 1 saniye bekledik

        loginButton = driver.find_element(By.ID,"login-button") # websitesi üzerinde id değeri login-button olan butonu selenium metodu ile bulduk ve değişkene atadık

        loginButton.click() # bulduğumuz elementte tıklama metodunu çalıştırdık

        sleep(1) # 1 saniye bekledik

        error_message = driver.find_element(By.CLASS_NAME,"error-message-container").text # websitesi üzerinde class değeri error-message-container olan metni selenium metodu ile bulduk metin bilgisini .text ile aldık ve değişkene atadık

        expected_message = "Epic sadface: Password is required" # ekranda beklediğimiz yazıyı değişkene atadık

        self.assertEqual(error_message,expected_message,"Beklenen mesajla ekrandaki mesaj uyumlu değil!") # ekrandaki mesaj ile beklediğimiz mesajı karşılaştırdık. Eğer aynı değilse konsola Beklenen mesajla ekrandaki mesaj uyumlu değil! mesajını yazdırdık.
        print("2. test başarılı!")

###-Kullanıcı adı "locked_out_user" şifre alanı "secret_sauce" gönderildiğinde "Epic sadface: Sorry, this user has been locked out." mesajı gösterilmelidir.
    def gonca_test3(self):
        driver=webdriver.Chrome()
        driver.get("https://www.saucedemo.com/")
        driver.maximize_window()
        sleep(1)
        fill_username = driver.find_element(By.ID,"user-name")
        fill_username.send_keys("locked_out_user")
        fill_password = driver.find_element(By.ID,"password")
        fill_password.send_keys("secret_sauce")
        sleep(1)
        loginButton = driver.find_element(By.ID,"login-button") # websitesi üzerinde id değeri login-button olan butonu selenium metodu ile bulduk ve değişkene atadık
        loginButton.click() # bulduğumuz elementte tıklama metodunu çalıştırdık
        sleep(1)
        error_message = driver.find_element(By.CLASS_NAME,"error-message-container").text # websitesi üzerinde class değeri error-message-container olan metni selenium metodu ile bulduk metin bilgisini .text ile aldık ve değişkene atadık
        expected_message = "Epic sadface: Sorry, this user has been locked out." # ekranda beklediğimiz yazıyı değişkene atadık
        self.assertEqual(error_message,expected_message,"Beklenen mesajla ekrandaki mesaj uyumlu değil!") # ekrandaki mesaj ile beklediğimiz mesajı karşılaştırdık. Eğer aynı değilse konsola Beklenen mesajla ekrandaki mesaj uyumlu değil! mesajını yazdırdık.
        print("3. test başarılı!")

        ##-Kullanıcı adı "standard_user" şifre "secret_sauce" gönderildiğinde kullanıcı "/inventory.html" sayfasına gönderilmelidir. Giriş yapıldıktan sonra kullanıcıya gösterilen ürün sayısı "6" adet olmalıdır.
    def gonca_test4(self):
        driver=webdriver.Chrome()
        driver.get("https://www.saucedemo.com/")
        driver.maximize_window()
        sleep(1)
        fill_username = driver.find_element(By.ID,"user-name")
        fill_username.send_keys("standard_user")
        fill_password = driver.find_element(By.ID,"password")
        fill_password.send_keys("secret_sauce")
        sleep(1)
        loginButton = driver.find_element(By.ID,"login-button")
        loginButton.click()
        sleep(10)

    




















testClass = Test_class() # yazdığımız test class'ını çağırdık
#testClass.gonca_test1() # yazdığımız test fonksiyonunu çalıştırmak için burada bu satırı yazıyoruz
#testClass.gonca_test2() # yazdığımız test fonksiyonunu çalıştırmak için burada bu satırı yazıyoruz
#testClass.gonca_test3()
testClass.gonca_test4()

        


