import pandas as pd
import pytest

import app


@pytest.fixture
def decode_df():
    return app.make_decode_dataframe(app.DECODES_FILE_PATH)


@pytest.fixture
def bitlink_df():
    return app.make_bitlink_dataframe(app.ENCODES_FILE_PATH)


def test_make_decode_dataframe():
    df = app.make_decode_dataframe(app.DECODES_FILE_PATH)
    assert isinstance(df, pd.DataFrame)
    assert not df.empty


def test_make_bitlink_dataframe():
    df = app.make_bitlink_dataframe(app.ENCODES_FILE_PATH)
    assert isinstance(df, pd.DataFrame)
    assert not df.empty


def test_count_clicks():
    pass
