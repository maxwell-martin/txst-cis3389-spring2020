# Question 2


dic1 = {'L1': ['NY', 'CT', 'NH', 'MA'], 'L2': ['TX', 'NM'], 'L3': ['CA', 'WA', 'AZ'], 'L4': ['ND', 'SD','WY', 'ID'], 'L5':['UT'],'L6':['MN','WI','KY']}


with open("Q2Output.txt", "w") as outfile:
    for key in dic1.keys():
        outfile.write(key + ": Number of states - " + str(len(dic1[key])) + "\n")
