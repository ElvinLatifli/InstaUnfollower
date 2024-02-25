#import required libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.action_chains import ActionChains


#INPUT USERNAME AND PASSWORD IN  TERMINAL
username = input("write your username:")
password = input("write your password:")

username_letters_list = []
for letter in username:
   username_letters_list.append(letter)

   
password_letters_list = []
for letter in password:
   password_letters_list.append(letter)



#Let's set the driver and put the target link 
driver =  webdriver.Chrome()
driver.get("https://www.instagram.com/accounts/login/")


"""
Here, I set it to take the username and password from a list and write them letter by letter. 
Thus, the risk of being perceived as a robot will decrease.

"""
WebDriverWait(driver, 4).until(expected_conditions.visibility_of_element_located((By.NAME,"username")))
login_bar = driver.find_element(By.NAME,"username")

for usr in username_letters_list:
   time.sleep(0.2)
   login_bar.send_keys(usr)
   
time.sleep(2)
password_bar = driver.find_element(By.NAME,"password")

for pswd in password_letters_list:
    time.sleep(0.3)
    password_bar.send_keys(pswd)


"""
<<-- IMPORTANT -->>

The code works smoothly, but when getting the list of followers you follow, 
it is necessary to constantly move the scroll bar on the right of the frame 
downwards so that all the users in the list are loaded and we can include them in the project. 
Here is your task, I added a 20-second wait when the list of people you follow opens. 
Manually, you pull the scroll bar down until all members are loaded. 
I recommend that you do the same process when getting the followers list. 
I couldn't solve this automatically with selenium. If anyone can do it, that would be great.
"""

#Our main operating function is here!
number = 0
big_number = 0
def main_operating():
    for i in range(1,100):
        time.sleep(5)
        global number
        global big_number
        big_number= big_number+1
        number = number + 1
        if number == 5:
          time.sleep(15)
          number = 0
          i=i-1
        if big_number == 15:
            time.sleep(120)
            big_number = 0
            i=i-1
        else:
            xpath_degil = f"/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/div[1]/div/div[{i}]"
            WebDriverWait(driver, 4).until(expected_conditions.visibility_of_element_located((By.XPATH, xpath_degil)))
            go_followers = driver.find_element(By.XPATH, xpath_degil)
            username_follower = go_followers.find_element(By.CSS_SELECTOR, "span._ap3a._aaco._aacw._aacx._aad7._aade")
            usernamess = (username_follower.text)
            if usernamess not in usernames:
                unfollow_button = driver.find_element(By.XPATH,f"/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/div[1]/div/div[{i}]/div/div/div/div[3]/div/div")
                time.sleep(0.8)
                unfollow_button.click()
                WebDriverWait(driver, 4).until(expected_conditions.visibility_of_element_located((By.XPATH,"/html/body/div[6]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[1]")))
                remove_button = driver.find_element(By.XPATH,"/html/body/div[6]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[1]")
                time.sleep(0.6)
                remove_button.click()
                print(usernamess,"removed")
            else:
                print("Bu kisiyi takip ediyorsun")

"""
In the section below, while writing my code, I set it to tick alerts and s when I log in to the account. 
I put a time period between each click to reduce the risk of being perceived as a robot.
if the code does not work for you, update the xpath addresses.
"""
time.sleep(0.7)
login_button = driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div[2]/div/div/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[3]/button/div")
login_button.click()

time.sleep(5)
WebDriverWait(driver, 4).until(expected_conditions.visibility_of_element_located((By.XPATH,"/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div/div")))
save_info = driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div/div")
save_info.click()
time.sleep(1)

WebDriverWait(driver, 4).until(expected_conditions.visibility_of_element_located((By.XPATH,"/html/body/div[3]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]")))
nof_button = driver.find_element(By.XPATH,"/html/body/div[3]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]")
nof_button.click()
time.sleep(2)

WebDriverWait(driver, 4).until(expected_conditions.visibility_of_element_located((By.XPATH,"/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[8]/div/span")))
profile_button = driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[8]/div/span")
profile_button.click()
time.sleep(1.2)

WebDriverWait(driver, 4).until(expected_conditions.visibility_of_element_located((By.XPATH,"/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/ul/li[3]/a")))
followes_list = driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/ul/li[3]/a")
followes_list.click()
time.sleep(1.3)

WebDriverWait(driver, 4).until(expected_conditions.visibility_of_element_located((By.XPATH,"/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div")))
followes_dic = driver.find_element(By.XPATH,"/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div")


#Get usernames of people you follow
time.sleep(20)
username_element = driver.find_elements(By.CSS_SELECTOR, "span._ap3a._aaco._aacw._aacx._aad7._aade") 
usernames = []
for element in username_element:
    usernames.append(element.text)

exit_button = driver.find_element(By.XPATH,"/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/button")
exit_button.click()

time.sleep(0.5)
WebDriverWait(driver, 4).until(expected_conditions.visibility_of_element_located((By.XPATH,"/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/ul/li[2]/a")))
followers_button = driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/ul/li[2]/a")
followers_button.click()
time.sleep(0.9)



"""
I added this part to make the code faster. 
It will search for the letter 'b' among the followers and subtract accordingly. 
If you want to process for all followers or use a different letter, 
you can delete the relevant part or change the letter.
"""
WebDriverWait(driver, 4).until(expected_conditions.visibility_of_element_located((By.XPATH,"/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div/input")))
fsearch_bar = driver.find_element(By.XPATH,"/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div/input")
fsearch_bar.send_keys("a")
time.sleep(15)


#Let's call our function
main_operating()

while True:
    continue