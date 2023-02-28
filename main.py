"""
Aplikasi deteksi gempa terkini
Modularisasi dengan function
"""

def ekkstraksi_data():
    """
    Tanggal: 28 Februari 2023,
    Waktu: 20:11:48 WIB
    Magnitudo: 4.0
    Kedalaman: 3 km
    Lokasi: LS=7.03  BT=106.64
    Pusat Gempa: berada di darat 11 km Tenggara Kab-Sukabumi
    Dirasakan: (Skala MMI): II-III Kota Sukabumi, II - III Pelabuhan Ratu, II Bogor, II Lebak, II Bayah
    :return:
    """
    hasil = dict()
    hasil['tanggal'] = '24 Agustus 2021'
    hasil['waktu'] = '20:11:48 WIB'
    hasil['magnitudo'] = '4.0'
    hasil['lokasi'] = {'ls':7.03, 'bt':106.64}
    hasil['pusat'] = 'Pusat gempa berada di darat 11 km Tenggara Kab-Sukabumi'
    hasil['dirasakan'] = 'Dirasakan (Skala MMI): II-III Kota Sukabumi, II - III Pelabuhan Ratu, II Bogor, II Lebak, ' \
                         'II Bayah'

    return hasil


def tampilkan_data(result):
    print('Gempa terakhir berdasarkan BMKG')
    print(f"Tanggal {result['tanggal']}")
    print(f"Waktu {result['waktu']}")
    print(f"Magnitudo {result['magnitudo']}")
    print(f"Lokasi LS={result['lokasi']['ls']}, BT={result['lokasi']['bt']}")
    print(f"Pusat {result['pusat']}")
    print(f"Dirasakan {result['dirasakan']}")


if __name__ == '__main__':
    print('Aplikasi utama')
    result = ekkstraksi_data()
    tampilkan_data(result)
