import sqlite3
conn = sqlite3.connect("datasheet.db")

class PCPart:
  def __init__(self, type, model, price):
    self.type = type
    self.model = model
    self.price = price
    
  def to_file(self):
    with open(self.model + ".txt", "w") as f:
      f.write("-Datora sastavdala-\n")
      f.write("Veids:" + self.type + "\n")
      f.write("Modelis:" + self.model + "\n")
      f.write("Cena:" + str(self.price) + "\n")
    
    
part1 = PCPart('RAM', 'Corsair Vengeance LPX 16GB', 99.99)
part1.to_file()


cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS datasheet (id INTEGER PRIMARY KEY, type VARCHAR, model VARCHAR, price FLOAT)")

cursor.execute("INSERT INTO datasheet (type, model, price) VALUES (?, ?, ?)", (part1.type, part1.model, part1.price))

cursor.execute("SELECT * FROM datasheet")
records = cursor.fetchall()
for row in records:
  for value in row:
    print(value, end=" ")
  print()

conn.commit()
conn.close()