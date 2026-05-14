# InstaBot

It is a smart, automated Instagram assistant built using Python and Instagrapi.  
It automatically messages new followers (if only followback to prevent tracking) and collects fitness-related data from them (but for now, it works partially).  
It mimics human-like behaviour to avoid detection or spam flags by Instagram.
We had used the random delay option and also waiting, responding, like features to sound more like human activities.

---

## Features

- Auto-login to Instagram using secure credentials
- Automatically detects new followers
- Sends a structured message/questionnaire to each new follower
- Avoids sending messages to already contacted users
- Includes human-like random delays between messages to mimic real interaction

---


## Challenges & Real Story
While testing the bot on a fresh Instagram page, I faced a **real ban-like experience**:
This was because I initially had **constant delays and bulk DMing** logic. Instagram’s AI flagged it as bot/spam behaviour.



## Learnings
> Building an Instagram bot isn’t just about automation; it’s about mimicking natural human interaction.

Instagram is strict with bots, and if you push the limits, it **will take action**. But if you’re smart and patient, automation can really scale your outreach in ethical ways. I think it needed to be used only one time per day bcz. What if it got banned again? So be clever and patient.

---

## Questions Sent by Bot
1. 👋 Welcome to our fitness page! Can I ask a few quick health questions to guide you better?
2. 1️⃣ What's your full name?
3. 2️⃣ How old are you?
4. 3️⃣ What's your height (in cm)?
5. 4️⃣ What's your weight (in kg)?
6. 5️⃣ What is your fitness goal? (customisable)

---

## 🛠 Setup Instructions
1) Clone the repo
2) Pip install the requirement 
3) Place real credentials in the .env file that include username and password 
4) Check your email and click on yes, it's me. 

## warning!!
I, Chetraj, do not recommend using this method to send messages to followers, as it is not official. There are multiple DMing providers available on the internet that offer a more secure and reliable way to communicate. I explored this method because I wanted to understand how the system works and assess its security.

**This is indeed vibe-coded, but it taught me more than I could learn by copying the code from a YouTube tutorial.**
