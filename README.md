# raspweathermonitor

Sensor de Umidade e Tempertura para dispositivos Raspberry. O raspweathermonitor expõem os resultados das medições em um Endpoint de uma REST API e que poderá ser consumida por outros sistemas.


## Componentes de hardware

O monitor ambiental é montado com os seguintes componentes de hardware:

1. Raspberry pi 3+
2. Protoboard
3. Sensor DHT11

### Montagem do sensor

Para a montagem do sensor ambiental é necessário conectar o Sensor DHT11 à pinagem do Raspberry. Para as ligações, identifique o pino de dados e de alimentação do DHT11. As conexões devem ser realizadas seguindo o seguinte esquema:

![RWM_esquema](https://user-images.githubusercontent.com/12073302/125294281-840bcf80-e2fa-11eb-8733-5ac51fb7290a.png)

Após montar o hardware, vamos à configuração dos softwares


## Componentes de Software

Para expor  parte de software vamos utilizar:

1. Raspberry Pi OS Lite (Kernel version: 5.10) [https://www.raspberrypi.org/software/operating-systems/]
2. Adafruit_Python_DHT [https://github.com/adafruit/Adafruit_Python_DHT]
3. Django [https://www.djangoproject.com/]
4. Django REST framework [https://github.com/encode/django-rest-framework/tree/master]

### Instalação do software

Instale o Raspberry Pi OS Lite de acordo com o tutorial disponível no site da distribuição:
https://www.raspberrypi.org/software/

Após instalar e atualizar o Sistema Operacional, instale o git, se ainda não tiver instalado:

```
$ sudo apt update
$ sudo apt install git
```

Instale os pacotes necessários para criar o ambientes virtuais no Python.

```
$ sudo apt install python3-venv
```

Clone o código do RaspWeatherMonitor e entre na pasta da aplicação:

```
$ git clone https://github.com/jscmenezes/raspweathermonitor.git
$ cd raspweathermonitor
```

Crie o ambiente python e ative-o:

```
$ python3 -m venv env_raspweathermonitor
$ source env_raspweathermonitor/bin/activate
```

Atualize o pip, gerenciador de pacotes do Python:

```
$ pip install --upgrade pip
```

Instale as dependências do RaspWeatherMonitor:

```
$ pip install -r requirements.txt
```

Para testar o funcionamento execute o script simpletest.py e o retorno deve mostrar a temperatura e a umidade medida pelo sensor:

```
$ python simpletest.py 
Temp=17.0*C  Humidity=92.0%
```


