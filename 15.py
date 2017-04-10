#!/usr/bin/env python
# coding: utf-8

# 예제 내용
# * 기본 위젯을 사용하여 기본 창을 생성
# * 다양한 레이아웃 위젯 사용

import sys

from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QSpacerItem
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QTextEdit
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QGroupBox

from PyQt5.QtWidgets import QBoxLayout
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QFormLayout

from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import Qt

__author__ = "Deokyu Lim <hong18s@gmail.com>"


class Form(QWidget):
    def __init__(self):
        QWidget.__init__(self, flags=Qt.Widget)

        self.setWindowTitle("Collapsable Notepad")
        self.setFixedWidth(640)
        self.setFixedHeight(480)

        layout_base = QBoxLayout(QBoxLayout.TopToBottom, self)
        self.setLayout(layout_base)

        # 첫 번째 그룹 QBoxLayout
        grp_1 = QGroupBox("QBoxLayout")
        layout_base.addWidget(grp_1)
        layout = QHBoxLayout()

        grp_1.btns = []
        grp_1.btns_text = ["색상", "크기", "동기화"]
        for i in grp_1.btns_text:
            grp_1.btns.append(QPushButton(i))

        for i in grp_1.btns:
            i.setFixedSize(30, 30)
            i.setStyleSheet("border:1px solid #dfdfdf")
            layout.addWidget(i)

        grp_1.setLayout(layout)

        # 두 번째 그룹 QGridLayout
        grp_2 = QGroupBox("QGridLayout")
        layout_base.addWidget(grp_2)
        grp_2_layout = QBoxLayout(QBoxLayout.LeftToRight)
        grp_2.setLayout(grp_2_layout)
        grp_2_layout.addWidget(QTextEdit())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = Form()
    form.show()
    exit(app.exec_())
