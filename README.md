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

