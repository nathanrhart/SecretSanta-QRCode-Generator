import random
import qrcode
import qrcode.image.svg
import time

"""Secret Santa QR Code Making Script"""

#ADDING THE NAMES INTO THE HAT
f = open("names.txt")
gifternames = f.read().splitlines()
gifteenames = gifternames[:] #make a copy of the variable
f.close()

numofnames = len(gifternames)


#SHUFFLING THE HATS OF GIFTEES TO GIFTERS
print("Assigning Everyone...")
def Shuffle():
  time.sleep(0.9)
  random.shuffle(gifternames)#shuffle gifternames
  random.shuffle(gifteenames)#shuffle gifteenames
  for i in range(0, numofnames):
    if gifternames[i] == gifteenames[i]:
      print("Collision Found, Shuffling Again!")
      Shuffle()
      break
  #sortingdict = dict(zip(gifternames,gifteenames) ) #assign to a dict
Shuffle()

#Checking the list, if all is good, will create the Codes

def MakeCodes():
  print("List made! Printing QR Codes!")
  time.sleep(0.6)
  for i in range(0, numofnames):
    print("Making QR Code for: " + (gifternames[i]) )
    im = qrcode.make(gifteenames[i])
    im.save(gifternames[i] + ".png", "PNG")
    time.sleep(0.8)
  print("Done!")
    

MakeCodes()


