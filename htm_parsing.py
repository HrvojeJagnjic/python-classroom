import requests
from bs4 import BeautifulSoup

rezultat=requests.get('https://plusportal.hr/politika/rasprodaja-bicikala-u-dvoristu-policijske-uprave-52878')

juha=BeautifulSoup(rezultat.text, 'html.parser') 

sadrzaj=juha.get_text(separator='\n')
juha_bezrezanaca=''
for line in sadrzaj.split('\n'):
    if line.strip():
        juha_bezrezanaca += line.strip() + '\n'

tekst=juha.find_all('p')
for item in tekst:
    if 'p' in item.text:
        print(item.text) 
        juha_bezrezanaca += item.text + '\n'   
    
print(juha_bezrezanaca)
