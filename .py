from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication
def play():
	ch=windows.edit.text()
	windows.aff.setText(ch)
app = QApplication([])
windows = loadUi ("ere.ui")
windows.show()
windows.btn.clicked.connect (play)
app.exec_()

