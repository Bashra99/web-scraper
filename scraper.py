import requests
from bs4 import BeautifulSoup
import json
# URL to scrape
url = 'https://en.wikipedia.org/wiki/Petra'

soup = BeautifulSoup(requests.get(url).content, 'html.parser')


def get_citations_needed_count(url):
    """get the number of citations needed
    """    
    return len(soup.find_all('sup', class_='noprint Inline-Template Template-Fact'))

def get_citations_needed_report(url):
    """get the report of the citations needed
    """    
    return [citation.text for citation in soup.find_all('p') if 'citation needed' in citation.text]

def saved_json_data(citations):
    """save the data in json file
    """    
    with open('citations.json', 'w') as json_file:
        json.dump(citations, json_file)

def main():
    print(f'The number of citations needed is {get_citations_needed_count(url)}')
    print(f'The report of the citations needed is {get_citations_needed_report(url)}')
    saved_json_data(get_citations_needed_report(url))

print(main())



if __name__ == "__main__":
    print(get_citations_needed_count(url))
    print(get_citations_needed_report(url))
    saved_json_data(get_citations_needed_report(url))