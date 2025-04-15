import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from statsmodels.tsa.holtwinters import ExponentialSmoothing




file_path = "/Users/onuruca/Desktop/eedi meü denizcilik/Analiz/BULKS/Bulk/Phase_5.xlsx"
# Excel dosyasını oku
def load_data(file_path):
    xls = pd.ExcelFile(file_path)
    df = pd.read_excel(xls, sheet_name="Original Data")
    return df




# Regresyon modeli ile tahmin fonksiyonu
def regression_forecast(df):
    X = df[["DWT", "Year", "Vref", "PME"]]
    y = df["EEDI"]
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    reg_model = LinearRegression()
    reg_model.fit(X_train, y_train)
    
    future_data = df.copy()
    future_data["Year"] = 2030
    future_X = future_data[["DWT", "Year", "Vref", "PME"]]
    future_data["Predicted_EEDI_2030"] = reg_model.predict(future_X)
    
    return future_data

# Sonuçları kaydetme fonksiyonu
def save_predictions(df, output_path):
    df.to_excel(output_path, sheet_name="Predictions", index=False)
    print(f"Tahmin sonuçları kaydedildi: {output_path}")

# Ana çalışma akışı
file_path = "/Users/onuruca/Desktop/eedi meü denizcilik/Analiz/BULKS/Bulk/Phase_5.xlsx"  # Güncellenmesi gereken dosya yolu
output_file_path = "/Users/onuruca/Desktop/eedi meü denizcilik/Analiz/BULKS/Bulk/deneme0.xlsx"

df = load_data(file_path)

df_with_predictions = regression_forecast(df)


save_predictions(df_with_predictions, output_file_path)
