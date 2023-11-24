import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout
from PyQt5.QtGui import QPixmap
import random

class RockPaperScissorsGame(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Камень, ножницы, бумага')
        self.setGeometry(100, 100, 400, 300)

        self.user_choice_label = QLabel('Ваш выбор:')
        self.computer_choice_label = QLabel('Выбор компьютера:')
        self.result_label = QLabel('Результат:')

        self.user_choice_button = QPushButton('Камень')
        self.user_choice_button.clicked.connect(lambda: self.make_choice('камень'))

        self.scissors_button = QPushButton('Ножницы')
        self.scissors_button.clicked.connect(lambda: self.make_choice('ножницы'))

        self.paper_button = QPushButton('Бумага')
        self.paper_button.clicked.connect(lambda: self.make_choice('бумага'))

        layout = QVBoxLayout()
        layout.addWidget(self.user_choice_label)
        layout.addWidget(self.user_choice_button)
        layout.addWidget(self.scissors_button)
        layout.addWidget(self.paper_button)
        layout.addWidget(self.computer_choice_label)
        layout.addWidget(self.result_label)

        self.setLayout(layout)

    def get_computer_choice(self):
        return random.choice(['камень', 'ножницы', 'бумага'])

    def determine_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return 'Ничья!'
        elif (
            (user_choice == 'камень' and computer_choice == 'ножницы') or
            (user_choice == 'ножницы' and computer_choice == 'бумага') or
            (user_choice == 'бумага' and computer_choice == 'камень')
        ):
            return 'Вы победили!'
        else:
            return 'Компьютер победил!'

    def make_choice(self, user_choice):
        computer_choice = self.get_computer_choice()

        user_choice_label = f'Ваш выбор: {user_choice}'
        computer_choice_label = f'Выбор компьютера: {computer_choice}'
        result = self.determine_winner(user_choice, computer_choice)

        self.user_choice_label.setText(user_choice_label)
        self.computer_choice_label.setText(computer_choice_label)
        self.result_label.setText(result)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    game = RockPaperScissorsGame()
    game.show()
    sys.exit(app.exec_())