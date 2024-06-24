# 2s1packgui

This project is a graphical user interface (GUI) application for managing storage containers. It allows users to load, mount, and move samples within containers, and it logs all operations to a log file and displays them in a scrollable text box within the GUI.

## Features

- Load samples into containers
- Mount samples on a global mounting system (gonio)
- Move samples between containers
- Enable or disable containers
- Log all operations to a file and display them in the GUI

## Requirements

- Python 3.x
- tkinter
- datetime
- logging

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/StorageContainerManagement.git
    cd StorageContainerManagement
    ```

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

Run the `unipack_gui.py` script to start the application:
```bash
python unipack_gui.py
```

### Load Tab

- **Enable Container**: Enable or disable the container. Only enabled containers can have samples loaded.
- **Load Samples**: Click on a button to load a sample (button turns light blue). Click again to unload (button turns back to default color).

### Mount Tab

- **Check Hold State**: If a sample is held, it cannot be mounted. A message will be displayed.
- **Mount Samples**: Click on a button to mount a sample (button turns red). Click again to unmount (button turns back to light blue).

### Move Tab

- **Move Samples**: Click on a button to hold a sample (button turns yellow). Click on another button to move the sample. If a sample is already loaded in the target position, a message will be displayed.

### Log

- The application logs all operations to a log file named `yymmdd_sample.log` in the execution directory.
- The log is also displayed in a scrollable text box at the bottom of each tab.

## Example

![Screenshot](screenshot.png)

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.


# 2s1packgui

このプロジェクトは、収納容器を管理するためのグラフィカルユーザーインターフェイス（GUI）アプリケーションです。ユーザーは、サンプルをコンテナにロード、マウント、移動することができ、すべての操作をログファイルに記録し、GUI内のスクロール可能なテキストボックスに表示します。

## 特徴

- サンプルをコンテナにロード
- サンプルをグローバルマウントシステム（gonio）にマウント
- コンテナ間でサンプルを移動
- コンテナを有効化または無効化
- すべての操作をファイルにログし、GUIに表示

## 必要条件

- Python 3.x
- tkinter
- datetime
- logging

## インストール

1. リポジトリをクローンします：
    ```bash
    git clone https://github.com/yourusername/StorageContainerManagement.git
    cd StorageContainerManagement
    ```

2. 必要な依存関係をインストールします：
    ```bash
    pip install -r requirements.txt
    ```

## 使い方

`unipack_gui.py`スクリプトを実行してアプリケーションを起動します：
```bash
python unipack_gui.py
```

### Loadタブ

- **Enable Container**：コンテナを有効または無効にします。有効なコンテナのみがサンプルをロードできます。
- **Load Samples**：ボタンをクリックしてサンプルをロードします（ボタンが水色に変わります）。もう一度クリックしてアンロードします（ボタンがデフォルトの色に戻ります）。

### Mountタブ

- **Check Hold State**：サンプルがホールドされている場合、マウントできません。メッセージが表示されます。
- **Mount Samples**：ボタンをクリックしてサンプルをマウントします（ボタンが赤に変わります）。もう一度クリックしてアンマウントします（ボタンが水色に戻ります）。

### Moveタブ

- **Move Samples**：ボタンをクリックしてサンプルをホールドします（ボタンが黄色に変わります）。別のボタンをクリックしてサンプルを移動します。ターゲット位置にすでにサンプルがロードされている場合、メッセージが表示されます。

### ログ

- アプリケーションは、すべての操作を実行ディレクトリにある `yymmdd_sample.log` という名前のログファイルに記録します。
- ログは各タブの下部にあるスクロール可能なテキストボックスにも表示されます。


## ライセンス

このプロジェクトはMITライセンスの下でライセンスされています。
```

