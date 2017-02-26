#-*- coding: utf8 -*-
import requests
import re
import logging
import pdfkit
import time
import os
from bs4 import BeautifulSoup

html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
</head>
<body>
{content}
</body>
</html>
"""

DOWNLOAD_URL='http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431608990315a01b575e2ab041168ff0df194698afac000#0'


def download_page(url):
    headers={'User_Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
    return requests.get(url,headers=headers).content

def parse_page(html,name):
    try:
        soup=BeautifulSoup(html,'lxml')
        body=soup.find_all(class_='x-wiki-content')[0]
        title=soup.find('h4').get_text()

        center_tag=soup.new_tag('center')
        title_tag=soup.new_tag('h1')
        title_tag.string=title
        center_tag.insert(1,title_tag)
        body.insert(1,center_tag)
        html=str(body)

        pattern="(<img .*?src=\")(.*?)(\")"
        def func(m):
            if not m.group(3).startswith('http'):
                rtn=m.group(1) + "http://www.liaoxuefeng.com" + m.group(2) +m.group(3)
                return rtn
            else:
                return m.group(1) + m.group(2) + m.group(3)

        html=re.compile(pattern).sub(func,html)
        html=html_template.format(content=html)
        html=html.encode('utf-8')
        with open(name,'wb') as f:
            f.write(html)
        return name

    except Exception as e:
        logging.error('解析错误',exc_info=True)

def save_pdf(htmls, file_name):
    options = {
        'page-size': 'Letter',
        'margin-top': '0.75in',
        'margin-right': '0.75in',
        'margin-bottom': '0.75in',
        'margin-left': '0.75in',
        'encoding': "UTF-8",
        'custom-header': [
            ('Accept-Encoding', 'gzip')
        ],
        'cookie': [
            ('cookie-name1', 'cookie-value1'),
            ('cookie-name2', 'cookie-value2'),
        ],
        'outline-depth': 10,
    }
    pdfkit.from_file(htmls, file_name, options=options)

def main():
    start=time.time()
    url=DOWNLOAD_URL
    file_name=u'tutorial.pdf'
    htmls=download_page(url)
    htmls=parse_page(htmls,'a.html')
    save_pdf(htmls,file_name)

  
    os.remove('a.html')

    total_time = time.time() - start
    print(u"总共耗时：%f 秒" % total_time)

if __name__=='__main__':
    main()


