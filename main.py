from PyQt5.QtWidgets import *
from main_gui import Ui_HesapMakinesi

class main(QMainWindow):
    def __init__(self) -> None:  #? Burayı anlamadın git araştır
        super().__init__()
        self.gui = Ui_HesapMakinesi()
        self.gui.setupUi(self)
        self.gui.pushButton_7.clicked.connect(self.b)
    def b(self):
        A = 1



app = QApplication([])
pencere = main()
pencere.show()
app.exec_()


