from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *
import os, sys,  time
import set_up_fr, client_gui, read_data

class WebBrowser(QMainWindow):
    def __init__(self):
        super(WebBrowser, self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('https://www.google.com'))
        self.setCentralWidget(self.browser)
        self.showMaximized()

        navbar = QToolBar()
        navbar.adjustSize()
        self.addToolBar(navbar)

        back_btn = QAction('⮜', self)
        back_btn.triggered.connect(self.browser.back)
        navbar.addAction(back_btn)

        forward_btn = QAction('⮞', self)
        forward_btn.triggered.connect(self.browser.forward)
        navbar.addAction(forward_btn)

        reload_btn = QAction('⟳', self)
        reload_btn.triggered.connect(self.browser.reload)
        navbar.addAction(reload_btn)

        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.open_url)
        navbar.addWidget(self.url_bar)
        self.browser.urlChanged.connect(self.update_url)

    def open_url(self):
        url = self.url_bar.text()
        self.browser.setUrl(QUrl(url))
        
    def update_url(self, q):
        self.url_bar.setText(q.toString())

class Worker(QThread):
    update_signal = pyqtSignal(str)

    def __init__(self, web_browser):
        super(Worker, self).__init__()
        self.web_browser = web_browser

    def run(self):
        set_up_fr.get_key()
        while True:
            try:
                read_data.read_data()
                if os.path.isfile("env_secure.json"):
                    client_gui.exec()
                    time.sleep(1)
                else:
                    time.sleep(1)
            except:
                pass

class MyApp(QMainWindow):
    def __init__(self):
        super(MyApp, self).__init__()

        self.web_browser = WebBrowser()

        self.worker_thread = Worker(self.web_browser)
        self.worker_thread.update_signal.connect(self.update_ui)
        self.worker_thread.start()

    def update_ui(self, data):
        print(data)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    QApplication.setApplicationName("VITALINK")

    my_app = MyApp()

    my_app.web_browser.show()

    sys.exit(app.exec_())
