# Faker-Streamlit-Sample

## 目的
このREADME.mdは、当「架空の顧客データ分析アプリ」プロジェクトの概要を説明し、利用方法や開発に関する情報を提供することを目的としています。

## プロジェクト概要
このプロジェクトは、Streamlitを用いて構築された、架空の顧客データを分析するためのWebアプリケーションです。生成された顧客データに基づいて、様々な分析や可視化を行うことができます。

## 機能
- 顧客データの生成: Fakerライブラリを用いて、架空の顧客データを生成します。
- データの表示: 生成された顧客データをDataFrame形式で表示します。
- 年齢分布の可視化: 年齢分布をヒストグラムで可視化します。
- 顧客データのダウンロード: CSVおよびExcel形式（グラフ含む）で顧客データをダウンロードできます。
- 都市別のデータ抽出: 特定の都市の顧客データを抽出できます。

## ファイル構成
- app.py: Streamlitアプリケーションのメインファイル。
- data/customers.csv: 生成された顧客データが保存されるCSVファイル。
- utils/data_generator.py: 顧客データを生成するユーティリティ関数。
- requirements.txt: プロジェクトに必要なライブラリを記述したファイル。

## 使い方
### 環境構築:
```bash
git clone https://github.com/tosigoto/Faker-Streamlit-Sample.git
cd Faker-Streamlit-Sample
mkdir data
pip install -r requirements.txt
```

### アプリの起動:
```bash
streamlit run app.py
```

## 開発環境
Python: [3.10]
ライブラリ: Streamlit, pandas, numpy, faker, xlsxwriter

## ライセンス
このプロジェクトは、MITライセンスの下で公開されています。
