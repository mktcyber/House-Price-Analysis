from PyQt5 import QtCore, QtGui, QtWidgets
from housesales import House
H = House()
H.train_model()
class Ui_predict_form(object):
    
    def clear_form(self):
        self.bedrooms.setText("")
        self.bathrooms.setText("")
        self.living_area.setText("")
        self.total_area.setText("")
        self.floors.setText("")
        self.waterfront.setText("")
        self.view.setText("")
        self.condition.setText("")
        self.grade.setText("")
        self.area_above.setText("")
        self.basement_area.setText("")
        self.built_year.setText("")
        self.renovation_year.setText("")
        self.zipcode.setText("")
        self.latitude.setText("")
        self.longitude.setText("")
        self.living_area_2.setText("")
        self.total_area_2.setText("")
        self.price.setText("")

    def set_LR(self, enabled):
        if enabled:
            score = H.get_model_score('LR')
            self.model_score.setText('{} %'.format(score))

    def set_GBR(self, enabled):
        if enabled:
            score = H.get_model_score('GBR')
            self.model_score.setText('{} %'.format(score))

    def predict_price(self):
        model_name = 'LR' if self.RB_LR.isChecked() else 'GBR'

        predicted_price = H.predict(model_name,
                                    0,
                                    self.bedrooms.text(),
                                    self.bathrooms.text(),
                                    self.living_area.text(),
                                    self.total_area.text(),
                                    self.floors.text(),
                                    self.waterfront.text(),
                                    self.view.text(),
                                    self.condition.text(),
                                    self.grade.text(),
                                    self.area_above.text(),
                                    self.basement_area.text(),
                                    self.built_year.text(),
                                    self.renovation_year.text(),
                                    self.zipcode.text(),
                                    self.latitude.text(),
                                    self.longitude.text(),
                                    self.living_area_2.text(),
                                    self.total_area_2.text(),
                                    )

        self.price.setText(str(predicted_price))

    def setupUi(self, predict_form):
        predict_form.setObjectName("predict_form")
        predict_form.resize(803, 598)
        self.centralwidget = QtWidgets.QWidget(predict_form)
        self.centralwidget.setObjectName("centralwidget")
        self.predict_btn = QtWidgets.QPushButton(self.centralwidget)
        self.predict_btn.setGeometry(QtCore.QRect(30, 450, 211, 71))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.predict_btn.setFont(font)
        self.predict_btn.setFlat(False)
        self.predict_btn.setObjectName("predict_btn")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(270, 440, 511, 111))
        self.groupBox.setObjectName("groupBox")
        self.price = QtWidgets.QLabel(self.groupBox)
        self.price.setGeometry(QtCore.QRect(50, 30, 431, 61))
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.price.setFont(font)
        self.price.setObjectName("price")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(300, 20, 481, 401))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.living_area = QtWidgets.QLineEdit(self.layoutWidget)
        self.living_area.setObjectName("living_area")
        self.gridLayout.addWidget(self.living_area, 1, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.built_year = QtWidgets.QLineEdit(self.layoutWidget)
        self.built_year.setObjectName("built_year")
        self.gridLayout.addWidget(self.built_year, 6, 4, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.layoutWidget)
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 4, 0, 1, 1)
        self.waterfront = QtWidgets.QLineEdit(self.layoutWidget)
        self.waterfront.setObjectName("waterfront")
        self.gridLayout.addWidget(self.waterfront, 2, 4, 1, 1)
        self.bedrooms = QtWidgets.QLineEdit(self.layoutWidget)
        self.bedrooms.setObjectName("bedrooms")
        self.gridLayout.addWidget(self.bedrooms, 0, 1, 1, 1)
        self.latitude = QtWidgets.QLineEdit(self.layoutWidget)
        self.latitude.setObjectName("latitude")
        self.gridLayout.addWidget(self.latitude, 10, 1, 1, 1)
        self.view = QtWidgets.QLineEdit(self.layoutWidget)
        self.view.setObjectName("view")
        self.gridLayout.addWidget(self.view, 3, 1, 1, 1)
        self.bathrooms = QtWidgets.QLineEdit(self.layoutWidget)
        self.bathrooms.setObjectName("bathrooms")
        self.gridLayout.addWidget(self.bathrooms, 0, 4, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.layoutWidget)
        self.label_9.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 10, 0, 1, 1)
        self.total_area_2 = QtWidgets.QLineEdit(self.layoutWidget)
        self.total_area_2.setObjectName("total_area_2")
        self.gridLayout.addWidget(self.total_area_2, 11, 4, 1, 1)
        self.label_19 = QtWidgets.QLabel(self.layoutWidget)
        self.label_19.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_19.setObjectName("label_19")
        self.gridLayout.addWidget(self.label_19, 2, 3, 1, 1)
        self.living_area_2 = QtWidgets.QLineEdit(self.layoutWidget)
        self.living_area_2.setObjectName("living_area_2")
        self.gridLayout.addWidget(self.living_area_2, 11, 1, 1, 1)
        self.basement_area = QtWidgets.QLineEdit(self.layoutWidget)
        self.basement_area.setObjectName("basement_area")
        self.gridLayout.addWidget(self.basement_area, 6, 1, 1, 1)
        self.condition = QtWidgets.QLineEdit(self.layoutWidget)
        self.condition.setObjectName("condition")
        self.gridLayout.addWidget(self.condition, 3, 4, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.layoutWidget)
        self.label_8.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 9, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.layoutWidget)
        self.label_7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 6, 0, 1, 1)
        self.floors = QtWidgets.QLineEdit(self.layoutWidget)
        self.floors.setObjectName("floors")
        self.gridLayout.addWidget(self.floors, 2, 1, 1, 1)
        self.renovation_year = QtWidgets.QLineEdit(self.layoutWidget)
        self.renovation_year.setObjectName("renovation_year")
        self.gridLayout.addWidget(self.renovation_year, 9, 1, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.layoutWidget)
        self.label_13.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 4, 3, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.layoutWidget)
        self.label_12.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 0, 3, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.layoutWidget)
        self.label_11.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 3, 3, 1, 1)
        self.label_18 = QtWidgets.QLabel(self.layoutWidget)
        self.label_18.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_18.setObjectName("label_18")
        self.gridLayout.addWidget(self.label_18, 10, 3, 1, 1)
        self.zipcode = QtWidgets.QLineEdit(self.layoutWidget)
        self.zipcode.setObjectName("zipcode")
        self.gridLayout.addWidget(self.zipcode, 9, 4, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.layoutWidget)
        self.label_10.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 11, 0, 1, 1)
        self.total_area = QtWidgets.QLineEdit(self.layoutWidget)
        self.total_area.setObjectName("total_area")
        self.gridLayout.addWidget(self.total_area, 1, 4, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.layoutWidget)
        self.label_16.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_16.setObjectName("label_16")
        self.gridLayout.addWidget(self.label_16, 6, 3, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.layoutWidget)
        self.label_17.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_17.setObjectName("label_17")
        self.gridLayout.addWidget(self.label_17, 9, 3, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 3, 0, 1, 1)
        self.longitude = QtWidgets.QLineEdit(self.layoutWidget)
        self.longitude.setObjectName("longitude")
        self.gridLayout.addWidget(self.longitude, 10, 4, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.layoutWidget)
        self.label_15.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_15.setObjectName("label_15")
        self.gridLayout.addWidget(self.label_15, 1, 3, 1, 1)
        self.grade = QtWidgets.QLineEdit(self.layoutWidget)
        self.grade.setObjectName("grade")
        self.gridLayout.addWidget(self.grade, 4, 1, 1, 1)
        self.area_above = QtWidgets.QLineEdit(self.layoutWidget)
        self.area_above.setObjectName("area_above")
        self.gridLayout.addWidget(self.area_above, 4, 4, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.layoutWidget)
        self.label_14.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_14.setObjectName("label_14")
        self.gridLayout.addWidget(self.label_14, 11, 3, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(48, 21, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 2, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 20, 261, 171))
        self.groupBox_2.setObjectName("groupBox_2")
        self.widget = QtWidgets.QWidget(self.groupBox_2)
        self.widget.setGeometry(QtCore.QRect(30, 40, 191, 91))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.RB_LR = QtWidgets.QRadioButton(self.widget)
        self.RB_LR.setChecked(True)
        self.RB_LR.setObjectName("RB_LR")
        self.verticalLayout.addWidget(self.RB_LR)
        self.RB_GBR = QtWidgets.QRadioButton(self.widget)
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.RB_GBR.setFont(font)
        self.RB_GBR.setAutoFillBackground(False)
        self.RB_GBR.setObjectName("RB_GBR")
        self.verticalLayout.addWidget(self.RB_GBR)
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(20, 200, 261, 131))
        self.groupBox_3.setObjectName("groupBox_3")
        self.model_score = QtWidgets.QLabel(self.groupBox_3)
        self.model_score.setGeometry(QtCore.QRect(60, 40, 191, 61))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.model_score.setFont(font)
        self.model_score.setObjectName("model_score")
        predict_form.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(predict_form)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 803, 26))
        self.menubar.setObjectName("menubar")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        predict_form.setMenuBar(self.menubar)
        self.actionClear = QtWidgets.QAction(predict_form)
        self.actionClear.setObjectName("actionClear")
        self.menuEdit.addAction(self.actionClear)
        self.menubar.addAction(self.menuEdit.menuAction())

        
    #Function Buinding...
        self.actionClear.triggered.connect(self.clear_form)
        self.RB_LR.toggled.connect(self.set_LR)
        self.RB_GBR.toggled.connect(self.set_GBR)
        self.predict_btn.clicked.connect(self.predict_price)

        self.retranslateUi(predict_form)
        QtCore.QMetaObject.connectSlotsByName(predict_form)

    def retranslateUi(self, predict_form):
        _translate = QtCore.QCoreApplication.translate
        predict_form.setWindowTitle(_translate("predict_form", "Predict"))
        self.predict_btn.setText(_translate("predict_form", "Predict Price"))
        self.groupBox.setTitle(_translate("predict_form", "Predicted Price"))
        self.price.setText(_translate("predict_form", ""))
        self.label_4.setText(_translate("predict_form", "Floors :"))
        self.label_3.setText(_translate("predict_form", "Living Area :"))
        self.label_6.setText(_translate("predict_form", "Grade :"))
        self.label_9.setText(_translate("predict_form", "Latitude :"))
        self.label_19.setText(_translate("predict_form", "Waterfront :"))
        self.label_8.setText(_translate("predict_form", "Renovation Year :"))
        self.label_7.setText(_translate("predict_form", "Basement Area :"))
        self.label_13.setText(_translate("predict_form", "Area Above :"))
        self.label_12.setText(_translate("predict_form", "Bathrooms :"))
        self.label_11.setText(_translate("predict_form", "Condition :"))
        self.label_18.setText(_translate("predict_form", "Longitude :"))
        self.label_2.setText(_translate("predict_form", "Bedrooms :"))
        self.label_10.setText(_translate("predict_form", "Alt Living Area :"))
        self.label_16.setText(_translate("predict_form", "Year built :"))
        self.label_17.setText(_translate("predict_form", "Zipcode :"))
        self.label_5.setText(_translate("predict_form", "View :"))
        self.label_15.setText(_translate("predict_form", "Total Area"))
        self.label_14.setText(_translate("predict_form", "Alt Total Area :"))
        self.groupBox_2.setTitle(_translate("predict_form", "Prediction Model"))
        self.RB_LR.setText(_translate("predict_form", "Linear Regression"))
        self.RB_GBR.setText(_translate("predict_form", "Gradient Boosting Regressor"))
        self.groupBox_3.setTitle(_translate("predict_form", "Current Model Score"))
        self.model_score.setText(_translate("predict_form", ""))
        self.menuEdit.setTitle(_translate("predict_form", "Edit"))
        self.actionClear.setText(_translate("predict_form", "Clear"))
        self.set_LR(True)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    predict_form = QtWidgets.QMainWindow()
    ui = Ui_predict_form()
    ui.setupUi(predict_form)
    predict_form.show()
    sys.exit(app.exec_())
