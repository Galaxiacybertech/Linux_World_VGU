import google.generativeai as genai

api_key = "ENTER_YOUR_API_KEY_HERE"
genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-2.5-flash")

print("Basic Chatbot Started")
print("Type 'exit' to stop\n")

while True:
    user = input("YOU: ")

    if user.lower() == "exit":
        print("BOT: Bye bye")
        break

    response = model.generate_content(user)
    print("BOT:", response.text)