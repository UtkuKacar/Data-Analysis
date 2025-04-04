import numpy as np

def detect_anomalies(df):
    if "FORCE_POS_1" not in df.columns:
        raise KeyError("FORCE_POS_1 sütunu bulunamadı.")
    
    mean_val = df["FORCE_POS_1"].mean()   #ortalama hesapla
    std_val = df["FORCE_POS_1"].std()   #std sapma hesapla
    df["Z_SCORE"] = (df["FORCE_POS_1"] - mean_val) / std_val   #z skorunu hesapla
    
    anomalies = df[np.abs(df["Z_SCORE"]) > 3]
    print(f"FORCE_POS_1 için tespit edilen anomali sayısı: {anomalies.shape[0]}")
    return anomalies

if __name__ == "__main__":
    from data_cleaning import clean_data
    from csv_extraction import extract_data
    df_raw = extract_data("data.csv")
    df_clean = clean_data(df_raw)
    anomalies = detect_anomalies(df_clean)
    print(anomalies.head(10))
