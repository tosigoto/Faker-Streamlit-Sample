import pandas as pd
from faker import Faker


def generate_customer_data(num_rows=1000):
    """
    架空の顧客データを生成する関数。
    Fakerライブラリを使用して、指定された件数の架空顧客データを生成します。
    生成されるデータは、名前、年齢、居住都市の情報を含みます。
    Args:
        num_rows (int, optional): 生成する顧客データの件数。デフォルトは1000件です。
    Returns:
        pandas.DataFrame: 生成された顧客データを含むDataFrame。
    """
    fake = Faker('ja_JP')
    data = {"name": [], "age": [], "city": []}
    for _ in range(num_rows):
        data["name"].append(fake.name())
        data["age"].append(fake.random_int(min=18, max=65))
        data["city"].append(fake.city())
    return pd.DataFrame(data)
