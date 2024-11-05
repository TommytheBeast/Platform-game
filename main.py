from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout

class main_menu():
    def show_gui(self):
        app = QApplication([])

        window = QWidget()
        window.setWindowTitle('Main Menu')

        layout = QVBoxLayout()

        start_button = QPushButton('Start')
        layout.addWidget(start_button)
        window.resize(1280, 960)
        
        window.setLayout(layout)
        window.show()

        app.exec_()
        
if __name__ == '__main__':
    main_menu().show_gui()