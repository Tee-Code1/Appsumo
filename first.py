import requests
from bs4 import BeautifulSoup
import pandas as pd

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'}

information =[]

a = "https://appsumo.com"
url = "https://appsumo.com/browse?type=freebie&sort=latest"
r = requests.get(url, headers=headers).text
commet = r.replace("-->", "").replace("<!--", "")
soup = BeautifulSoup(commet,"html.parser")

# soup = BeautifulSoup(r.text,"html.parser")

first = soup.find_all("div", class_= "new-card-design")
# second = first.find("div", class_="appsumo-deal-tile")
# third = second.find_all("div", class_= "p-3 description-container")

for i in first:
    info={
    "Title": i.find("p", class_="section-title d-block mt-3").text.strip(),
    "Discprition" : i.find("p", class_="d-block deal-description my-0").text.strip(),
    "Downloads": i.find("div", class_="deal-freebie-description").text.strip(),
    "Links": "https://appsumo.com" +i.find("a")["href"]

    }
    information.append(info)
print(information)

df = pd.DataFrame(information)
df.to_excel('Appsumo.xlsx', index=False)
print("Find.")















# links = {
#     "1" :"https://appsumo.com/browse?type=freebie",
#     "2":"https://appsumo.com/browse?type=freebie&sort=latest",
#     "3":"https://appsumo.com/browse?type=freebie&sort=review_count",
#    "4":"https://appsumo.com/browse?type=freebie&sort=rating",
#     "5":"https://appsumo.com/browse?type=freebie&sort=price_low",
#     "6":"https://appsumo.com/browse?type=freebie&sort=price_high",
#     "7":"https://appsumo.com/browse?type=freebie&sort=ending"
# }

# catergories = str(input("Whats categories do you want? "))
# for i in links:
#     if catergories == i:
#         print(links["1"])
#     else:
#         pass
#     if catergories != i:
#         print(links["2"])
#     else:
#         pass