# Carrega as bibliotecas
import Adafruit_DHT
import RPi.GPIO as GPIO
import time

# Define o tipo de sensor
sensor = Adafruit_DHT.DHT22

# Seta o modo de entrada de dados e define o pino GPIO em que o sensor está conectado
GPIO.setmode(GPIO.BOARD)
pino_sensor = 23

# Inicializa as variáveis em que serão armazenados os dados lidos do sensor
umid_anterior = 0;
temp_anterior = 0;

# Abre o arquivo TXT para a gravação dos logs de leitura do sensor
arq = open("data.txt", "w")

# Looping de coleta de dados do sensor
while(1):
    
    # Realiza a leitura dos dados do sensor
    umid, temp = Adafruit_DHT.read_retry(sensor, pino_sensor);
    
    # Verifica a ocorrência de possíveis erros na leitura
    if umid is not None and temp is not None:
        # Realiza a formatação dos dados lidos pelo sensor e printa na console
        print ("Temp = {0:0.1f}  Umidade = {1:0.1f}\n").format(temp, umid);
        print ("Proxima leitura em 5 minutos...\n");
        
        # Inicia a concatenação do texto a ser gravado no arquivo de Log.
        arq.write(time.strftime('%d %b %y  %H:%M:%S'));
        texto = ("   Temp = {0:0.1f}  Umidade = {1:0.1f}\n").format(temp, umid);
        
        # Grava o texto no arquivo de Log
        arq.write(texto);
        arq.write("\n");
    
    else:
        # Informa erro na leitura dos dados do sensor
        print("Erro na leitura dos dados do sensor !!!")
    
    # Delay de 5 minutos entre leituras
    time.sleep(300);