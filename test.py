from main import *

player = make_hero(name="Вася Питонов", hp_now=2, money=200, inventory=[" изношенный меч", "поношенный шит", "изношенная кольчуга"])

game = True
while game:
	visit_hub(player)
