from PyQt6.QtWidgets import *
from gui import *


class Logic(QMainWindow, Ui_MainWindow):
    def __init__(self) -> None:
        """Initializes variables and buttons and puts radiobuttons in a group"""
        super().__init__()
        self.Total_Votes = 0
        self.Isabella = 0
        self.Genji = 0
        self.Hannah = 0
        self.setupUi(self)
        self.Vote_btn.clicked.connect(lambda: self.vote())
        self.clear_btn.clicked.connect(lambda: self.clear())
        self.button_group = QButtonGroup(self)
        self.button_group.addButton(self.Choice_1)
        self.button_group.addButton(self.Choice_2)
        self.button_group.addButton(self.Choice_3)

    def clear(self) -> None:
        """Clears textboxes and labels"""
        self.ID_input.setText("")

        self.result_label.setText("")
        self.result_label.setStyleSheet("color:black;")

        # Clear radio buttons properly
        self.button_group.setExclusive(False)
        self.Choice_1.setChecked(False)
        self.Choice_2.setChecked(False)
        self.Choice_3.setChecked(False)
        self.button_group.setExclusive(True)

    def vote(self) -> None:
        """Validates application and tells you who you voted for and the totals"""
        numbers = self.ID_input.text()

        # Validation checks
        if numbers == "":
            self.result_label.setStyleSheet("color:red;")
            self.result_label.setText("ID must not be blank")
            return

        elif not numbers.isdigit():
            self.result_label.setStyleSheet("color:red;")
            self.result_label.setText("ID must be numbers")
            return

        elif len(numbers) != 6:
            self.result_label.setStyleSheet("color:red;")
            self.result_label.setText("ID must be 6 numbers long")
            return

        elif self.button_group.checkedButton() is None:
            self.result_label.setStyleSheet("color:red;")
            self.result_label.setText("You must select a candidate")
            return

        # If we reach here, all validation passed
        if self.Choice_1.isChecked():
            self.Isabella += 1
            candidate = "Isabella"
        elif self.Choice_2.isChecked():
            self.Hannah += 1
            candidate = "Hannah"
        elif self.Choice_3.isChecked():
            self.Genji += 1
            candidate = "Genji"

        self.Total_Votes += 1
        self.result_label.setStyleSheet("color:black;")
        self.result_label.setText(
            f"Voted {candidate}\n"
            f"Total Votes {self.Total_Votes} Isabella: {self.Isabella} Genji: {self.Genji} Hannah: {self.Hannah}"
        )
