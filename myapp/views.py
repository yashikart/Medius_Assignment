from django.shortcuts import render
from django.core.mail import EmailMessage
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from .emailform import EmailForm

def email_form(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            from_email = form.cleaned_data['from_email']
            to_email = form.cleaned_data['to_email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            # Set up WebDriver
            browser = webdriver.Chrome()
            google_form = 'https://forms.gle/WT68aV5UnPajeoSc8'
            browser.get(google_form)

            div_element = browser.find_elements(By.XPATH, '//div[@class="Xb9hP"]//input')
            address = browser.find_element(By.XPATH, '//div[@class="Pc9Gce Wic03c"]//textarea')
            address.send_keys("Marol Pipeline Andheri East Mumbai")
            code = browser.find_element(By.XPATH, '//span[@class="M7eMe"]//b')
            div_element[-1].send_keys(code.text)
            print(code.text)

            my_data = ["Yashika Tirkey","9987198692","tirki.yashika@gmail.com","400059","20-01-2001","Female"]
            count = 0
            print(div_element)
            for i in div_element:
                i.send_keys(my_data[count])
                time.sleep(1)
                count = count + 1
                if count == 6:
                    break

            submit_button = browser.find_element(By.XPATH, '//div[@role="button"]')
            submit_button_xpath = '//div[@role="button"]'
            submit_button = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.XPATH, submit_button_xpath)))
            browser.execute_script("arguments[0].scrollIntoView(true);", submit_button)
            submit_button.click()
            time.sleep(3)

            screenshot_path = 'Screenshot.png'
            browser.save_screenshot(screenshot_path)
            browser.quit()

            email = EmailMessage(
                subject,
                message,
                from_email,
                [to_email],

            )


            email.attach_file(screenshot_path)


            email.send()

            return render(request, 'home.html', {'success': True})

    else:
        form = EmailForm()

    return render(request, 'home.html', {'form': form})
