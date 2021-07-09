import mechanicalsoup
from requests.models import Response

browser = mechanicalsoup.StatefulBrowser()
url = "https://www.google.com/imghp?hl=en"

browser.open(url)
print(browser.get_url())

#get HTML
browser.get_current_page()

#target the search field
browser.select_form()
browser.get_current_form().print_summary()

#search for a term
search_term = 'Border Terrier'
browser["q"] = search_term

#submit search
browser.launch_browser()
response = browser.submit_selected()

print("New URL: ", browser.get_url())
print("Response:\n", response.text[:500])

#open url
new_url = browser.get_url()
browser.open(new_url)

#get HTML
page = browser.get_current_page()
all_images = page.find_all('img')

#target the src attruibute
image_source = []
for image in all_images:
    image = image.get('src')
    image_source.append(image)

image_source = [image for image in image_source if image.startswith('https')]

import os
import wget

path = os.getcwd()
path = os.path.join(path, search_term + "s")

#create the directory
os.mkdir(path)

#download all images
counter = 0
for image in image_source:
    save_as = os.path.join(path, search_term + str(counter) + ".jpg")
    wget.download(image, save_as)
    counter+=1
