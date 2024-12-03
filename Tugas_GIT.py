data_panen = {
    'lokasi1' : {
        'nama_lokasi' : 'Kebun A',
        'hasil_panen': {
            'padi' : 1200,
            'jagung' : 800,
            'kedelai' : 500
        }
    },
    'lokasi2': {
        'nama_lokasi' : 'Kebun B',
        'hasil_panen': {
            'padi' : 1500,
            'jagung' : 900,
            'kedelai' : 450
        }
    },
    'lokasi3': {
        'nama_lokasi' : 'Kebun C',
        'hasil_panen': {
            'padi' : 1100,
            'jagung' : 750,
            'kedelai' : 600
        }
    },
    'lokasi4': {
        'nama_lokasi' : 'Kebun D',
        'hasil_panen': {
            'padi' : 1300,
            'jagung' : 850,
            'kedelai' : 550
        }
    },
    'lokasi5': {
        'nama_lokasi' : 'Kebun E',
        'hasil_panen': {
            'padi' : 1400,
            'jagung' : 950,
            'kedelai' : 480
        }
    }
}

panen = (data_panen)

print(panen)

jagung = (data_panen['lokasi2']['hasil_panen']['jagung'])

print(f"Hasil panen jagung lokasi2 : {jagung}")

lokasi = (data_panen['lokasi3']['nama_lokasi'])

print(f"Nama lokasi 3 : {lokasi}")

jumlah_padi1 = (data_panen['lokasi1']['hasil_panen']['padi'])
jumlah_kedelai1 = (data_panen['lokasi1']['hasil_panen']['kedelai'])

jumlah_padi2 = (data_panen['lokasi2']['hasil_panen']['padi'])
jumlah_kedelai2 = (data_panen['lokasi2']['hasil_panen']['kedelai'])

jumlah_padi3 = (data_panen['lokasi3']['hasil_panen']['padi'])
jumlah_kedelai3 = (data_panen['lokasi3']['hasil_panen']['kedelai'])

jumlah_padi4 = (data_panen['lokasi4']['hasil_panen']['padi'])
jumlah_kedelai4 = (data_panen['lokasi4']['hasil_panen']['kedelai'])

jumlah_padi5 = (data_panen['lokasi5']['hasil_panen']['padi'])
jumlah_kedelai5 = (data_panen['lokasi5']['hasil_panen']['kedelai'])

padi = [
    data_panen['lokasi1']['hasil_panen']['padi'],
    data_panen['lokasi2']['hasil_panen']['padi'],
    data_panen['lokasi3']['hasil_panen']['padi'],
    data_panen['lokasi4']['hasil_panen']['padi'],
    data_panen['lokasi5']['hasil_panen']['padi']
]

kedelai = [
    data_panen['lokasi1']['hasil_panen']['kedelai'],
    data_panen['lokasi2']['hasil_panen']['kedelai'],
    data_panen['lokasi3']['hasil_panen']['kedelai'],
    data_panen['lokasi4']['hasil_panen']['kedelai'],
    data_panen['lokasi5']['hasil_panen']['kedelai']
]

for i,j in data_panen.items():
    nama_lokasi = j['nama_lokasi']
    hasil_panen = j['hasil_panen']

    if hasil_panen['padi'] > 1300 or hasil_panen['jagung'] > 800:
        print(f"Nama Lokasi {nama_lokasi} Memerlukan perhatian khusus")
    else:
        print(f"Nama Lokasi {nama_lokasi} Baik Baik Saja")

#Perubahan baru konflik
