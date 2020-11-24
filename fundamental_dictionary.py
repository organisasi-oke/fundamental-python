"""
type data dictionary
KVP
"""
kamus = {'anak': 'son', 'istri': 'wife', 'ayah': 'father', 'ibu': 'mother'}
print(kamus)
print(kamus['ayah'])

print('data ini dikirimkan server gojek untuk info di sekitar lokasi')
data_dari_server_gojek={
    'tanggal': '2020-11-21',
    'driver_list':[
        {'nama':'eko','jarak':10},
        {'nama':'dwi','jarak':100},
        {'nama':'tri','jarak':200},
        {'nama':'catur','jarak':500}
    ]
}
print(f'data dari server gojek{data_dari_server_gojek}')
print(f"driver di sekitar sini{data_dari_server_gojek['driver_list']}")
print(f"driver #1 {data_dari_server_gojek['driver_list'][0]}")
print(f"driver #4 {data_dari_server_gojek['driver_list'][3]}")
print(f"driver terdekat berjarak {data_dari_server_gojek['driver_list'][0]['jarak']} meter")