# AplicacaoBosch
Esta aplicação foi feita na linguagem Python e contém uma pasta com dois arquivos que devem ser rodados em conjunto (server.py e collector.py), segue passo a passo de como aplicar:
O servidor de código aberto:
  - Para os dados serem enviados a partir da aplicação, deve-se instalar primeiro o XAMPP que vai ser onde o servidor será rodado
  - Após a instalação, abra o aplicativo, localize os módulos Apache e MySQL, clique no botão "**START**" de ambos
  - No módulo do MySQL, selecione o botão "**Admin**" para abrir o phpMyAdmin na web
  - No phpMyAdmin, crie um banco de dados com o nome de **vehicledata**, com uma tabela de nome **vehicle_data** e com as seguintes colunas (speed, engine_temp, tire_pressure_front_left, tire_pressure_front_right, tire_pressure_rear_left, tire_pressure_rear_right, fuel_level, oil_pressure, battery_voltage, engine_rpm), todas com dados **INT**
  - Após o passo anterior, ir para a tela **Home**, acessar a aba de **Contas de Usuários** e criar um novo usuário com as seguintes informações:
      - Nome do usuário: usuario, senha: 123456, nome do host: localhost
  - Após inserir essas informações habilite, todas as caixas de seleção e execute

Como rodar a aplicação no Python:
- 1º abra o Visual Studio Code
- 2º Aperte Ctrl+ K e abra a pasta dentro do aplicativo
- 3º Alterações **server.py**:
  - Baixar as bibliotecas socket, mysql.connector
  - Alterar os campos host = 'localhost', user = 'usuario', password = '123456', baseando nas informações criadas na criação do usuário, host e senha no phpMyAdmin
  - Ao rodar o server.py no terminal, ele dará as informações "Connected by ('127.0.0.1', 57224)", o segundo número deverá ser aplicado na linha 31
    -> s.bind(('localhost', 57224))
- 4º Alterações **collector.py**:
  - Alterar o server_address = ('localhost', 57224) na linha 23, com as mesmas informações do server.py
