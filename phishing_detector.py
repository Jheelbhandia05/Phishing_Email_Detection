import os
import re

# -------------------------------
# EMAIL SELECTION MENU
# -------------------------------
print("📧 Choose email to analyze:")
print("1️⃣ Phishing Email")
print("2️⃣ Safe Email")

choice = input("Enter choice (1 or 2): ")

# -------------------------------
# FILE PATH SETUP
# -------------------------------
base_dir = os.path.dirname(os.path.abspath(__file__))

if choice == "1":
    file_path = os.path.join(base_dir, "sample_emails", "phishing_email.txt")
elif choice == "2":
    file_path = os.path.join(base_dir, "sample_emails", "safe_email.txt")
else:
    print("❌ Invalid choice")
    exit()

# -------------------------------
# READ EMAIL FILE
# -------------------------------
with open(file_path, "r", encoding="utf-8") as file:
    email_text = file.read()

email_text = email_text.lower()

print("\n🔍 Analyzing Email...\n")

# -------------------------------
# STEP 1: KEYWORD DETECTION
# -------------------------------
suspicious_words = ["urgent", "verify", "suspended", "click"]

found_word = False
for word in suspicious_words:
    if word in email_text:
        print(f"⚠️ Suspicious word detected: {word}")
        found_word = True

if not found_word:
    print("✅ No suspicious words found")

# -------------------------------
# STEP 2: LINK DETECTION (REGEX)
# -------------------------------
links = re.findall(r"http[s]?://\S+", email_text)

if links:
    print("\n🔗 Links found in email:")
    for link in links:
        print("   ", link)
        if ".xyz" in link or "login" in link:
            print("   ⚠️ Suspicious link detected")
else:
    print("\n✅ No links found in email")

# -------------------------------
# STEP 3: PHISHING RISK SCORE
# -------------------------------
print("\n📊 Phishing Risk Assessment:")

score = 0
score += len([w for w in suspicious_words if w in email_text])
score += len(links)

if score >= 5:
    print("🚨 HIGH RISK PHISHING EMAIL")
elif score >= 3:
    print("⚠️ MEDIUM RISK PHISHING EMAIL")
else:
    print("✅ LOW RISK EMAIL")
