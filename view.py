from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QLabel, QWidget, QPushButton, QComboBox, QVBoxLayout
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
import sys



def window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(300, 300, 1000, 500)
    win.setWindowTitle("EZN")

    win.textbox = QLineEdit(win)
    win.textbox.move(20, 40)
    win.textbox.resize(280, 40)

    win.textbox = QLineEdit(win)
    win.textbox.move(20, 100)
    win.textbox.resize(280, 40)

    win.textbox = QLineEdit(win)
    win.textbox.move(20, 160)
    win.textbox.resize(280, 40)

    win.textbox = QLineEdit(win)
    win.textbox.move(20, 220)
    win.textbox.resize(280, 40)

    win.textbox = QLineEdit(win)
    win.textbox.move(350, 40)
    win.textbox.resize(280, 40)

    win.textbox = QLineEdit(win)
    win.textbox.move(350, 100)
    win.textbox.resize(280, 40)

    button = QPushButton('Dodaj', win)
    button.setToolTip('This is an example button')
    button.move(670, 40)
    button.resize(280, 40)

    button = QPushButton('Dodaj', win)
    button.setToolTip('This is an example button')
    button.move(670, 100)
    button.resize(280, 40)

    button = QPushButton('Dodaj', win)
    button.setToolTip('This is an example button')
    button.move(670, 160)
    button.resize(280, 40)

    button = QPushButton('Dodaj', win)
    button.setToolTip('This is an example button')
    button.move(670, 220)
    button.resize(280, 40)

    combobox1 = QComboBox(win)
    combobox1.addItem('1')
    combobox1.addItem('2')
    combobox1.addItem('3')
    combobox1.addItem('4')
    combobox1.move(350, 160)
    combobox1.resize(280, 40)

    combobox2 = QComboBox(win)
    combobox2.addItem('1')
    combobox2.addItem('2')
    combobox2.addItem('3')
    combobox2.addItem('4')
    combobox2.move(350, 220)
    combobox2.resize(280, 40)


    win.asd=QLabel('Nazwa', win)
    win.asd.move(20,10)

    win.asd = QLabel('Ilosc Godzin', win)
    win.asd.move(350, 10)

    win.asd = QLabel('KLASA', win)
    win.asd.move(470, 1)

    win.asd = QLabel('ZAJECIA', win)
    win.asd.move(470, 75)

    win.asd = QLabel('NAUCZYCIEL', win)
    win.asd.move(470, 135)

    win.asd = QLabel('NAZWY ZAJEC', win)
    win.asd.move(470, 195)

    win.asd=QLabel('Imie i Nazwisko', win)
    win.asd.move(20,135)

    win.asd=QLabel('Sala', win)
    win.asd.move(350,135)

    win.asd=QLabel('Numer sali', win)
    win.asd.move(20,195)

    win.asd=QLabel('Typ sali', win)
    win.asd.move(350,195)

    win.show()
    sys.exit(app.exec_())

window()




