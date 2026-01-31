class Math():
    def __init__(self):
        self

    def celsius_to_farhenite(self,number):
        self.number=number
        return (9/5*number)+32
    
y=int(input("give me the no to convert = "))

math1=Math()
x=math1.celsius_to_farhenite(y)
print(f"{math1.celsius_to_farhenite(y)}°F")

