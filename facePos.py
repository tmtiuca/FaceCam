import unirest
import json
import serial
import sys

response = unirest.get("https://faceplusplus-faceplusplus.p.mashape.com/detection/detect?attribute=glass%2Cpose%2Cgender%2Cage%2Crace%2Csmiling&url=http%3A%2F%2Fwww.faceplusplus.com%2Fwp-content%2Fthemes%2Ffaceplusplus%2Fassets%2Fimg%2Fdemo%2F1.jpg",
  headers={
    "X-Mashape-Key": "DaPJj5tCvdmshEGrNax1LK8coEgOp1yasO8jsneovrAUexFPlJ",
    "Accept": "application/json"
  }
)
res = json.loads(response.raw_body)


sys.stdout.write(res['face'][0]['position']['center']['x'])



#ser = serial.Serial(0)  # open first serial port
#print ser.name , ' <-- name'         # check which port was really used
#ser.write("m")      # write a string
#ser.close()     

