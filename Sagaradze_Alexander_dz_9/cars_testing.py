from task_9_4 import *

police_suv = PoliceCar(100, 'black and white', 'Dodge Charger SRT-8')
saleen = SportCar(180, 'yellow', 'Saleen S7')
chevrolet = TownCar(65, 'brown', 'Chevrolet Orlando')
kamaz = WorkCar(40, 'orange', 'Mosvodokanal Kamaz')

police_suv.turn('left')
police_suv.go()
police_suv.turn('right')
police_suv.stop()

print(saleen.name, 'police: ', saleen.is_police)
saleen.show_speed()

kamaz.show_speed()
chevrolet.show_speed()