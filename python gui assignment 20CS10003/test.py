import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(1200, 800)
        label = QLabel('hello world')
        layout = QVBoxLayout()
        self.setLayout(layout)

        layout.addWidget(label)

if __name__ == '__main__':
    app = QApplication(sys.argv)

    app.setStyleSheet('''
    QWidget{
        font-size: 35px;
    }
    ''')
    myApp = MyApp()
    myApp.show()

    try:
        app.exec_()
    except SystemExit:
        print('Closing Window...')
        