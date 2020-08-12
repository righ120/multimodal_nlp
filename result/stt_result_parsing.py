from bs4 import BeautifulSoup

with open("ellen-1") as fp, open("ellen-1_parsing_output","w") as fw:
    soup = BeautifulSoup(fp, 'html.parser')
    tokens = soup.select(".token")
    for token in tokens:
        fw.write(token.text)
