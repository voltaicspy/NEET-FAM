{\rtf1\ansi\ansicpg1252\cocoartf2761
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww28300\viewh17700\viewkind0
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0

\f0\fs24 \cf0 import discord\
import asyncio\
import random\
\
# Define your questions and answers here\
questions = [\
    \{\
        "question": "What is the capital of France?",\
        "options": ["A. London", "B. Paris", "C. Berlin", "D. Madrid"],\
        "answer": "B"\
    \},\
    \{\
        "question": "Which planet is known as the Red Planet?",\
        "options": ["A. Mars", "B. Venus", "C. Jupiter", "D. Saturn"],\
        "answer": "A"\
    \},\
]\
\
# Discord client\
client = discord.Client(Put here.)\
\
# Function to send a random question\
async def send_question():\
    question = random.choice(questions)\
    question_text = question["question"] + "\\n" + "\\n".join(question["options"])\
\
    channel = client.get_channel(CHANNEL_ID)\
    await channel.send(question_text)\
\
    # Store the correct answer in a separate dictionary with the question's ID as key\
    # (You might want to store this in a database for more questions)\
    global correct_answers\
    correct_answers[str(question_text)] = question["answer"]\
\
# Event: Bot is ready\
@client.event\
async def on_ready():\
    print(f'Logged in as \{client.user\}')\
\
    # Schedule the daily question (adjust the time as needed)\
    while True:\
        await asyncio.sleep(86400)  # 86400 seconds = 24 hours\
        await send_question()\
\
# Event: Message received\
@client.event\
async def on_message(message):\
    # Check if the message is from the bot itself to avoid loops\
    if message.author == client.user:\
        return\
\
    # Check if the message is the correct answer to a previously sent question\
    if str(message.content).strip().upper() == correct_answers.get(str(message.reference.message_id)):\
        await message.channel.send(f"Correct answer! The answer is \{correct_answers.get(str(message.reference.message_id))\}")\
    else:\
        await message.channel.send("Incorrect answer. Try again!")\
\
client.run(\'91MY_BOT_TOKEN')\
}