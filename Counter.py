# Title: Counter
# Author: LightingParatoner
# Description: A simple counter using PySide6 as GUI

#Imports
from PySide6.QtWidgets import QGridLayout, QWidget, QLabel, QPushButton, QSpinBox, QApplication
#

#Variables
Counted_Number = 0
#

#PyQt definitions
app = QApplication([])
app.setStyle("Fusion")
app.setApplicationDisplayName("Counter")
window = QWidget()
layout = QGridLayout()
#

#QWidget definitions
Counted_Number_Label = QLabel("Number: ")
Counted_Number_Value = QLabel(str(Counted_Number))
Count_Amount_Label = QLabel("Count Amount: ")
Count_Amount_Value = QSpinBox()
Count_Up_Button = QPushButton("Count up")
Count_Down_Button = QPushButton("Count down")
Reset_Button = QPushButton("Reset")
#

#Range
Count_Amount_Value.setRange(1,2147483646)
#

#Layout positions
layout.addWidget(Counted_Number_Label, 1, 1)
layout.addWidget(Counted_Number_Value, 1, 2)
layout.addWidget(Count_Amount_Label, 2, 1)
layout.addWidget(Count_Amount_Value, 2, 2)
layout.addWidget(Count_Down_Button, 3, 1)
layout.addWidget(Reset_Button, 3, 2)
layout.addWidget(Count_Up_Button, 3, 3)
#

#Functions
def Count_Up():
	global Counted_Number, Count_Amount
	Counted_Number = Counted_Number + Count_Amount_Value.value()
	Counted_Number_Value.setText(str(Counted_Number))
	
def Count_Down():
	global Counted_Number, Count_Amount
	Counted_Number = Counted_Number - Count_Amount_Value.value()
	Counted_Number_Value.setText(str(Counted_Number))

def Reset():
	global Counted_Number
	Counted_Number = 0
	Counted_Number_Value.setText(str(Counted_Number))

Count_Up_Button.clicked.connect(Count_Up)
Count_Down_Button.clicked.connect(Count_Down)
Reset_Button.clicked.connect(Reset)
#

#Execution
window.setLayout(layout)
window.show()
app.exec()
#