import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor



file_path = "/Users/onuruca/Desktop/eedi meü denizcilik/Analiz/BULKS/Bulk/Phase_5.xlsx"

# Excel dosyasını oku
def load_data(file_path, sheet_name="Original Data"):
    df = pd.read_excel(file_path, sheet_name=sheet_name)
    return df

# Random Forest Regressor ile tahmin fonksiyonu
def random_forest_forecast(df):
    X = df[["DWT", "Year", "Vref", "PME"]]
    y = df["EEDI"]
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    rf_model = RandomForestRegressor(n_estimators=100, random_state=42)
    rf_model.fit(X_train, y_train)
    
    future_data = df.copy()
    future_data["Year"] = 2030
    future_X = future_data[["DWT", "Year", "Vref", "PME"]]
    future_data["Predicted_EEDI_2030"] = rf_model.predict(future_X)
    
    return future_data

# Sonuçları kaydetme fonksiyonu
def save_predictions(df, output_path):
    df.to_excel(output_path, sheet_name="Predictions", index=False)
    print(f"Tahmin sonuçları kaydedildi: {output_path}")

# Ana çalışma akışı
file_path = "/Users/onuruca/Desktop/eedi meü denizcilik/Analiz/BULKS/Bulk/Phase_5.xlsx"
sheet_name = "Original Data"
output_file_path = "/Users/onuruca/Desktop/eedi meü denizcilik/Analiz/BULKS/Bulk/deneme00.xlsx"

df = load_data(file_path, sheet_name)
df_with_predictions = random_forest_forecast(df)
save_predictions(df_with_predictions, output_file_path)
