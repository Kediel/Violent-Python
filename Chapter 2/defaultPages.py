import ftplib

def returnDefault(ftp):

    try:

        dirList = ftp.nlst()

    except:

        dirList = []
        print "[-] Could not list directory contents."
        print "[-] Skipping to next target."
        return

    retList = []

    for fileName in dirList:

        fn = fileName.lower()

        if '.php' in fn or '.htm' in fn or '.asp' in fn:
            
            print "[+] Found default page: " + fileName

            retList.append(fileName)

    return retlist

# Specify host IP
host = ' '
userName = 'guest'
passWord = 'guest'
ftp = ftplib.FTP(host)
ftp.login(userName, passWord)
returnDefault(ftp)

