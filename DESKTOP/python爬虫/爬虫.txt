herders={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36 Edg/92.0.902.84'}
html='''
<!DOCTYPE html>
<html>
<head>
    <title>csdn</title>
    <meta charset = "utf-8">
</head>
<body>
{a}
</body>
</html>
'''
def a_aa(a):
    m=re.compile(r"[\/\\\:\*\?\"\<\>\|]")
    n=re.sub(m,"_",a)
    return n
url = 'https://blog.csdn.net/hawk2014bj/article/list/1'#input("请输入要爬取的csdn博主链接(示:https://blog.csdn.net/xxx)")+'/article/list/1'
import requests,parsel,os,re,pdfkit,time
from tqdm import*
html_data=requests.get(url=url,headers=herders)
#print(html_data.text)
time = time.time()
with open("config.txt",mode="a",encoding="utf-8") as f:
    f.write('-------------')
    f.write('\n')
    f.write(str(time))
    f.write('\n')
    f.write('get ')
    f.write(url)
    f.write('\n')
    f.write(str(html_data))
    f.write('\n')


html_data_2 = parsel.Selector(html_data.text)
href=html_data_2.css('.article-list .article-item-box a::attr(href)').getall()
#href2=html_data_2.css('.ui-pager::text').getall()
#print(href)
#print(href2)
#print(html_data)

os.system("md html_ok")
os.system("md pdf_ok")
for i in tqdm(href):
    html_data_3=requests.get(url=i, headers=herders)
    i_1=parsel.Selector(html_data_3.text)
    t=i_1.css("#articleContentId::text").get()
    abc=i_1.css("#article_content").get()
    name=a_aa(i_1.css("#uid::attr(title)").get())
    kop=a_aa(t+"_"+name+".html")
    pdfp=a_aa(t+"_"+name+".pdf")
    asdfgasdfg=html.format(a=abc)
    #print(html_data_3)
    with open("config.txt",mode="a",encoding="utf-8") as f:
        f.write('time='+str(time))
        f.write('start ')
        f.write('get ')
        f.write(i)
        f.write('config  =  ')
        f.write(str(html_data_3))
        f.write('\n')
    with open("html_ok\\"+kop,mode="w",encoding="utf-8") as f:
        f.write(asdfgasdfg)
    #con=pdfkit.configuration(wkhtmltopdf='wkhtmltopdf.exe')
    #pdfkit.from_file("html_ok\\"+kop,"pdf_ok\\"+pdfp,con)

with open("pdf_ok\\sorry.txt",mode="w",encoding="utf-8") as f:
    f.write("正在研发中...")

print(" ")
print("爬取成功！")
with open("config.txt",mode="a",encoding="utf-8") as f:
    f.write('------------------------')
