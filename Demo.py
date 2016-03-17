import httplib
from time import sleep
import picamera
from RPi import GPIO
from subprocess import call
import os
conn=None
data=None
Global_Confidence = 0.0

body="{\"personGroupId\":\"123456\",\"faceIds\":[ \"23bb2de8-7ef6-4c49-a828-7bdd410bfc89\"],\"maxNumOfCandidatesReturned\":1}";

headers = {
    # Request headers
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': '58b001fc0d6648d9a836e289e893acdc'
}


###########################################
def FileUpload(Path):
	return

def FaceDetect(url):
  
    found_conf = False
    facedetectbody="{\"url\":\"https://raw.githubusercontent.com/rajeshkulandaivel/ImageServer/master/image.jpg\"}";
    conn = httplib.HTTPSConnection('api.projectoxford.ai')    
    conn.request("POST", "/face/v1.0/detect?returnFaceId=true&returnFaceLandmarks=false" , facedetectbody, headers)
    response = conn.getresponse()
    data = response.read()
    print data
    words = data.split(",")

    for word in words:
        # print the word

	innerwords = word.split(":")
        for innerword in innerwords:
		if(found_conf==True):
			innerword = innerword.replace("}","")
			innerword = innerword.replace("]","")
			print(innerword)
			found_conf=False
                        return innerword
		if(innerword == "[{\"faceId\""):
			found_conf=True
	conn.close()

	return

def FaceIdentify(groupid, faceid):
    found_conf = False
    print "In FaceIdentify" 
    conn = httplib.HTTPSConnection('api.projectoxford.ai')    
    body="{\"personGroupId\":\"1234\",\"faceIds\""
    body = body + ":[" + faceid + "],"
    body = body + "\"maxNumOfCandidatesReturned\":1}"
    print body
    conn.request("POST", "/face/v1.0/identify" , body, headers)
    response = conn.getresponse()
    data = response.read()
    words = data.split(",")
    print "Got response in Face identify" 
    print data
    print "+++++++++++" 
    for word in words:
        # print the word

	innerwords = word.split(":")
        for innerword in innerwords:
		if(found_conf==True):
			innerword = innerword.replace("}","")
			innerword = innerword.replace("]","")
			print(float(innerword))
			found_conf=False
			return float(innerword)
		if(innerword == "\"confidence\""):
			found_conf=True
    conn.close()
    return

def GetName(str):
	return "Rajesh"
###########################################
try:
	
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(36,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
	client = None
	
	while 1:
 		#print (GPIO.input(36))
	        if((GPIO.input(36)) ==1):
			sleep(1)
			if((GPIO.input(36))==1):
				print("Detected")
			with picamera.PiCamera() as camera:
				camera.start_preview()
				sleep(1)
				camera.capture('/home/pi/Desktop/Photoes/ImageServer/image.jpg')
				camera.stop_preview

				print("Captured")
			#os.system("cd /home/pi/Desktop/Photoes/ImageServer/")
			#os.system("git commit")
			#os.system("git push")
                        os.system('python Update.py')
			SearchFaceId = FaceDetect("test")
			if(FaceIdentify(body, SearchFaceId) >0.5):
				print ("Matchfound:" + GetName(1))
                        else:
                                print("Unknown face")
					
	
	
	        

except Exception as e:

    print e


