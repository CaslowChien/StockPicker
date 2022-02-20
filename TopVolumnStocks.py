def StacksList(x):
    #找成交量前100股票 from youtube, Python 網路爬蟲 Web Crawler 基本教學 By 彭彭

    #抓取網頁原始碼from yahoo
    import urllib.request as req
    import json
    url="https://tw.stock.yahoo.com/rank/volume?exchange=TAI"

    #取得授權
    request=req.Request(url,headers={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36"
    })

    #原始碼
    with req.urlopen(request) as response:
        data=response.read()

    #解析原始碼
    ##抓百大成交量股票
    import bs4
    root=bs4.BeautifulSoup(data,"html.parser")
    stocks=root.find_all("div",class_="D(f) Ai(c)")
    ##日期
    date=root.find("div",class_="D(f) Jc(sb) Jc(fe)--mobile Ai(c) C($c-link-text) Mb(12px)")

    #把百大放進list Of Stock
    listOfStock=[]
    for stock in stocks:
        listOfStock.append(stock.span.string)

    if x == "date": return date.span.string[-10:]
    else: return listOfStock
    #return (date, list of stocks)
    # return date.span.string[-10:],listOfStock