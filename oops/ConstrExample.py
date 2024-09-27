class ConstrExample:
    count = 0

    # constractor
    def __init__(self, name, email, phone_number):
        self.name = name
        self.email = email
        self.phone_number = phone_number
        ConstrExample.count = ConstrExample.count + 1
        print("Constructor invoked automatically")
        

    def display(self):
        print(self.name, self.email, self.phone_number)

st = ConstrExample("Sarah Hamad", "Sarah@text.com",  89698689 )
st.display()

st1 = ConstrExample("labia raide", "ladia@text.com", 667851111)
st1.display()

st2 = ConstrExample("raj kumar", "raj@text.com", 789689689)
st2.display()

print(ConstrExample.count)

