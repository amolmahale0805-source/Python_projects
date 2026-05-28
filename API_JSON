
import requests

def getdata():
    url="https://api.rootnet.in/covid19-in/stats/latest"
    response = requests.get(url)
    return response.json()

def show_summary(data):
    summary = data["data"]["summary"]

    print("\n----INDIA SUMMARY----")
    print(f"Total: {summary['total']}")
    print(f"Discharged: {summary['discharged']}")
    print(f"Deaths: {summary['deaths']}")

def show_state(data):

    states = data["data"]["regional"]

    user_state = input("Enter the State:")

    state_found = False

    for state in states:

        if user_state.lower() == state["loc"].lower():
            print(f"State: {state['loc']}")
            print(f"Discharged: {state['discharged']}")
            print(f"Deaths: {state['deaths']}")
            print(f"Total Confirmed: {state['totalConfirmed']}")

            state_found = True
            break
    if not state_found:
        print("State Not found")


data=getdata()

while True:

    print("\n1.India Summary")
    print("\n2.State Summary")
    print("\n3.Exit")

    choice=int(input("Enter Your Choice:"))

    if choice==1:
        show_summary(data)
    elif choice==2:
        show_state(data)
    elif choice==3:
        break
    else:
        print("Invalid Choice")



