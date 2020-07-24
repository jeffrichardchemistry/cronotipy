from cronotipy.cronotipy_ui import Ui_cronotipy_mw
#from cronotipy_ui import Ui_cronotipy_mw
import sys
from PyQt5.QtWidgets import (QLineEdit ,QLabel, QMainWindow, QDialog, QApplication,
                             QListWidget, QPushButton, QWidget, QVBoxLayout, QHBoxLayout,
                             QAbstractItemView, QFormLayout, QGridLayout, QSpinBox, QProgressBar,
                             QMessageBox)
from PyQt5.QtCore import Qt, QRect, QSize, QTimer
from PyQt5.QtGui import QFont, QGuiApplication, QIcon
from PyQt5 import QtCore
from PyQt5.QtTest import QTest
import subprocess
import os
import gi
gi.require_version('Notify', '0.7')
from gi.repository import Notify

Notify.init('Cronotipy')

ABSOLUT_PATH = os.path.dirname(os.path.realpath(__file__))

path_sound_notify = ABSOLUT_PATH+'/sounds/alert.wav'
path_logo = ABSOLUT_PATH+'/figs/logo.png'

class cronotipy(QMainWindow, QDialog):
    def __init__(self):
        super(cronotipy, self).__init__()

        # Get Window attributes from ui file
        self.cronotipy_ui = Ui_cronotipy_mw()
        self.cronotipy_ui.setupUi(self)
        self.setWindowIcon(QIcon(path_logo))

        cronotipy.initUI(self) #Another init, this makes code clean     

        self.title_and_time = {}  #get titles names and yours respectively time
        self.titles_typed = [] 

        self.unfreeze = QGuiApplication.processEvents #unfreeze

        self.startcronotipy = True #bool to while in start (start/stop)
        self.isOnOff_Notify = True #state of notify checkable menu
        self.isOnOff_Sound = True #state of sound checkable menu
        self.isOnOff_loop = False
        
    def initUI(self):

        #Create the QListWidget
        self.listwd = QListWidget()        
        self.listwd.setSelectionMode(QAbstractItemView.ExtendedSelection) #This Method enable ctrl and click selection
        self.listwd.doubleClicked.connect(self.renameActualize)

        #Buttons
        self.cronotipy_ui.btn_create.clicked.connect(self.addLines)
        self.cronotipy_ui.btn_create.setStyleSheet(style_buttons)
        self.cronotipy_ui.btn_remove.clicked.connect(self.removeLines)
        self.cronotipy_ui.btn_remove.setStyleSheet(style_buttons)
        self.btn_start = QPushButton('Start')
        self.btn_start.setStyleSheet(style_buttons)
        self.btn_stop = QPushButton('Stop')
        self.btn_stop.setStyleSheet(style_buttons)
        self.btn_start.clicked.connect(self.start)
        self.btn_stop.clicked.connect(self.stop)

        #Create widget inside QDockWidget
        self.dock = cronotipy.createDockwidget(self)   
        self.dock.layout().addWidget(self.cronotipy_ui.btn_create, alignment = Qt.AlignCenter) #align button
        self.dock.layout().addWidget(self.cronotipy_ui.btn_remove, alignment = Qt.AlignCenter) #align button
        self.dock.layout().addWidget(self.btn_start, alignment = Qt.AlignCenter)
        self.dock.layout().addWidget(self.btn_stop, alignment = Qt.AlignCenter)
        self.dock.layout().addWidget(self.listwd) #QList stay below buttons

        #QScrollBar
        self.vbox_top = QFormLayout() #vbox, but the true is formbox lol
        self.cronotipy_ui.scrollAWD_top.setLayout(self.vbox_top)#put the vbox layout inside scrollbars widget
        self.cronotipy_ui.scrollA_top.setStyleSheet(style_scrollbar)
        self.vbox_bot = QFormLayout()
        self.cronotipy_ui.scrollAWD_bot.setLayout(self.vbox_bot)#put the vbox layout inside scrollbars widget
        self.cronotipy_ui.scrollA_bot.setStyleSheet(style_scrollbar)

        #MenuBar
        self.cronotipy_ui.menu_Notify_On_Off.triggered.connect(self.turnOnOffnotify)
        self.cronotipy_ui.menu_Sound_On_Off.triggered.connect(self.turnOnOffsound)
        self.cronotipy_ui.menu_Loop_On_Off.triggered.connect(self.turnOnOffloop)
        self.cronotipy_ui.menu_Quit.triggered.connect(self.quitMenu)



    def createDockwidget(self):
        #create widget Inside QDock
        self.layoutdock = QVBoxLayout()
        self.dockedwidget = QWidget()
        
        self.cronotipy_ui.dockwd.setWidget(self.dockedwidget)   
        self.cronotipy_ui.dockwd.setStyleSheet(style)     #change appearance
        self.dockedwidget.setLayout(self.layoutdock)
        
        return self.dockedwidget


    def start(self):
        self.startcronotipy = True

        get_titles = [self.listwd.item(item).text() for item in range(self.listwd.count())]
        title_message = {}

        for title in get_titles:
            title_message[title] = self.findChild(QLineEdit, title).text()
            #timeinseconds = cronotipy.time2seconds(self, self.title_and_time[title])
            #print(timeinseconds)
        
        seconds_title = {}
        cnt = 0
        cnt_finish = 0
        while self.startcronotipy:#start counts
            cnt += 1
            try: #try for when to delete the title at the time of counting
                for i, title in enumerate(get_titles):
                    time = cronotipy.time2seconds(self, self.title_and_time[title])#calc time in seconds

                    if cnt == 1: #get dictionary just in first iteration
                        seconds_title[time] = title

                    self.findChild(QProgressBar, get_titles[i]).setMaximum(time)#set max value of progbar
                    self.findChild(QProgressBar, get_titles[i]).setTextVisible(True)
                    self.findChild(QProgressBar, get_titles[i]).setValue(cnt)#change value of progbar
            except KeyError:
                #QUANDO DELETAMOS UM TITULO ENQUANTO A CONTAGEM TA ROLANDO DA ESSE KEYERROR
                #ESSE TRY RESOLVE ISSO, MAS PRECISO TIRAR ESSE TITULO DO DICIONARIO PARA NAO APARECER NOTIFICAÇÃO
                pass
            
            if cnt in seconds_title.keys(): #when cnt pass through time
                if self.isOnOff_Notify:
                    Notify.Notification.new(seconds_title[cnt], title_message[seconds_title[cnt]], path_logo).show()
                
                if self.isOnOff_Sound:
                    subprocess.run('play {} &'.format(path_sound_notify), shell=True)

                cnt_finish += 1

            elif cnt_finish == len(seconds_title): #when the last notify finish
                self.startcronotipy = False
                if self.isOnOff_Notify:
                    Notify.Notification.new('Done!', 'All notifications are over.', path_logo).show()
                

            QTest.qWait(1000)
        #loop
        if self.isOnOff_loop:
            cronotipy.start(self)
    
    def stop(self):
        self.startcronotipy = False
        self.isOnOff_loop = False

    def renameActualize(self):
        #cronotipy.actualizeEditables(self)
        dialog = AddNotifiy()
        dialog.setWindowTitle('Titles Rename')
        dialog.setStyleSheet("background-color: rgba(84, 84, 84, 0.5);")
        state = dialog.exec_()
        
        time = [dialog.spinbox_hours.value(), dialog.spinbox_minutes.value(), dialog.spinbox_seconds.value()]
        
        get_title = dialog.edit.text() #get the typed
        #get_title = cronotipy._testTitle(self, title=get_title)

        if get_title == '' or state == 0:
            pass
        else:
            cronotipy.removeLines(self)
            self.listwd.addItem(get_title) #add a item in QList "title - left"
            cronotipy.addText2ScrollBar(self, title=get_title)  #add a QLine in QScroll "message - right"
            cronotipy.addProgressbar2ScrollBar(self, title=get_title, time=time) #add a QProgressBar in QSCROLL bot

            self.title_and_time[get_title] = time #update title and time in dictionary
          
    def addLines(self):
        get = AddNotifiy() #instancing dialog
        get.setWindowTitle('Add a notifier')
        get.setStyleSheet("background-color: rgba(84, 84, 84, 0.5);")
        state = get.exec_() # show dialog
                
        #get time from spinboxes
        time = [get.spinbox_hours.value(), get.spinbox_minutes.value(), get.spinbox_seconds.value()]
        get_title = get.edit.text() #get the typed
        self.titles_typed.append(get_title) #store titles to check equal titles

        get_title = cronotipy._testTitle(self, title=get_title)

        if get_title == '' or state == 0:
            pass
        else:
            self.listwd.addItem(get_title) #add a item in QList "title - left"
            cronotipy.addText2ScrollBar(self, title=get_title)  #add a QLine in QScroll "message - right"
            cronotipy.addProgressbar2ScrollBar(self, title=get_title, time=time) #add a QProgressBar in QSCROLL bot

            self.title_and_time[get_title] = time
                     
    def removeLines(self):
        getselected = self.listwd.selectedItems() #take the selected items

        for i in getselected:
            item2remove = self.listwd.takeItem(self.listwd.row(i)).text() #str, name of object selected is the same name of QLine ObjectName
            #child = self.findChild(QLineEdit, item2remove.text()).objectName() #this lines returns the objectName of QLine
            child = self.findChild(QLineEdit, item2remove).deleteLater() #remove the QLine with objectname "item2remove"
            self.findChild(QProgressBar, item2remove).deleteLater()
            self.findChild(QLabel, item2remove).deleteLater()
            try: #this is for rename and next remove item
                self.titles_typed.remove(item2remove)
            except:
                pass
            self.title_and_time.pop(item2remove)

    def addText2ScrollBar(self, title):
        #Add QLine in TOP SCROLLBAR           
        line = QLineEdit(self)
        line.setPlaceholderText('Type a message for {}'.format(title))
        line.setObjectName(title)

        self.vbox_top.addWidget(line) #put line object inside vbox
    
    def addProgressbar2ScrollBar(self, title, time =[]):
        #Add progressbar in BOT SCROLLBAR
        progressbar = QProgressBar(self)
        progressbar.setObjectName(title)
        progressbar.setValue(100)
        progressbar.setTextVisible(False)
        progressbar.setStyleSheet(style_progbar)

        progresslabel = QLabel(title + '  ({:02d}:{:02d}:{:02d}):'.format(time[0], time[1], time[2]))
        progresslabel.setObjectName(title)

        self.vbox_bot.addRow(progresslabel, progressbar)

    def time2seconds(self, time = []):
        hour2seconds = time[0]*3600
        min2seconds = time[1]*60
        seconds = time[2]*1
        return hour2seconds+min2seconds+seconds

    def turnOnOffnotify(self):
        if self.cronotipy_ui.menu_Notify_On_Off.isChecked():
            self.isOnOff_Notify = True
        
        if not self.cronotipy_ui.menu_Notify_On_Off.isChecked():
            self.isOnOff_Notify = False
            
    def turnOnOffsound(self):
        if self.cronotipy_ui.menu_Sound_On_Off.isChecked():
            self.isOnOff_Sound = True
        
        if not self.cronotipy_ui.menu_Sound_On_Off.isChecked():
            self.isOnOff_Sound = False
    
    def turnOnOffloop(self):
        if self.cronotipy_ui.menu_Loop_On_Off.isChecked():
            self.isOnOff_loop = True
            
        
        if not self.cronotipy_ui.menu_Loop_On_Off.isChecked():
            self.isOnOff_loop = False

        print(self.cronotipy_ui.menu_Loop_On_Off.isChecked())

    def quitMenu(self):
        cronotipy.stop(self)
        self.close()

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Closing Window', 'Do you really want to close this application?',
                                    QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            cronotipy.stop(self)
            event.accept()
        
        else:
            event.ignore()

    def _testTitle(self, title):
        n_titles_contained = self.titles_typed.count(title) #number of times that title appears

        if n_titles_contained == 1:
            return title
        elif title in self.titles_typed:
            self.titles_typed.append(title+'{}'.format(n_titles_contained))
            return title+'{}'.format(n_titles_contained)

#Custom Dialog to add a title and rename
class AddNotifiy(QDialog):
    def __init__(self):
        super().__init__()
        
        self.labeltitle = QLabel('Title:')
        self.labeltitle.setStyleSheet("background-color: rgba(84, 84, 84, 0.0);")
        self.edit = QLineEdit()
        self.edit.setPlaceholderText('Title for notification.')
        self.edit.setStyleSheet("background-color: rgba(84, 84, 84, 0.4);")
        self.edit.selectAll()

        self.timelabel = QLabel('Time')
        self.timelabel.setStyleSheet("background-color: rgba(84, 84, 84, 0.0);")
        self.timelabel.setAlignment(Qt.AlignCenter)

        self.button = QPushButton('OK')
        self.button.clicked.connect(self.accept)

        self.labelspin_hours = QLabel('Hours:')
        self.labelspin_hours.setStyleSheet("background-color: rgba(84, 84, 84, 0.0);")
        self.spinbox_hours = QSpinBox()
        
        self.labelspin_minutes = QLabel('Minutes:')
        self.labelspin_minutes.setStyleSheet("background-color: rgba(84, 84, 84, 0.0);")
        self.spinbox_minutes = QSpinBox()

        self.labelspin_seconds = QLabel('Seconds:')        
        self.labelspin_seconds.setStyleSheet("background-color: rgba(84, 84, 84, 0.0);")
        self.spinbox_seconds = QSpinBox()
        
        #layout = QVBoxLayout()
        layout = QFormLayout()
        layout.addRow(self.labeltitle, self.edit)
        layout.addWidget(self.timelabel)
        layout.addRow(self.labelspin_hours,self.spinbox_hours)
        layout.addRow(self.labelspin_minutes, self.spinbox_minutes)
        layout.addRow(self.labelspin_seconds, self.spinbox_seconds)
        layout.addWidget(self.button)

        self.setLayout(layout)

style = "color: rgb(255, 255, 255); \
         background-color: rgba(84, 84, 84, 0.4);"

style_scrollbar = "color: rgb(255, 255, 255); \
                   background-color: rgba(84, 84, 84, 0.0);"

style_buttons = "color: rgb(255, 255, 255); \
                   background-color: rgba(84, 84, 84, 0.4);"

style_progbar = """
            QProgressBar{
                border: 2px solid grey;
                border-radius: 5px;
                text-align: center
            }

            QProgressBar::chunk {
                background-color: #8f8f91;
                margin: 0.5px;
            }
            """

    #Update Items as a editable, i'm not using this function    
    #def actualizeEditables(self):
    #    for index in range(self.listwd.count()):
    #        item = self.listwd.item(index)
    #        item.setFlags(item.flags() | Qt.ItemIsEditable)  
def runGUI():
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    gui = cronotipy()
    gui.show()   
    
    sys.exit(app.exec_())

""" if __name__ == '__main__':
    runGUI() """

        
