from bs4 import BeautifulSoup

file_path = r'C:\Users\baliq\Desktop\Web Scraping\Premier League Stats _ FBref.html'

def read_html_file():
    with open(file_path, 'r', encoding='utf-8') as f:
        html_content = f.read()
    return BeautifulSoup(html_content, 'html.parser')
