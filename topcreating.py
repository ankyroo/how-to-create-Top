n = int(input("Enter the number from which you want to create the top anime list:"))
#144-149 numbering and top creating
user_list = []
el = 0
while el < n:
    string = 'Top' + str(el + 1) + ": "
    user_list.append(input(string))
    el += 1 #Adds columns up to the specified number
    #150-151 adding "Top-"
for i, anime in enumerate(user_list, start=1): #Numerating process for Top like Top10
    print(f"Top{i}-{anime}") #'f' formating {}