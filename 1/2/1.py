from urllib import request
import lxml.html

etree = lxml.html.etree

parser = etree.HTMLParser(encoding='utf-8')
html = etree.parse("renren.html", parser=parser)

# 获取所有tr标签
# trs= html.xpath("//tr")
# for tr in trs:
#     print(etree.tostring(tr,encoding= 'utf-8').decode('utf-8'))


# 获取第二个tr
# trs = html.xpath("//tr[2]")[0]
# print(etree.tostring(trs,encoding='utf-8').decode('utf-8'))

# 获取clss里even
# trs = html.xpath("//tr[@class = 'even']")
# for tr in trs:
#     print(etree.tostring(tr, encoding='utf-8').decode("utf-8"))

# 获取a标签href属性
# asss = html.xpath("//a/@href")
# for assx in asss:
# print("http://hr.tencent.com/"+assx)
# print(etree.tostring(assx, encoding='utf-8').decode("utf-8"))


trs = html.xpath("//tr[position()>1]")
for tr in trs:
    href = tr.xpath(".//a/@href")[0]
    flutter = "http://hr.tencent.com/" + href
    title = tr.xpath("./td[1]//text()")[0]
    print(title)
    break
