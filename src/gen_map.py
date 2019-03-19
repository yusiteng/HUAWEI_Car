class Road:
    def __init__(self, id, length, speed, channel, begin,end, isDuplex):
        self.id = id
        self.length = length
        self.speed = speed
        self.channel = channel
        self.begin = begin
        self.end = end
        self.isDuplex = isDuplex

class Cross:
    def __init__(self,id, road1, road2, road3, road4):
        self.id = id
        self.roads = [road1, road2, road3, road4]
        self.neighbors = [-1,-1,-1,-1]
    def printt(self):
        print('id=',self.id,'roads=',self.roads,'neighbors=',self.neighbors)

class Car:
    def __init__(self,id,start,des,speed, planTime):
        self.id = id
        self.start = start
        self.dex= des
        self.speed = speed
        self.planTime = planTime
class Map:
    def __init__(self, crossfilepath, roadfilepath, carfilepath):
        crossinfolist = open(crossfilepath).readlines()
        crossinfolist[-1] += 'z'
        roadinfolist = open(roadfilepath).readlines()
        roadinfolist[-1] += 'z'
        carinfolist = open(carfilepath).readlines()
        carinfolist[-1] += 'z'
        self.crosslist = dict()
        self.roadlist = dict()
        self.carlist = dict()


        for roadinfo in roadinfolist[1:]:
            #print(roadinfo[1:-2].split(', '))
            id, length, speed, channel, begin, end, isDuplex = [int(x) for x in roadinfo[1:-2].split(', ')]
            self.roadlist[id] = Road(id,length,speed,channel,begin,end,isDuplex)
        for crossinfo in crossinfolist[1:]:
            id, road1, road2, road3, road4 = [int(x) for x in crossinfo[1:-2].split(', ')]
            self.crosslist[id] = Cross(id, road1,road2,road3,road4)
            i = 0
            for aroad in self.crosslist[id].roads:
                if aroad != -1:
                    self.crosslist[id].neighbors[i] = self.roadlist[aroad].begin if self.roadlist[aroad].begin != id else \
                    self.roadlist[aroad].end
            self.crosslist[id].printt()
        for carinfo in carinfolist[1:]:
            id, start, des, speed, planTime = [int(x) for x in carinfo[1:-2].split(', ')]
            self.carlist[id] = Car(id,start,des,speed, planTime)
        pass

if __name__ == '__main__':
    map =Map('1-map-training-1/cross.txt','1-map-training-1/road.txt','1-map-training-1/car.txt')
