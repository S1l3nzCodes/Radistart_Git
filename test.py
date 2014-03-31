import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtWebKit import *

app = QApplication(sys.argv)
web = QWebView()
web.settings().setAttribute(QWebSettings.PluginsEnabled, True)
web.show()
web.load(QUrl('http://192.168.2.200/RVP')) # Change path to actual file.
sys.exit(app.exec_())
