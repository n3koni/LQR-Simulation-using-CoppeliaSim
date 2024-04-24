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

    k = [ -17.7, 9.2, 2, -55.2]
    
    global U 
    U = -k[0]*x1 + k[1]*x2 - k[2]*x3 + k[3]*x4
    
    sim.setJointTargetVelocity(f_motor, (U))


    pass

def sysCall_sensing():
# put your sensing code here
    ori = sim.getObjectOrientation(body, ref)
    ypr = sim.alphaBetaGammaToYawPitchRoll(ori[0], ori[1], ori[2])
    sim.setFloatSignal("yaw_setpoint", 0.03)
    global yaw_setpoint
    ys= sim.getFloatSignal("yaw_setpoint")
    
    
    
    l_v, a_v = sim.getObjectVelocity(body)
    x1 = 0 - a_v[2] 
    x2 = yaw_setpoint - ypr[0]
    
        
    x3 = 0 - a_v[1]
    x4 = 0 - ypr[1] 
    
    message,data,data2 = sim.getSimulatorMessage()
         ############### Keyboard Input ##############

    if (message == sim.message_keypress):    
        
        if (data[0]==2007): # forward up arrow
            drive_speed = sim.setJointTargetVelocity(d_motor, -7)
            

        if (data[0]==2008): # backward down arrow
            drive_speed = sim.setJointTargetVelocity(d_motor, 7)#add drive wheel speed here
            
            
        if (data[0]==2009): # left arrow key
            yaw_setpoint = ypr[0] + ys

            #change yaw_setpoint for required turning over here
                
        if (data[0]==2010): # right arrow key
            yaw_setpoint = ypr[0] + (-ys)

            
        if (data[0]==115):
            drive_speed = sim.setJointTargetVelocity(d_motor, 0)
            yaw_setpoint = ypr[0]
            
        
    #else:
        #sim.setFloatSignal("yaw_setpoint", 0)
        #drive_speed = sim.setJointTargetVelocity(d_motor, 10)# This is an example, decide what's best
        #ds = sim.getJointTargetVelocity(d_motor)
        #print(ds)
        #abc = ypr[0] + yaw_setpoint
        
        #print(ypr[0])
        # # This is an example, decide what's best
        
    

    
    #########################################
    return x1, x2, x3, x4
    
    pass

def sysCall_cleanup():
    # do some clean-up here
    pass
    # See the user manual or the available code snippets for additional callback functions?and?details
