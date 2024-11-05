from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout
import random
class main_menu():
    def show_gui(self):
        app = QApplication([])

        self.hello = ["Yo","Wassup","Hello"]

        window = QWidget()
        window.setWindowTitle('Main Menu')

        layout = QVBoxLayout()

        start_button = QPushButton('Start')
        start_button.resize(500,500)
        layout.addWidget(start_button)
        start_button.clicked.connect(self.start_prompt)
        
        exit_button = QPushButton('Exit')
        exit_button.resize(500,500)
        exit_button.clicked.connect(app.quit)
        layout.addWidget(exit_button)
        window.resize(1280, 960)
        
        window.setLayout(layout)
        window.show()

        app.exec_()
        
    def start_prompt(self):
        self.text.setText(random.choice(self.hello))
        
if __name__ == '__main__':
    main_menu().show_gui()