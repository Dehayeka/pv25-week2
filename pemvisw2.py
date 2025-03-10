from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QFormLayout, QLabel,
    QLineEdit, QRadioButton, QPushButton, QGroupBox, QComboBox, QTextEdit
)
import sys

class RegistrationForm(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Week 2 : Layout - User Registration Form")
        
        main_layout = QVBoxLayout()
        
        # Identitas Section
        identity_group = QGroupBox("Identitas (vertical box layout)")
        identity_layout = QVBoxLayout()
        identity_text = QTextEdit("Nama : nama_anda\nNim : nim_anda\nKelas : kelas_anda")
        identity_text.setReadOnly(True)
        identity_layout.addWidget(identity_text)
        identity_group.setLayout(identity_layout)
        
        # Navigation Section
        nav_group = QGroupBox("Navigation (horizontal box layout)")
        nav_layout = QHBoxLayout()
        home_btn = QPushButton("Home")
        about_btn = QPushButton("About")
        contact_btn = QPushButton("Contact")
        nav_layout.addWidget(home_btn)
        nav_layout.addWidget(about_btn)
        nav_layout.addWidget(contact_btn)
        nav_group.setLayout(nav_layout)
        
        # User Registration Section
        reg_group = QGroupBox("User Registration (form layout)")
        reg_layout = QFormLayout()
        full_name = QLineEdit()
        email = QLineEdit()
        phone = QLineEdit()
        gender_male = QRadioButton("Male")
        gender_female = QRadioButton("Female")
        country = QComboBox()
        country.addItems(["Select", "USA", "UK", "India", "Germany", "France"])
        
        gender_layout = QHBoxLayout()
        gender_layout.addWidget(gender_male)
        gender_layout.addWidget(gender_female)
        
        reg_layout.addRow("Full Name:", full_name)
        reg_layout.addRow("Email:", email)
        reg_layout.addRow("Phone:", phone)
        reg_layout.addRow("Gender:", gender_layout)
        reg_layout.addRow("Country:", country)
        reg_group.setLayout(reg_layout)
        
        # Actions Section
        action_group = QGroupBox("Actions (horizontal box layout)")
        action_layout = QHBoxLayout()
        submit_btn = QPushButton("Submit")
        cancel_btn = QPushButton("Cancel")
        action_layout.addWidget(submit_btn)
        action_layout.addWidget(cancel_btn)
        action_group.setLayout(action_layout)
        
        # Add sections to main layout
        main_layout.addWidget(identity_group)
        main_layout.addWidget(nav_group)
        main_layout.addWidget(reg_group)
        main_layout.addWidget(action_group)
        
        self.setLayout(main_layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = RegistrationForm()
    window.show()
    sys.exit(app.exec_())