# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\MyCode\ShutDown.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!
##
from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import *
from PyQt4.QtGui import QDialog,QFrame,QLabel,QLineEdit,QPushButton,QLCDNumber,QWidget
from PyQt4.QtGui import QApplication
from PyQt4.QtCore import QTimer,QTime,SIGNAL
import sys,os,win32process

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(414, 117)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("shutdown.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.NowTime = QtGui.QLCDNumber(Dialog)
        self.NowTime.setGeometry(QtCore.QRect(70, 0, 131, 71))
        self.NowTime.setStyleSheet(_fromUtf8("color:rgb(0, 85, 255)"))
        self.NowTime.setDigitCount(5)
        self.NowTime.setMode(QtGui.QLCDNumber.Hex)
        self.NowTime.setSegmentStyle(QtGui.QLCDNumber.Flat)
        self.NowTime.setObjectName(_fromUtf8("NowTime"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 0, 61, 41))
        self.label.setStyleSheet(_fromUtf8("font: 75 16pt \"微软雅黑\";\n"
"color: rgb(48, 86, 255)"))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 35, 61, 31))
        self.label_2.setStyleSheet(_fromUtf8("font: 75 16pt \"微软雅黑\";\n"
"color: rgb(48, 86, 255)"))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(220, 0, 61, 41))
        self.label_3.setStyleSheet(_fromUtf8("font: 75 16pt \"微软雅黑\";\n"
"color: rgb(255, 0, 127)"))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(220, 35, 61, 31))
        self.label_4.setStyleSheet(_fromUtf8("font: 75 16pt \"微软雅黑\";\n"
"color: rgb(255, 0, 127)"))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.EndTime = QtGui.QLCDNumber(Dialog)
        self.EndTime.setGeometry(QtCore.QRect(280, 0, 131, 71))
        self.EndTime.setAutoFillBackground(False)
        self.EndTime.setStyleSheet(_fromUtf8("color:rgb(255, 0, 127)"))
        self.EndTime.setNumDigits(5)
        self.EndTime.setDigitCount(5)
        self.EndTime.setSegmentStyle(QtGui.QLCDNumber.Flat)
        self.EndTime.setProperty("value", 0.0)
        self.EndTime.setObjectName(_fromUtf8("EndTime"))
        self.label_5 = QtGui.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(80, 85, 71, 21))
        self.label_5.setStyleSheet(_fromUtf8("font: 12pt \"微软雅黑\";\n"
"color:rgb(85, 170, 0)"))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.LastHourEdit = QtGui.QSpinBox(Dialog)
        self.LastHourEdit.setGeometry(QtCore.QRect(150, 85, 41, 21))
        self.LastHourEdit.setObjectName(_fromUtf8("LastHourEdit"))
        self.LastHourEdit.setMaximum(23)
        self.LastHourEdit.setMinimum(0)        
        self.LastHourEdit.setWrapping(True)
        
        self.LastMinuteEdit = QtGui.QSpinBox(Dialog)
        self.LastMinuteEdit.setGeometry(QtCore.QRect(192, 85, 41, 21))
        self.LastMinuteEdit.setObjectName(_fromUtf8("LastHourEdit"))
        self.LastMinuteEdit.setMaximum(59)
        self.LastMinuteEdit.setMinimum(0)               
        self.LastMinuteEdit.setWrapping(True)
        
        self.CreateTask = QtGui.QPushButton(Dialog)
        self.CreateTask.setGeometry(QtCore.QRect(240, 80, 91, 28))
        self.CreateTask.setStyleSheet(_fromUtf8("font: 75 11pt \"微软雅黑\";\n"
"color:rgb(170, 0, 255)"))
        self.CreateTask.setObjectName(_fromUtf8("CreateTask"))

        self.retranslateUi(Dialog)

        QtCore.QMetaObject.connectSlotsByName(Dialog)


    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.label.setText(_translate("Dialog", "当前", None))
        self.label_2.setText(_translate("Dialog", "时间", None))
        self.label_3.setText(_translate("Dialog", "关机", None))
        self.label_4.setText(_translate("Dialog", "时间", None))
        self.label_5.setText(_translate("Dialog", "设定时间:", None))
        self.CreateTask.setText(_translate("Dialog", "确  认", None))


class MyFrame(QDialog,Ui_Dialog):
    def __init__(self,parent=None):
        super(MyFrame,self).__init__(parent)
        self.setupUi(self)
        self.init()
        self.connect(self.CreateTask,SIGNAL("clicked()"),self.createTask)


    def init(self):
        self.timerShow = QtCore.QTimer()
        self.timerShow.timeout.connect(self.showTime)
        self.timerShow.start(1000)

    def createTask(self):
        hours = int(self.LastHourEdit.text())
        minutes = int(self.LastMinuteEdit.text())
        self.ShutTimeHour = hours
        self.ShutTimeMinute = minutes

        time = QTime.currentTime()
        
        self.ShutTimeHour = (time.hour()+ hours)%24
        if minutes+time.minute()>=60:
            self.ShutTimeHour+=1
        self.ShutTimeMinute=(time.minute()+minutes)%60
        
        self.timerShutDown = QTimer()
        self.timerShutDown.timeout.connect(self.cycle)
        self.timerShutDown.start(1000)
        self.CreateTask.setEnabled(False)
        if self.ShutTimeHour>=10:
            strHour = str(self.ShutTimeHour)
        else:
            strHour = '0'+"%s"%self.ShutTimeHour

        if self.ShutTimeMinute>=10:
            strMinute = str(self.ShutTimeMinute)
        else:
            strMinute = '0'+"%s"%self.ShutTimeMinute        
        
        text = "%s:%s"%(strHour,strMinute  )
        self.EndTime.display("%s"%text)

    def cycle(self):
        timer = QTime.currentTime()
        if timer.hour()==self.ShutTimeHour and timer.minute()==self.ShutTimeMinute:
            self.timerShow.stop()
            self.timerShutDown.stop()
            #os.system('shutdown -s -f -t 1')
            handle=win32process.CreateProcess('C:\\Windows\\System32\\shutdown.exe',' /s',None,None,0,win32process.CREATE_NEW_CONSOLE , None , None ,win32process.STARTUPINFO())
            #print('shut down')

    def showTime(self):
        
        timer = QTime.currentTime()
        
        text = timer.toString('hh:mm')
        
        if timer.second() % 2 == 0:
            text = text[:2] + ' ' + text[3:]

        self.NowTime.display("%s"%text)

if __name__=="__main__":
    app=QApplication(sys.argv)  
    dialog=MyFrame()
    dialog.show()    
    app.exec_()       





































































