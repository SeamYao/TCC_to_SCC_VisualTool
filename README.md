# Visual tool for converting traditional Chinese characters to simplified Chinese characters

pip install zhconv
pip install PyQt5
pip install pyinstaller


use cmd pyinstaller -F -w outPutProject1.py --add-data="resource;."



import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QTextEdit, QPushButton
import zhconv
