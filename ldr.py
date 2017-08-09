from gpiozero import LightSensor

ldr =  LightSensor(23)
i=0
while True:
    #ldr.wait_for_light()
    #i+=1
    #print("Light detected! ",i)
    if (ldr.wait_for_light()):
        i+=1
        print("Light detected! ",i)
    if (ldr.wait_for_dark()):
        i+=1
        print("No light detected",i)

    

