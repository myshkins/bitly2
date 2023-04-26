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
    df["bitlink"] = "http://" + df["domain"] + "." + df["hash"]
    df.set_index("long_url", inplace=True)
    return df


def count_clicks(df: pd.DataFrame, year: int):
    filtered = df[df["timestamp"].dt.year == year]
    grouped = filtered.groupby("bitlink").count()
    grouped.drop(["user_agent", "timestamp", "referrer"], axis=1, inplace=True)
    grouped.columns = ["count"]
    return grouped


def join_dfs(df_counts: pd.DataFrame, df_bitlinks: pd.DataFrame) -> pd.DataFrame:
    joined = df_bitlinks.join(df_counts, on="bitlink", how="left")
    # joined = df_counts.join(df_bitlink, on="bitlink", how="inner")
    return joined


timer = Timer()
timer.start()
df_decodes = make_decode_dataframe(DECODES_FILE_PATH)
df_bitlink = make_bitlink_dataframe(ENCODES_FILE_PATH)
df_counts = count_clicks(df_decodes, 2021)
joined = join_dfs(df_counts, df_bitlink)
timer.stop()
print(df_bitlink)
print(df_counts)
print(joined)
