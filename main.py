"""
Aplikasi deteksi gempa terkini
MODULARISASI DENGAN FUNCTION
MODULARISASI DENGAN PACKAGE
"""
import gempaterkini

if __name__ == '__main__':
    print('Aplikasi utama')
    result = gempaterkini.ekkstraksi_data()
    gempaterkini.tampilkan_data(result)
