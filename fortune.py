

print("🔮 Welcome to Piyush Jain's Fortune Teller (21JE0650) 🔮")
mood = input("How are you feeling today? (happy/sad/neutral): ").strip().lower()

if mood == "happy":
    fortune = "Great things await you, says Piyush! Keep smiling."
elif mood == "sad":
    fortune = "Tough times don't last, but tough people like you do."
elif mood == "neutral":
    fortune = "Balance brings peace. Embrace the calm."
else:
    fortune = "Hmm... I sense a mysterious aura. Be ready for surprises."

print(f"✨ Your fortune: {fortune} ✨")
