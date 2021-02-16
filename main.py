from PyQt5 import QtCore, QtGui, QtWidgets
from predict_form import Ui_predict_form
from housesales import House

H = House()

class Ui_MainWindow(object):
    
    def show_graph(self):

        if self.graph_name == "bedrooms":
            H.bedrooms()

        elif self.graph_name == "floors":
            H.floors()    

        elif self.graph_name == "sqft_living":
            H.price_square_feet()

        elif self.graph_name == "long":
            H.longitude_price()

        elif self.graph_name == "lat":
            H.latitude_price()

        elif self.graph_name == "bedrooms_price":
            H.bedrooms_price()

        elif self.graph_name == "waterfront_price":
            H.waterfront_price()

        elif self.graph_name == "floors_price":
            H.floors_price()

        elif self.graph_name == "zipcode_price":
            H.zipcode_price()



    def bedroom_menu(self):
        self.title_lbl.setText("House - Bedrooms")
        self.graph_name = "bedrooms"
        self.groupBox.setEnabled(True)
    

    def floors_menu(self):
        self.title_lbl.setText("House - Floors")
        self.graph_name = "floors"
        self.groupBox.setEnabled(True)

    def per_square_feet_menu(self):
        self.title_lbl.setText("Price - Area")
        self.graph_name = "sqft_living"
        self.groupBox.setEnabled(False)

    def longitude_price(self):
        self.title_lbl.setText("Price - Longitude")
        self.graph_name = "long"
        self.groupBox.setEnabled(False)

    def latitude_price(self):
        self.title_lbl.setText("Price - latitude")
        self.graph_name = "lat"
        self.groupBox.setEnabled(False)


    def bedrooms_price(self):
        self.title_lbl.setText("Price - bedrooms")
        self.graph_name = "bedrooms_price"
        self.groupBox.setEnabled(False)

    def waterfront_price(self):
        self.title_lbl.setText("Price - waterfront")
        self.graph_name = "waterfront_price"
        self.groupBox.setEnabled(False)

    def floors_price(self):
        self.title_lbl.setText("Price - floors")
        self.graph_name = "floors_price"
        self.groupBox.setEnabled(False)

    def zipcode_price(self):
        self.title_lbl.setText("Price - zipcode")
        self.graph_name = "zipcode_price"
        self.groupBox.setEnabled(False)

    def find_value(self):
        value = self.inputValue.text()
        print(self.graph_name)
        count = H.find_values(self.graph_name, value)
        self.answer.setText(str(count))

    def openPredictWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_predict_form()
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self, MainWindow):

        self.graph_name = "bedrooms"
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(657, 375)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(50, 90, 391, 221))
        self.groupBox.setObjectName("groupBox")
        self.widget = QtWidgets.QWidget(self.groupBox)
        self.widget.setGeometry(QtCore.QRect(30, 30, 271, 161))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.inputValue = QtWidgets.QLineEdit(self.widget)
        self.inputValue.setObjectName("inputValue")
        self.gridLayout.addWidget(self.inputValue, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.Find_btn = QtWidgets.QPushButton(self.widget)
        self.Find_btn.setObjectName("Find_btn")
        self.gridLayout.addWidget(self.Find_btn, 1, 1, 1, 1)
        self.answer = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.answer.setFont(font)
        self.answer.setAlignment(QtCore.Qt.AlignCenter)
        self.answer.setObjectName("answer")
        self.gridLayout.addWidget(self.answer, 2, 1, 1, 1)
        self.show_graph_btn = QtWidgets.QPushButton(self.centralwidget)
        self.show_graph_btn.setGeometry(QtCore.QRect(470, 110, 171, 61))
        self.show_graph_btn.setObjectName("show_graph_btn")
        self.title_lbl = QtWidgets.QLabel(self.centralwidget)
        self.title_lbl.setGeometry(QtCore.QRect(50, 10, 561, 71))
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.title_lbl.setFont(font)
        self.title_lbl.setObjectName("title_lbl")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 657, 26))
        self.menuBar.setObjectName("menuBar")
        self.menuPrice = QtWidgets.QMenu(self.menuBar)
        self.menuPrice.setObjectName("menuPrice")
        self.menuGeography = QtWidgets.QMenu(self.menuBar)
        self.menuGeography.setObjectName("menuGeography")
        self.menuPrice_2 = QtWidgets.QMenu(self.menuBar)
        self.menuPrice_2.setObjectName("menuPrice_2")
        MainWindow.setMenuBar(self.menuBar)
        self.actionPrice = QtWidgets.QAction(MainWindow)
        self.actionPrice.setObjectName("actionPrice")
        self.actionBedrooms = QtWidgets.QAction(MainWindow)
        self.actionBedrooms.setObjectName("actionBedrooms")
        self.actionFloors = QtWidgets.QAction(MainWindow)
        self.actionFloors.setObjectName("actionFloors")
        self.actionPer_Square_Feet = QtWidgets.QAction(MainWindow)
        self.actionPer_Square_Feet.setObjectName("actionPer_Square_Feet")
        self.actionLocation = QtWidgets.QAction(MainWindow)
        self.actionLocation.setObjectName("actionLocation")
        self.actionLatitude = QtWidgets.QAction(MainWindow)
        self.actionLatitude.setObjectName("actionLatitude")
        self.actionBeedrooms = QtWidgets.QAction(MainWindow)
        self.actionBeedrooms.setObjectName("actionBeedrooms")
        self.actionWaterFront = QtWidgets.QAction(MainWindow)
        self.actionWaterFront.setObjectName("actionWaterFront")
        self.actionFloors_2 = QtWidgets.QAction(MainWindow)
        self.actionFloors_2.setObjectName("actionFloors_2")
        self.actionZipcode = QtWidgets.QAction(MainWindow)
        self.actionZipcode.setObjectName("actionZipcode")
        self.actionShow_Graph = QtWidgets.QAction(MainWindow)
        self.actionShow_Graph.setObjectName("actionShow_Graph")
        self.actionPredict = QtWidgets.QAction(MainWindow)
        self.actionPredict.setObjectName("Predict")
        self.menuPrice.addAction(self.actionBedrooms)
        self.menuPrice.addAction(self.actionFloors)
        self.menuGeography.addAction(self.actionShow_Graph)
        self.menuPrice_2.addAction(self.actionPer_Square_Feet)
        self.menuPrice_2.addAction(self.actionLocation)
        self.menuPrice_2.addAction(self.actionLatitude)
        self.menuPrice_2.addAction(self.actionBeedrooms)
        self.menuPrice_2.addAction(self.actionWaterFront)
        self.menuPrice_2.addAction(self.actionFloors_2)
        self.menuPrice_2.addAction(self.actionZipcode)
        self.menuPrice_2.addSeparator()
        self.menuPrice_2.addAction(self.actionPredict)
        self.menuBar.addAction(self.menuPrice.menuAction())
        self.menuBar.addAction(self.menuGeography.menuAction())
        self.menuBar.addAction(self.menuPrice_2.menuAction())

        self.actionBedrooms.triggered.connect(self.bedroom_menu)
        self.actionFloors.triggered.connect(self.floors_menu)

        self.actionPer_Square_Feet.triggered.connect(self.per_square_feet_menu)
        self.actionShow_Graph.triggered.connect(H.geography)
        self.actionLocation.triggered.connect(self.longitude_price)
        self.actionLatitude.triggered.connect(self.latitude_price)
        self.actionBeedrooms.triggered.connect(self.bedrooms_price)
        self.actionWaterFront.triggered.connect(self.waterfront_price)
        self.actionFloors_2.triggered.connect(self.floors_price)
        self.actionZipcode.triggered.connect(self.zipcode_price)
        self.actionPredict.triggered.connect(self.openPredictWindow)

        self.Find_btn.clicked.connect(self.find_value)
        self.show_graph_btn.clicked.connect(self.show_graph)
        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)



        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "House Analysis"))
        self.groupBox.setTitle(_translate("MainWindow", "House Count"))
        self.label_2.setText(_translate("MainWindow", "Output:"))
        self.label.setText(_translate("MainWindow", "Quantity"))
        self.Find_btn.setText(_translate("MainWindow", "Find"))
        self.answer.setText(_translate("MainWindow", "0.000"))
        self.show_graph_btn.setText(_translate("MainWindow", "Show Overall Graph"))
        self.title_lbl.setText(_translate("MainWindow", "House - Bedrooms"))
        self.menuPrice.setTitle(_translate("MainWindow", "House"))
        self.menuGeography.setTitle(_translate("MainWindow", "Geography"))
        self.menuPrice_2.setTitle(_translate("MainWindow", "Price"))
        self.actionPrice.setText(_translate("MainWindow", "Price"))
        self.actionBedrooms.setText(_translate("MainWindow", "Bedrooms"))
        self.actionFloors.setText(_translate("MainWindow", "Floors"))
        self.actionPer_Square_Feet.setText(_translate("MainWindow", "Per Square Feet"))
        self.actionLocation.setText(_translate("MainWindow", "Longitude"))
        self.actionLatitude.setText(_translate("MainWindow", "Latitude"))
        self.actionBeedrooms.setText(_translate("MainWindow", "Bedrooms"))
        self.actionWaterFront.setText(_translate("MainWindow", "WaterFront"))
        self.actionFloors_2.setText(_translate("MainWindow", "Floors"))
        self.actionZipcode.setText(_translate("MainWindow", "Zipcode"))
        self.actionPredict.setText(_translate("MainWindow", "Predict"))
        self.actionShow_Graph.setText(_translate("MainWindow", "Show Graph"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
