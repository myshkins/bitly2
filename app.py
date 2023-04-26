from datetime import datetime as dt
import pandas as pd

from timer import Timer

ENCODES_FILE_PATH = "encodes.csv"
DECODES_FILE_PATH = "decodes.json"


def make_decode_dataframe(path: str) -> pd.DataFrame:
    df = pd.read_json(path)
    df["timestamp"] = pd.to_datetime(df["timestamp"])
    return df


def make_bitlink_dataframe(path: str) -> pd.DataFrame:
    df = pd.read_csv(path, header=0)
    df["bitlinks"] = "http://" + df["domain"] + "." + df["hash"]
    return df


def count_clicks(df: pd.DataFrame, year: int):
    filtered = df[df["timestamp"].dt.year == year]
    grouped = filtered.groupby("bitlink").count()
    return grouped


def join_dfs(df_counts: pd.DataFrame, df_bitlinks: pd.DataFrame) -> pd.DataFrame:
    joined = df_counts.join()

timer = Timer()
timer.start()
df = make_decode_dataframe(DECODES_FILE_PATH)
bit_df = make_bitlink_dataframe(ENCODES_FILE_PATH)
print(bit_df)
fdf = count_clicks(df, 2021)
timer.stop()
print(fdf)
