# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import requests as requests
import writer as Writer


# query = {'id': '8'}
# git_api = 'https://api.github.com/users/ChrissantDC'
API_ENDPOINT = "https://pastebin.com/api/api_post.php"
API_KEY = 'u60hbW4__49DzHjSahZ_LXaqitB7ukVi'
source_code = Writer.final_value
# print('scode is: ' + source_code)
response = requests.post(API_ENDPOINT)
# python PycharmProjects\RestAPI\main.py C:\Users\delac\PycharmProjects\RestAPI test.csv

data = {
        'api_dev_key': API_KEY,
        'api_option': 'paste',
        'api_paste_code': source_code,
        'api_paste_format': 'python'
        }

r = requests.post(url=API_ENDPOINT, data=data)

pastebin_url = r.text
print("The pastebin URL is:%s"%pastebin_url)

# print(response.headers['date'])
# print(response.json())

# Create a new resource
# response = requests.post('https://httpbin.org/post', data = {'key':'value'})
# Update an existing resource
# requests.put('https://httpbin.org/put', data = {'key':'value'})

# >>>TO AUTHENTICATE APIs THAT REQUIRE AUTHENTICATION:<<<
# requests.get
# (
#   'https://api.github.com/user',
#   auth=HTTPBasicAuth('username', 'password')
# )


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
