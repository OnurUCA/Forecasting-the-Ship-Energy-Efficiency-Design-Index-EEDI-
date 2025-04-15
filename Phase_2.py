import pandas as pd

# Dosyanın yolunu belirtelim
file_path = "/Users/onuruca/Desktop/eedi meü denizcilik/Analiz/CONTAINER/container.xlsx"

# Excel dosyasını oku
xls = pd.ExcelFile(file_path)

# Gerekli sütunları belirleyelim
selected_columns = [
    "Capacity (DWT)\n", "Year of delivery\n", "Required EEDI-Mandatory",
    "Required EEDI-Non-mandatory*", "Attained EEDI-Mandatory",
    "Attained EEDI-Non-mandatory", "Vref (knot)", "PME (kW)"
]

# İlk sayfadaki veriyi oku
df = pd.read_excel(xls, sheet_name=xls.sheet_names[0])

# Belirtilen sütunları içeren yeni DataFrame oluştur
filtered_df = df[selected_columns]

# Temizlenmiş veriyi kaydet
filtered_file_path = "/Users/onuruca/Desktop/eedi meü denizcilik/Analiz/CONTAINER/Phase_2.xlsx"
filtered_df.to_excel(filtered_file_path, index=False)

print(f"Temizlenmiş veri kaydedildi: {filtered_file_path}")
