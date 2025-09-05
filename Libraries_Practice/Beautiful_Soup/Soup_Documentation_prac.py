import requests
from bs4 import BeautifulSoup

r = requests.get("https://parhlefailhojayega.ga")
code = r.content

soup = BeautifulSoup(code, "html.parser")



               # FUNCTIONS:
# print(soup.prettify())    # return content in a pretty way
# print(soup.title)         # returns the title tag in the page
# print(soup.title.name)    # returns "title"
# print(soup.title.string)  # returns exactly the name of page's title
# print(soup.title.parent.name)     # returns head
# print(soup.p)             # returns first paragraph
# print(soup.p["class"])    # returns first paragraph's class
# print(soup.a)             # returns the first anchor tag
# print(soup.find_all("a")) # returns all the anchor tag present in the page
# print(soup.find(id="signupUserName")) # returns the whole line related to that argument
# print(soup.get_text())      # returns the text written in the HTML page








                    # COMMON TASKS
# Extract the URL or links present in the anchor tag in HTML file
# for link in soup.find_all("a"):
#     un_complete_link = link.get("href")
#     print(f"https://codewithharry.com{un_complete_link}")




                    # KINDS OF OBJECTS
# 1. Tag
# 2. NavigableString
# 3. BeautifulSoup
# 4. Comment

# Description about objects

# 1. Tag:
# para_tag = soup.p
# print(para_tag.name)          # Returns the name of the tag.
# para_tag.name = "article"     # Change the tag to the given argument tag.
# print(para_tag["class"])      # You can use the tag as dictionary to get the value of the attributes of the tag.
# print(para_tag.attrs)         # Returns all the attributes of the tag.
# para_tag["class"] = "text_muted"    # Modifies the values of the attributes of the tag as we do in dictionaries.
# para_tag["id"] = "arsalan"    # Add a new attribute as in dictionaries.
# del para_tag["id"]            # Remove the attribute from the tag.
# print(para_tag.get("class"))  # Returns the value of the given attribute's key.
# multi_valued_attributes=None  # Use this at BeautifulSoup class constructor to remove multi values

# 2. NavigableString

# para_tag = soup.findAll("p")
# for i in para_tag:
#     try:
#         i.string.replace_with("My name is Akuma")  # Return the text in para as a navigable string
#         print(i)
#     except AttributeError:
#         print("None")
#         continue

# footer_tag = soup.footer

# for i in soup.body.descendants: # The ".descendants" attribute lets you iterate over all of a tag’s children
#     print(i)


# for i in soup.p.strings:    # for multiple strings in one tag
#     print(i)


# for string in soup.stripped_strings:   # for removing spaces in the strings
#     print(repr(string))

# para = soup.findAll("p")
# for i in para:
#     print(i)

print(soup.contents[0].name)

