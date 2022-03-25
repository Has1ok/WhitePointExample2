def setup():
    global pointX,pointY, pointZ, deltaX, deltaY, deltaZ
    size(500,500)
    background(255)
    pointX = 1
    pointY = 1
    pointZ = 1
    deltaX = 1
    deltaY = 1
    deltaZ = 2
def draw():
    global pointX,pointY, pointZ, deltaX, deltaY, deltaZ
    pointX += random(1) * deltaX/2
    pointY += random(1) * deltaY/2
    pointZ += random(10) * deltaZ/4

    stroke(0,random(200),0)
    #line (pointX, pointY, pointZ, 1) 
    noFill()
    noStroke()
    line(pointX, pointY, pointZ, random(50))
    #line(pointX*2,pointY*5, pointZ*.5, random(20))
    stroke(0, 200, 0)
    bezier(pointX, pointY, pointZ, deltaX, deltaY, deltaZ, 15, 80)
    
    fill(pointZ*.6,0,0)
    noStroke()
    circle(pointX, pointY, pointZ/2)
   
    if pointY > 495:
        deltaY = -10
    if pointY < 3:
        deltaY = 5
    if pointX > 495:
        deltaX = -15
    if pointX < 3:
        deltaX = 5
    if pointZ > 495:
        deltaZ = -15
    if pointZ < 3:
        deltaZ = 3
    if pointX > 500: 
      save("result.jpg")
      exit ()

            
    
