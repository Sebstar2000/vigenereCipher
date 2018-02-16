alphNum = {"a":0,"b":1,"c":2,"d":3,"e":4,"f":5,"g":6,"h":7,"i":8,"j":9,"k":10,"l":11,"m":12,"n":13,"o":14,"p":15,"q":16,"r":17,"s":18,"t":19,"u":20,"v":21,"w":22,"x":23,"y":24,"z":25}
numAlph = {0:"a",1:"b",2:"c",3:"d",4:"e",5:"f",6:"g",7:"h",8:"i",9:"j",10:"k",11:"l",12:"m",13:"n",14:"o",15:"p",16:"q",17:"r",18:"s",19:"t",20:"u",21:"v",22:"w",23:"x",24:"y",25:"z"}

deOrEn = input("Decrypt or Encrypt (e/d)")
which = ""
if (deOrEn == "Decrypt" or deOrEn == "decrypt" or deOrEn == "d"):
    which = "d"
elif (deOrEn == "Encrypt" or deOrEn == "encrypt" or deOrEn == "e"):
    which = "e"
else:
    print("Neither decrypt nor encrypt was selected")
    raise SystemExit

cipherKey = input("Enter Cipher Key:").lower()
keyLength = len(cipherKey)
    
userInput = input("Enter phrase:").lower()
inputLen = len(userInput)

output = ""

def encryptInput(keyPos, userPos):
    if userInput[userPos].isalpha() != True:
        output += userInput[userPos]
        return
    outputNum = alphNum[cipherKey[keyPos]] + alphNum[userInput[userPos]]
    if outputNum > 25:
        outputNum = outputNum - 26
    global output
    output += numAlph[outputNum]
    
    
def decryptInput(keyPos, userPos):
    if userInput[userPos].isalpha() != True:
        output += userInput[userPos]
        return
    outputNum =  alphNum[userInput[userPos]] - alphNum[cipherKey[keyPos]]
    if outputNum < 0:
        outputNum = outputNum + 26
    global output
    output += numAlph[outputNum]
    
counter = 0
for i in range(inputLen):
    if(which == "e"):encryptInput(counter, i)
    elif(which == "d"):decryptInput(counter, i)
    if counter < keyLength-1 :
        counter += 1
    else:
        counter = 0
print(output)
