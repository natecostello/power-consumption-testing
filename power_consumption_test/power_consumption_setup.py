"""This module contains the test fixture for power consumption testing."""

import os
from riden_monitor import RidenMonitor
from instrument_logger import InstrumentLogger

class PCTestFixture:
    """This is the test fixture"""
    def __init__(self) -> None:

        # power supply is required
        if not os.path.exists('/dev/ttyUSBrd6018'):
            raise ValueError('No Riden RD6018 Detected')
        powersupply_port = '/dev/ttyUSBrd6018'
        self._powersupply_monitor = RidenMonitor(port=powersupply_port)
        # self._powersupply_monitor.start()

        # setup logger
        self._logger = InstrumentLogger()
        self._logger.addinstrument(self._powersupply_monitor)

    @property
    def powersupply_monitor(self) -> RidenMonitor:
        """Accessor"""
        return self._powersupply_monitor

    @property
    def logger(self) -> InstrumentLogger:
        """Accessor"""
        return self._logger

    def start(self) -> None:
        """Starts any Instrument threads"""
        if self.powersupply_monitor:
            self.powersupply_monitor.start()

    def stop(self) -> None:
        """Stops any Instrument threads"""
        if self.powersupply_monitor:
            self.powersupply_monitor.stop()
