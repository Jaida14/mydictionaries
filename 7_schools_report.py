"""
Process the JSON file named school_data.json. Display only those schools 
that are part of the ACC, Big 12, Big Ten, and SEC divisons. 

Copy that info here:

"NCAA/NAIA conference number football (IC2020)","372","American Athletic Conference"
"NCAA/NAIA conference number football (IC2020)","108","Big Twelve Conference"
"NCAA/NAIA conference number football (IC2020)","107","Big Ten Conference"
"NCAA/NAIA conference number football (IC2020)","130","Southeastern Conference"


Display report for all universities that have a graduation rate for Women over 75%
Display report for all universities that have a total price for in-state students living off campus over $50,000



"""

import json
infile = open("school_data.json", "r")

schools = json.load(infile)  # useing the infile with the json library

# extracting value of that key and to see if that value matched if any in this list
conference_schools = [372, 108, 107, 130]

# counting the elements, the number of dictionaries (each dictionary is a school)
print(len(schools))

for school in schools:  # school would be a dictionary and schools a list bc whole thing is a list
    if school["NCAA"]["NAIA conference number football (IC2020)"] in conference_schools:
        if school["Graduation rate  women (DRVGR2020)"] >= 75:
            print(
                f"Univeristy: {school['instnm']}\nGraduation Rate for Women:{school['Graduation rate  women (DRVGR2020)']} %\n")
            # if doing double quotes for f string, single quotes must be done for inside

for school in schools:
    if school["NCAA"]["NAIA conference number football (IC2020)"] in conference_schools:
        if school["Total price for in-state students living on campus 2020-21 (DRVIC2020)"] is not None:
            if school["Total price for in-state students living on campus 2020-21 (DRVIC2020)"] > 50000:
                print(
                    f"Univeristy: {school['instnm']}\nTotal price for in-state students living on campus 2020-21: $ {school['Total price for in-state students living on campus 2020-21 (DRVIC2020)']}\n")
