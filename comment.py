from bs4 import BeautifulSoup
  
markup = open("data/warcout.txt", 'rb')
soup = BeautifulSoup(markup, 'html.parser')
  
#finding the div with the id
div_bs4 = soup.find('div', {"data-testid": "comment"})
  
print(str(div_bs4))

