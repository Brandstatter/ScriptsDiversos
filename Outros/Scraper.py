import os
from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "https://www.gov.br/mre/pt-br/assuntos/Embaixadas-Consulados-Missoes/de-outros-paises-no-brasil"

page = urlopen(url)
html = page.read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")
#print(soup.find_all("img"))
email_list = soup.find_all('a', attrs={"class": "email-link"})
#print(email_list)
file = open("Emails.txt","w")
print(len(email_list))
# Something in between 159 and 160 is add a blank space on the list.
print(email_list[160])
for email in email_list:
    if email.get_text != " ":
        line = email.get_text() + "\n"
        file.write(line)