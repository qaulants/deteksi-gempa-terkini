import requests
from bs4 import BeautifulSoup


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
    try:
        content = requests.get('https://bmkg.go.id')
    except Exception:
        return None

    if content.status_code == 200:
        soup = BeautifulSoup(content.text, 'html.parser')

        result = soup.find('span',{'class':'waktu'})
        result = result.text.split(', ')
        tanggal = result[0]
        waktu = result[1]

        result = soup.find('div',{'class':'col-md-6 col-xs-6 gempabumi-detail no-padding'})
        result = result.findChildren('li')
        i = 0
        magnitudo = None
        kedalaman = None
        ls = None
        bt = None
        lokasi = None
        dirasakan = None

        for res in result:
            if i == 1:
                magnitudo = res.text
            elif i == 2:
                kedalaman = res.text
            elif i == 3:
                koordinat = res.text.split(' - ')
                ls = koordinat[0]
                bt = koordinat[1]
            elif i == 4:
                lokasi = res.text
            elif i == 5:
                dirasakan = res.text
            i = i + 1

        hasil = dict()
        hasil['tanggal'] = tanggal
        hasil['waktu'] = waktu
        hasil['magnitudo'] = magnitudo
        hasil['kedalaman'] = kedalaman
        hasil['koordinat'] = {'ls': ls, 'bt': bt}
        hasil['lokasi'] = lokasi
        hasil['dirasakan'] = dirasakan
        return hasil
    else:
        return None

def tampilkan_data(result):
    if result is None:
        print("Tidak bisa menemukan data gempa terkini")
        return

    print('Gempa terakhir berdasarkan BMKG')
    print(f"Tanggal {result['tanggal']}")
    print(f"Waktu {result['waktu']}")
    print(f"Magnitudo {result['magnitudo']}")
    print(f"Kedalaman {result['kedalaman']}")
    print(f"Lokasi {result['lokasi']}")
    print(f"Koordinat LS={result['koordinat']['ls']}, BT={result['koordinat']['bt']}")
    print(f"Dirasakan {result['dirasakan']}")

if __name__ == '__main__':
    print('Ini adalah package gempaterkini')
    print('hai')