from htmlparser import PageElement
import requests

if __name__ == '__main__':
    html = requests.get("https://www.nytimes.com/2017/02/20/us/politics/mcmaster-national-security-adviser-trump.html")
    pe = PageElement(html.text)
    for element in pe.all_elements("p", attrs={'class': "story-content"}):
        print(element.text())

    html = open("data.html", 'r').read()
    pe = PageElement(html)

    for element in pe.element("section", attrs={"id": "top-news"}).all_elements('h2', attrs={"class": "story-heading"}):
        alink = element.tag('a')
        print(alink)
