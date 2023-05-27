from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QLabel

app = QApplication([])
window = QWidget()
window.setWindowTitle('Виды спортов')
window.resize(400, 300)

button1 = QPushButton('Football')
button2 = QPushButton('Basketball')
button3 = QPushButton('Hockey')
button4 = QPushButton('Volleyball')
button5 = QPushButton('Tennis')
button6 = QPushButton('Baseball')
button7 = QPushButton('Rugby')
button8 = QPushButton('Boxing')
button9 = QPushButton('Chees')
button10 = QPushButton('Golf')

layoutV = QVBoxLayout()
layoutH1 = QHBoxLayout()
layoutH2 = QHBoxLayout()
layoutH3 = QHBoxLayout()
layoutH4 = QHBoxLayout()
layoutH5 = QHBoxLayout()

layoutH1.addWidget(button1, alignment = Qt.AlignCenter)
layoutH1.addWidget(button2, alignment = Qt.AlignCenter)
layoutH2.addWidget(button3, alignment = Qt.AlignCenter)
layoutH2.addWidget(button4, alignment = Qt.AlignCenter)
layoutH3.addWidget(button5, alignment = Qt.AlignCenter)
layoutH3.addWidget(button6, alignment = Qt.AlignCenter)
layoutH4.addWidget(button7, alignment = Qt.AlignCenter)
layoutH4.addWidget(button8, alignment = Qt.AlignCenter)
layoutH5.addWidget(button9, alignment = Qt.AlignCenter)
layoutH5.addWidget(button10, alignment = Qt.AlignCenter)


layoutV.addLayout(layoutH1)
layoutV.addLayout(layoutH2)
layoutV.addLayout(layoutH3)
layoutV.addLayout(layoutH4)
layoutV.addLayout(layoutH5)
window.setLayout(layoutV)

window.show()
app.exec_()