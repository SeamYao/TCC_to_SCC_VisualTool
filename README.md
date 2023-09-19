# Visual tool for converting traditional Chinese characters to simplified Chinese characters

需安裝的庫

pip install zhconv

pip install PyQt5

pip install pyinstaller

運行生成exe

use cmd pyinstaller -F -w  TCC_to_SCC_VisualTool.py --add-data="resource;."



import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QTextEdit, QPushButton
import zhconv

未來工作

1.更改界面

2.更多形式的轉變
