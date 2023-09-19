"""
@Author: SengYew 975258711@qq.com/fung975258711@gmail.com
@Create-Date: 2023-09-14 01:11:00
@LastEditors: SengYew 975258711@qq.com/fung975258711@gmail.com
@LastEditTime: 2023-09-14 01:12:00
@FilePath: D:\PyProject\develop\develop.py
@Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
"""

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import zhconv

class TitleControl(QMainWindow):
    def __init__(self,parent = None):
        super(TitleControl,self).__init__(parent)

        bar = self.menuBar()
        file = bar.addMenu("File")
        file.addAction("New")

        self.cnFontChange = CnFontChange(self)
        self.setCentralWidget(self.cnFontChange)

class CnFontChange(QWidget):
    def __init__(self, parent = None):
        super(CnFontChange,self).__init__(parent)

        layout = QHBoxLayout(self)

        self.inputTextBox = QTextEdit()
        self.changeTextButton = QPushButton("繁體字轉簡體字")
        self.changeTextButton.clicked.connect(self.change_text)
        self.outputTextBox = QTextEdit()

        layout.addWidget(self.inputTextBox)
        layout.addWidget(self.changeTextButton)
        layout.addWidget(self.outputTextBox)

        self.setWindowTitle("SetBox")

    def change_text(self):
        text = self.inputTextEdit.toPlainText()
        print(text)
        convertex_text = zhconv.convert(text, 'zh-cn')
        self.outputTextBox.append(convertex_text)




def main():
    app = QApplication(sys.argv)
    ex = TitleControl()
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()


