#!/usr/bin/python3

# This Python file uses the following encoding: utf-8
# main_widget.py BSZET-DD Template
# Copyright © 2022 SRE

import os
import sys
import random

sys.dont_write_bytecode = True  # noqa: E402
sys.path.insert(0, os.path.abspath(
                os.path.join(os.path.dirname(__file__), '..')))  # noqa: E402

from PySide6.QtUiTools import loadUiType

from PySide6.QtCore import (
     QCoreApplication,
     Signal,
     Slot,
     Qt
     )

from PySide6.QtWidgets import (
     QApplication
     )

UIFilename = "form.ui"
Form, Base = loadUiType(os.path.join(sys.path[1], UIFilename))

move_pxl_count = 10
MAX_X = 1000
MAX_Y = 500
AVATAR_BASE_X = 10
AVATAR_BASE_Y = 60
AVATAR_DEFAULT_SIZE = 40

class MainWindow(Base, Form):
    def __init__(self, parent=None):
        super(self.__class__, self).__init__(parent)
        self.setupUi(self)
        self.set_lblElementInfo()

    avatar_x = 0; avatar_y = 0
    avatar_size = AVATAR_DEFAULT_SIZE
    red = 85; green = 170; blue = 0

    def set_lblElementInfo(self):
        self.lblElementInfo.setText("Position: ( " + str(self.avatar_x) + " | " + str(self.avatar_y) + " )\nSize: " + str(self.avatar_size) + " px")

    def set_avatar_geometry(self):
        self.btnAvatar.setGeometry(self.avatar_x + AVATAR_BASE_X, self.avatar_y + AVATAR_BASE_Y, self.avatar_size, self.avatar_size)
        self.set_lblElementInfo()

    def change_avatar_pos(self, delta_x, delta_y):
        self.set_avatar_pos(self.avatar_x + delta_x, self.avatar_y + delta_y)

    def set_avatar_pos(self, x, y):
        self.avatar_x = MAX_X if x > MAX_X else (x if x > 0 else 0)
        self.avatar_y = MAX_Y if y > MAX_Y else (y if y > 0 else 0)
        self.set_avatar_geometry()

    def change_avatar_size(self, size):
        self.avatar_size += size
        self.set_avatar_geometry()

    def set_avatar_size(self, size):
        self.avatar_size = size
        self.set_avatar_geometry()

    def set_avatar_color(self):
        clr_str = "rgb(" + str(self.red) + ", " + str(self.green) + ", " + str(self.blue) + ")"
        self.lblClr.setText(clr_str)
        self.btnAvatar.setStyleSheet("QPushButton { background-color: " + clr_str + " }")

    def set_color_sliders(self):
        self.sldRed.setValue(self.red)
        self.sldGreen.setValue(self.green)
        self.sldBlue.setValue(self.blue)

    @Slot()
    def on_btnResetPosition_clicked(self):
        self.set_avatar_pos(0, 0)

    @Slot()
    def on_btnMoveUp_clicked(self):
        self.change_avatar_pos(0, -move_pxl_count)

    @Slot()
    def on_btnMoveDown_clicked(self):
        self.change_avatar_pos(0, move_pxl_count)

    @Slot()
    def on_btnMoveLeft_clicked(self):
        self.change_avatar_pos(-move_pxl_count, 0)

    @Slot()
    def on_btnMoveRight_clicked(self):
        self.change_avatar_pos(move_pxl_count, 0)

    @Slot()
    def on_btnLetShrink_clicked(self):
        self.change_avatar_size(-10)

    @Slot()
    def on_btnLetGrow_clicked(self):
        self.change_avatar_size(10)

    @Slot()
    def on_btnResetSize_clicked(self):
        self.set_avatar_size(AVATAR_DEFAULT_SIZE)

    @Slot()
    def on_sldRed_valueChanged(self):
        self.red = self.sldRed.value()
        self.set_avatar_color()

    @Slot()
    def on_sldGreen_valueChanged(self):
        self.green = self.sldGreen.value()
        self.set_avatar_color()

    @Slot()
    def on_sldBlue_valueChanged(self):
        self.blue = self.sldBlue.value()
        self.set_avatar_color()

    @Slot()
    def on_btnRand_clicked(self):
        self.red = random.randint(0, 255); self.green = random.randint(0, 255); self.blue = random.randint(0, 255)
        self.set_avatar_color()
        self.set_color_sliders()


if __name__ == "__main__":
    QCoreApplication.setAttribute(Qt.AA_ShareOpenGLContexts)
    app = QApplication(sys.argv)
    os.chdir(sys.path[1])
    widget = MainWindow()
    widget.show()

    sys.exit(app.exec())
