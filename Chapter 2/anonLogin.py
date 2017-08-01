import ftplib

def anonLogin(hostname):

    try:

        ftp = ftplib.FTP(hostname)
        # Add credentials
        ftp.login('anonymous', 'me@your.com')
        print '\n[*] ' + str(hostname) + ' FTP Anonymous Logon Succeeded.'
        ftp.quit()
        
        return True

    except Exception, e:

        print '\n[-] ' + str(hostname) + ' FTP Anonymous Logon Failed.'

        return False

# Add FTP host IP.
host = ''
anonLogin(host)
