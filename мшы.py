import sys
import random
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox

class HangmanApp(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Виселица')
        self.setGeometry(300, 300, 300, 200)

        self.words = ['python', 'hangman', 'game', 'pyqt', 'programming']
        self.secret_word = random.choice(self.words)
        self.display_word = ['_' for _ in self.secret_word]

        self.label = QLabel(f'Слово: {" ".join(self.display_word)}', self)
        self.input_box = QLineEdit(self)
        self.button = QPushButton('Угадать букву', self)
        self.button.clicked.connect(self.guess_letter)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.input_box)
        layout.addWidget(self.button)

        self.setLayout(layout)

        self.attempts_left = 6

    def guess_letter(self):
        letter = self.input_box.text().lower()

        if len(letter) != 1 or not letter.isalpha():
            QMessageBox.warning(self, 'Некорректный ввод', 'Пожалуйста, введите одну букву.')
            return

        if letter in self.secret_word:
            for i, char in enumerate(self.secret_word):
                if char == letter:
                    self.display_word[i] = letter

            self.label.setText(f'Слово: {" ".join(self.display_word)}')

            if '_' not in self.display_word:
                QMessageBox.information(self, 'Поздравляю!', 'Вы угадали слово!')
                self.reset_game()
        else:
            self.attempts_left -= 1
            if self.attempts_left == 0:
                QMessageBox.information(self, 'Конец игры', f'Вы проиграли! Загаданное слово было: {self.secret_word}')
                self.reset_game()

        self.input_box.clear()

    def reset_game(self):
        self.secret_word = random.choice(self.words)
        self.display_word = ['_' for _ in self.secret_word]
        self.label.setText(f'Слово: {" ".join(self.display_word)}')
        self.attempts_left = 6

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = HangmanApp()
    window.show()
    sys.exit(app.exec_())