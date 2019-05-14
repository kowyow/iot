#!/usr/bin/env python3
from rpi_rf import RFDevice

rfdevice = RFDevice(17)
rfdevice.enable_tx()
rfdevice.tx_repeat = 5
rfdevice.tx_code(1688168, 1, 350, 24)
rfdevice.cleanup()
