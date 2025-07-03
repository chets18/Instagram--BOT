# 🤖 InstaFitness Bot

**InstaFitness Bot** is a smart, automated Instagram assistant built using Python and Instagrapi.  
It automatically messages new followers (if only followback to prevent from tracking), collects fitness-related data from them (but for now it works partially), and stores it in a structured format.  
It mimics human-like behavior to avoid detection or spam flags by Instagram.
we had used the random delay option and also waiting, reponding like features to sound more like human activities.

---

## 🚀 Features

- ✅ **Auto-login to Instagram using secure credentials**
- ✅ **Automatically detects new followers**
- ✅ **Sends a structured message/questionnaire to each new follower**
- ✅ **Avoids sending messages to already contacted users**
- ✅ **Includes human-like random delays between messages to mimic real interaction**
- ✅ **Stores responses in a structured JSON file**
- ✅ **Flask server setup to view collected responses in the browser**
- ✅ **show either remains to send or not**
- ✅ **Export collected data in csv or word format**

## future features
- [ ] **Collect more data from followers**
- [ ] **Send personalized messages based on collected data**
- [ ] **Automatically unfollow users after a certain period of time**
- [ ] **colllect data and store in cloud database (e.g . MongoDB, supabase)**
- [ ] **Add more advanced filtering options for followers (e.g. by location, interests)**
- [ ] **save the data in a structured format (e.g. CSV, JSON)**
- [ ] **viwes data and give real time interaction**
---


## ⚠️ Challenges & Real Story

### 🤯 What Happened?

While testing the bot on a fresh Instagram page, I faced a **real ban-like experience**:

This was because I initially had **constant delays and bulk DMing** logic. Instagram’s AI flagged it as bot/spam behavior.



## ✅ Learnings

> Building an Instagram bot isn’t just about automation — it’s about mimicking natural human interaction.

Instagram is strict with bots, and if you push the limits, it **will take action**. But if you’re smart and patient, automation can really scale your outreach in ethical ways. i think it needed to be used only one time per day bcz. what if it got banned again? so be clever and take patient.

---

## 💬 Questions Sent by Bot
[
1. 👋 Welcome to our fitness page! Can I ask a few quick health questions to guide you better?
2. 1️⃣ What's your full name?
3. 2️⃣ How old are you?
4. 3️⃣ What's your height (in cm)?
5. 4️⃣ What's your weight (in kg)?
6. 5️⃣ What is your fitness goal? (costomisable)]

---

## 🛠 Setup Instructions

### 1. Clone the Repository
