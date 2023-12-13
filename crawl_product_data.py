import pandas as pd
import requests
import time
import random
from tqdm import tqdm

# cookies = {
#     'TIKI_GUEST_TOKEN': '8jWSuIDBb2NGVzr6hsUZXpkP1FRin7lY',
#     'TOKENS': '{%22access_token%22:%228jWSuIDBb2NGVzr6hsUZXpkP1FRin7lY%22%2C%22expires_in%22:157680000%2C%22expires_at%22:1763654224277%2C%22guest_token%22:%228jWSuIDBb2NGVzr6hsUZXpkP1FRin7lY%22}',
#     'amp_99d374': 'eSc-_0HT1um7cb57E7dwA0...1enloc6a2.1enlohtdv.3.2.5',
#     'amp_99d374_tiki.vn': 'eSc-_0HT1um7cb57E7dwA0...1enloc6a2.1enlocds8.0.1.1',
#     '_gcl_au': '1.1.559117409.1605974236',
#     '_ants_utm_v2': '',
#     '_pk_id.638735871.2fc5': 'b92ae025fbbdb31f.1605974236.1.1605974420.1605974236.',
#     '_pk_ses.638735871.2fc5': '*',
#     '_trackity': '70e316b0-96f2-dbe1-a2ed-43ff60419991',
#     '_ga_NKX31X43RV': 'GS1.1.1605974235.1.1.1605974434.0',
#     '_ga': 'GA1.1.657946765.1605974236',
#     'ai_client_id': '11935756853.1605974227',
#     'an_session': 'zizkzrzjzlzizqzlzqzjzdzizizqzgzmzkzmzlzrzmzgzdzizlzjzmzqzkznzhzhzkzdzhzdzizlzjzmzqzkznzhzhzkzdzizlzjzmzqzkznzhzhzkzdzjzdzhzqzdzizd2f27zdzjzdzlzmzmznzq',
#     'au_aid': '11935756853',
#     'dgs': '1605974411%3A3%3A0',
#     'au_gt': '1605974227146',
#     '_ants_services': '%5B%22cuid%22%5D',
#     '__admUTMtime': '1605974236',
#     '__iid': '749',
#     '__su': '0',
#     '_bs': 'bb9a32f6-ab13-ce80-92d6-57fd3fd6e4c8',
#     '_gid': 'GA1.2.867846791.1605974237',
#     '_fbp': 'fb.1.1605974237134.1297408816',
#     '_hjid': 'f152cf33-7323-4410-b9ae-79f6622ebc48',
#     '_hjFirstSeen': '1',
#     '_hjIncludedInPageviewSample': '1',
#     '_hjAbsoluteSessionInProgress': '0',
#     '_hjIncludedInSessionSample': '1',
#     'tiki_client_id': '657946765.1605974236',
#     '__gads': 'ID=ae56424189ecccbe-227eb8e1d6c400a8:T=1605974229:RT=1605974229:S=ALNI_MZFWYf2BAjzCSiRNLC3bKI-W_7YHA',
#     'proxy_s_sv': '1605976041662',
#     'TKSESSID': '8bcd49b02e1e16aa1cdb795c54d7b460',
#     'TIKI_RECOMMENDATION': '21dd50e7f7c194df673ea3b717459249',
#     '_gat': '1',
#     'cto_bundle': 'i6f48l9NVXNkQmJ6aEVLcXNqbHdjcVZoQ0k2clladUF2N2xjZzJ1cjR6WG43UTVaRmglMkZXWUdtRnJTNHZRbmQ4SDAlMkZwRFhqQnppRHFxJTJCSEozZXBqRFM4ZHVxUjQ2TmklMkJIcnhJd3luZXpJSnBpcE1nJTNE',
#     'TIKI_RECENTLYVIEWED': '58259141',
# }


# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:83.0) Gecko/20100101 Firefox/83.0',
#     'Accept': 'application/json, text/plain, */*',
#     'Accept-Language': 'vi-VN,vi;q=0.8,en-US;q=0.5,en;q=0.3',
#     'Referer': 'https://tiki.vn/dien-thoai-samsung-galaxy-m31-128gb-6gb-hang-chinh-hang-p58259141.html?src=category-page-1789&2hi=0',
#     'x-guest-token': '8jWSuIDBb2NGVzr6hsUZXpkP1FRin7lY',
#     'Connection': 'keep-alive',
#     'TE': 'Trailers',
# }

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7,fr-FR;q=0.6,fr;q=0.5',
    'Referer': 'https://tiki.vn/chao-chong-dinh-inox-day-tu-nguyen-khoi-day-lien-elmich-trimax-classic-el-2702ol-size-24cm-p195111061.html?itm_campaign=CTP_YPD_TKA_PLA_UNK_ALL_UNK_UNK_UNK_UNK_X.282888_Y.1865208_Z.3899618_CN.AUTO---Chao-chong-dinh-Inox-day-tu-nguyen-khoi-day-lien-Elmich-Trimax-Classic-EL-2702OL-size-24cm---2023%2F12%2F06-11%3A24%3A33&itm_medium=CPC&itm_source=tiki-ads&spid=195111062',
    'x-guest-token': 'Q31ySXN0o2q67tOUBkJAGuxLZlcdIzDY',
    'Connection': 'keep-alive',
    'TE': 'Trailers',
}

cookies = {
    '_trackity': 'f65de3e5-7ee4-e4e8-138d-f20b7e0418a8',
    'TOKENS': '{%22access_token%22:%22Q31ySXN0o2q67tOUBkJAGuxLZlcdIzDY%22%2C%22expires_in%22:157680000%2C%22expires_at%22:1860122442039%2C%22guest_token%22:%22Q31ySXN0o2q67tOUBkJAGuxLZlcdIzDY%22}',
    'delivery_zone': 'Vk4wMzQwMjQwMTM=',
    '_ga': 'GA1.1.1158343469.1702442443', 
    '_gcl_au': '1.1.645631702.1702442447', 
    'tiki_client_id': '1158343469.1702442443',
    '_hjSessionUser_522327': 'eyJpZCI6IjNiMDdkMzkxLTE0ZTQtNTk0MC05MzY2LWU5YzE1ZDBlMjE5MSIsImNyZWF0ZWQiOjE3MDI0NDI0NDY4MDUsImV4aXN0aW5nIjp0cnVlfQ==',
    '_fbp': 'fb.1.1702442466961.7493116', 
    '_hjIncludedInSessionSample_522327': '0', 
    '_hjSession_522327': 'eyJpZCI6ImU3MjU3MGFlLWY3OGUtNGIzOS1iODVhLTQ1Njk0ZTNkMWQ3YiIsImNyZWF0ZWQiOjE3MDI0Nzg3NjI5NTMsImluU2FtcGxlIjpmYWxzZSwic2Vzc2lvbml6ZXJCZXRhRW5hYmxlZCI6ZmFsc2V9',
    '_hjAbsoluteSessionInProgress': '0',
    'amp_99d374': '1GHmZDwu3ulrBJeqvnSpSU...1hhhq8do3.1hhhqv95a.3v.4p.8o',
    'cto_bundle': 'ic4X419STVFhdTRWUU10c3YxbWZ2Y2xrRFglMkJ2NHhmUGRuYnM0QjRjVlVjT0NpVm5hNFZRZiUyRkh6OFNZaFowVlB2eG1OQmNpcXZDdWV2bjclMkYzTEowbEduU2YyeEJ5bGRBJTJGc3pOUlhva09Zc3g3Wk04NDg0RUFyMnNxeFZ0QktkWm9WMHhiWlE3MmNiM1prMTlJTVBGN3hUb05oQjVKalAwQk9ORXZYYmRkOUlqUlBKTiUyRkJEbXNUSnVMUlZWY3hUaHhkNkl4',
    '_ga_S9GLR1RQFJ': 'GS1.1.1702478754.2.1.1702479583.60.0.0'

}

params = (
    ('platform', 'web'),
    ('spid', 195111062)
    #('include', 'tag,images,gallery,promotions,badges,stock_item,variants,product_links,discount_tag,ranks,breadcrumbs,top_features,cta_desktop'),
)

def parser_product(json):
    d = dict()
    d['id'] = json.get('id')
    d['sku'] = json.get('sku')
    d['short_description'] = json.get('short_description')
    d['price'] = json.get('price')
    d['list_price'] = json.get('list_price')
    d['price_usd'] = json.get('price_usd')
    d['discount'] = json.get('discount')
    d['discount_rate'] = json.get('discount_rate')
    d['review_count'] = json.get('review_count')
    d['order_count'] = json.get('order_count')
    d['inventory_status'] = json.get('inventory_status')
    d['is_visible'] = json.get('is_visible')
    d['stock_item_qty'] = json.get('stock_item').get('qty')
    d['stock_item_max_sale_qty'] = json.get('stock_item').get('max_sale_qty')
    d['product_name'] = json.get('meta_title')
    d['brand_id'] = json.get('brand').get('id')
    d['brand_name'] = json.get('brand').get('name')
    return d


df_id = pd.read_csv('product_id_ncds.csv')
p_ids = df_id.id.to_list()
print(p_ids)
result = []
count = 0
for pid in tqdm(p_ids, total=len(p_ids)):
    response = requests.get('https://tiki.vn/api/v2/products/{}'.format(pid), headers=headers, params=params, cookies=cookies) # 
    if count == 200:
        break
    if response.status_code == 200:
        print('Crawl data {} success !!!'.format(pid))
        result.append(parser_product(response.json()))
    time.sleep(random.randrange(3, 5))
    count += 1
df_product = pd.DataFrame(result)
df_product.to_csv('crawled_data_ncds.csv', index=False)
