#создай приложение для запоминания информации
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from random import shuffle

class Question():
    def __init__(self, question, right_answer, wrong_1, wrong_2, wrong_3):
        self.question = question
        self.right_answer = right_answer
        self.wrong_1 = wrong_1
        self.wrong_2 = wrong_2
        self.wrong_3 = wrong_3
#создание приложения и главного окна
app = QApplication([])
main_win = QWidget()
main_win.resize(1000, 500)
main_win.setWindowTitle('Memory Card')
question = QLabel('Какой национальности не существует?')
RadioGroupBox = QGroupBox('Варианты ответов:')
rbtn_1 = QRadioButton('Энцы')
rbtn_2 = QRadioButton('Смурфы')
rbtn_3 = QRadioButton('Чулымцы')
rbtn_4 = QRadioButton('Алеуты')
answer_btn = QPushButton('Ответить')
#создаем линии: горизонтальные и вертикальные
layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()
layout_ans4 = QVBoxLayout()
#прикрепляем ответы к вертикальным линиям
layout_ans2.addWidget(rbtn_1, alignment = Qt.AlignCenter)
layout_ans2.addWidget(rbtn_2, alignment = Qt.AlignCenter)
layout_ans3.addWidget(rbtn_3, alignment = Qt.AlignCenter)
layout_ans3.addWidget(rbtn_4, alignment = Qt.AlignCenter)
#вертикальные линии прекрепляем к горизонтальным
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)
#заключаем в блок, группу
RadioGroupBox.setLayout(layout_ans1)
AnsRadioBox = QGroupBox('Результаты теста')
layout_q1 = QHBoxLayout()
layout_q2 = QHBoxLayout()
layout_q3 = QVBoxLayout()
result = QLabel('Правильно/неправильно')
right = QLabel('Правильный ответ')
layout_q1.addWidget(result)
layout_q2.addWidget(right, alignment = Qt.AlignHCenter)
layout_q3.addLayout(layout_q1)
layout_q3.addLayout(layout_q2)
AnsRadioBox.setLayout(layout_q3)
AnsRadioBox.hide()

def show_question():
    AnsRadioBox.hide()
    RadioGroupBox.show()
    answer_btn.setText('Ответить')
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)

def show_result():
    RadioGroupBox.hide()
    AnsRadioBox.show()
    answer_btn.setText('Следующий вопрос')

def show_start():
    if answer_btn.text() == 'Ответить':
        show_result()
    else:
        show_question()
answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]

def ask(question_, right_answer, wrong_1, wrong_2, wrong_3):
    shuffle(answers)
    answers[0].setText(right_answer)
    answers[1].setText(wrong_1)
    answers[2].setText(wrong_2)
    answers[3].setText(wrong_3)
    question.setText(question_)
    right.setText(right_answer)
    show_question()

def check_answer():
    if answers[0].isChecked():
        show_correct('Правильно!')
    elif answers[1].isChecked or answers[2].isChecked or answers[3].isChecked():
        show_correct('Неверно!')

def show_correct(res):
    result.setText(res)
    show_result()

ask('Государственный язык Бразилии:', 'Португальский', 'Испанский', 'Итальянский', 'Бразильский')
answer_btn.clicked.connect(check_answer)
layout_ans4.addWidget(question, alignment = Qt.AlignCenter)
layout_ans4.addWidget(RadioGroupBox, alignment = Qt.AlignCenter)
layout_ans4.addWidget(AnsRadioBox, alignment = Qt.AlignHCenter)
layout_ans4.addWidget(answer_btn, alignment = Qt.AlignCenter)
main_win.setLayout(layout_ans4)
main_win.show()
app.exec_()