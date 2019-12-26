######################################################################
#    FUNÇÃO SCRIPT.: CRIAR USUÁRIO SONICWALL VIA TERMINAL            #
#------------------------------------------------------------------- #
#                                                                    #
#       DESENVOLVIMENTO.: BRUNO GABRIEL			                         #
#       EMAIL.: BRUDARKO@GMAIL.COM  	                               #
#       DATA CRIACAO.: 26/12/2019                                    #
#       VERSAO.: 1.0_201912						                               #
#                                               		                 #
######################################################################
#
import paramiko
import time #

# Informações
fwSshPort = '22' # Porta SSH
fwUser = 'admin' # Nome do administrador atual
fwPass = 'password' # Senha do administrador atual

def exec():
	try:
		fwIp = input("\nQual o IP do SonicWALL?\n")
	# Conexão SSH.
		client = paramiko.SSHClient()
		client.load_system_host_keys()
		client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		client.connect(fwIp, port=fwSshPort, username=fwUser, password=fwPass, look_for_keys=False)
	# Cria o canal.
		sendchannel = client.invoke_shell()
	# Envia o comando.
		sendchannel.sendall('configure\n')
		time.sleep(2)
		sendchannel.sendall('\ruser local\n')
		time.sleep(2)
		sendchannel.sendall('\ruser User password Password member-of "SonicWALL Administrators"\n')
		time.sleep(2)
		sendchannel.sendall('\rcommit\n')
		time.sleep(1)
		print("\nUsuário criado com sucesso.")
	# Fecha o canal.
		sendchannel.close()
		print("\nConexão encerrada.")
	finally:
		client.close()

if __name__ == '__main__':
	exec()
