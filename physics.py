def a(mass, acceleration):
    force =mass*acceleration
    print(f'force = {force}N')
a(1000,30)

def b(distance, time):
    speed =distance / time
    print(f"spped = {speed}m/s")
b(300,60)

def c(initial_velocity, final_velocity, time):
    acceleration = (final_velocity-initial_velocity)/time
    print(f'acceleration = {acceleration}m/s^2')
c(40,25, 24)

def  d(force,distance):
    work = force*distance
    print(f'work = {work}J')
d(50,25)

def e(displacement,time):
    velocity=displacement/time
    print(f'velocity={velocity}m/s')
e(500,20)