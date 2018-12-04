from urllib import request
from bs4 import BeautifulSoup


class NovelGet(object):
    def __init__(self, url):
        self.html = ''
        self.tag_string = ''
        self.url = url

    def get_html(self):
        rep = request.urlopen(self.url)
        html_content = rep.read()
        html_content = str(html_content, encoding='utf-8')
        self.html = html_content
        return self.html

    def get_text(self):
        soup = BeautifulSoup(self.html, 'html.parser')
        read_tag = soup.find('div', class_='j_readContent')
        self.tag_string = str(read_tag.contents[1])
        self.tag_string = self.tag_string.replace('<p>', '\n').replace('</p>', '')
        return self.tag_string


if __name__ == '__main__':
    novel = ''
    urls = ['https://read.qidian.com/chapter/-WkNjDCxgv6RTIpqx7GUJA2/YsQf3E-oiR62uJcMpdsVgA2',
            'https://read.qidian.com/chapter/-WkNjDCxgv6RTIpqx7GUJA2/jThFps4zB_Fp4rPq4Fd4KQ2',
            'https://read.qidian.com/chapter/-WkNjDCxgv6RTIpqx7GUJA2/x2yh_sYZBzX4p8iEw--PPw2',
            'https://read.qidian.com/chapter/-WkNjDCxgv6RTIpqx7GUJA2/-LWEHxMgLab4p8iEw--PPw2',
            'https://read.qidian.com/chapter/-WkNjDCxgv6RTIpqx7GUJA2/z8mhFSiOVO62uJcMpdsVgA2']

    for index in range(5):
        novel = novel + '\n================第' + str(index + 1) + '章================'
        chapter = NovelGet(urls[index])
        chapter.get_html()
        chapter.get_text()
        novel += chapter.tag_string

    print(novel)
