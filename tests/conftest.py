import logging
import subprocess
import time

import pytest
from appium import webdriver

from utils.android_utils import android_get_desired_capabilities


@pytest.fixture(scope='session')
def run_appium_server():
    subprocess.Popen(
        ['appium', '-a', '0.0.0.0', '-p', '4723', '--allow-insecure', 'adb_shell'],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        stdin=subprocess.DEVNULL,
        shell=True
    )
    time.sleep(5)
    # я вручну запускав сервер через "Appium Server GUI" перед запуском тестів


@pytest.fixture(scope='session')
def get_udid():
    logging.info('Connected device detection')
    adb_devices_list = subprocess.check_output('adb devices').decode('utf-8').split('\n')[1:]
    devices_count = len([item for item in adb_devices_list if '\tdevice' in item])
    if devices_count:
        logging.info(f'{devices_count} device{"s" if devices_count > 1 else ""} found')
        # якщо під'єднано декілька пристроїв, буде выбрано udid першого в списку
        udid = adb_devices_list[0].split('\t')[0]
        logging.info(f'Got {udid} device UDID') if udid else logging.critical('UDID detection failed')

        return udid
    else:
        logging.critical('No device connected')


@pytest.fixture(scope='session')
def driver(run_appium_server, get_udid):
    driver = webdriver.Remote('http://localhost:4723/wd/hub', android_get_desired_capabilities(get_udid))
    logging.info('Driver created') if driver else logging.critical('Driver creation failed')
    yield driver
    driver.quit()
    logging.info('Driver stopped')
