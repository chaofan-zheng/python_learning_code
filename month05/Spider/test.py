from urllib.parse import urlencode
base_url = 'https://search.1688.com/service/marketOfferResultViewService'
params2 = {
    'keywords': '女装',}
url2 = base_url + urlencode(params2,encoding='gbk')
print(url2)
print('女装'.encode(encoding='gbk'))
