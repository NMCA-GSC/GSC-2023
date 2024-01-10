import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QListWidget
from PyQt5.QtBluetooth import QBluetoothDeviceDiscoveryAgent, QBluetoothDeviceInfo

class BluetoothApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Bluetooth App")
        self.setGeometry(100, 100, 400, 400)

        self.device_list = QListWidget(self)

        self.discover_button = QPushButton("Discover Devices", self)
        self.discover_button.clicked.connect(self.discover_devices)

        layout = QVBoxLayout()
        layout.addWidget(self.device_list)
        layout.addWidget(self.discover_button)
        self.setLayout(layout)

        self.discovery_agent = QBluetoothDeviceDiscoveryAgent(self)
        self.discovery_agent.deviceDiscovered.connect(self.device_discovered)

    def discover_devices(self):
        self.device_list.clear()
        self.discovery_agent.start()

    def device_discovered(self, device_info):
        name = device_info.name()
        address = device_info.address().toString()
        self.device_list.addItem(f"{name} ({address})")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = BluetoothApp()
    window.show()
    sys.exit(app.exec_())
