from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from random import choice
import config
from tkinter import Tk

driver = webdriver.Edge(config.driver_path)
driver.get("http://lms.adithyatech.edu.in/login/index.php")
driver.find_element_by_id("username").send_keys(config.username)
driver.find_element_by_id("password").send_keys(config.password)
driver.find_element_by_id("loginbtn").click()

sleep(1)
windows_opened = driver.window_handles
main_window = windows_opened[0]

for window in windows_opened:
    if window != main_window:
        driver.switch_to.window(window)
        driver.close()

driver.switch_to.window(windows_opened[0])
driver.find_element_by_link_text(config.quiz_title).click()

def quiz_attender():


    try:
        elem = driver.find_element_by_id("confirmdialog").find_elements_by_tag_name("button")

    except NoSuchElementException:
        quiz_clicker()

    else:
        elem[-1].click()
        quiz_clicker()


def quiz_clicker():

    try :
        driver.find_element_by_class_name("multichoice")

    except NoSuchElementException:
        driver.find_element_by_class_name("continuebutton").click()
        print("There is some sort of error in trying to attend this section")
        sleep(1)
        windows_opened = driver.window_handles
        main_window = windows_opened[0]

        for window in windows_opened:
            if window != main_window:
                driver.switch_to.window(window)
                driver.close()

        driver.switch_to.window(windows_opened[0])
        driver.find_element_by_link_text(config.quiz_title).click()

    else:
        mcqs = driver.find_elements_by_class_name("multichoice")
        for mcq in mcqs:
            choices = mcq.find_elements_by_css_selector("input[type='radio']")
            choice_count = len(choices)
            if config.any_specified_choice :
                if choice_count == 0:
                    mcq.find_element_by_class_name("r0").find_element_by_tag_name("input").click()

                elif config.specified_choice <= len(choices):
                    choices[config.specified_choice].click()

                else:
                    choices[0].click()

            else :
                if choice_count == 0:
                    driver.find_element_by_class_name("r0").find_element_by_tag_name("input").click()

                else:
                    random_choice = choice(choices)
                    random_choice.click()
            # mcq.find_element_by_class_name("formulation").find_element_by_css_selector(f"input[type='radio'][value='{decided_choice}'']").click()
        driver.find_element_by_class_name("submitbtns").find_element_by_tag_name("input").click()
        final_submit = driver.find_elements_by_class_name("submitbtns")[-1]
        final_submit.find_element_by_class_name("singlebutton").click()
        sleep(1)
        elem_2 = driver.find_element_by_id("confirmdialog").find_elements_by_tag_name("button")
        elem_2[-1].click()
        try:
            driver.find_element_by_link_text("Finish review").click()

        except NoSuchElementException:
            pass

        finally:
            driver.find_element_by_class_name("continuebutton").find_element_by_tag_name("input").click()



for i in range(config.session_start,config.session_end+1):

    try:
        driver.find_element_by_link_text(f"Session {i} - Quiz").click()

    except NoSuchElementException:
        print(f"There are no Session {i} - Quiz")

    else:
        quiz_value = driver.find_element_by_class_name("quizattempt")

        try:
            quiz_value.find_element_by_css_selector("input[type='submit'][value='Attempt quiz now']")

        except NoSuchElementException:
            try:
                quiz_value.find_element_by_css_selector("input[type='submit'][value='Continue the last attempt']")

            except NoSuchElementException:
                print(f"You have already attended the quiz in Session {i}.")
                quiz_value.find_element_by_class_name("continuebutton").click()

            else:
                quiz_value.click()
                quiz_attender()
                print(f"Session {i} - Quiz has been attended")

        else:
            quiz_value.click()
            sleep(1)
            quiz_attender()
            print(f"Session {i} - Quiz has been attended")









































































from tkinter import Tk, Label


caption_title = "Courtesy of kulla Nari kootam,\n\nSole Authors,\nVikram, John, Dinesh, Madhan."

root = Tk()
root.title("LMS Quiz Bot")
root.configure(bg="#132226")
root.resizable(False, False)
caption = Label(root,text=caption_title,bg="#132226",fg="#1187a8",font=("Roboto Mono",10))
caption.pack()
root.mainloop()