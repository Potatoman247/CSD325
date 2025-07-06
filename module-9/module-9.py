import requests
import json

#response = requests.get("http://api.open-notify.org/astros.json")
#print(response.status_code)

def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=2)
    print(text)
    
#jprint(response.json())


chosenClass = requests.get("https://www.dnd5eapi.co/api/2014/classes")
print(chosenClass.status_code)
def main():
    try:
        myClass = input("Please Select Your Class:")
        apiString = "https://www.dnd5eapi.co/api/2014/classes/" + myClass
        chosenClass = requests.get(apiString)
        print(chosenClass.status_code)
        print(chosenClass.json())
        jprint(chosenClass.json())
    except:
        print("Invalid argument, Please Try again.")
        print(chosenClass.status_code)
        main()
        
main()
