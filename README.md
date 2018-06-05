## Vortice Mock
Prerequisiti:

    python3 
    pip
    
Per scaricare le dipendenze
    
    pip install -r requirements.txt
          
Per lanciare il server con bonjour:

    ./runserver-bonjour.py


Metodi: 

Connect to WiFi

    --> POST /connect
    
    request body:
    {
      "ssid": "Officina_Network",
      "password": "password"
    }
    response code: 204
    response body: <empty>
    

Check WiFi status

    --> GET /check
    
    request parameters: []
    response code: 204
    response body: <empty>
    

Hello

    --> GET /hello
    
    request parameters: []
    response code: 200
    response body:
    {
      "serial": "1234567890",
      "model": {
        "version": "1",
        "type": "asdf"
      },
      "firmware": "asdf"
    }
    
    
Register to MQTT

    --> POST /register
    
    request body:
    {
      "serial": "1234567890",
      "topic": "asdf",
      "certificate": "asdf",
      "privateKey": "asdf"
    }
    response code: 204
    response body: <empty>
