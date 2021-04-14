# coding: UTF-8 
#Modified By Crypt1cSoul

from urllib2 import Request, urlopen, URLError, HTTPError 

def Space(n):
	i = 0
	while i<=n:
		print " ",
		i+=1


def Apf():
	f = open("cryptic.txt","r");
	link = raw_input("Enter Website link :: ")
	print "\n\nPossible panels : \n"
	while True:
		sub_link = f.readline()
		if not sub_link:
			break
		req_link = "http://"+link+"/"+sub_link
		req = Request(req_link)
		try:
			response = urlopen(req)
		except HTTPError as e:
			continue
		except URLError as e:
			continue
		else:
			print "cryptic :: ",req_link

def csoul():
	Space(9); print("""
              \033[96m
                     d8888 8888888b.  8888888888
                    d88888 888   Y88b 888
                   d88P888 888    888 888
                  d88P 888 888   d88P 8888888
                 d88P  888 8888888P"  888
                d88P   888 888        888
               d8888888888 888        888
              d88P     888 888        888
    +===============================================+
    |..............Admin Panel Finder...............|
    +-----------------------------------------------+
    |#Modified By  =>>    Crypt1cSoul               |
    |#Join=>> Gray Hat Hackers Community on Facebook|
    |#TG =>> https://t.me/joinchat/Q5IC1RPcsysxMjg1 |
    |#Note =>> Educational Purpose Only             |
    |-----------------------------------------------|
    |       -- GRAY HAT HACKERS COMMUNITY --        |
    +===============================================+ """)
                                        
                                      
	Space(9); print "     "
	Space(1); print " (Website link should be test.com or www.test.com) "
	Space(3); print "      "

csoul()
Apf()


 
