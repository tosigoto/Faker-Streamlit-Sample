import io
import base64
import streamlit as st
import pandas as pd
import xlsxwriter  # Excelファイル生成用
from utils.data_generator import generate_customer_data


def main():
    """
    架空の顧客データ分析アプリのメイン関数。

    この関数は、Streamlitアプリの全体的な処理を定義します。
    顧客データを生成し、DataFrameに変換、表示します。
    さらに、年齢分布のヒストグラム、顧客データのダウンロードリンクを生成します。
    """
    st.title("架空顧客データ分析アプリ")

    # 顧客データの生成 (必要に応じてカスタマイズ)
    num_customers = st.slider("顧客人数", 100, 10000, 1000)
    customer_data = generate_customer_data(num_customers)

    # CSVファイルへの保存 (必要に応じて)
    customer_data.to_csv("data/customers.csv", index=False)

    # CSVファイルからデータを読み込む
    df = pd.read_csv("data/customers.csv")

    st.write("生成された顧客データ")
    st.dataframe(df)

    # 年齢分布のヒストグラム
    st.subheader("年齢分布")
    st.bar_chart(df["age"])

    # ダウンロードリンクの生成
    csv_download_link = get_table_download_link(df)
    excel_download = create_excel_file(df, df["age"])
    excel_b64 = base64.b64encode(excel_download).decode()
    excel_href = f'<a href="data:application/vnd.openxmlformats-officedocument.spreadsheetml.sheet;base64,{excel_b64}" download="customer_data.xlsx">Download Excel file</a>'

    # ダウンロードリンクを表示
    st.markdown(csv_download_link, unsafe_allow_html=True)
    st.markdown(excel_href, unsafe_allow_html=True)

    # 都市の頻度
    st.subheader("居住都市")
    st.bar_chart(df["city"].value_counts())

    # 特定の都市の顧客データを抽出
    selected_city = st.selectbox("都市を選択", df["city"].unique())
    filtered_df = df[df["city"] == selected_city]
    st.dataframe(filtered_df, hide_index=True)


# ダウンロードボタン
def get_table_download_link(df):
    """
    Pandas DataFrameからCSVダウンロードリンクを生成する関数。
    Args:
        df (pandas.DataFrame): ダウンロード対象のDataFrame。
    Returns:
        str: CSVファイルをダウンロードするためのHTMLタグ。
    """
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(
        csv.encode()
    ).decode()  # some strings <-> bytes conversions necessary here
    href = f'<a href="data:file/csv;base64,{b64}" download="customer_data.csv">Download csv file</a>'
    return href


# Excelファイルを作成する関数
def create_excel_file(df, age_data):
    """
    Pandas DataFrameと年齢データ、グラフをExcelファイルに変換する関数。
    Args:
        df (pandas.DataFrame): DataFrameデータ。
        age_data (pandas.Series): 年齢データ。
    Returns:
        bytes: Excelファイルのバイナリデータ。
    """
    output = io.BytesIO()
    workbook = xlsxwriter.Workbook(output)
    worksheet = workbook.add_worksheet()

    # データフレームをシートに書き込む
    worksheet.write("A1", "Customer Data")
    row = 1
    for column in df.columns:
        worksheet.write(row, 0, column)
        row += 1
    for index, row in df.iterrows():
        row_num = index + 2
        for col_num, value in enumerate(row):
            worksheet.write(row_num, col_num, value)

    # グラフをシートに書き込む
    chart = workbook.add_chart({"type": "column"})
    chart.add_series({"values": "=Sheet1!$B$2:$B$" + str(len(age_data) + 1)})
    worksheet.insert_chart("D2", chart)

    workbook.close()
    output.seek(0)
    return output.getvalue()


if __name__ == "__main__":
    main()
