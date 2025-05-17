import sys
import webbrowser
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel, QComboBox,
    QSlider, QPushButton, QMessageBox, QHBoxLayout, QSpacerItem, QSizePolicy
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from pycaw.pycaw import AudioUtilities, ISimpleAudioVolume

class VolumeBooster(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Volume fonem grave🙏🏼🙏🏼😭😭)
        self.setGeometry(500, 300, 400, 220)
        self.setFixedSize(400, 220)

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        # Apply dark theme stylesheet
        self.setStyleSheet("""
            QWidget {
                background-color: #2e3440;
                color: #d8dee9;
                font-family: 'Segoe UI';
            }
            QLabel {
                font-size: 12pt;
            }
            QComboBox {
                background-color: #3b4252;
                border: 1px solid #4c566a;
                padding: 5px;
                color: #eceff4;
                font-size: 11pt;
            }
            QComboBox QAbstractItemView {
                background-color: #434c5e;
                selection-background-color: #88c0d0;
                color: #eceff4;
            }
            QSlider::groove:horizontal {
                border: 1px solid #4c566a;
                height: 8px;
                background: #434c5e;
                border-radius: 4px;
            }
            QSlider::handle:horizontal {
                background: #81a1c1;
                border: 1px solid #4c566a;
                width: 18px;
                margin: -5px 0;
                border-radius: 9px;
            }
            QPushButton {
                background-color: #5e81ac;
                border: none;
                padding: 8px;
                color: #eceff4;
                font-size: 11pt;
                border-radius: 6px;
            }
            QPushButton:hover {
                background-color: #81a1c1;
            }
            QPushButton:pressed {
                background-color: #4c566a;
            }
        """)

        # Title
        title = QLabel("SLIDERS per app volume")
        title_font = QFont("Segoe UI", 16, QFont.Bold)
        title.setFont(title_font)
        title.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(title)

        self.layout.addSpacing(10)

        # Select app label and dropdown
        self.label = QLabel("Select an app:")
        self.label.setFont(QFont("Segoe UI", 10))
        self.layout.addWidget(self.label)

        self.combo = QComboBox()
        self.combo.setFont(QFont("Segoe UI", 10))
        self.layout.addWidget(self.combo)

        self.layout.addSpacing(10)

        # Volume slider label and slider in horizontal layout
        volume_layout = QHBoxLayout()
        self.slider_label = QLabel("Volume: 100%")
        self.slider_label.setFont(QFont("Segoe UI", 10))
        volume_layout.addWidget(self.slider_label)

        volume_layout.addItem(QSpacerItem(20, 10, QSizePolicy.Expanding, QSizePolicy.Minimum))

        self.slider = QSlider(Qt.Horizontal)
        self.slider.setMinimum(0)
        self.slider.setMaximum(100)
        self.slider.setValue(100)
        self.slider.setFixedWidth(200)
        volume_layout.addWidget(self.slider)

        self.layout.addLayout(volume_layout)

        self.layout.addSpacing(15)

        # Buttons layout
        buttons_layout = QHBoxLayout()

        self.boost_button = QPushButton("Apply Volume")
        self.boost_button.setFont(QFont("Segoe UI", 10))
        self.boost_button.setFixedWidth(120)
        buttons_layout.addWidget(self.boost_button)

        buttons_layout.addSpacing(20)

        self.web_button = QPushButton("Open Math Realize Website")
        self.web_button.setFont(QFont("Segoe UI", 10))
        self.web_button.setFixedWidth(200)
        buttons_layout.addWidget(self.web_button)

        self.layout.addLayout(buttons_layout)

        # Connect signals
        self.boost_button.clicked.connect(self.apply_volume)
        self.slider.valueChanged.connect(self.update_label)
        self.web_button.clicked.connect(self.open_website)

        self.sessions = []
        self.update_sessions()

    def update_sessions(self):
        self.combo.clear()
        self.sessions = []
        sessions = AudioUtilities.GetAllSessions()
        for session in sessions:
            process = session.Process
            if process and process.name():
                if process.name().lower() not in ["system", "system sounds"]:
                    self.sessions.append(session)
                    self.combo.addItem(process.name())

        if self.sessions:
            self.combo.setCurrentIndex(0)
        else:
            self.combo.addItem("No audio sessions found")
            self.boost_button.setEnabled(False)
            self.slider.setEnabled(False)

    def update_label(self, value):
        self.slider_label.setText(f"Volume: {value}%")

    def apply_volume(self):
        index = self.combo.currentIndex()
        if not self.sessions or index >= len(self.sessions):
            QMessageBox.warning(self, "Error", "No app selected or no sessions available.")
            return

        session = self.sessions[index]
        volume_interface = session._ctl.QueryInterface(ISimpleAudioVolume)

        volume_value = self.slider.value() / 100.0  # 0.0 to 1.0

        try:
            volume_interface.SetMasterVolume(volume_value, None)
            QMessageBox.information(
                self, "Success", f"Volume set to {int(volume_value * 100)}% for {self.combo.currentText()}"
            )
        except Exception as e:
            QMessageBox.warning(self, "Error", f"Failed to set volume: {str(e)}")

    def open_website(self):
        url = "https://mathrealize.web.app"
        webbrowser.open(url)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = VolumeBooster()
    window.show()
    sys.exit(app.exec())
