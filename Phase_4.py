import pandas as pd

# Dosyanın yolunu belirtelim
file_path = "/Users/onuruca/Desktop/eedi meü denizcilik/Analiz/TANKER/Phase_3.xlsx"

# Excel dosyasını oku
df = pd.read_excel(file_path, sheet_name="Sheet1")

# Gerekli sütunları belirleyelim
selected_columns = [
    "Capacity\n(DWT)", "Year of delivery", "Vref (knot)", "PME (kW)"
]

# Belirtilen sütunları içeren yeni DataFrame oluştur
filtered_df = df[selected_columns]

# Temizlenmiş veriyi kaydet
filtered_file_path = "/Users/onuruca/Desktop/eedi meü denizcilik/Analiz/TANKER/Phase_4.xlsx"
filtered_df.to_excel(filtered_file_path, index=False)

print(f"Temizlenmiş veri kaydedildi: {filtered_file_path}")
