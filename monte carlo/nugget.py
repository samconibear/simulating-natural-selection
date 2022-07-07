import random

class unit:


    def __init__(self, ID, x, y, food, speed, energy, sight_range):
        self.ID=ID
        self.x=x
        self.y=y
        self.food=food
        self.speed=speed
        self.energy=energy
        self.sight_range=sight_range

    def move(self, fd, world_size):
        edge = world_size - 1
        if self.energy <= 0.5:  # running out of energy
            pass
        else:
            self.energy -= ((self.speed)**2)
            sr = []
            sight_area_limit = 2*self.sight_range
            x_ = self.x - self.sight_range
            y_ = self.y - self.sight_range
            while x_-self.x < self.sight_range+1: # creates the sight range
                sr.append([x_, self.y])
                for jj in range(self.sight_range):
                    yp = self.y + jj + 1
                    ym = self.y - jj - 1
                    sr.append([x_, yp])
                    sr.append([x_, ym])
                x_ += 1

            for ii in range(len(sr)):
                if sr[ii] in fd:
                    print('---------------------------',sr[ii])
                    if self.x < sr[ii][0]:
                        self.x += 1
                    if self.x > sr[ii][0]:
                        self.x -= 1
                    if self.y < sr[ii][1]:
                        self.y += 1
                    if self.y > sr[ii][1]:
                        self.y -= 1
                    else:
                        pass
                    break
                else: #if no food within sight range
                            #moving in x
                    if abs(self.x) == edge:
                        if self.x == edge:
                            self.x -= 1
                        else:
                            self.x += 1
                    else:
                        self.x += random.choice([1, -1, 0])
                    #moving in y
                    if abs(self.y) == edge:
                        if self.y == edge:
                            self.y -= 1
                        else:
                            self.y += 1
                    else:
                        self.y += random.choice([1, -1, 0])
            coords = (self.x, self.y)
            print(self.__dict__)
            if coords in fd:  # the eating of food
                self.food += 1
                w = fd.index((self.x, self.y))
                return w

    def show(self):
        return self.x , ',', self.y,'| Food:',self.food,'| Speed:',self.speed,self.energy