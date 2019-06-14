from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import json

def click_more_btn(driver):
    driver.execute_script("all_more_btn = document.querySelectorAll('._4sxc._42ft');for(i=0;i<all_more_btn.length;i++){all_more_btn[i].click()}")
    # print("run click more btn funtion ")
    # more_btn_all = driver.find_elements_by_css_selector("._4sxc._42ft")
    # print("more_btn_all : ", more_btn_all)
    # for more_btn in more_btn_all:
    #     print("more_btn : ",more_btn)
    #     more_btn.click()

def find_comments(post):
    try:
        print("run function")
        comment_box = post.find_element_by_css_selector("._7a8-")
        print("comment_box : ",comment_box)
        # try:
        #     comment_more_btn = comment_box.find_element_by_css_selector("._4sxc._42ft")
        #     print("run comment_more_btn : ",comment_more_btn)
        #     comment_more_btn.click()
        # except:
        #     sleep(.5)

        data_comments = comment_box.find_elements_by_css_selector("._6c7i")
        print("data_comments : ", data_comments)
        all_comments = []
        for data_comment in data_comments:
            comment_name = data_comment.find_element_by_css_selector("._6qw4").text
            print("comment_name :",comment_name)
            comment_text = data_comment.find_element_by_css_selector("._3l3x").text
            print("comment_text :",comment_text)
            comment = {
                'name' : comment_name,
                'text' : comment_text
            }
            print("comment : ",comment)
            all_comments.append(comment)
        return all_comments
    except:
        print("error the find_comments function")

driver = webdriver.Firefox()
driver.get("https://www.facebook.com/New-UM-Secrets-359374200910281/")
driver.implicitly_wait(1)

for i in range(10):
    sleep(1)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

driver.find_element_by_css_selector("._62up").click()
driver.execute_script("document.getElementById('u_0_1l').style.display='none'")
sleep(5)

click_more_btn(driver)#function for click all more button
sleep(1)

data_lists = []

posts = driver.find_elements_by_css_selector("#u_0_1b > ._1xnd > ._1xnd ._4-u2._4-u8._5jmm._5pat")

print("<p>posts len : ", len(posts),"</p>")
for post in posts:
    try:
        post_content = post.find_element_by_css_selector("._5pbx.userContent._3576")
        # post_content = post_content.get_attribute('innerHTML')
        post_content = post_content.text
        post_content = post_content.replace('"','\'')
        try:
            post_comments = find_comments(post)
        except:
            post_comments = 'error / no'
            print("no post_comments")

        post_time = post.find_element_by_css_selector(".timestampContent").text
    except:
        post_content = 'error'   
        post_time = 'error' 
    try:
        post_like = post.find_element_by_css_selector("._81hb").text
    except:
        post_like = "0"
    data_list = {
        'post_time' : post_time,
        'post_content' : post_content,
        'post_comments' : post_comments,
        'post_like' : post_like 
    }

    data_lists.append(data_list)

print("<p>lists len : ", len(data_lists),"</p>")

with open('data.json', 'w', encoding='utf-8') as outfile:
    json.dump(data_lists, outfile, ensure_ascii=False, indent=4)



driver.quit()