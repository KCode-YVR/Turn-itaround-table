import sys
import pygame

from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QPushButton,
    QSlider,
    QVBoxLayout,
    QLabel,
)
from PySide6.QtCore import Qt


class MusicPlayer(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Turn(itaround)table")

        self.isPaused = False

        pygame.mixer.init()
        pygame.mixer.music.load("Under the sun.mp3")

        self.statusLabel = QLabel("Ready to play")
        self.playPauseButton = QPushButton("Play")
        self.volumeSlider = QSlider(Qt.Orientation.Horizontal)

        self.volumeSlider.setRange(0, 100)
        self.volumeSlider.setValue(50)

        pygame.mixer.music.set_volume(0.5)

        self.playPauseButton.clicked.connect(self.toggleMusic)
        self.volumeSlider.valueChanged.connect(self.changeVolume)

        layout = QVBoxLayout()
        layout.addWidget(self.playPauseButton)
        layout.addWidget(self.volumeSlider)
        layout.addWidget(self.statusLabel)
        self.setLayout(layout)
    
    def toggleMusic(self):
        if not pygame.mixer.music.get_busy() and not self.isPaused:
            pygame.mixer.music.play()
            self.playPauseButton.setText("Pause")
            self.statusLabel.setText("Playing music")
        elif self.isPaused:
            pygame.mixer.music.unpause()
            self.isPaused = False
            self.playPauseButton.setText("Pause")
            self.statusLabel.setText("Playing music")
        else:
            pygame.mixer.music.pause()
            self.isPaused = True
            self.playPauseButton.setText("Resume")
            self.statusLabel.setText("Paused")

    def changeVolume(self, value):
        vol = value/100
        pygame.mixer.music.set_volume(vol)
        self.statusLabel.setText(f"Volume: {value}%")

app = QApplication(sys.argv)
window = MusicPlayer()
window.show()
sys.exit(app.exec())


            

        

