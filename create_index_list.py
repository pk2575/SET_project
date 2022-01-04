from bs4 import BeautifulSoup
import requests


def create_index_list():

# preparing soup
    source = requests.post(f"http://www.nepalstock.com/indices")
    soup = BeautifulSoup(source.text, "lxml")

#filtering data
    table = soup.find(id ="index")
    contents =table.find_all("option")

#creating index-code dictionary and indices list
    code_list = []
    index_list = []
    for entry in contents:
        entry =str(entry)
        entry = (entry.replace('<option value="','').replace('"','').replace("</option>","").split(">"))
        entry.reverse()
        code_list.append(entry)
        index_list.append(entry[0])
    index_dict = dict(code_list)


# what to do with processed data
    return index_list,index_dict   


