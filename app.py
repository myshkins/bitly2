from datetime import datetime as dt
import json
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
    df["bitlink"] = "http://" + df["domain"] + "/" + df["hash"]
    return df


def count_clicks(df: pd.DataFrame, year: int):
    filtered = df[df["timestamp"].dt.year == year]
    grouped = filtered.groupby("bitlink", as_index=False).count()
    grouped.drop(["user_agent", "timestamp", "referrer"], axis=1, inplace=True)
    grouped.columns = ["bitlink", "count"]
    return grouped


def join_dfs(df_counts: pd.DataFrame, df_bitlink: pd.DataFrame) -> pd.DataFrame:
    joined = pd.merge(df_bitlink, df_counts)
    joined.drop(["domain", "hash", "bitlink"], axis=1, inplace=True)
    joined.sort_values(by=["count"])
    return joined

def jsonify(df: pd.DataFrame) -> str:
    temp = df.to_json(orient="values")
    _temp = json.loads(temp)
    result = [{k: v} for k, v in _temp]
    return result


timer = Timer()
timer.start()
df_decodes = make_decode_dataframe(DECODES_FILE_PATH)
df_bitlink = make_bitlink_dataframe(ENCODES_FILE_PATH)
df_counts = count_clicks(df_decodes, 2021)
joined = join_dfs(df_counts, df_bitlink)
result = jsonify(joined)
timer.stop()
print(result)