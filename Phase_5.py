
# 1000 ile çarpılmışı

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

# 1. Veri Okuma
file_path = "/Users/onuruca/Desktop/eedi meü denizcilik/Analiz/CONTAINER/Phase_4.xlsx"  # Dosya yolu
xls = pd.ExcelFile(file_path)  # Excel dosyasını açma
df = pd.read_excel(xls, sheet_name='Sheet1')  # İlk sayfayı okuma

# 2. Sütun İsimlerini Düzenleme
df.columns = ['DWT', 'Year', 'Vref', 'PME']

# 3. Eksik Verileri Kontrol Etme
if df.isnull().sum().sum() > 0:
    print("Eksik veri bulundu. Lütfen kontrol ediniz.")
else:
    print("Eksik veri bulunmamaktadır.")

# 4. EEDI Hesaplaması için Sabitler
SFC = 0.19  # Spesifik Yakıt Tüketimi (t/kWh)
CF = 3.114  # Karbon Faktörü (tCO2/tFuel)

# 5. EEDI Hesaplaması (gCO₂ / ton-mil)
df['EEDI'] = (df['PME'] * SFC * CF * 1000) / (df['DWT'] * df['Vref'])

# 6. Makine Öğrenmesi İçin Veriyi Hazırlama
X = df[['DWT', 'Year', 'Vref', 'PME']]
y = df['EEDI']

# 7. Veriyi Eğitim ve Test Setine Ayırma
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 8. Modeli Eğitme
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# 9. Test Seti Üzerinde Tahmin Yapma
y_pred = model.predict(X_test)

# 10. Modelin Performansını Değerlendirme
mae = mean_absolute_error(y_test, y_pred)
print(f"Model Ortalama Mutlak Hata (MAE): {mae:.6f} gCO₂ / ton-mil")

# 12. Sonuçları Excel Dosyasına Kaydetme
output_file = "/Users/onuruca/Desktop/eedi meü denizcilik/Analiz/CONTAINER/Phase_5.xlsx"
with pd.ExcelWriter(output_file) as writer:
    df.to_excel(writer, sheet_name='Original Data', index=False)

print(f"Tahmin sonuçları Excel dosyasına kaydedildi: {output_file}")
