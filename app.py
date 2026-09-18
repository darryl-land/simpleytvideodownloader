import sys
import shutil
import os
import signal
import faulthandler
faulthandler.enable()
from PyQt6.QtCore import Qt, QProcess, QProcessEnvironment, QCommandLineOption, QCommandLineParser, QTimer
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import (
    QApplication,
    QCheckBox,
    QLabel,
    QLineEdit,
    QMainWindow,
    QProgressBar,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QWidget,
    QTextEdit,
    QMessageBox,
)
os.environ["QT_LOGGING_RULES"] = "*.warning=false"
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        signal.signal(signal.SIGINT, signal.SIG_DFL)
        self.urla = marg
        self.setWindowTitle("Simple YT Video Downloader")
        self.widget = QLineEdit()
        self.widget.setPlaceholderText("Enter your YouTube video URL")
        self.outputer = QTextEdit(self)
        self.outputer.setReadOnly(True)
        self.widget.returnPressed.connect(self.entereda)
        layout = QVBoxLayout()
        layoutb = QHBoxLayout()
        label = QLabel("Simple YT Video Downloader")
        font = label.font()
        font.setPointSize(30)
        label.setFont(font)
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(label)
        layout.addWidget(self.outputer)
        layoutb.addWidget(self.widget)
        self.button = QPushButton("Download", self)
        self.button.clicked.connect(self.clickedy)
        layoutb.addWidget(self.button)
        midget = QWidget()
        midget.setLayout(layoutb)
        layout.addWidget(midget)
        self.cap = QCheckBox(text="Enable auto-generated english captions")
        layout.addWidget(self.cap)
        fidget = QWidget()
        fidget.setLayout(layout)
        self.setCentralWidget(fidget)
        self.process = QProcess(self)
        env = QProcessEnvironment.systemEnvironment()
        pathy = os.path.expanduser("~/.local/bin/") + ":" + env.value('PATH')
        env.insert("PATH", pathy)
        self.process.setProcessEnvironment(env)
        self.process.readyReadStandardOutput.connect(self.dod)
        self.process.finished.connect(self.donee)
        self.clickedydo()
        self.installer()
    def dod(self):
        data = self.process.readAllStandardOutput().data().decode(errors='ignore')
        self.fodd(data)
    def fodd(self, text):
        print(text)
        self.outputer.insertPlainText(text)
    def entereda(self):
        print("Return pressed!")
        print(self.widget.text())
        theresta = ["-oL", "-eL", "yt-dlp", "-P","~/Videos/"]
        if self.process.state() == QProcess.ProcessState.Running:
            return
        if self.cap.isChecked():
            theresta.append("--embed-subs")
            theresta.append("--write-auto-subs")
            theresta.append("--sub-langs")
            theresta.append("en")
            theresta.append(self.widget.text())
        else:
            theresta.append(self.widget.text())
        thingyy = "stdbuf"
        print(thingyy, theresta)
        self.process.start(thingyy, theresta)
    def clickedy(self):
        print(self.widget.text())
        if self.process.state() == QProcess.ProcessState.Running:
            return
        theresta = ["-oL", "-eL", "yt-dlp", "-P","~/Videos/"]
        if self.process.state() == QProcess.ProcessState.Running:
            return
        if self.cap.isChecked():
            theresta.append("--embed-subs")
            theresta.append("--write-auto-subs")
            theresta.append("--sub-langs")
            theresta.append("en")
            theresta.append(self.widget.text())
        else:
            theresta.append(self.widget.text())
        thingyy = "stdbuf"
        print(thingyy, theresta)
        self.process.start(thingyy, theresta)
    def clickedydo(self):
        print(self.urla)
        print(type(self.urla))
        if self.process.state() == QProcess.ProcessState.Running:
            return
        if self.urla:
            theresta = ["-oL", "-eL", "yt-dlp", "-P","~/Videos/"]
            if self.process.state() == QProcess.ProcessState.Running:
                return
            theresta.extend(self.urla)
            thingyy = "stdbuf"
            print(thingyy, theresta)
            self.process.start(thingyy, theresta)
    def donee(self, exitcodde, exit_status):
        if exit_status == QProcess.ExitStatus.NormalExit:
            if exitcodde == 0:
                finga = QMessageBox.information(self, "Simple YT Video Downloader", "Done downloading! Exited with exit code " + str(exitcodde))
                if os.path.exists(os.path.expanduser("~/.local/bin/yt-dlp")):
                    os.chmod(os.path.expanduser("~/.local/bin/yt-dlp"), 0o775)
            else:
                finga = QMessageBox.warning(self, "Simple YT Video Downloader", "Uh oh! Something went wrong. Exit code " + str(exitcodde))
        else:
            finga = QMessageBox.critical(self, "Simple YT Video Downloader", "Ahhh! Something went very very wrong!")
    def installer(self):
        if shutil.which("yt-dlp") is None:
            installd = QMessageBox.question(self, "Warning", "yt-dlp was not found on your system. Select \"Yes\" if you want to install it in your ~/.local/bin directory.")
            if installd == QMessageBox.StandardButton.Yes:
                os.makedirs(os.path.expanduser("~/.local/bin"), exist_ok=True)
                listee = ["-O", os.path.expanduser("~/.local/bin/yt-dlp"), "https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp_linux"]
                print("wget", listee)
                self.process.start("wget", listee)
app = QApplication(sys.argv)
app.setApplicationName("Simple YT Video Downloader")
app.setApplicationVersion("1.2.0")
app.setStyle("Fusion") # just here for the time being until i put a theme
parser = QCommandLineParser()
parser.setApplicationDescription("Another very very very simple and easy to use PyQt6 video downloader app that uses yt-dlp")
parser.addHelpOption()
parser.addVersionOption()
parser.addPositionalArgument("url", "URLs to download", "[URL]")
parser.process(app)
app.setWindowIcon(QIcon("unnamed.png"))
global marg
marg = parser.positionalArguments()
window = MainWindow()
window.show()
app.exec()
