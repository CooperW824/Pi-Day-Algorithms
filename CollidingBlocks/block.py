

class block:
    mass = 0.0
    velocity = 0.0
    position = 0.0
    wallCollisions = 0

    def __init__(self, mass, vel, pos) -> None:
        self.mass= mass
        self.velocity = vel
        self.position = pos

    def updatePosition(self, delta_t):
        self.position += self.velocity*delta_t
        if self.position <= 0:
            self.velocity = self.velocity *-1
            self.wallCollisions += 1
            self.position = 0

    def updateVelocity(self, new_vel):
        self.velocity = new_vel

    def setPosition(self, new_pos):
        self.position = new_pos

    def getPosition(self):
        return self.position

    def getVelocity(self):
        return self.velocity
    
    def getMass(self):
        return self.mass

    def getWallCollisions(self):
        return self.wallCollisions
