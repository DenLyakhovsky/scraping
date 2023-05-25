from bs4 import BeautifulSoup
import requests
import xlsxwriter

url = 'https://wolf.ua/uk/razdely/poligrafiya/'
rr = requests.get(url)

soup = BeautifulSoup(rr.text, 'lxml')

data = soup.find_all(class_='product-column x5 text-center')

elemensts = []
for i in data:
    name = i.find(class_='product-name').text.strip()
    img = 'https:' + i.find('img').get('src')
    elemensts.append({
        'name': name,
        'img': img
    })

book = xlsxwriter.Workbook('Items.xlsx')
page = book.add_worksheet()

row = 0
colum = 0

page.set_column('A:A', 20)
page.set_column('B:B', 10)

for i in elemensts:
    page.write(row, colum, i['name'])
    page.write(row, colum + 1, i['img'])
    row += 1

book.close()
