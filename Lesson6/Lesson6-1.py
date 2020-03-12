from time import sleep
class TrafficLight:
    color = "NoColor"
    def running(self):
        i = 1
        while True:
            print("Красный")
            sleep(7)
            print("Желтый")
            sleep(2)
            print("Зеленый")
            sleep(2)
            i +=1
            if i ==10:
                break


trafficLight = TrafficLight()
trafficLight.running()