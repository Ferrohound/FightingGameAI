import sys
from time import sleep
from py4j.java_gateway import JavaGateway, GatewayParameters, CallbackServerParameters, get_field
from BruceL33p import BruceL33p
from machete import Machete

def check_args(args):
        for i in range(argc):
		if args[i] == "-n" or args[i] == "--n" or args[i] == "--number":
			global GAME_NUM
			GAME_NUM = int(args[i+1])

def start_game():
	Bruce = BruceL33p(gateway)
	manager.registerAI("BruceL33p", Bruce)
	manager.registerAI("Machete", Machete(gateway))
	
	print("Opponent 1.")
	for i in range(GAME_NUM):
		print("Start game", i)
		game = manager.createGame("ZEN", "LUD", "BruceL33p", "RandomAI")
		manager.runGame(game)
		print("After game", i)
		sys.stdout.flush()
		
	print("Opponent 2.")
	for i in range(GAME_NUM):
		print("Start game", i)
		game = manager.createGame("ZEN", "ZEN", "BruceL33p", "MctsAi")
		manager.runGame(game)
	
		print("After game", i)
		sys.stdout.flush()
	
	print("Opponent 3.")
	for i in range(GAME_NUM):
		print("Start game", i)
		game = manager.createGame("ZEN", "LUD", "BruceL33p", "Machete")
		manager.runGame(game)
		print "nap time my dude!"
		Bruce.WriteQTable("QTable.txt")
		Bruce.WriteRTable("RTable.txt")
		sleep(60)
		print "RUDE AWAKENING *ANGERY*"
	
		print("After game", i)
		sys.stdout.flush()
	
	print("Training Complete.")	

def close_gateway():
	gateway.close_callback_server()
	gateway.close()
	
def main_process():
	check_args(args)
	start_game()
	close_gateway()

args = sys.argv
argc = len(args)
GAME_NUM = 1
gateway = JavaGateway(gateway_parameters=GatewayParameters(port=6000), callback_server_parameters=CallbackServerParameters(port=0))
python_port = gateway.get_callback_server().get_listening_port()
gateway.java_gateway_server.resetCallbackClient(gateway.java_gateway_server.getCallbackClient().getAddress(), python_port)
manager = gateway.entry_point

main_process()


