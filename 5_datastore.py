# Below is a dictionary that contains information about real estate space for
# a doctor's office. Using the dictionary, create a csv file that has details
# for each space represented as rows. Name your file 'retail_space.csv.


'''
Your final output should look like:

room-number,use,sq-ft,price
100,reception,50,75
101,waiting,250,75
102,examination,125,150
103,examination,125,150
104,office,150,100

'''


datastore = {"medical": [
    {"room-number": 100,
     "use": "reception",
        "sq-ft": 50,
        "price": 75
     },
    {"room-number": 101,
     "use": "waiting",
        "sq-ft": 250,
        "price": 75
     },
    {"room-number": 102,
     "use": "examination",
        "sq-ft": 125,
        "price": 150
     },
    {"room-number": 103,
     "use": "examination",
        "sq-ft": 125,
        "price": 150
     },
    {"room-number": 104,
     "use": "office",
        "sq-ft": 150,
        "price": 100
     }

]
}


retail_space = open("retail_space.csv", "w")

retail_space.write("room-number,use,sq-ft,price\n")


for value in datastore["medical"]:# datastore["medical"] this is a list so it is iterable; each iteration (value) is one dictionary
    retail_space.write(
        f"{value['room-number']}, {value['use']}, {value['sq-ft']}, {value['price']}\n") #breaking each value iteration down


retail_space.close()
