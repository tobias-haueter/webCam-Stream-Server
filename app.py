from flask import Flask,render_template,Response
import cv2

app=Flask(__name__)

def generate_frames():
    camera = cv2.VideoCapture(0)
    while True:
            
        ## read the camera frame
        success,frame=camera.read()
        if not success:
            break
        else:
            ret,buffer=cv2.imencode('.jpg',frame)
            frame=buffer.tobytes()

        yield(b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video')
def video():
    return Response(generate_frames(),mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__=="__main__":
    #app.run(host="localhost", port=5000, debug=True)
    app.run(host="0.0.0.0", port=502, debug=True)


