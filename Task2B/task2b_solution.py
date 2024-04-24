#python
roller = None
sjoint = None
d_motor = None
f_motor = None
roller = None
U = None
body = None
d_wheel = None
yaw_setpoint = 0
def sysCall_init():
    # do some initialization here
      global body
      body = sim.getObjectHandle('bike_respondable')
      global roller
      roller = sim.getObjectHandle('roller')
      global sjoint 
      sjoint = sim.getObjectHandle('spherical_joint')
      global f_motor
      f_motor = sim.getObjectHandle("front_motor")
      global d_motor
      d_motor = sim.getObjectHandle("drive_motor")
      global d_wheel
      d_wheel = sim.getObjectHandle("drivewheel_sphere")
      global ref
      ref = sim.getObjectHandle("reference_frame")
      pass

def sysCall_actuation():
    # put your actuation code here

    x1, x2, x3, x4 = sysCall_sensing()

    k = [-18.7, 18.2, 2, -49]
        
    U = -k[0]*x1 + k[1]*x2 - k[2]*x3 + k[3]*x4
    sim.setJointTargetVelocity(f_motor, (U))


    pass

def sysCall_sensing():
        # put your sensing code here
    global yaw_setpoint
    yaw_setpoint = sim.getFloatSignal("yaw_setpoint")
    print(yaw_setpoint)
    
    ori = sim.getObjectOrientation(body, ref)
    ypr = sim.alphaBetaGammaToYawPitchRoll(ori[0], ori[1], ori[2])
    
    #print("YPR")
    #print(ypr)
    
    ###
    l_v, a_v = sim.getObjectVelocity(body)
    #getObjectPose(body, ref)
    #print("a_V")
    #print(a_v)
    
    #print("tfvel")
    #print(tfvel)
    x1 = yaw_setpoint - a_v[2] 
    x2 = 0 - ypr[0]
    
        
    x3 = 0 - a_v[1]
    x4 = 0 - ypr[1]    
    
    
    return x1, x2, x3, x4
    pass

def sysCall_cleanup():
    # do some clean-up here
    pass
    # See the user manual or the available code snippets for additional callback functions and details
