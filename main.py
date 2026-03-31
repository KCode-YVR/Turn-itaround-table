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


        self.setWindowTitle("Python Music Player")

        self.is_paused = False

        pygame.mixer.init()

        pygame.mixer.music.load("song.mp3")

        self.status_label = QLabel("Ready to play")
        self.play_pause_button = QPushButton("Play")
        self.volume_slider = QSlider(Qt.Orientation.Horizontal)

        self.volume_slider.setRange(0, 100)
        self.volume_slider.setValue(50)

        
        pygame.mixer.music.set_volume(0.5)

        self.play_pause_button.clicked.connect(self.toggle_music)
        self.volume_slider.valueChanged.connect(self.change_volume)

        layout = QVBoxLayout()
        layout.addWidget(self.status_label)
        layout.addWidget(self.play_pause_button)
        layout.addWidget(self.volume_slider)
        self.setLayout(layout)

    def toggle_music(self):
        if not pygame.mixer.music.get_busy() and not self.is_paused:
            pygame.mixer.music.play()
            self.play_pause_button.setText("Pause")
            self.status_label.setText("Playing")
        elif self.is_paused:
            pygame.mixer.music.unpause()
            self.is_paused = False
            self.play_pause_button.setText("Pause")
            self.status_label.setText("Playing")
        else:
            pygame.mixer.music.pause()
            self.is_paused = True
            self.play_pause_button.setText("Resume")
            self.status_label.setText("Paused")

    def change_volume(self, value):
        volume = value / 100
        pygame.mixer.music.set_volume(volume)
        self.status_label.setText(f"Volume: {value}%")


app = QApplication(sys.argv)
window = MusicPlayer()
window.show()
sys.exit(app.exec())