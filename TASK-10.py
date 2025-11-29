class VisitorForm:
    def _init_(self):
        self._name = None
        self._aboutLW = "We provide training in holistic approach."
        self._phone = None
        self._email = None
        self._age = None
        self._wifipass = "mypass"
        self._purpose = None

    # setters
    def setName(self, name):
        self._name = name

    def setPhone(self, phone):
        self._phone = phone

    def setEmail(self, email):
        self._email = email

    def setPurpose(self, purpose):
        self._purpose = purpose

    def setAge(self, myage):
        self._age = myage   

    # getters
    def getAge(self):
        return self._age

    def getWifiPass(self):
        return self._wifipass

    def _str_(self):
        return (
            f"\n---- Visitor Details ----\n"
            f"Name       : {self._name}\n"
            f"Phone      : {self._phone}\n"
            f"Email      : {self._email}\n"
            f"Age        : {self._age}\n"
            f"Purpose    : {self._purpose}\n"
            f"About LW   : {self._aboutLW}\n"
            f"WiFi Pass  : {self._wifipass}\n"
            f"-------------------------"
        )

v1 = VisitorForm()

print("Enter Visitor Details")

name = input("Enter Name: ")
phone = input("Enter Phone Number: ")
email = input("Enter Email: ")

while True:
    age = int(input("Enter Age: "))
    if age >= 0:
        break
    else:
        print("Age cannot be negative. Please enter again.")

purpose = input("Enter Purpose of Visit: ")

v1.setName(name)
v1.setPhone(phone)
v1.setEmail(email)
v1.setAge(age)
v1.setPurpose(purpose)

print(v1)