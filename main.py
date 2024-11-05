from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QLineEdit
import random
class main_menu():
    def show_gui(self):
        app = QApplication([])

        self.hello = ["Yo","Wassup","Hello"]

        window = QWidget()
        window.setWindowTitle('Main Menu')

        layout = QVBoxLayout()
        
        placeholder_text = QLineEdit(self.hello[0])
        placeholder_text.setReadOnly(True)
        placeholder_text.move(20,20)
        placeholder_text.resize(200,40)
        layout.addWidget(placeholder_text)

        start_button = QPushButton('Start')
        start_button.resize(500,500)
        start_button.clicked.connect(lambda: placeholder_text.setText(random.choice(self.hello)))
        layout.addWidget(start_button)

        
        exit_button = QPushButton('Exit')
        exit_button.resize(500,500)
        exit_button.clicked.connect(app.quit)
        layout.addWidget(exit_button)
        window.resize(1280, 960)
        
        window.setLayout(layout)
        window.show()

        app.exec_()
        
        
if __name__ == '__main__':
    main_menu().show_gui()