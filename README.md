# Revenge on Scammers

## Introduction

Ever gotten one of those annoying scam messages? One day, I got a message from a "company" that looked something like this:

> Dear customer, your delivery is waiting for tax payment (2.65$). You can pay here: [https://tortsp.ru/il](https://tortsp.ru/il)

Obviously, I didn't fall for it because I'm not an idiot. But I did open Burp Suite Community Edition and had some fun.

## The Plan

I recorded the POST requests these scammers were using and decided to give them a taste of their own medicine. I created a program to send a lot of requests to their website. In each request, I included a fake but valid credit card number. Every time a request was sent, the scammer had to pay a small fee to their third-party payment processor (like 2¢).

Over time, the scammer started losing money. Eventually, they must have gotten notifications about that and shut down the website(so it was an even bigger success). But I didn't stop there.

## Extra Fun

The scammer also had a login page. So, I added a function to flood their database with fake usernames and passwords. If someone entered real credentials, the hacker would need to go through all the junk I sent to find them, making their job a lot harder.

for the cherry on the cake, I reported their number (+972 51-2882738) and their website as scams.

## The Goal

Now, I want everyone to be able to stop these scammers. If each of us does this to every phishing scam, we can make this tactic useless and shut them down for good.

## Instructions

1. **Setup**: Make sure you have Python installed..

2. **Install Dependencies**: My script required only one library to download:
    ```bash
    pip install requests
    ```

3. **Get the Payload Data**: Open Burp Suite or the default network scanner in your web browser.
     - Record all of the traffic when you enter data on the webpage.
     - Locate where the website is sending the data and capture the data it sends.
     - Copy the relevant information. You may need to copy the cookies to the headers (and maybe some other things). Put the data like username, credit card number, etc., in the data field in a JSON format.
     - Put the URL it is sending to in the appropriate place in your script.

4. **execute the code!!**

## Conclusion

Scammers beware! We're onto you, and we're not going to let you get away you're fucked. Let's make the internet a safer place for everyone.

Happy scamming the scammers!
