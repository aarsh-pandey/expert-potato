import cv2 
import requests
import io

api_url = "https://api.ocr.space/parse/image"

response=None

def sendImageToAPI(frame):
    global response
    _ , compress = cv2.imencode(".jpg",frame,[1,90])
    file_bytes= io.BytesIO(compress)
    response = requests.post(api_url,files={"file.jpg":file_bytes},data={"apikey":"9bb5c5730e88957"})
    print(response.json().get("ParsedResults")[0].get("ParsedText"))

def captureFromPhone():
    vid = cv2.VideoCapture("http://192.168.43.1:8080/video") 
    
    while(True): 
        # Capture the video frame 
        # by frame 
        ret, frame = vid.read() 
        # Display the resulting frame 
        cv2.imshow('frame', frame) 
        
        # the 'q' button is set as the 
        # quitting button you may use any 
        # desired button of your choice 
        # if cv2.waitKey(1) == ord("q"):
            # break
        if cv2.waitKey(1) & 0xFF == ord('r'): 
            if(ret):
                img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                # cv2.imwrite("test.png",frame)
                sendImageToAPI(img)

                vid.release() 
                cv2.destroyAllWindows()

                return response.json().get("ParsedResults")[0].get("ParsedText")
                break
    
    # After the loop release the cap object 
    # print(frame.shape)
    vid.release() 
    # Destroy all the windows 
    cv2.destroyAllWindows()



if __name__ == "__main__":
    # captureFromPhone()
    img = cv2.imread("images.png")
    sendImageToAPI(img)