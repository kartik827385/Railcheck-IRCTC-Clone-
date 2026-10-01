import requests
class Railcheck:
  def __init__(self):
    user_input = input("""How would you like to proceed ?
                       1. Enter 1 to check live train status 
                       2. Enter 2 to check PNR
                       3. Enter 3 to check train schedule""")
    if user_input == "1":
      print("live train status")
    elif user_input =="2":
      print("PNR")
    else:
      self.train_schedule()
  def train_schedule(self):
    train_no = input("Enter the train number")
    self.fetch_data(train_no)
    Data = request.get("")
    Data = data.json()
    print(Data)

for i in data['route']:
  print(i['station name'],"|",i['arrival time'],"|",i['departure time'],"|",i['distance'],"kms")

obj = Railcheck()
