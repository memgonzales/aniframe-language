# smaller and smaller circles
set CANVAS_BACKGROUND to "#000000"
set FRAME_RATE to 60
set CANVAS_WIDTH to 500
set CANVAS_HEIGHT to 500

marker = ellipse(250, 250, 300, 300) 

fr = 1
i = 0

repeat(6): 
    new_marker: Object = ellipse(250, 250, 300-i*10, 300-i*10) 
    marker += new_marker
    i += 1
    info(300-i*10)
    
    if i > 30:
        break
    
    repeat(6):
        info(300-i*10)
        new_marker: Object = ellipse(250, 250, 300-i*10, 300-i*10)
        marker += new_marker
        i += 1
        
        if i > 30:
            break

marker.resize(0.5, 1, 1500)
marker.resize(3, 500, 1500)

marker.draw(1, 1000)