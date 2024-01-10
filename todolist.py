
# newDicc = {
#     "basittodos": [
#         {
#             "id": 1,
#             "todoName": "Education",
#             "status": "Pending"
#         },
#         {
#             "id": 2,
#             "todoName": "Work",
#             "status": "Compoleted"
#         }
#     ]
# }


# print(newDicc)


# userdata = {
#     "basit": {
#         "userEmail": "basit@gmail.com",
#         "userPass": "123456"
#     },
#     "haseeb": {
#         "userEmail": "haseeb@gmail.com",
#         "userPass": "1234568"
#     },
# }

# userdata = [
#     {
#         "userName": "Basit",
#         "userEmail": "basit@gmail.com",
#         "userPass": "123456"
#     },
#     {
#         "userName": "Haseeb",
#         "userEmail": "haseeb@gmail.com",
#         "userPass": "1234568"
#     },
# ]

import uuid


todoData: dict = {
    "f3feasfgweafleiwyriow8u34": [
        {
            "todoName": "Company",
            "todoStatus": "Pending"
        }
    ]
}

userData: list[dict] = [{
    "userName": "ba",
    "userEmail": "ba",
    "userPass": "ba",
    "userId": "f3feasfgweafleiwyriow8u34"
}]


def get_required_input(prompt: str):
    while True:
        userInput = input(prompt)
        if userInput:
            return userInput
        else:
            print("Input is required. Please enter something.")


def main():
    loggedInUser: False or dict = False

    while True:
        print("1 - Signup")
        print("2 - Login")
        print("3 - Exit")

        choiceForLogSign = int(get_required_input(
            "\nPlease choose from above and write index "))

        if (choiceForLogSign == 1):
            userName = get_required_input("\nPlease enter your name : ")
            userEmail = get_required_input("\nPlease enter your email : ")
            userPass = get_required_input("\nPlease enter your password : ")
            isSignedUp = regesterNewUser(
                userData, userName, userEmail, userPass)
            if isSignedUp:
                print("\nPlease login with the credentials")
            else:
                print("\nFailed to create account")

        elif (choiceForLogSign == 2):
            userEmail = get_required_input("\nPlease enter your email : ")
            userPass = get_required_input("\nPlease enter your password : ")
            isLoggedIn = loginUser(userData, userEmail, userPass)
            if not isLoggedIn:
                print("\nInvalid pass or email")
            else:
                loggedInUser = isLoggedIn
                print(f"\nYou are now interacting as {
                      isLoggedIn["userName"]}\n")
                processAfterLoginProfile(main, loggedInUser)
                break
        if (choiceForLogSign == 3):
            break
        else:
            print("Invalid Choice")


def processAfterLoginProfile(back, loggedInUser):
    while True:
        print("1 - Profile")
        print("2 - Todos")
        print("3 - Back")
        print("4 - Exit")

        choiceForProfile = int(get_required_input(
            "\nPlease choose from above and write index "))

        if (choiceForProfile == 1):
            processAfterProfileProfile(loggedInUser)
        elif (choiceForProfile == 2):
            proccessTodos(processAfterLoginProfile, loggedInUser)
        elif (choiceForProfile == 3):
            back()
            break
        elif (choiceForProfile == 4):
            break
        else:
            print("Invalid choice")


def proccessTodos(back, loggedInUser: str):
    while True:
        print("1 - Get All Todos")
        print("2 - Create a New Todo")
        print("3 - delete a Todo")
        print("4 - update a Todo")
        print("5 - Back")
        print("6 - Exit")

        choiceForTodos = int(get_required_input(
            "\nPlease choose from above and write index "))

        if (choiceForTodos == 1):
            userAllTodos = todoData.get(loggedInUser["userId"])
            # userAllTodos = filter(lambda x: x["userId"] == userId, todoData)
            print("\nAllTodos", userAllTodos, "\n")
        elif (choiceForTodos == 2):
            createNewTodo(loggedInUser["userId"])
        elif (choiceForTodos == 3):
            todoNameToBeDel = get_required_input(
                "\nPlease Enter the todo name to be deleted ")
            deleteTodo(loggedInUser["userId"], todoNameToBeDel)
        elif (choiceForTodos == 4):
            todoNameToBeUpdated = get_required_input(
                "\nPlease Enter the todo name to be updated ")
            newStatus = get_required_input("\nPlease enter the new status ")
            updateTodo(loggedInUser["userId"], todoNameToBeUpdated, newStatus)
        elif (choiceForTodos == 5):
            back(main, loggedInUser)
            break
        elif (choiceForTodos == 6):
            break


def updateTodo(userId: str, todoName: str, newStatus: str):
    todoOldDataWithId = todoData.get(userId)
    if todoOldDataWithId:
        for todo in todoOldDataWithId:
            if todo["todoName"] == todoName:
                todo["todoStatus"] = newStatus
                return
        print(f"\nCould not found '{todoName}' todo ")
    else:
        print(f"\nUser not found and '{todoName}' todo also not found ")


def deleteTodo(userId: str, todoName: str):
    if userId in todoData:
        todoList = todoData[userId]
        for todo in todoList:
            if todo["todoName"] == todoName:
                todoList.remove(todo)
                print(f"\nTodo '{todoName}' deleted successfully.\n")
                return
        print(f"\nTodo '{todoName}' not found.\n")
    else:
        print(f"\n User Not Exists and todo '{todoName}' not found! \n")


def createNewTodo(userId: str):
    newTodoName = get_required_input("\nPlease Enter the todo name ")
    todoOldDataWithId = todoData.get(userId)

    if todoOldDataWithId:
        alreadyExists = list(
            filter(lambda x: x["todoName"] == newTodoName, todoData[userId]))
        # alreadyExists = next(filter(lambda x: x["todoName"] == newTodoName, todoData[userId]))
        if len(alreadyExists) == 0:
            todoData[userId].append({
                "todoName": newTodoName,
                "todoStatus": "Pending",
            })
        else:
            print("\nAlready Exists")
            return
    else:
        todoData[userId] = [
            {
                "todoName": newTodoName,
                "todoStatus": "Pending",
            }
        ]
    print("\nAdded succcessfully")


def processAfterProfileProfile(loggedInUser):
    while True:
        print(f"\nYour Profile \n Name: {loggedInUser["userName"]} \n Email: {
              loggedInUser["userEmail"]}\n")
        editorChoice = input(
            "Would you like to change anything (Y/N) N ") or "N"
        if (editorChoice == "N"):
            break
        elif (editorChoice == "Y"):
            newName = input(f"Please enter new Name: default {
                            loggedInUser["userName"]} ") or loggedInUser["userName"]
            newEmail = input(f"Please enter new Email: {
                             loggedInUser["userEmail"]} ") or loggedInUser["userEmail"]
            newPass = input(f"Please enter new Pass: {
                            loggedInUser["userEmail"]} ") or loggedInUser["userPass"]
            isUpdated = handleEditProfile(
                loggedInUser, newName, newEmail, newPass)
            if isUpdated:
                break


def handleEditProfile(loggedInUser, newName: str, newEmail: str, newPass: str):
    for user in userData:
        if (user["userEmail"] == loggedInUser["userEmail"] and user["userPass"] == loggedInUser["userPass"]):
            isConfirm = get_required_input(
                "\nType Y if your are confirm and N if no ")
            if (isConfirm == "Y"):
                user["userName"] = newName
                user["userEmail"] = newEmail
                user["userPass"] = newPass
                print("\nSuccessfully updated", userData)
                return True
            else:
                print("Operation cancelled")
                break


def regesterNewUser(userData: list[dict], userName: str, userEmail: str, userPass: str) -> bool:
    userData.append({
        "userName": userName,
        "userEmail": userEmail,
        "userPass": userPass,
        "userId": uuid.uuid4().hex
    })
    print(f"\nSuccessfully Signed Up ")
    return True


def loginUser(userData: list[dict], userEmail: str, userPass: str):
    for user in userData:
        if (user["userEmail"] == userEmail and user["userPass"] == userPass):
            return user


main()
