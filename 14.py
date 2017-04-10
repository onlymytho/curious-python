#!/usr/bin/env python
# coding: utf-8

# 예제 내용
# * 기본 위젯을 사용하여 기본 창을 생성
# * Layout 을 이용하여 위젯을 배치

import sys

from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QBoxLayout

from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import Qt

__author__ = "Deokyu Lim <hong18s@gmail.com>"


class Form(QWidget):
	def __init__(self):
		QWidget.__init__(self, flags=Qt.Widget)

		# 배치될 위젯 변수 선언
		self.lb_1 = QLabel()
		self.lb_2 = QLabel()
		self.pb_1 = QPushButton()
		self.pb_2 = QPushButton()

        # 레이아웃 선언 및 Form Widget에 설정
		self.layout_1 = QBoxLayout(QBoxLayout.TopToBottom, self)
		self.layout_2 = QBoxLayout(QBoxLayout.LeftToRight)
		self.layout_3 = QBoxLayout(QBoxLayout.LeftToRight)

        # 부모 레이아웃에 자식 레이아웃을 추가
		self.layout_1.addLayout(self.layout_2)
		self.layout_1.addLayout(self.layout_3)
		self.setLayout(self.layout_1)
		self.init_widget()

	def init_widget(self):
		self.setWindowTitle("Layout Basic")
		self.setFixedWidth(640)

		# 라벨1의 설정 및 레이아웃 추가
		self.lb_1.setText("레이아웃 생성하기")
#		self.lb_1.setStyleSheet("background-color: yellow")
		self.pb_1.setText("완료")
		self.layout_2.addWidget(self.lb_1)
		self.layout_2.addWidget(self.pb_1)

		# 라벨2의 설정 및 레이아웃 추가
		self.lb_2.setText("스타일 지정하기")
#		self.lb_2.setStyleSheet("background-color: red")
		self.pb_2.setText("완료")
		self.pb_2.setStyleSheet("width: 30px; height: 30px;")
		self.layout_3.addWidget(self.lb_2)
		self.layout_3.addWidget(self.pb_2)


if __name__ == "__main__":
	app = QApplication(sys.argv)
	form = Form()
	form.show()
	exit(app.exec_())
