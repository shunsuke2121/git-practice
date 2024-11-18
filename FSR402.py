import spidev
import time

# SPIの設定
spi = spidev.SpiDev()
spi.open(0, 0)
spi.max_speed_hz = 1000000

def read_adc(channel):
    if channel < 0 or channel > 1:
        return -1
    adc = spi.xfer2([1, (8 + channel) << 4, 0])
    data = ((adc[1] & 3) << 8) + adc[2]
    return data

try:
    while True:
        value = read_adc(0)
        voltage = value * 3.3 / 1023
        print(f"ADC Value: {value}, Voltage: {voltage:.2f}V")
        time.sleep(0.5)
except KeyboardInterrupt:
    spi.close()
