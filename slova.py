import sys
import random
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout

class GuessNumberApp(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Искусственный Интеллект: Угадай число')
        self.setGeometry(300, 300, 300, 200)

        self.secret_number = random.randint(1, 100)
        self.attempts = 0

        self.label = QLabel('Введите число от 1 до 100:')
        self.input_box = QLineEdit(self)
        self.button = QPushButton('Проверить', self)
        self.button.clicked.connect(self.check_guess)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.input_box)
        layout.addWidget(self.button)

        self.setLayout(layout)

    def check_guess(self):
        try:
            guess = int(self.input_box.text())
            self.attempts += 1

            if guess == self.secret_number:
                self.label.setText(f'Поздравляю! Вы угадали число {self.secret_number} за {self.attempts} попыток.')
            elif guess < self.secret_number:
                self.label.setText('Нет, попробуйте большее число.')
            else:
                self.label.setText('Нет, попробуйте меньшее число.')
        except ValueError:
            self.label.setText('Пожалуйста, введите целое число.')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = GuessNumberApp()
    window.show()
    sys.exit(app.exec_())