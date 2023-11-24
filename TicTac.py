import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QMessageBox, QHBoxLayout

class TicTacToeApp(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Крестики-нолики')
        self.setGeometry(300, 300, 300, 300)

        self.buttons = [(QPushButton(' '))*3 for _ in range(3)]

        layout = QVBoxLayout()

        for row in self.buttons:
            button_row = QHBoxLayout()
            for button in row:
                button_row.addWidget(button)
                button.clicked.connect(self.on_button_click)
            layout.addLayout(button_row)

        self.setLayout(layout)

        self.current_player = 'X'

    def on_button_click(self):
        button = self.sender()

        if button.text() == ' ':
            button.setText(self.current_player)

            if self.check_winner():
                QMessageBox.information(self, 'Победа!', f'Игрок {self.current_player} победил!')
                self.reset_board()
            else:
                self.current_player = 'O' if self.current_player == 'X' else 'X'

    def check_winner(self):
        # Проверка по горизонтали, вертикали и диагоналям
        for i in range(3):
            if self.buttons[i][0].text() == self.buttons[i][1].text() == self.buttons[i][2].text() != ' ':
                return True
            if self.buttons[0][i].text() == self.buttons[1][i].text() == self.buttons[2][i].text() != ' ':
                return True
        if self.buttons[0][0].text() == self.buttons[1][1].text() == self.buttons[2][2].text() != ' ':
            return True
        if self.buttons[0][2].text() == self.buttons[1][1].text() == self.buttons[2][0].text() != ' ':
            return True
        return False

    def reset_board(self):
        for row in self.buttons:
            for button in row:
                button.setText(' ')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = TicTacToeApp()
    window.show()
    sys.exit(app.exec_())
