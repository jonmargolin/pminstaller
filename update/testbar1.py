
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys
from woocommerce import API
import json
from threading import Thread
import  threading
from contextlib import closing
import requests
from Queue import Queue
import zipfile
import getpass
import os
class Worker(threading.Thread):

    def __init__(self, queue):
        self.__queue = queue

        threading.Thread.__init__(self)
    def zip(self,file,file_path):

       with zipfile.ZipFile(file, "r") as z:
            z.extractall("C:\\Users\\"+file_path)
            z.close()
            os.remove(file)


class start(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.wcapi = API(
            url="http://psdev.pskiss.com",
            consumer_key="ck_fc533175c1e0817a29f0f6879366b0c8c62bf19b",
            consumer_secret="cs_cdbbe45f3b87940e11991dcd632da402a9308d10",
            timeout=30,



        )
        if hasattr(sys, '_MEIPASS'):
             palette = QPalette()
             palette.setBrush(QPalette.Background,QBrush(QPixmap(os.path.join(sys._MEIPASS,"Installer.png"))))
             self.setAutoFillBackground(True)
             self.setPalette(palette)
             self._filenewIcon = QIcon(QPixmap(os.path.join(sys._MEIPASS,"pmlogo.jpg")))
             css_path = os.path.join(sys._MEIPASS, "style.css")
             with open(css_path,"r") as fh:
               self.setStyleSheet(fh.read())
        else:
         self._filenewIcon = QIcon(QPixmap("pmlogo.jpg"))
         palette = QPalette()
         palette.setBrush(QPalette.Background,QBrush(QPixmap("Installer.png")))
         self.setAutoFillBackground(False)
         self.setPalette(palette)
         sshFile="style.css"
         sub="resource"
         with open(sshFile,"r") as fh:
           self.setStyleSheet(fh.read())
        self.setWindowTitle("Presets Mentor Installer")
        self.setWindowIcon(self._filenewIcon)
        self.layout = QGridLayout()
        self.text=QLabel()

        QDialog.setFixedSize(self,800,600)
        self.thread_count = threading.active_count()
        self.threads = []
        self.msg_queue = Queue()
        self.settext()
        self.button2 = QPushButton("submit")
        self.group_box = QGroupBox()
        moods = [QCheckBox("Canon"),QCheckBox("Nikon"), QCheckBox("Sony"),QCheckBox("Other")]
        #self.group_box.setCheckable(True)
        self.chk_vlayout = QVBoxLayout()
        self.mood_button_group = []
        for i in xrange(len(moods)):
            # Add each radio button to the button layout
         self.chk_vlayout.addWidget(moods[i])
         self.mood_button_group.append(moods[i])
            # Add each radio button to the button group & give it an ID of i
         #self.mood_button_group.addButton(moods[i])
        self.button2.setFixedWidth(180)
        #self.chk_vlayout.addWidget(self.button2)
        self.group_box.setLayout(self.chk_vlayout)
        self.group_box.setFixedWidth(200)
        self.group_box.setStyleSheet("border:0; padding-left:10px; font-size:18px;")
        self.layout.setAlignment(self.group_box,Qt.AlignRight)
        self.setLayout(self.layout)
        self.progress = QProgressBar(self)
        self.progress.setGeometry(260, 385, 280, 20)
        self.progress.hide()
        self.setFocus()

    def setback(self,img):
         if hasattr(sys, '_MEIPASS'):
             palette = QPalette()
             palette.setBrush(QPalette.Background,QBrush(QPixmap(os.path.join(sys._MEIPASS,img))))
             self.setAutoFillBackground(True)
             self.setPalette(palette)
         else:
            palette = QPalette()
            palette.setBrush(QPalette.Background,QBrush(QPixmap(img)))
            self.setAutoFillBackground(False)
            self.setPalette(palette)

    def settext(self):
        self.button = QPushButton("Next")
        self.button.setMaximumSize(180,180)
        self.button.setMinimumSize(150,30)
        self.layout.addWidget(self.button,0,1)
        self.setContentsMargins(100,100,100,100)
        self.button.clicked.connect(self.setOrderId)
        self.layout.setAlignment(self.button, Qt.AlignBottom)


    def setOrderId(self):
        self.setback("Installer2.png")
        self.button.hide()
        #self.btn1=QGroupBox()
        #self.btnc=QVBoxLayout()
        self.line_edit = QLineEdit()
        self.line_edit.setFixedHeight(30)
        self.line_edit.setFixedWidth(180)
        self.button1 = QPushButton("submit")
        self.line_edit.setFocus()
        self.button1.clicked.connect(self.get_order_id)
        self.button1.setFixedHeight(30)
        self.layout.addWidget(self.line_edit,1,1)
        self.layout.addWidget(self.button1,2,1)
        self.setContentsMargins(100,340,100,180)

    def  get_order_id(self):
        self.order_id=self.line_edit.text()
        try:
         j = (self.wcapi.get("orders/" +self.order_id+"?filter[meta]=true").json())
         if j[u'order'][u'status'] == "completed":
          #if d < 3 :
          d=j[u'order'][u'order_meta'][u'number']
          self.x= int(float(d))
          if self.x < 100 :
           self.line_edit.hide()
           self.button1.hide()
         #self.label.setText("")
           self.setback("Installer3.png")
           self.layout.addWidget(self.group_box,1,0)
           self.button2.setFixedWidth(150)
           self.button2.setFixedHeight(30)
           self.layout.addWidget(self.button2,1 ,1 )
           self.setContentsMargins(200,400,350,50)
           self.layout.setAlignment(self.button2,Qt.AlignBottom)
           self.button2.clicked.connect(self.setcamType)
          else:
           self.setback("Installer6.png")
           self.text.setText("<a href='mailto:info@presetmentor.com'>info@presetmentor.com</a>")
           self.text.setOpenExternalLinks(True)
           self.layout.addWidget(self.text,0,1)

           self.setContentsMargins(90,350,90,70)
           self.button1.setFixedWidth(180)
           self.layout.setAlignment(self.button1,Qt.AlignJustify)
           self.layout.setAlignment(self.line_edit,Qt.AlignJustify)
           self.text.setStyleSheet("font-size:35px;margin-right: 80px;font-family: Open sans-serif;")
        except:
         self.setback("Installer6.png")
         self.setContentsMargins(100,400,100,100)

    def setcamType(self):
     self.group_box.hide()
     self.button2.hide()
     self.text.hide()
     self.setback("Installer4.png")
     came = []
     for i in range(0,4):
           if self.mood_button_group[i].isChecked():
            typecam= str(self.mood_button_group[i].text())
            came.append(typecam)
     self.http_call(came)
     self.last_scren()
    def http_call(self,cam):
     self.progress.show()
     input_file = "http://psdev.pskiss.com/wp-content/installer/installer_path.json"
     f = requests.get(input_file, auth=('test', 'test1234'))
     f.close()
     text = f.text
     obj=[]
     tj =  list(json.loads(text))
     self.username = getpass.getuser()
     for c in cam:
         c=c+".zip"
         tj.append({ 'url':'http://psdev.pskiss.com//wp-content/installer/CameraRaw/CameraProfiles/'+c,'file':c,'path':"AppData\\Roaming\\Adobe\\CameraRaw\\CameraProfiles"})
     for url in tj:

            #thread_count = threading.active_count()
            clean_url = url[u'url']
            file_path = self.username+"\\"+url[u'path']
            short_url = '/'.join(clean_url.split('/')[:-1])
            local_name = url[u'file']
            self.download(clean_url,local_name,file_path)
            self.progress.reset()
            self.progress.deleteLater()

    def download(self, url, local_name,file_path):
     s = requests.session()
     s.close()
     #s.keep_alive = False
     self.completed = 0
     self.progress.setValue(0)
     try:
       with closing(s.get(url,auth=('test', 'test1234'),stream=True))as response:
        if  response.ok:
            response.raise_for_status()
            total_size = int(response.headers.get('content-length', 0));
            self.progress.setMaximum(total_size)
           # msg_queue.put(lambda: HelloApp.on_startPb(self.p,total_size))
            local_file =open(local_name, 'wb')
            for chunk in response.iter_content(chunk_size=400024):

                    if chunk:
                     QCoreApplication.processEvents()
                     local_file.write(chunk)
                     self.completed += 400024
                     self.progress.setValue(self.completed)

            w=Worker(Queue)
            work=Thread(target=Worker.zip,args=(w,),kwargs={'file':local_name,'file_path':file_path}, name='zip')
            work.setDaemon(True)
            work.start()
     except requests.exceptions.HTTPError as err:
         self.setback("Installer6.png")

    def on__startbar(self,total):

        self.progress.setValue(0)
        self.progress.setMaximum(total)
    def on_download_complete(self,url, file_name):
        print ("complited "+file_name)

        self.lock.release()
    def on__updatabar(self):
          self.completed += 1024
          self.progress.setValue(self.completed)
    def last_scren(self):
        self.x=self.x+1

        data={"order": {
        "order_meta": {"number":self.x}
                   }}
        self.wcapi.put("orders/" +self.order_id+"?filter[meta]=true",data).json()
        #self.group_box.hide()
        #self.button2.hide()
        self.progress.hide()
        self.setback("Installer5.png")
        self.text5=QLabel('<a href="https://www.youtube.com/watch?v=sLV8cqTGECE">Click Here To Watch our Tutorial</a>')
        self.text5.setOpenExternalLinks(True)
        self.layout.addWidget(self.text5)
        self.setContentsMargins(30,400,100,80)
        self.layout.setAlignment(self.text5,Qt.AlignCenter)

app = QApplication(sys.argv)
dialog = start()
dialog.show()
app.exec_()

