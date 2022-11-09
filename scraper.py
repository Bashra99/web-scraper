import requests
from bs4 import BeautifulSoup
import json
# URL to scrape
url = 'https://en.wikipedia.org/wiki/Petra'

soup = BeautifulSoup(requests.get(url).content, 'html.parser')



def get_citations_needed_count(url):
    """get the number of citations needed
    """    
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    return len(soup.find_all("a",title="Wikipedia:Citation needed"))
   
obj_citations={}
def get_citations_needed_report(url):
    """get the report of the citations needed
    """    
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    citation_needed_arr=soup.find_all(title="Wikipedia:Citation needed")
    counter=0
    for citation in citation_needed_arr:
        counter+=1
        report=citation.parent.parent.parent.text.strip()
        obj_citations[f"citation needed {counter}" ]=report
        print(f"citation needed {counter} : {report} \n ")
    # return (obj_citations)



def saved_json_data(citations):
    """save the data in json file
    """    
    with open('citations.json', 'w') as json_file:
        json.dump(citations, json_file)

        



if __name__ == "__main__":
    print(f'The number of citations needed is {get_citations_needed_count(url)}')
    # get_citations_needed_report(url)

    saved_json_data(obj_citations)
    get_citations_needed_report(url)



