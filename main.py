from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import QMessageBox
from src.perceptron import Perceptron
import random
import math

class MainWindow(QtWidgets.QMainWindow, QtWidgets.QWidget):

    buttonInput = []
    inputState = [0] * 35
    letterButtons =[]
    letter = []
    expected = [1,0,0,0,1,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0]
    p = Perceptron

    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi('mainwindow.ui', self)

        self.buttonInput = [self.btn1, self.btn2, self.btn3, self.btn4, self.btn5, self.btn6,
                        self.btn7, self.btn8, self.btn9, self.btn10, self.btn11, self.btn12,
                        self.btn13, self.btn14, self.btn15, self.btn16, self.btn17, self.btn18,
                        self.btn19, self.btn20, self.btn21, self.btn22, self.btn23, self.btn24,
                        self.btn25, self.btn26, self.btn27, self.btn28, self.btn29, self.btn30,
                        self.btn31, self.btn32, self.btn33, self.btn34, self.btn35]
        self.letterButtons = [self.btnA, self.btnB, self.btnC, self.btnD, self.btnE, self.btnF,
                                self.btnG, self.btnH, self.btnI, self.btnJ, self.btnK, self.btnL,
                                self.btnM, self.btnN, self.btnO, self.btnP, self.btnQ, self.btnR,
                                self.btnS, self.btnT, self.btnU, self.btnV, self.btnW, self.btnX,
                                self.btnY, self.btnZ]

        # Get letters from a text file
        filename = "letter.txt"
        file = open(filename, "r")
        for line in file:
            #print(line)
            self.letter.append(line)

        self.p = Perceptron(self.letter, self.expected, 0.1, 500)

        # On click buttonInputs
        for i in range(len(self.buttonInput)):
            self.buttonInput[i].clicked.connect(lambda checked, x=i: self.changeColor(self.buttonInput[x], x))

        # On click letters
        for i in range(26):
            self.letterButtons[i].clicked.connect(lambda checked, x=self.p.get_letter(i): self.letterClick(x))

        self.btnTrain.clicked.connect(self.train)
        self.btnRecognize.clicked.connect(self.recognize)


    def changeColor(self, button, x):
        if self.p.get_input_state(x) is 0:
            button.setStyleSheet("background-color: gray")
            self.p.set_input_state(x, 1)
        else:
            button.setStyleSheet("background-color: button")
            self.p.set_input_state(x, 0)

    def letterClick(self, data):
        data = data.replace('\n', '')
        data = data.split(',')
        i = 0
        for x in range(len(data)):
            self.buttonInput[x].setStyleSheet("background-color: button")
            self.p.set_input_state(x, 0)
        for s in data:
            if s is "1":
                self.buttonInput[i].setStyleSheet("background-color: gray")
                self.p.set_input_state(i, 1)
            i+=1
    
    def train(self):
        self.p.train()
        self.btnTrain.setEnabled(False)
        self.btnRecognize.setEnabled(True)

    def recognize(self):
        self.showdialog(self.p.recognize())

    def showdialog(self, result):
        msgBox = QMessageBox( self )
        msgBox.setIcon( QMessageBox.Information )
        msgBox.setText( result )

        msgBox.addButton( QMessageBox.Yes )
        msgBox.show()



if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())