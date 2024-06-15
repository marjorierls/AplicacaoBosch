import socket
import mysql.connector

# Configurações do banco de dados
host = 'localhost'
user = 'usuario'
password = '123456'
database = 'vehicledata'

def save_data(data):
    # Salvar os dados no MySQL
    conn = mysql.connector.connect(host=host, user=user, password=password, database=database)
    cursor = conn.cursor()
    insert_query = '''
        INSERT INTO vehicle_data 
        (speed, engine_temp, tire_pressure_front_left, tire_pressure_front_right, 
        tire_pressure_rear_left, tire_pressure_rear_right, fuel_level, oil_pressure, 
        battery_voltage, engine_rpm) 
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    '''
    cursor.execute(insert_query, (data["speed"], data["engine_temp"], data["tire_pressure_front_left"],
                                   data["tire_pressure_front_right"], data["tire_pressure_rear_left"],
                                   data["tire_pressure_rear_right"], data["fuel_level"], data["oil_pressure"],
                                   data["battery_voltage"], data["engine_rpm"]))
    conn.commit()
    conn.close()

def main():
    # Start TCP server to receive data from collector
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('localhost', 57224))
        s.listen()
        print("O servidor está esperando pela conexão...")
        while True:
            conn, addr = s.accept()
            with conn:
                print('Conectado por: ', addr)
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break
                    # Decodificar os dados
                    received_data = eval(data.decode())
                    # Dados salvos no banco de dados
                    save_data(received_data)
                    print("Data received and saved:", received_data)

if __name__ == "__main__":
    main()
