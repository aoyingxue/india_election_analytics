import urllib.request
# import urllib2
import re
import os


## open html and read
def getHTML(url):
    page=urllib.request.urlopen(url)
    html=page.read()
    page.close()
    return html

## compile and find all the pdf that we need
def getURL(html):
    # reg=r'(Ac\d\d\d)'
    reg=r'(AC\d\d\d)'
    url_re=re.compile(reg)
    url_lst=url_re.findall(html.decode('GB18030'))
    return (url_lst)

## get the file
def getFile(url):
    file_name=url.split('/')[-1]
    u=urllib.request.urlopen(url)
    f=open(file_name,"wb")

    block_sz=8192
    while True:
        buffer=u.read(block_sz)
        if not buffer:
            break
        f.write(buffer)
    f.close()
    print("Successful download"+""+file_name)


# root_url="https://www.elections.tn.gov.in/TNLA2016/FORM%20-%2020/"
# raw_url="https://www.elections.tn.gov.in/Form20.aspx"
root_url="https://www.elections.tn.gov.in/Web/FORM20_2011"
raw_url="https://www.elections.tn.gov.in/Web/form20_2011.htm"

html = getHTML(raw_url)
url_lst=getURL(html)[1:] ## delete the first "Ac"

print(len(url_lst))
print(getURL(html))

# os.mkdir("pdf")
os.chdir(os.path.join(os.getcwd(),"pdf"))

for url in url_lst[:]:
    url=root_url+"/"+url+".PDF"
    getFile(url)