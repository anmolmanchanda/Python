import requests
from bs4 import BeautifulSoup

def scrape_website(url):
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        titles = soup.find_all('h2', class_='font-polysans text-20 font-bold leading-100 tracking-1 md:text-24 lg:text-20')
        #titles = soup.find_all('h1', class_='mb-28 hidden max-w-[900px] font-polysans text-45 font-bold leading-100 selection:bg-franklin-20 lg:block')


        print("Latest Article Titles:")
        for index, title in enumerate(titles, start=1):
            print(f"{index}. {title.get_text(strip=True)}")
    else:
        print(f"Failed to retrieve the web page. Status code: {response.status_code}")

website_url = 'https://theverge.com'
#website_url = 'https://www.theverge.com/2024/6/11/24175689/apple-vision-pro-2-wwdc-2024-keynote-best-updates'

scrape_website(website_url)