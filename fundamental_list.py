anak= ['eko', 'dwi', 'tri', 'catur']
print(anak)
anak.append('limo')
print(anak)
print('menyapa anak ke 2')
print(f'hai {anak[1]}')

print('menyapa semua anak cara sederhana')
for a in anak:
    print(f'hai {a}')

print('menyapa semua anak cara ribet')
for a in range(0,len(anak)):
    print(f'hai {anak[a]}')