from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.appiumby import AppiumBy

import json

# Set up desired capabilities
desired_caps = {
    "platformName": "Android",             
    "platformVersion": "15.0",             
    "deviceName": "emulator-5554",         
    "appPackage": "com.instagram.android", 
    "appActivity": ".activity.MainTabActivity", 
    "automationName": "UiAutomator2",      
    "noReset": True, 
    "fullReset": False 
}



# Initialize the Appium driver
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_capabilities=desired_caps)

# Wait for the app to load
wait = WebDriverWait(driver, 10)


el2 = driver.find_element(by=AppiumBy.XPATH, value="(//android.widget.ImageView[@resource-id=\"com.instagram.android:id/tab_icon\"])[4]")
el2.click()
el3 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="REEL")
el3.click()

video_path = "/storage/emulated/0/DCIM/Part_144.mp4"
file_input = driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
file_input.send_keys(video_path)

# Tap "Next" after video selection
next_button = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Next")
next_button.click()

# Wait for video processing (adjust sleep time as needed)
time.sleep(5)

# Add caption for the reel
caption_field = driver.find_element(AppiumBy.ID, "com.instagram.android:id/caption")
caption_field.send_keys("Check out my latest reel! #Automation")

# Open the scheduling option
schedule_option = driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='Schedule']")
schedule_option.click()

# Set the desired date and time for scheduling
# Assuming we interact with date/time pickers; adjust locators as per UI
date_picker = driver.find_element(AppiumBy.XPATH, "//android.widget.DatePicker")
date_picker.send_keys("2024-11-22")  # Replace with your desired date

time_picker = driver.find_element(AppiumBy.XPATH, "//android.widget.TimePicker")
time_picker.send_keys("10:30 AM")  # Replace with your desired time

# Confirm scheduling
confirm_schedule_button = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Confirm Schedule")
confirm_schedule_button.click()

# Finalize the reel upload
share_button = driver.find_element(AppiumBy.ID, "com.instagram.android:id/share_button")
share_button.click()

print("Reel scheduled successfully!")
