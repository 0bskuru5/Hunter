from exif import Image
import webbrowser
import os
import time

def banner():
  print("""
#######  ###  ##   ######   ####### 
 ##   #  ###  ##     ##      ##   # 
 ##       #####      ##      ##     
 ####      ###       ##      ####   
 ##       #####      ##      ##     
 ##   #  ##  ###     ##      ##     
#######  ##  ###   ######   ####    

    
  """)
  recon()
def recon():
  target = input("please input your target image ex. sample.jpg: ")
  def dms_to_dd(gps_coords, gps_coords_ref):
      d, m, s =  gps_coords
      dd = d + m / 60 + s / 3600
      if gps_coords_ref.upper() in ('S', 'W'):
          return -dd
      elif gps_coords_ref.upper() in ('N', 'E'):
          return dd
      else:
          raise RuntimeError('Incorrect gps_coords_ref {}'.format(gps_coords_ref))

  with open(target, 'rb') as image_file:
      my_image = Image(image_file)

      make = my_image.make
      model = my_image.model

      print(f"Device information - Image")
      print("----------------------------")
      print("Make: " + make)
      print("Model: "+ model)
      lat = dms_to_dd(my_image.gps_latitude, my_image.gps_latitude_ref)
      lng = dms_to_dd(my_image.gps_longitude, my_image.gps_longitude_ref)
      print("Latitude: "+ str(lat))
      print("Longitude: "+str(lng))
      print("wait a second i am opening the target location on youur browser.")
      result = "https://www.google.com/maps/place/"+ str(lat) +","+ str(lng)
      webbrowser.open(result)
      menu()
def menu ():
    goback = input("Do You want to Go back to main menu y/n: ")
    if (goback == "y"):
        print("Thanks for Using this tool!!!")
        time.sleep(1)
        os.system('python3 hunter.py')
    elif(goback == "n"):
        print("Here we go again!")
        time.sleep(1)
        banner()

banner()
