import csv_extraction
import data_cleaning
import eda_analysis
import anomaly_detection
import performance_analysis
import reporting
import pandas as pd

def main():
    csv_file = "data.csv"
    
    print("1) CSV'den veri çıkarılıyor...")
    df_raw = csv_extraction.extract_data(csv_file)
    print(f"Ham veri seti: {df_raw.shape[0]} satır")
    
    print("2) Veri temizleniyor...")
    df_clean = data_cleaning.clean_data(df_raw)
    print(f"Temiz veri seti: {df_clean.shape[0]} satır")

    df_clean.to_csv("cleaned_data.csv", index=False)
    print("Temizlenmiş veri 'cleaned_data.csv' dosyasına kaydedildi.")
    
    print("3) Keşifsel analiz (EDA) yapılıyor...")
    eda_analysis.eda_summary(df_clean)
    
    print("4) Anomali tespiti yapılıyor...")
    anomalies = anomaly_detection.detect_anomalies(df_clean)
    
    print("5) Performans analizi yapılıyor...")
    df_ok = performance_analysis.performance_analysis(df_clean)
    
    print("6) Rapor hazırlanıyor...")
    reporting.generate_report(df_clean)

if __name__ == "__main__":
    main()
