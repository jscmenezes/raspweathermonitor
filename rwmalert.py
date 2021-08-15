import Adafruit_DHT
from time import sleep
from subprocess import call

sensor = Adafruit_DHT.DHT11
pin = 17

def getHumidity():
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)    
    return humidity

def getTemperature():
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    return temperature


if (__name__ == '__main__'):
    while True:
        temperatura = getTemperature()
        umidade = getHumidity()
        if temperatura < 10 or temperatura > 25:
            call(["telegram-send", 'Alerta de Temperatura!!! \n Temp = {0:0.1f}*C'.format(temperatura)])

        if umidade > 95 or umidade < 60:
            call(["telegram-send", 'Alerta de Umidade!!! \n Umidade = {0:0.1f}%'.format(umidade)])

        sleep(300)
