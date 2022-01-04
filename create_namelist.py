from bs4 import BeautifulSoup
import requests



def create_namelist():


#preparing soup
    source = requests.post(f"http://www.nepalstock.com/company",data={"_limit":"500"} ).text
    soup = BeautifulSoup(source, "lxml")

#scraping
    row_list = []
    x_list = []
    namelist = []

# finding rows
    row_list= soup.find_all("tr")

#first two rows and last one are not required

    for row in row_list[2:-1]:   
# finding cell 
        for cell in row.find_all("td"): 
            x_list.append(cell.text.strip()) 
        print(x_list)
        namelist.append(x_list)
        x_list = []

    return namelist
namelist = create_namelist()
print(namelist)


