from PyQt5 import QtWidgets, uic, QtCore, QtGui
from PyQt5.QtCore import pyqtSignal, QFileInfo, QUrl
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtWidgets import (QApplication, QMainWindow, QPushButton, QLabel, QSlider, QGridLayout, QPushButton)
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QLabel, \
    QSlider, QStyle, QSizePolicy, QFileDialog
import sys
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtGui import QIcon, QPalette
from PyQt5.QtCore import Qt, QUrl, QTimer
import os
import sys
import random
import zipfile



class App(QMainWindow, QWidget):
    def allhide(self):
        self.decaptacon.hide()
        self.dancem.hide()
        self.badg.hide()
        self.cr.hide()
        self.iff.hide()
        self.rrin.hide()
        self.abr.hide()
        self.sshe.hide()
        self.ohno.hide()

    def __init__(self):
        super().__init__()
        uic.loadUi(r"pleer_design.ui", self)

        self.s = [self.decep, self.dance, self.bad, self.curc, self.get, self.rings, self.she, self.my, self.oh]
        self.song.setText("")

        self.c = 0
        self.flag = True

        self.player = QMediaPlayer(self)
        self.verticalSlider.valueChanged[int].connect(self.change_volume)
        self.verticalSlider.setValue(100)
        self.volume = self.verticalSlider.value()
        # self.horizontalSlider.sliderMoved.connect(self.set_position)

        self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)

        self.decetaconbutton.clicked.connect(self.decep)
        self.dancebutton.clicked.connect(self.dance)
        self.guybutton.clicked.connect(self.bad)
        self.crucifedbutton.clicked.connect(self.curc)
        self.detbutton.clicked.connect(self.get)
        self.ringsbutton.clicked.connect(self.rings)
        self.shebutton.clicked.connect(self.she)
        self.MyButton.clicked.connect(self.my)
        self.ofbutton.clicked.connect(self.oh)

        self.play.clicked.connect(self.playMedia)
        self.reset.clicked.connect(self.resetMedia)
        self.pause.clicked.connect(self.pauseMedia)
        self.random.clicked.connect(self.randomMedia)
        self.forward.clicked.connect(self.forwrar)
        self.backward.clicked.connect(self.backwar)

        self.allhide()


        #
        # self.mediaPlayer.stateChanged.connect(self.mediastate_changed)
        # self.mediaPlayer.positionChanged.connect(self.position_changed)
        # self.mediaPlayer.durationChanged.connect(self.duration_changed)


        self.horizontalSlider.setRange(0, 0)  # Initial range
        self.horizontalSlider.sliderMoved.connect(self.set_position)
        self.player.positionChanged.connect(self.position_changed)
        self.player.durationChanged.connect(self.duration_changed)
        hbox_labels = QHBoxLayout()
        hbox_labels.addWidget(self.time1)
        hbox_labels.addWidget(self.time2)



    def change_volume(self, value):
        self.player.setVolume(value)


    def decep(self):
        self.c = 0
        self.song.setText("Deceptacon")
        self.player.setMedia(
            QMediaContent(QUrl.fromLocalFile(
                r'Le_Tigre_-_Deceptacon_48052957.mp3')))
        self.player.play()
        self.allhide()
        self.decaptacon.show()

    def dance(self):
        self.c = 1
        self.song.setText("Dance Motherfucker")
        self.player.setMedia(
            QMediaContent(QUrl.fromLocalFile(
                r"Scum_of_the_Earth_-_Dance_Motherfucker_71559688.mp3")))
        self.player.play()
        self.allhide()
        self.dancem.show()

    def bad(self):
        self.c = 2
        self.song.setText("Bad Guy")
        self.player.setMedia(
            QMediaContent(QUrl.fromLocalFile(
                r"Billie_Eilish_-_bad_guy_63154737.mp3")))
        self.player.play()
        self.allhide()
        self.badg.show()

    def curc(self):
        self.c = 3
        self.song.setText("Crucified")
        self.player.setMedia(
            QMediaContent(QUrl.fromLocalFile(
                r"Army Of Lovers - Crucified.mp3")))
        self.player.play()
        self.allhide()
        self.cr.show()

    def get(self):
        self.c = 4
        self.song.setText("Get It Up")
        self.player.setMedia(
            QMediaContent(QUrl.fromLocalFile(
                r"Mindless_Self_Indulgence_-_Get_It_Up_64292243.mp3")))
        self.player.play()
        self.allhide()
        self.iff.show()

    def rings(self):
        self.c = 5
        self.song.setText("7 rings")
        self.player.setMedia(
            QMediaContent(QUrl.fromLocalFile(
                r"Ariana_Grande_-_7_rings_61522389.mp3")))
        self.player.play()
        self.allhide()
        self.rrin.show()

    def she(self):
        self.c = 6
        self.song.setText("She Burned Me Down")
        self.player.setMedia(
            QMediaContent(QUrl.fromLocalFile(
                r"Type_O_Negative_-_She_Burned_Me_Down_73200420.mp3")))
        self.player.play()
        self.allhide()
        self.sshe.show()

    def my(self):
        self.c = 7
        self.song.setText("Teenagers")
        self.player.setMedia(
            QMediaContent(QUrl.fromLocalFile(
                r"My_Chemical_Romance_-_Teenagers_48131445.mp3")))
        self.player.play()
        self.allhide()
        self.abr.show()

    def oh(self):
        self.c = 8
        self.song.setText("Oh No!")
        self.player.setMedia(
            QMediaContent(QUrl.fromLocalFile(
                r"Marina_And_The_Diamonds_-_Oh_No_48228200.mp3")))
        self.player.play()
        self.allhide()
        self.ohno.show()

    def forwrar(self):
        k = self.c + 1
        if self.c != 8:
            self.forward.clicked.connect(self.s[k])
            self.c = k
        else:
            self.forward.clicked.connect(self.s[0])
            self.c = 0

    def backwar(self):
        k = self.c - 1
        if self.c != 0:
            self.backward.clicked.connect(self.s[k])
            self.c = k
        else:
            self.backward.clicked.connect(self.s[8])
            self.c = 8

    def playMedia(self):
        self.player.play()

    def pauseMedia(self):
        self.player.pause()

    def resetMedia(self):
        self.player.stop()

    def mediastate_changed(self, state):
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.playBtn.setIcon(
                self.style().standardIcon(QStyle.SP_MediaPause)
            )
        else:
            self.playBtn.setIcon(
                self.style().standardIcon(QStyle.SP_MediaPlay)
            )

    def position_changed(self, position):
        self.horizontalSlider.setValue(position)
        self.time1.setText(self.format_time(position))

    def duration_changed(self, duration):
        self.horizontalSlider.setRange(0, duration)
        self.time2.setText(self.format_time(duration))

    def randomMedia(self):
        r = random.choice(self.s)
        self.random.clicked.connect(r)

    def set_position(self, position):
        self.player.setPosition(position)

    def format_time(self, ms):
        seconds = (ms // 1000) % 60
        minutes = (ms // (1000 * 60)) % 60
        return "{:02d}:{:02d}".format(minutes, seconds)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    rt = App()
    rt.show()
    sys.exit(app.exec())