#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @File : main.py
# @Project : sequence_screening
# @Software: PyCharm
# @Author : 大红昕
# @Time : 2020/7/8 14:00
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
import pandas as pd
import interface


class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.data_frame = pd.DataFrame()
        self.sequence = list()
        self.open_balst_file_flag = False
        self.open_sequence_file_flag = False
        self.context = list()
        self.ui = interface.Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.open_blast_file_button_success_click)
        self.ui.pushButton_3.clicked.connect(self.screen_button_success_click)
        self.ui.pushButton_2.clicked.connect(self.open_sequence_file_button_success_click)
        self.ui.pushButton_4.clicked.connect(self.comparison_button_success_click)
        self.ui.pushButton_6.clicked.connect(self.save_file_button_success_click)

    def open_blast_file_button_success_click(self):
        self.ui.lineEdit_3.setText("读入文件中请稍等")
        filename = QFileDialog.getOpenFileName(self, '选择文件', './')
        if filename[0] != "":
            self.data_frame = pd.read_excel(filename[0], names=[i for i in "ABCDEFGHIJKL"], header=None)
            self.open_balst_file_flag = True
            self.ui.lineEdit_3.setText("blast结果文件读入成功！")
            self.ui.lineEdit.setText("共%d行数据" % self.data_frame.shape[0])
        else:
            self.ui.lineEdit_3.setText("请选择文件！")

    def screen_button_success_click(self):
        if self.open_balst_file_flag:
            line_1_combox = self.ui.comboBox.currentText()
            line_1_value = self.ui.lineEdit_4.text()
            line_2_combox = self.ui.comboBox_2.currentText()
            line_2_value = self.ui.lineEdit_5.text()
            if line_2_value == "" or line_2_value == "":
                self.ui.lineEdit_3.setText("请输入筛选条件")
            else:
                if line_1_combox == "大于等于":
                    self.data_frame = self.data_frame[self.data_frame.C >= int(line_1_value)]
                if line_1_combox == "大于":
                    self.data_frame = self.data_frame[self.data_frame.C > int(line_1_value)]
                if line_2_combox == "大于等于":
                    self.data_frame = self.data_frame[self.data_frame.L >= int(line_2_value)]
                if line_2_combox == "大于":
                    self.data_frame = self.data_frame[self.data_frame.L > int(line_2_value)]
                self.data_frame = self.data_frame.drop_duplicates(subset="B", keep="first", inplace=False)
                self.data_frame = self.data_frame.reset_index(drop=True)
                self.ui.lineEdit_3.setText("共筛选出%d条数据" % self.data_frame.shape[0])
                self.ui.lineEdit.setText("共%d行数据" % self.data_frame.shape[0])
        else:
            self.ui.lineEdit_3.setText("请先导入数据")

    def open_sequence_file_button_success_click(self):
        count = 0
        self.ui.lineEdit_3.setText("读入文件中请稍等")
        filename = QFileDialog.getOpenFileName(self, '选择文件', './')
        if filename[0] != "":
            with open(filename[0], mode="r", encoding="utf-8") as f:
                for line in f.readlines():
                    self.sequence.append(line.strip("\n"))
                    if line[0] == ">":
                        count += 1
            self.ui.lineEdit_3.setText("序列文件读入成功！")
            self.ui.lineEdit_2.setText("共读入%d条序列" % count)
            self.open_sequence_file_flag = True
        else:
            self.ui.lineEdit_3.setText("请选择文件！")

    def comparison_button_success_click(self):
        if self.open_balst_file_flag and self.open_sequence_file_flag:
            count = 0
            for i in range(len(self.data_frame.B)):
                start = ">" + self.data_frame.B[i]
                if start in self.sequence:
                    count += 1
                    index = self.sequence.index(start)
                    while True:
                        self.context.append(self.sequence[index])
                        if self.sequence[index + 1][0] == ">":
                            break
                        index += 1
            self.ui.lineEdit_3.setText("比对完成，共%d条数据" % count)
        else:
            self.ui.lineEdit_3.setText("请先载入数据")
    def save_file_button_success_click(self):
        filename = QFileDialog.getSaveFileName(self, '选择文件', './')
        with open(filename[0], mode="w+", encoding="utf-8") as f:
            for code in self.context:
                f.writelines(code)
                f.writelines("\n")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    show = MyWindow()
    show.show()
    sys.exit(app.exec_())
