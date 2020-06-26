#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @File : main.py
# @Project : shengwu
# @Software: PyCharm
# @Author : 大红昕
# @Time : 2020/6/24 17:15
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QTableWidgetItem
import numpy as np
import UI
import sys

str_ = [i for i in "ACDEFGHIKLMNPQRSTVWY"]


class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.calculated_flag = False
        self.context = {value: key for key, value in enumerate(str_)}
        self.table = np.zeros((8, 20))
        self.data = list()
        self.ui = UI.Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.open_file_success_click_button)
        self.ui.pushButton_2.clicked.connect(self.calculate_success_click_button)
        self.ui.lineEdit.setText("请务必保证文件格式与示例相同！")

    def open_file_success_click_button(self):
        self.data = []
        self.table = np.zeros((8, 20))
        filename = QFileDialog.getOpenFileName(self, '选择文件', './', '*.txt')
        if filename[0]:
            with open(filename[0], 'r', encoding='utf-8', errors='ignore') as f:
                for key, value in enumerate(f):
                    if (key + 1) % 2 == 0:
                        self.data.append(value.strip("\n"))
            for value in self.data:
                self.ui.listWidget.addItem(value)
            self.ui.lineEdit.setText("文件读入成功！")
            self.calculated_flag = False
        else:
            self.ui.lineEdit.setText("请选择文件！")

    def calculate_success_click_button(self):
        if self.calculated_flag is False:
            if self.data:
                self.calculate()
                for i in range(8):
                    for j in range(20):
                        new_item = QTableWidgetItem(str(self.table[i][j] / 8))
                        self.ui.tableWidget.setItem(i + 1, j, new_item)
                        self.table[i][j] = 0
                self.ui.lineEdit.setText("计算完成！")
                self.calculated_flag = True
            else:
                self.ui.lineEdit.setText("请载入文件！")

    def calculate(self):
        for value_1 in self.data:
            for key in range(len(value_1)):
                self.table[key][int(self.context.get(value_1[key]))] += 1


if __name__ == "__main__":
    app = QApplication(sys.argv)
    show = MyWindow()
    show.show()
    sys.exit(app.exec_())
