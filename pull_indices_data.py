from bs4 import BeautifulSoup
import requests
from create_index_list import create_index_list

list,dict = create_index_list()


def pull_indices_data(index_list,index_dict):
    for x in index_list:

# preparing soup
        index = index_dict[x]
        print(index)
        web = requests.post("http://www.nepalstock.com/indices",data={"index": index })
        soup = BeautifulSoup(web.text, "lxml")

#scraping 
        row_list = []
        x_list = []
        index_data = []

# finding rows
        row_list = soup.find_all("tr")

#first  row and last one are not required
        for row in row_list[1:-1]:   

# finding cell
            for cell in row.find_all("td"):  
                x_list.append(cell.text.strip()) 
            print(x_list)
            index_data.append(x_list)
            x_list = []
        return index_data
indices_data = pull_indices_data(index_list= list, index_dict= dict)
print(indices_data)

    