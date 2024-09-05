from lxml import etree

a1 = etree.parse('xpath_本地文件.html')
# a2 = a1.xpath('//ul/li')

# text() 拿标签中的内容

# a2 =a1.xpath('//ul/li[@id]')

# a2 = a1.xpath('//ul/li[@id="a1"]/text()')

# a2 = a1.xpath('//ul/li[@id="a1"]/@class')
a2 = a1.xpath('//ul/li[contains(@id,"a")]/text()')
print(a2)