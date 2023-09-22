import sys
from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QGridLayout, QLineEdit, QPushButton, QComboBox


class SpeedCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Speed Calculator")
        grid = QGridLayout()

        # Create Widgets
        distance_label = QLabel("Distance")
        self.distance_line_edit = QLineEdit()
        self.combo_box = QComboBox()
        self.combo_box.addItems(["Metric(km)", "Imperial(miles)"])
        time_label = QLabel("Time in hours")
        self.time_line_edit = QLineEdit()
        calculate_button = QPushButton("Calculate ")
        calculate_button.clicked.connect(self.calculate_speed)
        self.output_label = QLabel("")

        # Add widgets to grid
        grid.addWidget(distance_label, 0, 0)
        grid.addWidget(self.distance_line_edit, 0, 1)
        grid.addWidget(self.combo_box, 0, 2)
        grid.addWidget(time_label, 1, 0)
        grid.addWidget(self.time_line_edit, 1, 1)
        grid.addWidget(calculate_button, 2, 1)
        grid.addWidget(self.output_label, 3, 0, 1, 3)

        self.setLayout(grid)

    def calculate_speed(self):
        if self.combo_box.currentText() == "Metric(km)":
            distance = float(self.distance_line_edit.text())
            time = float(self.time_line_edit.text())
            speed = distance / time
            unit = "km/h"
        else:
            distance = float(self.distance_line_edit.text())
            time = float(self.time_line_edit.text())
            speed = distance / (time * 1.6)
            unit = "miles/h"
        self.output_label.setText(f"Average Speed: {round(speed,2)} {unit}")


app = QApplication(sys.argv)
speed_calculator = SpeedCalculator()
speed_calculator.show()
sys.exit(app.exec())

