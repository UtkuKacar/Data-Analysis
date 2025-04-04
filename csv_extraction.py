import pandas as pd
import re

def extract_data(csv_file):
    df = pd.read_csv(csv_file, header=None, names=["raw"])
    df = df[df["raw"].notna()]
    df["raw"] = df["raw"].str.strip('"')
    
    date_pattern = re.compile(r'^\d{2}/\d{2}/\d{4}')
    mask = df["raw"].str.match(date_pattern).fillna(False)
    data_rows = df[mask]
    
# Tokenlara ayır ve temizle result ile döndür
    def parse_row(row):
        tokens = row.split()
        if len(tokens) < 7:
            return None
        date = tokens[0]
        time = tokens[1]
        code = tokens[2]
        result = " ".join(tokens[3:-3])
        product = tokens[-3]
        force1 = tokens[-2]
        force2 = tokens[-1]
        return {
            "date": date,
            "time": time,
            "code": code,
            "result": result,
            "product": product,
            "force1": force1,
            "force2": force2
        }
    
    parsed = data_rows["raw"].apply(parse_row)
    parsed = parsed.dropna()
    df_parsed = pd.DataFrame(parsed.tolist())
    return df_parsed

if __name__ == "__main__":
    csv_file = "data.csv"
    df = extract_data(csv_file)
    print("Parsed Data (ilk 10 satır):")
    print(df.head(10))
