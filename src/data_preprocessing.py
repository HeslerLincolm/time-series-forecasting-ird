import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def load_data(path: str) -> pd.DataFrame:
    """
    Load raw IRD dataset
    """
    df = pd.read_excel(
        path,
        sheet_name=1,
        skiprows=2,
        header=None,
    )
    return df

def parse_spanish_dates(df: pd.DataFrame, date_col: str) -> pd.DataFrame:
    """
    Convert Spanish month abbreviations to datetime.
    """

    spanish_to_english = {
        'Ene': 'Jan', 'Feb': 'Feb', 'Mar': 'Mar', 'Abr': 'Apr',
        'May': 'May', 'Jun': 'Jun', 'Jul': 'Jul', 'Ago': 'Aug',
        'Set': 'Sep', 'Sep': 'Sep', 'Oct': 'Oct', 'Nov': 'Nov', 'Dic': 'Dec'
    }

    df = df.copy()

    df[date_col] = df[date_col].replace(spanish_to_english, regex=True)
    df[date_col] = pd.to_datetime(df[date_col], format='%d%b%y')

    return df

def set_time_index(df: pd.DataFrame, date_col: str) -> pd.DataFrame:
    df = df.copy()
    df.set_index(date_col, inplace=True)
    return df

def split_time_series(df, train_ratio=0.7, val_ratio=0.15):
    """
    Chronological split for time series.
    """

    n_total = len(df)

    train_end = int(n_total * train_ratio)
    val_end = train_end + int(n_total * val_ratio)

    train = df.iloc[:train_end].copy()
    val = df.iloc[train_end:val_end].copy()
    test = df.iloc[val_end:].copy()

    return train, val, test

def add_differencing(df, column: str, order: int):
    df = df.copy()

    series = df[column]

    for _ in range(order):
        series = series.diff()

    df[f"{column}_diff_{order}"] = series

    return df

def prepare_scaled_splits(train_df, valid_df, test_df, target_col):
    """
    Convert the data to numpy and apply MinMax scaling.
    
    Returns:
        train_scaled, valid_scaled, test_scaled, scaler
    """

    # Convertir a numpy
    train_data = train_df[target_col].values.reshape(-1, 1)
    valid_data = valid_df[target_col].values.reshape(-1, 1)
    test_data  = test_df[target_col].values.reshape(-1, 1)

    # Escalado
    scaler = MinMaxScaler()

    train_scaled = scaler.fit_transform(train_data)
    valid_scaled = scaler.transform(valid_data)
    test_scaled  = scaler.transform(test_data)

    return train_scaled, valid_scaled, test_scaled, scaler