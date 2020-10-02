def fun(s):
    isValid = False
    if(s.count('@') > 1 or s.count('.') != 1):
        return isValid
    elif(s.count('@') == 1 or s.count(".") == 1):
        try: 
            user, follow = s.split("@")
            website, ext = follow.split(".")
            if(len(ext) <= 3):
                isValid = True
            else:
                return isValid
    
            if(website.isalnum() or website.isalpha()):
                isValid = True
            else:
                return False
        
            if(('_' in user) or ('-' in user)):
                user = user.replace('_', "")
                user = user.replace('-', "")
                if(user.isalnum()):
                    isValid = True
                else:
                    return False
            elif(user.isalnum() or user.isalpha()):
                isValid = True
            else:
                return False
        except Exception as e:
            pass
        
        

    return isValid
def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)