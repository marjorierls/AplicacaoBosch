import socket
import random
import time

def collect_data():
    # Geração de dados
    data = {
        "speed": random.randint(60, 120),
        "engine_temp": random.randint(70, 100),
        "tire_pressure_front_left": random.randint(28, 35),
        "tire_pressure_front_right": random.randint(28, 35),
        "tire_pressure_rear_left": random.randint(28, 35),
        "tire_pressure_rear_right": random.randint(28, 35),
        "fuel_level": random.randint(10, 50),
        "oil_pressure": random.randint(20, 80),
        "battery_voltage": random.uniform(11.5, 13.5),
        "engine_rpm": random.randint(1000, 5000)
    }
    return data

def send_data(data):
    try:
        # Conexão com o servidor
        server_address = ('localhost', 57224)
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect(server_address)
            # Enviar dados para o servidor
            s.sendall(str(data).encode())
    except Exception as e:
        print("Error while sending data:", e)

def main():
    count = 0
    while count < 10:
        # Pegar os dados
        data = collect_data()
        # Enviar os dados para o servidor
        send_data(data)
        time.sleep(5)
        count += 1

if __name__ == "__main__":
    main()
