import re
from urllib import request
from urllib import error
from w3lib.html import remove_tags
class Spider():
    url='https://book.douban.com/top250'
    href_pattern=r'<a href="(.*?)".*?>'
    z_pattern=r'<td valign="top">(.*?)</td>'
    name_pattern=r'<a .*?>(.*?)</a>'
    author_pattern=r'<a .*?>(.*?)</a>'
    title_pattern = r'<span property="v:itemreviewed">(.*?)</span>'
    info_pattern= r'<div id="info".*?>(.*?)</div>'
    public_pattern=r'出版社:?</span>(.*?)<br/>'
    public_year_pattern=r'出版年:?</span>(.*?)<br/>'
    page_pattern=r'页数:?</span>(.*?)<br/>'
    price_pattern=r'定价:?</span>(.*?)<br/>'
    isbn_pattern=r'ISBN:?</span>(.*?)<br/>'
    nei_pattern=r'<div class="intro".*?>(.*?)</div>'
    nei_n_pattern=r'<p>(.*?)</p>'
    # name_pattern=r'<a .*?>.*<span .*?>(.*?)</span>.*?</a>'
    def __mulity_url(self):
        url = 'https://book.douban.com/top250?start={}'
        more_url=[]
        for i in range(0, 226, 25):
            mul_url = url.format(i)
            more_url.append(mul_url)
        return more_url
    def __fetch_html(self,pageurl):
        more_html=[]
        for url in pageurl:
            r=request.urlopen(url)
            html=r.read()
            html=str(html,encoding='utf-8')
            more_html.append(html)
        return more_html
    def __detail_url(self,pagehtml):
        detail_list=[]
        for html in pagehtml:
            z_tab = re.findall(Spider.z_pattern,html, re.S)
            for x in z_tab:
                detail_url = re.findall(Spider.href_pattern, x, re.S)[0]
                detail_list.append(detail_url)
        return detail_list
    def __detail_html(self,bookurl):
        detail_html=[]
        global index
        index=0
        # r = request.urlopen(bookurl[0])
        # html = r.read()
        # html = str(html, encoding='utf-8')
        # detail_html.append(html)
        for url in bookurl:
            print('正在处理……', url)
            try:
                r=request.urlopen(url)
                html = r.read()
                html = str(html, encoding='utf-8')
                detail_html.append(html)
            except error.URLError as e:
                print('页面不存在')
                index+=1
        print(index)
        return detail_html

    def __lizi(self,detail_html):
        for html in detail_html:
            title=re.findall(Spider.title_pattern,html,re.S)[0]
            info=re.findall(Spider.info_pattern,html,re.S)[0]
            author=re.findall(Spider.author_pattern,info,re.S)[0].strip().replace('\n','').replace(' ','')
            nei_list=re.findall(Spider.nei_pattern,html,re.S)[0]
            content=remove_tags(nei_list)
            nei = re.sub(Spider.nei_n_pattern,'',content).strip()
            public=re.findall(Spider.public_pattern,info,re.S)[0]
            public_year=re.findall(Spider.public_year_pattern,info,re.S)[0]
            page = re.findall(Spider.page_pattern, info, re.S)[0]
            price = re.findall(Spider.price_pattern, info, re.S)[0]
            isbn=re.findall(Spider.isbn_pattern, info, re.S)[0]
            print('title',title)
            print('author',author)
            print('public',public)
            print('nei',nei)
            print('page',page)
            print('price',price)
            print('public_year',public_year)
            print('isbn',isbn)
            print('-'*80)

    def go(self):
        pageurl=self.__mulity_url()
        html=self.__fetch_html(pageurl)
        detail_url=self.__detail_url(html)
        detail_html=self.__detail_html(detail_url)
        self.__lizi(detail_html)
spider=Spider()
spider.go()