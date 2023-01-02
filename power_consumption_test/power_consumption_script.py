"""This script leverages PCTestFixture to record powersupply
parameters during a power consumption test. Power supply should
be set to appropriate voltage (and current), and enabled prior
to starting the script.  Secure logging prior to securing the
power supply and equipment under test to avoid invalidating
power consumption calculations."""

import time
from power_consumption_setup import PCTestFixture

test_fixture = PCTestFixture()

test_fixture.start()
time.sleep(1)
file_name = input('Enter the name of the test file')

if file_name != '':
    test_fixture.logger.filename = file_name
else:
    test_fixture.logger.filename = 'power_consumption'

print ('Starting to Log')

test_fixture.logger.start()

val = input('Enter any key to secure logging and stop the test:')
test_fixture.logger.stop()
