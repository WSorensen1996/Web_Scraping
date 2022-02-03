    
    
    
    
def add_email_to_file(emails): 
    f = open("emaillist.txt", "a")
    for email in emails: 
        f.writelines(email+"\n")
    f.close()

