from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QDialog, QStackedWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton
from PyQt5 import QtCore
from PyQt5.uic import loadUi
import sys
import random

class WelcomeScreen(QDialog):
    def __init__(self):
        super(WelcomeScreen, self).__init__()
        loadUi("welcomescreen.ui", self) 
        self.mode1btn.clicked.connect(self.gotomode1)
        self.mode2btn.clicked.connect(self.gotomode2)
        self.mode3btn.clicked.connect(self.gotomode3)
        
    def gotomode1(self):
        mode = mode1screen()
        widget.addWidget(mode)
        widget.setCurrentIndex(widget.currentIndex()+1)
        
    def gotomode2(self):
        mode = mode2screen()
        widget.addWidget(mode)
        widget.setCurrentIndex(widget.currentIndex()+1)
        
    def gotomode3(self):
        mode = mode3screen()
        widget.addWidget(mode)
        widget.setCurrentIndex(widget.currentIndex()+1)
      


class mode1screen(QDialog):
    def __init__(self):
        super(mode1screen, self).__init__()
        loadUi("mode1screen.ui",self)
        
        #################################################################
        #                                                               #
        #     change this part with actual question                     #
        #################################################################
        num = random.randint(2,300)
        mode = random.randint(1,2)
        #1 = range questions
        #2 = domain question 
        self.question.setText("num is "+ str(num))
        
        self.low_bound = QLineEdit(self)
        self.high_bound = QLineEdit(self)
        self.label = QLabel(self)
        self.label.setGeometry(70,520,600,90)
        if mode == 1:
            
            self.label.setText("The range of the function is           ,")
            self.low_bound.move(525,520)
            self.high_bound.move(635,520)
            self.go.clicked.connect(self.rangecheck)
            
        else:
            self.label.setText("The domain of the function is          ,")
            self.low_bound.move(530,520)
            self.high_bound.move(640,520)
            self.go.clicked.connect(self.domaincheck)
            
        self.label.setStyleSheet("color: white; border: none; font: 16pt 'MS Shell Dlg 2';")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        
        
        
        self.low_bound.resize(85,80)
        self.low_bound.setStyleSheet("color: black; background-color: white ; font: 18pt 'MS Shell Dlg 2'; border-radius: 12px")
        self.low_bound.setAlignment(QtCore.Qt.AlignCenter)
        
        
        
        self.high_bound.resize(85,80)
        self.high_bound.setStyleSheet("color: black; background-color: white ; font: 18pt 'MS Shell Dlg 2'; border-radius: 12px")
        self.high_bound.setAlignment(QtCore.Qt.AlignCenter)
        
        #############################
        
        self.home.clicked.connect(self.gohome)  
        self.skip.clicked.connect(self.gotomode1) 
        
        
                    
                    
        
    def gohome(self):
        mode = WelcomeScreen()
        widget.addWidget(mode)
        widget.setCurrentIndex(widget.currentIndex()+1)
        
    def gotomode1(self):
        mode = mode1screen()
        widget.addWidget(mode)
        widget.setCurrentIndex(widget.currentIndex()+1)
    
    def domaincheck(self):
            value = 2
            low = self.low_bound.text()
            high = self.high_bound.text()
            if value == 1:
                self.message.setText("Good job cunt")
            else:
                self.message.setText("You dumb cunt")
            
    def rangecheck(self):
            value = 2
            low = self.low_bound.text()
            high = self.high_bound.text()
            
            
                
                
            
            
            if value == 1:
                self.message.setText("Good job cunt")
            else:
                self.message.setText("You dumb cunt")   


class mode2screen(QDialog):
    answervalue = int
    
    def __init__(self):
        
        super(mode2screen, self).__init__()
        loadUi("mode2screen.ui",self)
        self.answervalue = 1
        
        
        #################################################################
        #                                                               #
        #     change this part with actual question                     #
        #################################################################
        num = random.randint(3, 99)
        self.question.setText("num is "+ str(num))
        
        ############################################
        self.home.clicked.connect(self.gohome) 
        self.skip.clicked.connect(self.gotomode2)
        self.choice.clicked.connect(self.btnbijective)
        self.go.clicked.connect(self.answercheck)
        
    def gohome(self):
        mode = WelcomeScreen()
        widget.addWidget(mode)
        widget.setCurrentIndex(widget.currentIndex()+1)
        
    def gotomode2(self):
        mode = mode2screen()
        widget.addWidget(mode)
        widget.setCurrentIndex(widget.currentIndex()+1)
        
    def btnbijective(self):
        self.choice.setText("Bijective")
        self.choice.clicked.connect(self.btnsurjective)
        self.answervalue = 2
        
        
    def btnsurjective(self):
        self.choice.setText("Surjective")
        self.choice.clicked.connect(self.btninjective)
        self.answervalue= 3
      
        
        
    def btninjective(self):
        self.choice.setText("Injective")
        self.choice.clicked.connect(self.btnbijective)
        self.answervalue = 1
        
    
    
    
    
        #################################################################
        #                                                               #
        #     change this part                                          #
        #################################################################  
    def answercheck(self):
        if self.answervalue == 2:
            self.message.setText("Good job cunt")
        else:
            self.message.setText("You dumb cunt")
           

        ################################    

        
        
        
class mode3screen(QDialog):
    def __init__(self):
        
        #################################################################
        #                                                               #
        #     change all these values, for 3rd scroll                   #
        #################################################################
        
        input_val = 3
        output_val = 9
        self.question_num = 3
        domain1 = "Z-R"
        domain2 = "R-R"
        
        ######################
        super(mode3screen, self).__init__()
        loadUi("mode3screen.ui",self)
        
        self.input.setText(str(input_val))
        self.output.setText(str(output_val))
        self.questions_label.setText(str(self.question_num))
        
        
        self.function1 = QLabel(self)
        self.function1.setGeometry(70,550,60,60)
        self.function1.setText("1")
        self.function1.setStyleSheet("color: white; background-color: rgb(79, 79, 79); font: 16pt 'MS Shell Dlg 2'; border-radius: 15px")
        self.function1.setAlignment(QtCore.Qt.AlignCenter)
        
        self.domain1 = QLabel(self)
        self.domain1.setGeometry(160,535,90,90)
        self.domain1.setText(domain1)
        self.domain1.setStyleSheet("color: black; background-color: white ; font: 18pt 'MS Shell Dlg 2'; border-radius: 15px")
        self.domain1.setAlignment(QtCore.Qt.AlignCenter)
        
        self.textbox1 = QLineEdit(self)
        self.textbox1.move(280,535)
        self.textbox1.resize(550,90)
        self.textbox1.setStyleSheet("color: black; background-color: white ; font: 18pt 'MS Shell Dlg 2'; border-radius: 15px")
        self.textbox1.setAlignment(QtCore.Qt.AlignCenter)
        
        
        self.function2 = QLabel(self)
        self.function2.setGeometry(70,665,60,60)
        self.function2.setText("2")
        self.function2.setStyleSheet("color: white; background-color: rgb(79, 79, 79); font: 16pt 'MS Shell Dlg 2'; border-radius: 15px")
        self.function2.setAlignment(QtCore.Qt.AlignCenter)
        
        self.domain2 = QLineEdit(self)
        self.domain2.setGeometry(160,650,90,90)
        self.domain2.setText(domain2)
        self.domain2.setStyleSheet("color: black; background-color: white ; font: 18pt 'MS Shell Dlg 2'; border-radius: 15px")
        self.domain2.setAlignment(QtCore.Qt.AlignCenter)
        
        self.textbox2 = QLineEdit(self)
        self.textbox2.move(280,650)
        self.textbox2.resize(550,90)
        self.textbox2.setStyleSheet("color: black; background-color: white ; font: 18pt 'MS Shell Dlg 2'; border-radius: 15px")
        self.textbox2.setAlignment(QtCore.Qt.AlignCenter)
        
        if self.question_num ==3:
            
            self.function3 = QLabel(self)
            self.function3.setGeometry(70,780,60,60)
            self.function3.setText("2")
            self.function3.setStyleSheet("color: white; background-color: rgb(79, 79, 79); font: 16pt 'MS Shell Dlg 2'; border-radius: 15px")
            self.function3.setAlignment(QtCore.Qt.AlignCenter)
            
            self.domain3 = QLineEdit(self)
            self.domain3.setGeometry(160,765,90,90)
            self.domain3.setText(domain2)
            self.domain3.setStyleSheet("color: black; background-color: white ; font: 18pt 'MS Shell Dlg 2'; border-radius: 15px")
            self.domain3.setAlignment(QtCore.Qt.AlignCenter)
            
            self.textbox3 = QLineEdit(self)
            self.textbox3.move(280,765)
            self.textbox3.resize(550,90)
            self.textbox3.setStyleSheet("color: black; background-color: white ; font: 18pt 'MS Shell Dlg 2'; border-radius: 15px")
            self.textbox3.setAlignment(QtCore.Qt.AlignCenter)
            
            
            
      
        
            
            
        self.go.clicked.connect(self.answercheck) 
        self.home.clicked.connect(self.gohome) 
        self.skip.clicked.connect(self.gotomode3)
    
        #################################################################
        #                                                               #
        #     change this part                                          #
        #################################################################  
    def answercheck(self):
        value = 2
        function1 = self.textbox1.text()
        function2 = self.textbox2.text()
        if self.question_num ==3:
            function3 = self.textbox3.text()
            
            
        
        
        if value == 1:
            self.message.setText("Good job cunt")
        else:
            self.message.setText("You dumb cunt")
            
    ################################################
    
    def gohome(self):
        mode = WelcomeScreen()
        widget.addWidget(mode)
        widget.setCurrentIndex(widget.currentIndex()+1)
        
    def gotomode3(self):
        mode = mode3screen()
        widget.addWidget(mode)
        widget.setCurrentIndex(widget.currentIndex()+1)
       
        
        


    

app = QApplication(sys.argv)
welcome = WelcomeScreen()
widget = QStackedWidget()
widget.addWidget(welcome)

widget.show()
sys.exit(app.exec())




