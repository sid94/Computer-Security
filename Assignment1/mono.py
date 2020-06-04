import sys
import os
import string
import random as r

seed = list(range(97,123))
r.seed(1)
r.shuffle(seed)

if(not os.path.isfile('in.txt')):
    print("Input file not found")
    sys.exit()

def encryption():
      dummyseed =  seed[::-1]
      charmap = {}
      for i in range(97,123):
            charmap[chr(i)] = chr(dummyseed.pop(-1))
            
      for key,val in charmap.items():
            print(key+ '-' + val,end=", ")
      
      myfile = open('out.txt', 'w')  
      with open('in.txt') as f:
        while True:
          c = f.read(1)
          if not c:
            print("End of file")
            break
          myfile.write("%s" % charmap[c])
          
      myfile.close()
      print("Content written in the file out.txt")
      
      
def decryption():
      dummyseed =  seed[::-1]
      charmap = {}
      for i in range(97,123):
            charmap[chr(dummyseed.pop(-1))] = chr(i)
         
      for key,val in charmap.items():
            print(key+ '-' + val,end=", ")
            
      myfile = open('in1.txt', 'w')  
      with open('out.txt') as f:
        while True:
          c = f.read(1)
          if not c:
            print("End of file")
            break
          myfile.write("%s" % charmap[c])
          
      myfile.close()
      print("Content written in the file in1.txt")
      
def main(param):
      if(not len(param) == 3):
            print("Please enter python mono.py <file1> <fil2> <1 or 0>")
            sys.exit()
            
      if(param[-1] == "1"):
            assert(os.path.isfile('in.txt') and os.path.isfile('out.txt'))
            assert(param[0] == "in.txt" and param[1] == "out.txt" and param[2] == "1")
            f = open('out.txt', 'r+')
            f.truncate(0)
            encryption()
            
      if(param[-1] == "0"):
            assert(os.path.isfile('out.txt') and os.path.isfile('in1.txt'))
            assert(param[0] == "out.txt" and param[1] == "in1.txt" and param[2] == "0")
            f = open('in1.txt', 'r+')
            f.truncate(0)
            decryption()
            
      sys.exit()
      
if __name__ == '__main__':
    main(sys.argv[1:])




    
