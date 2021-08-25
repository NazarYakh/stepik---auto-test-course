browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/explicit_wait2.html")

price = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "100"))
button = browser.find_element_by_css_selector(".card-body > .btn-primary")
button.click()


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


x_element = browser.find_element_by_id("input_value")
x = x_element.text
y = calc(x)
input1 = browser.find_element_by_id("answer")
input1.send_keys(y)

button2 = browser.find_element_by_id("solve")
button2.click()
time.sleep(5)