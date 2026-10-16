import sys
import shutil
import os
import signal
import faulthandler
faulthandler.enable()
import urllib.request
from PyQt6.QtCore import Qt, QProcess, QProcessEnvironment, QCommandLineOption, QCommandLineParser, QSettings, QStandardPaths
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
    QButtonGroup,
    QToolButton,
    QDialog,
    QDialogButtonBox,
)
os.environ["QT_LOGGING_RULES"] = "*.warning=false"
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        signal.signal(signal.SIGINT, signal.SIG_DFL)
        self.setting = QSettings()
        QIcon.setThemeName("breeze")
        self.urla = marg
        self.setObjectName("simpleytvideodownloader")
        self.setWindowTitle("Simple YT Video Downloader")
        self.xdgdatahomeee = QStandardPaths.writableLocation(QStandardPaths.StandardLocation.AppDataLocation)
        print(self.xdgdatahomeee)
        self.widget = QLineEdit()
        self.widget.setPlaceholderText("Enter your YouTube video URL")
        self.outputer = QTextEdit(self)
        self.outputer.setReadOnly(True)
        self.widget.returnPressed.connect(self.clickedy)
        layout = QVBoxLayout()
        layoutb = QHBoxLayout()
        label = QLabel("Simple YT Video Downloader")
        font = label.font()
        font.setPointSize(30)
        label.setFont(font)
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(label)
        layout.addWidget(self.outputer)
        self.baryy = QProgressBar()
        self.baryy.setRange(0, 1000)
        layout.addWidget(self.baryy)
        layoutb.addWidget(self.widget)
        self.button = QPushButton("Download", self)
        self.button.clicked.connect(self.clickedy)
        layoutb.addWidget(self.button)
        midget = QWidget()
        midget.setLayout(layoutb)
        layout.addWidget(midget)
        self.settingsb = QToolButton()
        self.settingsb.setText("Settings")
        self.settingsb.clicked.connect(self.opensetty)
        layout.addWidget(self.settingsb)
        fidget = QWidget()
        fidget.setLayout(layout)
        self.setCentralWidget(fidget)
        self.process = QProcess(self)
        env = QProcessEnvironment.systemEnvironment()
        pathy = self.xdgdatahomeee + ":" + env.value('PATH')
        env.insert("PATH", pathy)
        self.process.setProcessEnvironment(env)
        self.process.readyReadStandardOutput.connect(self.dod)
        self.process.finished.connect(self.donee)
        self.clickedydo()
    def dod(self):
        data = self.process.readAllStandardOutput().data().decode("utf-8", errors='ignore')
        self.fodd(data)
    def fodd(self, text):
        self.baryy.setValue(0)
        fink = text.replace("\r", "\n")
        for line in fink.splitlines():
            if "%" in line:
                try:
                    for word in line.split():
                        if "%" in word:
                            figad = word.replace("%", "").replace("[", "").replace("]", "")
                            floatynum = float(figad)
                            if 0.0 <= floatynum <= 100.0:
                                self.baryy.setFormat(str(floatynum) + "%")
                                self.baryy.setValue(int(floatynum * 10))
                                break
                except ValueError:
                    pass
        print(text)
        self.outputer.insertPlainText(text)
    def clickedy(self):
        print(self.widget.text())
        if self.process.state() == QProcess.ProcessState.Running:
            return
        self.installer()
        if os.path.exists(self.xdgdatahomeee + "/yt-dlp"):
            os.chmod(self.xdgdatahomeee + "/yt-dlp", 0o775)
        theresta = ["-oL", "-eL", "yt-dlp", "-P","~/Videos/"]
        if self.process.state() == QProcess.ProcessState.Running:
            return
        if self.setting.value("cap", False, type=bool):
            theresta.append("--embed-subs")
            theresta.append("--write-auto-subs")
            theresta.append("--sub-langs")
            theresta.append("en")
        if self.setting.value("marksponsor", False, type=bool):
            theresta.append("--sponsorblock-mark")
            theresta.append("sponsor")
        if self.setting.value("blocksponsor", False, type=bool):
            theresta.append("--sponsorblock-remove")
            theresta.append("sponsor")
        if self.setting.value("metdataa", False, type=bool):
            theresta.append("--embed-metadata")
        if self.setting.value("thummail", False, type=bool):
            theresta.append("--embed-thumbnail")
        theresta.append(self.widget.text())
        thingyy = "stdbuf"
        print(thingyy, theresta)
        self.process.start(thingyy, theresta)
    def clickedydo(self):
        if self.process.state() == QProcess.ProcessState.Running:
            return
        if self.urla:
            self.installer()
            if os.path.exists(self.xdgdatahomeee + "/yt-dlp"):
                    os.chmod(self.xdgdatahomeee + "/yt-dlp", 0o775)
            theresta = ["-oL", "-eL", "yt-dlp", "-P","~/Videos/"]
            if self.process.state() == QProcess.ProcessState.Running:
                return
            theresta.extend(self.urla)
            thingyy = "stdbuf"
            self.process.start(thingyy, theresta)
    def donee(self, exitcodde, exit_status):
        if exit_status == QProcess.ExitStatus.NormalExit:
            if exitcodde == 0:
                finga = QMessageBox.information(self, "Simple YT Video Downloader", "Done downloading! Exited with exit code " + str(exitcodde))
            else:
                finga = QMessageBox.warning(self, "Simple YT Video Downloader", "Uh oh! Something went wrong. Exit code " + str(exitcodde))
        else:
            finga = QMessageBox.critical(self, "Simple YT Video Downloader", "Ahhh! Something went very very wrong!")
    def installer(self):
        if os.path.exists(self.xdgdatahomeee + "/yt-dlp") == False:
            installd = QMessageBox.question(self, "Warning", "yt-dlp is not installed in this app yet. Select \"Yes\" if you want to install it.")
            if installd == QMessageBox.StandardButton.Yes:
                os.makedirs(self.xdgdatahomeee, exist_ok=True)
                with urllib.request.urlopen("https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp_linux") as fingabd:
                    with open(self.xdgdatahomeee + "/yt-dlp", "wb") as ytdlpfiley:
                        ytdlpfiley.write(fingabd.read())
    def opensetty(self):
        self.setty = QDialog(self)
        self.setty.setWindowTitle("Settings")
        layout = QVBoxLayout()
        self.cap = QCheckBox("Embed auto-generated english captions")
        self.cap.setChecked(self.setting.value("cap", False, type=bool))
        layout.addWidget(self.cap)
        self.sponsorygroup = QButtonGroup()
        self.sponsorygroup.setExclusive(True)
        sponsorstuff = ["Mark segments with sponsors with SponsorBlock", "Remove sponsors with SponsorBlock"]
        for stuffys in sponsorstuff:
            checkboxy = QCheckBox(stuffys)
            if stuffys == "Mark segments with sponsors with SponsorBlock":
                checkboxy.setChecked(self.setting.value("marksponsor", False, type=bool))
            else:
                checkboxy.setChecked(self.setting.value("blocksponsor", False, type=bool))
            layout.addWidget(checkboxy)
            self.sponsorygroup.addButton(checkboxy)
        self.metdataa = QCheckBox("Embed video metadata")
        self.metdataa.setChecked(self.setting.value("metdataa", False, type=bool))
        layout.addWidget(self.metdataa)
        self.thummail = QCheckBox("Embed video thumbmail")
        self.thummail.setChecked(self.setting.value("thummail", False, type=bool))
        layout.addWidget(self.thummail)
        self.updaterr = QPushButton()
        self.updaterr.setText(" Update yt-dlp to latest version")
        self.updaterr.setIcon(QIcon.fromTheme("system-software-update"))
        self.updaterr.clicked.connect(self.updatee)
        layout.addWidget(self.updaterr)
        yesno = QDialogButtonBox.StandardButton.Apply | QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel | QDialogButtonBox.StandardButton.Reset
        self.yesnoboxy = QDialogButtonBox(yesno)
        self.yesnoboxy.clicked.connect(self.sava)
        layout.addWidget(self.yesnoboxy)
        self.setty.setLayout(layout)
        self.setty.exec()
    def sava(self, buttony):
        whatbuton = self.yesnoboxy.standardButton(buttony)
        if whatbuton == QDialogButtonBox.StandardButton.Ok:
            self.setting.setValue("cap", self.cap.isChecked())
            self.setting.setValue("metdataa", self.metdataa.isChecked())
            self.setting.setValue("thummail", self.thummail.isChecked())
            if self.sponsorygroup.checkedButton():
                if self.sponsorygroup.checkedButton().text() == "Mark segments with sponsors with SponsorBlock":
                    self.setting.setValue("marksponsor", True)
                    self.setting.setValue("blocksponsor", False)
                else:
                    self.setting.setValue("blocksponsor", True)
                    self.setting.setValue("marksponsor", False)
            else:
                self.setting.setValue("marksponsor", False)
                self.setting.setValue("blocksponsor", False)
            self.setty.accept()
        elif whatbuton == QDialogButtonBox.StandardButton.Apply:
            self.setting.setValue("cap", self.cap.isChecked())
            self.setting.setValue("metdataa", self.metdataa.isChecked())
            self.setting.setValue("thummail", self.thummail.isChecked())
            if self.sponsorygroup.checkedButton():
                if self.sponsorygroup.checkedButton().text() == "Mark segments with sponsors with SponsorBlock":
                    self.setting.setValue("marksponsor", True)
                    self.setting.setValue("blocksponsor", False)
                else:
                    self.setting.setValue("blocksponsor", True)
                    self.setting.setValue("marksponsor", False)
            else:
                self.setting.setValue("marksponsor", False)
                self.setting.setValue("blocksponsor", False)
        elif whatbuton == QDialogButtonBox.StandardButton.Reset:
            self.setting.clear()
            self.setting.sync()
            self.setty.reject()
            self.opensetty()
        else:
            self.setty.reject()
    def updatee(self):
        if self.process.state() == QProcess.ProcessState.Running:
            return
        if os.path.exists(self.xdgdatahomeee + "/yt-dlp") == True:
            listea = ["-oL", "-eL", "yt-dlp", "-U"]
            thingyd = "stdbuf"
            self.process.start(thingyd, listea)
app = QApplication(sys.argv)
app.setOrganizationName("simpleytvideodownloader")
app.setApplicationName("simpleytvideodownloader")
app.setDesktopFileName("io.github.darrylland.simpleytvideodownloader")
app.setApplicationVersion("1.4.0")
app.setStyle("Breeze")
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
