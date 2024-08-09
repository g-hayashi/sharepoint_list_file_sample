# SharePoint Online File List Retriever

このプロジェクトは、Microsoft Graph APIを利用してSharePoint OnlineからSite、Drive、Fileの一覧を取得するPythonプログラムです。

SharePointからAPI経由でアクセスする場合、旧来はAzure ACSを利用していたのですが、Azure ACSは廃止となります。

https://learn.microsoft.com/ja-jp/sharepoint/dev/sp-add-ins/retirement-announcement-for-azure-acs

意外とGraphを利用したデータ取得の方法が見つからなかったので、サンプルとして記載。

## 必要な環境

- Python 3.x
- Microsoft Graph APIのアクセス権
- 必要なPythonライブラリ（requestsなど）
```sh
 pip install msal requests
 pip install python-dotenv
```
## 使用方法


1. 環境変数にシークレット情報を指定し、`Main.py`を実行して、SharePoint OnlineからSite、Drive、Fileの一覧を取得します。
    ```bash
    python main.py
    ```

2. 必要に応じて、`Main.py`内の設定を変更して、特定のSiteやDriveを指定します。

## ライセンス

このプロジェクトはMITライセンスの下で公開されています。詳細については、LICENSEファイルを参照してください。
