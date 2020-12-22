# InstaMail

***NOTE INSTAMAIL DOES NOT EXPLOIT INSTAGRAM TO GRAB ACCOUNT INFORMATION! THIS IS NOT A EXPLOIT PLEASE DO NOT TREAT IS AS SUCH!!!**


**Description**

Instamail is an account parser for Instagram. This is done because users input their email in multiple fields in the account creation process. Instamail uses Instagram's built in API search query and writes it to a file or prints it to the terminal. This script was written to spread awareness of accidental user input and should not be used for anything malicious! this script is just showing how easy it is to abuse accidental user input. accidental user input is a major problem and must be addressed, especially by big tech companies.

**Requirments**

InstaMail requires the Requests module, this can be installed with:

```

pip3 install requests

```

InstaMail also needs a valid sessionid to work.



The first step is to log in to Instagram from here:

https://www.instagram.com/accounts/login/





once logged in you will need to inspect element, it will look different for each browser, I will go over the most popular two chrome and firefox.



chrome:



1) rightclick the page and select the inspect option.



2) you will see tabs on the top of the page, select the application tab. This will bring you to where your cookies are stored



3) under storage you will see cookies clicking this will bring down all websites with cookies stored in your browser.



4) click https://instagram.com , this will display all cookies for Instagram, the one you will need is labeled sessionid, copy this.



Firefox:



1) rightclick the page and select the Inspect Element option.



2) you will see tabs on the page, select the storage tab. This will bring you to where your cookies are stored



3) under cookies you will see https://instagram.com , click this and copy the cookie labeled session id



And you're Done! Run:
```
python3 instamail.py
```

