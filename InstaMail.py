#! /usr/bin/python3
import requests
import re

print('-' * 100)
print('\nWelcome to ryes instagram acount parser!')
print('''

@@@@@@@   @@@ @@@  @@@@@@@@     @@@  @@@  @@@   @@@@@@   @@@@@@@   @@@  @@@   @@@@@@
@@@@@@@@  @@@ @@@  @@@@@@@@     @@@  @@@  @@@  @@@@@@@@  @@@@@@@@  @@@  @@@  @@@@@@@
@@!  @@@  @@! !@@  @@!          @@!  @@!  @@!  @@!  @@@  @@!  @@@  @@!  !@@  !@@
!@!  @!@  !@! @!!  !@!          !@!  !@!  !@!  !@!  @!@  !@!  @!@  !@!  @!!  !@!
@!@!!@!    !@!@!   @!!!:!       @!!  !!@  @!@  @!@  !@!  @!@!!@!   @!@@!@!   !!@@!!
!!@!@!      @!!!   !!!!!:       !@!  !!!  !@!  !@!  !!!  !!@!@!    !!@!!!     !!@!!!
!!: :!!     !!:    !!:          !!:  !!:  !!:  !!:  !!!  !!: :!!   !!: :!!        !:!
:!:  !:!    :!:    :!:          :!:  :!:  :!:  :!:  !:!  :!:  !:!  :!:  !:!      !:!
::   :::     ::     :: ::::      :::: :: :::   ::::: ::  ::   :::   ::  :::  :::: ::
 :   : :     :     : :: ::        :: :  : :     : :  :    :   : :   :   :::  :: : :

''')
print('-' * 100)

session_id = input('Paste sessionid here:')
choice = input('Write results to a file? Defaults to printing results: Y or N?')
choices = ['y', 'n']

if choice.lower() not in choices:
    print('INVALID CHOICE')
    quit()




email_user_dict = {}
# You can add more emails to seach here.
emails_list = ['gmail', 'yahoo', 'zoho', 'mail', 'protonmail', 'live', 'outlook', 'aol', 'aim']


print('\nCreating email list...')

for mail in emails_list:
    r = requests.get('https://www.instagram.com/web/search/topsearch/?context=blended&query=%40{}.com'.format(mail), cookies={'sessionid' : session_id})
    emails = r.text
    email_list = emails.split('"user"')


    username_unclean = []
    emails_unclean = []

    for i in email_list:
        x = i.find("username")
        y = i.find('is_private')
        z = i[x:y].replace(', ', ':::', 1)
        d = z.split(":::")
        try:
            if d[0] == '' or d[1] == '':
                continue
            else:
                username_unclean.append(d[0])
                emails_unclean.append(d[1])
        except IndexError:
            continue

    def email_cleanup(email):
        x = email.replace('"full_name": "', '')
        y = x.replace('", "', '')
        if re.match(r'[^@]+@[^@]+\.[^@]+', y):
            if re.findall(r'[ +\\]', y):
                return False
            else:
                return y
        else:
            return False

    def username_cleanup(user):
        if user == '':
            return False
        x = user.replace('username": "', '')
        y = x.replace('"', '')
        return y

    def cleanup(users, mails):
        for x, y in zip(users, mails):
            user = username_cleanup(x)
            email = email_cleanup(y)
            if user == False or email == False:
                continue
            else:
                email_user_dict[user] = email

    cleanup(username_unclean, emails_unclean)

if choice.lower() == 'y':
    with open('emails.txt', 'w') as emails:
        for i in email_user_dict.keys():
            emails.write(i + ' : ' + email_user_dict[i] + '\n')
    print('File emails.txt has been created!')
else:
    for i in email_user_dict.keys():
        print(i + ' : ' + email_user_dict[i])
