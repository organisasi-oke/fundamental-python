import requests

print('Hello world')
try:
    r = requests.get('https://google.com')
    if r.status_code == 200:
        print(r.text)
except Exception as e:
    print('ada error', e)

jumlah_anak=4
for index_anak in range(1,jumlah_anak+1):
    #print('anak ke-',index_anak)
    print(f'anak ke- {index_anak}')