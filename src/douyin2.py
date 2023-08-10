import requests
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.188',
    'Accept':'*/*',
'Accept-Encoding':'gzip, deflate, br',
'Accept-Language':'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
'Content-Length':'4662',
'Content-Type':'application/json; charset=UTF-8',
'Origin':'https://www.douyin.com',
'Referer':'https://www.douyin.com/',
'Sec-Ch-Ua':'"Not/A)Brand";v="99", "Microsoft Edge";v="115", "Chromium";v="115"',
'Sec-Ch-Ua-Mobile':'?0',
'Sec-Ch-Ua-Platform':'"Windows"',
'Sec-Fetch-Dest':'empty',
'Sec-Fetch-Mode':'cors',
'Sec-Fetch-Site':'cross-site'
}
res = requests.post(url='https://www.douyin.com/video/7168790019187035399',headers=headers,verify=False).text
print(res)