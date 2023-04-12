from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import cv2
from skimage import io
import numpy as np
from css import styleCss
from filtrage import Tf, Filtre


class PhotoLabel(QLabel):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setAlignment(Qt.AlignCenter)
        self.setText('\n\n Drop Image Here \n\n')
        self.setStyleSheet('''
        QLabel {
            border: 4px dashed #aaa;
        }''')

    def setPixmap(self, *args, **kwargs):
        super().setPixmap(*args, **kwargs)
        self.setStyleSheet('''
        QLabel {
            border: none;
        }''')


class Ui_Form(QWidget):
    
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(919, 533)
        Form.setStyleSheet(styleCss)  #*****************************************

        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(-20, -10, 1331, 561))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setMaximumSize(QtCore.QSize(180, 16777215))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_12 = QtWidgets.QFrame(self.frame_2)
        self.frame_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.verticalLayout.addWidget(self.frame_12)
        self.frame_10 = QtWidgets.QFrame(self.frame_2)
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.verticalLayout.addWidget(self.frame_10)
        self.frame_4 = QtWidgets.QFrame(self.frame_2)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_4)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(31, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.frame_4)
        self.pushButton.setMinimumSize(QtCore.QSize(80, 22))
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 0, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(31, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 2, 1, 1)
        self.verticalLayout.addWidget(self.frame_4)
        self.frame_5 = QtWidgets.QFrame(self.frame_2)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.frame_5)
        self.gridLayout_5.setObjectName("gridLayout_5")
        spacerItem2 = QtWidgets.QSpacerItem(31, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem2, 0, 0, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.frame_5)
        self.comboBox.setMinimumSize(QtCore.QSize(80, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout_5.addWidget(self.comboBox, 0, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(31, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem3, 0, 2, 1, 1)
        self.verticalLayout.addWidget(self.frame_5)
        self.frame_6 = QtWidgets.QFrame(self.frame_2)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_6)
        self.gridLayout_3.setObjectName("gridLayout_3")
        spacerItem4 = QtWidgets.QSpacerItem(31, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem4, 0, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.frame_6)
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 0, 1, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(31, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem5, 0, 2, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(31, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem6, 1, 0, 1, 1)
        self.spinBox_f = QtWidgets.QSpinBox(self.frame_6)
        self.spinBox_f.setMinimumSize(QtCore.QSize(80, 22))
        self.spinBox_f.setMinimum(0)
        self.spinBox_f.setMaximum(100000)
        self.spinBox_f.setSingleStep(10)
        self.spinBox_f.setObjectName("spinBox_f")
        self.gridLayout_3.addWidget(self.spinBox_f, 1, 1, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(31, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem7, 1, 2, 1, 1)
        self.verticalLayout.addWidget(self.frame_6)
        self.frame_7 = QtWidgets.QFrame(self.frame_2)
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frame_7)
        self.gridLayout_4.setObjectName("gridLayout_4")
        spacerItem8 = QtWidgets.QSpacerItem(31, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem8, 0, 0, 1, 1)
        self.label_1 = QtWidgets.QLabel(self.frame_7)
        self.label_1.setObjectName("label_1")
        self.gridLayout_4.addWidget(self.label_1, 0, 1, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(31, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem9, 0, 2, 1, 1)
        spacerItem10 = QtWidgets.QSpacerItem(31, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem10, 1, 0, 1, 1)
        self.spinBox_order = QtWidgets.QSpinBox(self.frame_7)
        self.spinBox_order.setMinimumSize(QtCore.QSize(80, 22))
        self.spinBox_order.setProperty("value", 1)
        self.spinBox_order.setObjectName("spinBox_order")
        self.gridLayout_4.addWidget(self.spinBox_order, 1, 1, 1, 1)
        spacerItem11 = QtWidgets.QSpacerItem(31, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem11, 1, 2, 1, 1)
        self.verticalLayout.addWidget(self.frame_7)
        self.frame_8 = QtWidgets.QFrame(self.frame_2)
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_8)
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem12 = QtWidgets.QSpacerItem(31, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem12, 0, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_8)
        self.pushButton_2.setMinimumSize(QtCore.QSize(80, 22))
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_2.addWidget(self.pushButton_2, 0, 1, 1, 1)
        spacerItem13 = QtWidgets.QSpacerItem(31, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem13, 0, 2, 1, 1)
        self.verticalLayout.addWidget(self.frame_8)
        self.frame_9 = QtWidgets.QFrame(self.frame_2)
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.verticalLayout.addWidget(self.frame_9)
        self.frame_11 = QtWidgets.QFrame(self.frame_2)
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.verticalLayout.addWidget(self.frame_11)
        self.horizontalLayout.addWidget(self.frame_2)
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.label_filtre = PhotoLabel(self.frame_3)
        self.label_filtre.setGeometry(QtCore.QRect(10, 280, 341, 231))
        self.label_filtre.setObjectName("label_filtre")
        self.label_img = PhotoLabel(self.frame_3)
        self.label_img.setGeometry(QtCore.QRect(10, 20, 341, 231))
        self.label_img.setObjectName("label_img")
        self.label_tf = PhotoLabel(self.frame_3)
        self.label_tf.setGeometry(QtCore.QRect(380, 20, 341, 231))
        self.label_tf.setObjectName("label_tf")
        self.label_resulta = PhotoLabel(self.frame_3)
        self.label_resulta.setGeometry(QtCore.QRect(380, 280, 341, 231))
        self.label_resulta.setObjectName("label_resulta")
        self.label_somme = PhotoLabel(self.frame_3)
        self.label_somme.setGeometry(QtCore.QRect(750, 150, 341, 231))
        self.label_somme.setObjectName("label_somme")
        self.horizontalLayout.addWidget(self.frame_3)



        self.pushButton.clicked.connect(self.open_image)
        self.pushButton_2.clicked.connect(self.test)


        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)





    def test(self):
        img = self.filename
        img1 = io.imread(img)
        img = cv2.cvtColor(img1, cv2.COLOR_RGB2GRAY)

        self.freqence = self.spinBox_f.value()
        self.order = self.spinBox_order.value() 
        self.content = self.comboBox.currentText() 

        ILPF = Filtre().idealLowPass(img,self.freqence)
        IHPF = Filtre().idealHighPass(img,self.freqence)
        BLPF = Filtre().ButterwortLow(img,self.freqence,self.order)
        BHPF = Filtre().ButterwortHigh(img,self.freqence,self.order)
        GLPF = Filtre().GaussianLow(img,self.freqence)
        GHPF = Filtre().GaussianHigh(img,self.freqence)
        Laplacien ,H, g  = Filtre().LaplacianFilter(img)

        if self.content == "ILPF" :
            test = ILPF
        elif self.content == "IHPF" :
            test = IHPF
        elif self.content == "BLPF":
            test = BLPF
        elif self.content == "BHPF":
            test = BHPF
        elif self.content == "GLPF":
            test = GLPF
        elif self.content == "Laplacien":
            Laplacien = Laplacien
            g = g
            H = H

        else : 
            test = GHPF


#////////////////////////////////////////////////////////////////
        if self.content == "Laplacien":

            LapScaled, H, g= Filtre().LaplacianFilter(img)

            for x in range(H.shape[0]):
                for y in range(H.shape[1]):
                     H[x][y] = np.uint8( ((H[x][y] - np.min(H))/ 4864))

            for x in range(g.shape[0]):
                for y in range(g.shape[1]):
                    g[x][y] = np.uint8(255 * (g[x][y]))

            for x in range(LapScaled.shape[0]):
                for y in range(LapScaled.shape[1]):
                    LapScaled[x][y] = np.uint8(( 255 * (LapScaled[x][y] + 1)) / 2 )
            
            cv2.imwrite("!!!!_Interdit_utiliser_cette_image_LapScaled.png", (LapScaled))
            cv2.imwrite("!!!!_Interdit_utiliser_cette_image_H.png", (H))
            cv2.imwrite("!!!!_Interdit_utiliser_cette_image_g.png", (g))

            self.label_filtre.setPixmap(QPixmap("!!!!_Interdit_utiliser_cette_image_H.png"))
            self.label_resulta.setPixmap(QPixmap("!!!!_Interdit_utiliser_cette_image_lapScaled.png"))      
            self.label_somme.setPixmap(QPixmap("!!!!_Interdit_utiliser_cette_image_g.png"))      


        else :

            F = Tf().FFT(img)
            G = test * F
            g = np.real(Tf().inversFFT(G))



            for x in range(test.shape[0]):
                for y in range(test.shape[1]):
                    test[x][y] = np.uint8(255 * (test[x][y]))

            cv2.imwrite("!!!!_Interdit_utiliser_cette_image_g.png", (g))
            cv2.imwrite("!!!!_Interdit_utiliser_cette_image_ss.png", (test))

            self.label_filtre.setPixmap(QPixmap("!!!!_Interdit_utiliser_cette_image_ss.png"))
            self.label_resulta.setPixmap(QPixmap("!!!!_Interdit_utiliser_cette_image_g.png"))      





    def dragEnterEvent(self, event):
        if event.mimeData().hasImage:
            event.accept()
        else:
            event.ignore()

    def dragMoveEvent(self, event):
        if event.mimeData().hasImage:
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        if event.mimeData().hasImage:
            event.setDropAction(Qt.CopyAction)
            self.filename = event.mimeData().urls()[0].toLocalFile()
            event.accept()
            self.open_image(self.filename)
        else:
            event.ignore()

    def open_image(self, filename=None):
        if not filename:
            self.filename, _ = QFileDialog.getOpenFileName(self, 'Select Photo', QDir.currentPath(), 'Images (*.png *.jpg)')
            if not self.filename:
                return

        img1 = io.imread(self.filename)
        img = cv2.cvtColor(img1, cv2.COLOR_RGB2GRAY)
        cv2.imwrite("!!!!_Interdit_utiliser_cette_image_gray.png", (img))


        # self.label_img.setPixmap(QPixmap(self.filename))
        self.label_img.setPixmap(QPixmap("!!!!_Interdit_utiliser_cette_image_gray.png"))

        img = Tf().FFT(img)
        img = Tf().Spectrum(img)

        cv2.imwrite("!!!!_Interdit_utiliser_cette_image_fft.png", (img))
        self.label_tf.setPixmap(QPixmap("!!!!_Interdit_utiliser_cette_image_fft.png"))

        self.test()





    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Othmane ELAZRI   Anass EL HALLANI   Younes EL BELGHITI"))

        self.pushButton.setText(_translate("Form", "open_image"))
        self.comboBox.setItemText(0, _translate("Form", "ILPF"))
        self.comboBox.setItemText(1, _translate("Form", "BLPF"))
        self.comboBox.setItemText(2, _translate("Form", "GLPF"))
        self.comboBox.setItemText(3, _translate("Form", "IHPF"))
        self.comboBox.setItemText(4, _translate("Form", "BHPF"))
        self.comboBox.setItemText(5, _translate("Form", "GHPF"))
        self.comboBox.setItemText(6, _translate("Form", "Laplacien"))
        self.label.setText(_translate("Form", " cut of freqency"))
        self.label_1.setText(_translate("Form", "        order"))
        self.pushButton_2.setText(_translate("Form", "generez"))
        self.label_filtre.setText(_translate("Form", ""))
        self.label_img.setText(_translate("Form", ""))
        self.label_tf.setText(_translate("Form", ""))
        self.label_resulta.setText(_translate("Form", ""))
        self.label_somme.setText(_translate("Form", ""))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
