#3)შექმენით for ციკლი 150ის დიაპაზონში და შეამოწმეთ თითოეული რიცხვი, თუ ეს რიცხვი არის ლუწი, მაშინ დაბეჭდეთ "Luwia" და გვერძე მიაწერეთ რიცხვი (მინიშნება ---> print("Luwia", i) ხოლო თუ იქნება კენტი, დაბეჭდეთ "Kentia" და გვერძე მიუწერეთ ეს რიცხვი.

for i in range(150):
     if i % 2 == 0:
        print("Luwia")
     elif i % 2 == 1:
        print("kentia")