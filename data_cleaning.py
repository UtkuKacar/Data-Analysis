import pandas as pd

def clean_data(df):
    #Virgülleri noktaya dönüştür
    df["force1"] = pd.to_numeric(df["force1"].astype(str).str.replace(",", "."), errors="coerce")
    df["force2"] = pd.to_numeric(df["force2"].astype(str).str.replace(",", "."), errors="coerce")
    
    #Negatif verileri filtrele
    df = df[(df["force1"] >= 0) & (df["force2"] >= 0)]

    if "result" in df.columns:
        df["result"] = df["result"].str.upper()

    df = df.rename(columns={"force1": "FORCE_POS_1", "force2": "FORCE_POS_2"})
    
    return df

if __name__ == "__main__":
    from csv_extraction import extract_data
    df_raw = extract_data("data.csv")
    df_clean = clean_data(df_raw)
    print("Temizlenmiş veri örneği:")
    print(df_clean.head(10))
