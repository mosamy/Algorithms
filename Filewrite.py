__author__ = 'mosamy'
def addEmail(filename, name, email):
    f = open(filename, 'a') # replace the mode

    # Append name and email, each record should end with

    f.write(name + ' ' + email + '\n')
    f.close()
    return f

addEmail("test.txt", "mohamed samy", "msamy@sufgeeks.org")
addEmail("test.txt", "mosamy", "m_raafat_samy@hotmail.com")