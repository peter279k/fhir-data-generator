import requests
from bs4 import BeautifulSoup


def extract_profile_url(html_file):
    html_file = html_file.replace('.html', '.json')
    req_url = f'https://mitw.dicom.org.tw/IG/PA/{html_file}'
    response = requests.get(req_url)

    return response.json()['meta']['profile'][0]

response = requests.get('https://mitw.dicom.org.tw/IG/PA/example.html')
response.encoding = 'utf-8'

mappings = []

soup = BeautifulSoup(response.text, 'html.parser')
ul_lists = soup.select('ul')
for index in range(6, 9+1):
    mapping = []
    for ul_list in ul_lists[index]:
        if ul_list is None:
            continue

        soup = BeautifulSoup(str(ul_list), 'html.parser')
        a_element = soup.select_one('a')
        if a_element is not None:
            mapping += {
                'profile_url': extract_profile_url(a_element['href']),
                'value': a_element['href'].split('-')[1].lower(),
                'name': a_element.get_text(),
            },

    mappings += mapping,


print(mappings[0])
print(mappings[1])
print(mappings[2])
print(mappings[3])
