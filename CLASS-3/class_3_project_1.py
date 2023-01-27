
# Assignment
# Class -03
# 1. Create CRUD (Create, Read, Update, Delete) Operation.


raju_mia_info = ["raju", "mia", 23, "Dhaka", "DIU"]

while True:
    user_input = input("Inter what do you wnat---(Create, Read, Update, Delete, close): ")
    if user_input == "close":
        break
    elif user_input == "read":
        print("This is your List.", raju_mia_info)

    elif user_input == "create":
        add_value = input("inter your new create value: ")
        raju_mia_info.append(add_value)
        print("This is your new list value: ", raju_mia_info)

    elif user_input == "update":
        change_value = input("inter your changes value: ")
        update_change_value = input("inter your update change value")

        if change_value in raju_mia_info:
            index_track = raju_mia_info.index(change_value)
            raju_mia_info[index_track] = update_change_value

            print("this is your updated list", raju_mia_info)

        else:
            print("wrong input-not match the value-plz inter currect input again")

    
    elif user_input == "deleted":
        deleted_value = input("inter your deleted value plz: ")
        if deleted_value in raju_mia_info:
            raju_mia_info.remove(deleted_value)
            print("this is your new list after delted the value", raju_mia_info)

        else:
            print("value is not match --try agein plz")



    else:
        print("inter your rigft choice(Create, Read, Update, Delete, close): ")



