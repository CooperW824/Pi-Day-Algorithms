
from block import block

smallBlock = block(1, 0.0, 5)
powerOfhundred = int(input("Enter the power of one-hundred that dictates the large block's mass: "))
largeBlock = block(100**powerOfhundred, -5, 10)


delta_t = 0.1
collisions = 0

def calculateVelocities(m1, m2, u1, u2) -> list:
    v1 =  ((m1-m2)/(m1+m2))*u1 + ((2*m2)/(m1+m2))*u2
    v2 =  ((2*m1)/(m1+m2))*u1 + ((m2-m1)/(m1+m2))*u2
    return [v1, v2]


exit = False

while(not exit):
    smallBlock.updatePosition(delta_t)
    largeBlock.updatePosition(delta_t)
    if(largeBlock.getPosition() <= smallBlock.getPosition()):
        collisions += 1
        velocities = calculateVelocities(smallBlock.getMass(), largeBlock.getMass(), smallBlock.getVelocity(), largeBlock.getVelocity())
        smallBlock.updateVelocity(velocities[0])
        largeBlock.updateVelocity(velocities[1])
    if((smallBlock.getVelocity() >= 0 and largeBlock.getVelocity() >= 0) and largeBlock.getVelocity() - smallBlock.getVelocity() > 0 ):
        exit = True

collisions += smallBlock.getWallCollisions()

print("Collisions: " + str(collisions))


