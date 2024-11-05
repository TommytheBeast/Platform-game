from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLineEdit, QMessageBox
from PyQt5.QtCore import Qt, QTimer, QRect
from PyQt5.QtGui import QPixmap, QPainter
import random
import sys

class MainMenu:
    def __init__(self):
        self.hello = ["Yo", "Wassup", "Hello"]
        self.app = QApplication([])

    def show_gui(self):
        # Set up the main window
        window = QWidget()
        window.setWindowTitle('Main Menu')
        layout = QVBoxLayout()

        # Placeholder text
        self.placeholder_text = QLineEdit(self.hello[0])
        self.placeholder_text.setReadOnly(True)
        self.placeholder_text.setFixedSize(200, 40)
        layout.addWidget(self.placeholder_text)

        # Start button
        start_button = QPushButton('Start')
        start_button.setFixedSize(100, 40)
        start_button.clicked.connect(lambda: self.placeholder_text.setText(random.choice(self.hello)))
        start_button.clicked.connect(self.start_game)
        layout.addWidget(start_button)

        # Exit button
        exit_button = QPushButton('Exit')
        exit_button.setFixedSize(100, 40)
        exit_button.clicked.connect(self.app.quit)
        layout.addWidget(exit_button)

        # Finalize layout
        window.setLayout(layout)
        window.setFixedSize(400, 300)
        window.show()
        
        # Run the application
        self.app.exec_()

    def start_game(self):
        # Initialize the game window
        self.game_window = QWidget()
        self.game_window.setWindowTitle('Platform Game')
        
        # Game layout and canvas
        game_layout = QVBoxLayout()
        self.canvas = GameCanvas(sprite_path="C:/test_sprite.png")  # Update with your sprite path
        game_layout.addWidget(self.canvas)
        
        self.game_window.setLayout(game_layout)
        self.game_window.setFixedSize(1280, 960)
        self.game_window.show()
        self.canvas.setFocus()

class GameCanvas(QWidget):
    def __init__(self, sprite_path):
        super().__init__()
        self.setFocusPolicy(Qt.StrongFocus)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_game)
        self.timer.start(16)  # ~60 FPS

        # Load sprite image
        self.sprite = QPixmap(sprite_path)
        if self.sprite.isNull():
            QMessageBox.critical(self, "Error", f"Could not load sprite from path: {sprite_path}")
            sys.exit()  # Ensure that the application exits if the sprite fails to load

        self.sprite_width = self.sprite.width()
        self.sprite_height = self.sprite.height()

        # Player attributes
        self.player_x = 100  # Start in a more central position
        self.player_y = 500  # Position above the bottom
        self.velocity_x = 0
        self.velocity_y = 0
        self.gravity = 0.5
        self.jump_strength = -10
        self.is_jumping = False

        # Define platforms (QRect objects)
        self.platforms = [
            QRect(50, 600, 200, 20),  # Bottom-left platform
            QRect(300, 500, 200, 20),  # Middle platform
            QRect(600, 400, 200, 20),  # Top-right platform
        ]

    def paintEvent(self, event):
        painter = QPainter(self)
        
        # Draw platforms
        painter.setBrush(Qt.darkGray)
        for platform in self.platforms:
            painter.drawRect(platform)

        # Draw player sprite
        painter.drawPixmap(self.player_x, self.player_y, self.sprite_width, self.sprite_height, self.sprite)

    def keyPressEvent(self, event):
        try:
            # Movement and jump controls
            if event.key() == Qt.Key_A:
                self.velocity_x = -5
            elif event.key() == Qt.Key_D:
                self.velocity_x = 5
            elif event.key() in (Qt.Key_W, Qt.Key_Space) and not self.is_jumping:
                self.velocity_y = self.jump_strength
                self.is_jumping = True
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Key Press Error: {str(e)}")
            sys.exit()

    def keyReleaseEvent(self, event):
        # Stop horizontal movement when keys are released
        if event.key() in (Qt.Key_A, Qt.Key_D):
            self.velocity_x = 0

    def update_game(self):
        try:
            # Update player position and apply gravity
            self.player_x += self.velocity_x
            self.player_y += self.velocity_y
            self.velocity_y += self.gravity

            # Platform collision detection
            for platform in self.platforms:
                if (self.player_y + self.sprite_height >= platform.y() and
                    self.player_y + self.sprite_height <= platform.y() + 20 and
                    self.player_x + self.sprite_width > platform.x() and
                    self.player_x < platform.x() + platform.width()):
                    # Land on platform
                    self.player_y = platform.y() - self.sprite_height
                    self.velocity_y = 0
                    self.is_jumping = False

            # Collision with ground (bottom of the window)
            if self.player_y >= self.height() - self.sprite_height:
                self.player_y = self.height() - self.sprite_height
                self.velocity_y = 0
                self.is_jumping = False

            # Prevent going off-screen
            self.player_x = max(0, min(self.width() - self.sprite_width, self.player_x))

            # Refresh canvas
            self.repaint()
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Update Game Error: {str(e)}")
            sys.exit()

# Run the application
if __name__ == '__main__':
    main_menu = MainMenu()
    main_menu.show_gui()
