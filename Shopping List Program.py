# 10/20/2020
# Emilio Alvarado
# Shopping List Program

import time
import os
import pymongo
from pymongo import MongoClient

# pprint library is used to make the output look more pretty
from pprint import pprint

# connect to MongoDB, change the << MONGODB URL >> to reflect your own connection string
client = MongoClient('mongodb+srv://EAlvarado:8Hi!199325!@clusteremilio0.8vzxx.mongodb.net/<dbname>?retryWrites=true&w=majority')
db= client.EAlvarado
mycol = db.ShoppingList

# Create empty list
#shoppingList = []

#Name
print ("Hello! Welcome to your shopping list!\n")
Name1 = input("Please enter your name: ")
time.sleep(1)

#Main Menu
def main_menu():
    print ("\nWelcome " + Name1.title())
    print ("_______________________________________")
    print ("********** Main Menu **********")
    print ("\n\nPlease select an option:")
    print ("\n1. Add An Item")
    print ("\n2. Delete An Item")
    print ("\n3. View Your List")
    print ("\n4. Delete List")
    print ("\n5. Close Shopping List")

    #cmd choice
    cmdChoice = input("\n> ")

    #Cmd If Statements
    if cmdChoice == '1':
        add_Item()
    elif cmdChoice == '2':
        delete_Item()
    elif cmdChoice == '3':
        view_List()
    elif cmdChoice == '4':
        delete_List()
    elif cmdChoice == '5':
        print ('Good Day!')
        time.sleep(1)
        os._exit(0)
    else:
        print ("That is not an option. Please try again")
        time.sleep(1)
        os.system('cls')
        return main_menu()


#Add Item Function
def add_Item():
    os.system('cls')
    print('What item would you like to add?\n')
    additem = input('>')
    additemdb = {'Item' : (additem).title(), 'User' : (Name1).title()}
    mycol.insert_one(additemdb)
    print (additem + " added to list")
    time.sleep(1)
    print ("\nwould you like to add another item? (Y/N)")
    item_Decision = input ('>')
    if item_Decision == 'Y' or item_Decision == 'y':
        return add_Item()
    else:
        os.system('cls')
        return main_menu()


  
    
#Delete Item Function
def delete_Item():
    os.system('cls')
    for x in mycol.find():
        print(x["Item"]) 
    time.sleep(2)
    print('\nWhat item would you like to delete?')
    itemDelete = input('>')
    mycol.delete_one({"Item":itemDelete.title()}) 
    time.sleep(1)
    print(itemDelete + ' has been removed from your list \n')
    for x in mycol.find():
        print(x["Item"]) 
    print ("\nwould you like to delete another item? (Y/N)")
    item_Decision = input ('>')
    if item_Decision == 'Y' or item_Decision == 'y':
        return delete_Item()
    else:
        os.system('cls')
        return main_menu()



#View List Function
def view_List():
    os.system('cls')
    print('Here is your current shopping list\n')
    for x in mycol.find():
        print(x["Item"])   
    returnHome = input('\nPress any key to return to the main menu')
    os.system('cls')
    return main_menu()

#Delete List Function
def delete_List():
    os.system('cls')
    print('Are you sure you want to delete your shopping?(Y/N)')
    item_Decision = input ('>')
    if item_Decision == 'Y' or item_Decision == 'y':
        mycol.delete_many({})
        print('Your list has been deleted')
        time.sleep(2)
        return main_menu()
    else:
        os.system('cls')
        return main_menu()
    
    
main_menu()
