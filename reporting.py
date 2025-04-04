import matplotlib.pyplot as plt

def generate_report(df):

    if "result" in df.columns:
        result_counts = df["result"].value_counts()     #result sütunu ile ok ve nok sayısını hesapla
        print("Sonuç Dağılımı:")
        print(result_counts)
        
        plt.figure(figsize=(6,4))
        result_counts.plot(kind="bar", color=["green", "red"])
        plt.title("OK / NOK Dağılımı")
        plt.xlabel("Sonuç")
        plt.ylabel("Adet")
        plt.tight_layout()
        plt.savefig("reporting_chart.jpg", format="jpg", dpi=300)
        plt.show()
    else:
        print("result sütunu bulunamadı, raporlama yapılamıyor.")

if __name__ == "__main__":
    from data_cleaning import clean_data
    from csv_extraction import extract_data
    df_raw = extract_data("data.csv")
    df_clean = clean_data(df_raw)
    generate_report(df_clean)
