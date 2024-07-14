Technologies Used

    1. Django: Python-based web framework for backend development.
    2. Selenium: Web browser automation tool for controlling web browsers through Python scripts.
    3. SMTP Library: Python library for sending emails.

Approaching the assignment involved first understanding the requirements thoroughly, then planning the project structure with Django for backend handling. 
Next, I integrated Selenium for automated interactions with the Google Form, ensuring form submission was streamlined. Error handling was implemented to manage exceptions gracefully, and SMTP library was utilized to send emails with captured screenshots.
Testing was crucial to validate each step of the automation process. Finally, documentation was prepared to provide clear insights into project functionality and usage, ensuring a comprehensive submission. 
    
    if request.method == 'POST':
    form = EmailForm(request.POST)
    if form.is_valid():
    
Checks if the request method is POST and initializes an EmailForm with the POST data, validating it to ensure required fields (from_email, to_email, subject, message) are correctly filled.

Selenium uses Chrome WebDriver to locate and interact with elements on a Google Form:
  1. div_elements: Finds all input fields within a div classed Xb9hP.
  2. address: Locates a textarea inside a div with classes Pc9Gce and Wic03c.
  3. code: Identifies a span with class M7eMe containing a b tag, typically used for a verification code

     div_elements = browser.find_elements(By.XPATH, '//div[@class="Xb9hP"]//input')
     address = browser.find_element(By.XPATH, '//div[@class="Pc9Gce Wic03c"]//textarea')
     code = browser.find_element(By.XPATH, '//span[@class="M7eMe"]//b')

send_keys() method is essential for automating interactions with web forms, where you need to fill out fields, enter text, or simulate user input through scripts or automated tests.
          
          element = browser.find_element(By.XPATH, '//input[@id="username"]')
          element.send_keys("example@gmail.com")

EmailMessage class to construct an email message and attach a file:

EmailMessage: This is a class provided by Django's django.core.mail module for creating email messages programmatically.
Parameters:

subject: Subject line of the email.
message: Body or content of the email.
from_email: Sender's email address.
[to_email]: List containing the recipient's email address(es).
cc=['hr@themedius.ai']: Optional parameter specifying email addresses to be included in the CC (carbon copy) field.
After constructing the email message, the code attaches a file (screenshot_path) to the email using the attach_file() method. This method adds the specified file as an attachment to the email message before sending it.

    email = EmailMessage(
    subject,
    message,
    from_email,
    [to_email],
    cc=['hr@themedius.ai'],
    )
    email.attach_file(screenshot_path)
