from instagrapi import Client
import json
import os
import time
import random
import re
from dotenv import load_dotenv

# Load credentials
load_dotenv()
USERNAME = os.getenv('INSTAGRAM_USERNAME')
PASSWORD = os.getenv('INSTAGRAM_PASSWORD')

# Initialize client
cl = Client()
cl.login(USERNAME, PASSWORD)

# Load saved data
DATA_FILE = "data.json"
if os.path.exists(DATA_FILE):
    with open(DATA_FILE, "r") as f:
        saved_data = json.load(f)
else:
    saved_data = {}

# Questions to be sent
QUESTIONS = [
    "👋 Hey! Welcome to our fitness hub. Can I ask a few quick questions to personalize your journey?",
    "1️⃣ What's your full name?",
    "2️⃣ How old are you?",
    "3️⃣ What's your height (in cm)?",
    "4️⃣ What's your weight (in kg)?",
    "5️⃣ What is your fitness goal?"
]

# Parse messages for useful info
def parse_user_message(message):
    data = {
        "full_name": None,
        "age": None,
        "height_cm": None,
        "weight_kg": None,
        "goal": None
    }

    name_match = re.findall(r"\b([A-Z][a-z]+(?:\s+[A-Z][a-z]+)+)\b", message)
    if name_match:
        data["full_name"] = name_match[0]

    age_match = re.search(r"\b(\d{1,2})\s*(?:years|yrs|yo)?\b", message, re.IGNORECASE)
    if age_match:
        data["age"] = age_match.group(1)

    height_match = re.search(r"\b(\d{2,3})\s*(?:cm|centimeters?)\b", message, re.IGNORECASE)
    if height_match:
        data["height_cm"] = height_match.group(1)

    weight_match = re.search(r"\b(\d{2,3})\s*(?:kg|kilograms?)\b", message, re.IGNORECASE)
    if weight_match:
        data["weight_kg"] = weight_match.group(1)

    goal_match = re.search(r"(?:goal\s*is\s*|I\s*want\s*to\s*|aim\s*to\s*|plan\s*to\s*)(.*)", message, re.IGNORECASE)
    if goal_match:
        data["goal"] = goal_match.group(1).strip()

    return data

# Send messages to new followers
def send_questionnaire():
    followers = cl.user_followers(cl.user_id)
    for user_id, user in followers.items():
        username = user.username
        if username in saved_data:
            continue

        print(f"📩 Sending questions to @{username}")
        for q in QUESTIONS:
            cl.direct_send(text=q, user_ids=[user_id])
            time.sleep(random.uniform(2.5, 6.5))  # human-like delay

        saved_data[username] = {"status": "questions_sent"}
        with open(DATA_FILE, "w") as f:
            json.dump(saved_data, f, indent=4)

# Scan DMs and extract answers
def scan_direct_messages():
    threads = cl.direct_threads(amount=20)
    for thread in threads:
        for user in thread.users:
            username = user.username
            if username not in saved_data or "goal" in saved_data[username]:
                continue  # skip users with data or not targeted

            messages = [msg.text for msg in thread.messages if msg.user_id == user.pk]
            combined = " ".join(reversed(messages))

            extracted = parse_user_message(combined)
            if any(extracted.values()):
                saved_data[username] = extracted
                print(f"✅ Data saved from @{username}: {extracted}")

                with open(DATA_FILE, "w") as f:
                    json.dump(saved_data, f, indent=4)

# === RUN THE BOT ===

send_questionnaire()

print("⏳ Waiting for 60–90 seconds to let users reply...")
time.sleep(random.randint(60, 90))

scan_direct_messages()

print("✅ Bot completed this run successfully!")
