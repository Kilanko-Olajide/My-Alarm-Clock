import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import QTimer, QTime, Qt


class clock(QWidget):
    def __init__(self):
        super().__init__()
        self.label = QLabel( self)
        self.timer = QTimer(self)
        self.initUI()
         

    def initUI(self):
        self.setWindowTitle("Clock")
        self.setGeometry(650, 400, 350, 150)
        

        vbox = QVBoxLayout()
        vbox.addWidget(self.label)

        self.setLayout(vbox)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setStyleSheet("font-size: 150px;"
                                "font-family: Ariel;"
                                 "color: red;" )
        self.setStyleSheet("background-color: black;")

        self.timer.timeout.connect(self.correct_time)
        self.timer.start(1000)
        self.correct_time()


    def correct_time(self):
        current_time = QTime.currentTime().toString("hh:mm:ss AP")
        self.label.setText(current_time)
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    clock = clock()
    clock.show()
    sys.exit(app.exec_())
