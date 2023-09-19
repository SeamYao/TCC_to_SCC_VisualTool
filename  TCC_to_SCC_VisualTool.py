import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QTextEdit, QPushButton
import zhconv
class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        bar = self.menuBar()
        file = bar.addMenu("File")
        file.addAction("New")

        self.setWindowTitle("QTextEdit Example")

        central_widget = QWidget()
        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        self.input_text_edit = QTextEdit()
        layout.addWidget(self.input_text_edit)

        self.output_text_edit = QTextEdit()
        layout.addWidget(self.output_text_edit)

        button = QPushButton("Copy Text")
        button.clicked.connect(self.copy_text)
        layout.addWidget(button)

        self.setCentralWidget(central_widget)

    def copy_text(self):
        text = self.input_text_edit.toPlainText()
        convertex_text = zhconv.convert(text, 'zh-cn')

        self.output_text_edit.setText(convertex_text)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())