# x = [ [5,2,3], [10,8,9] ] 
# x[1][0] = 15
# print(x[1][0])
# ********************************************************************
# students = [
#      {'first_name':  'Michael', 'last_name' : 'Jordan'},
#      {'first_name' : 'John', 'last_name' : 'Rosales'}
# ]

# students[0]['last_name'] = 'Bryant'
# print(students)
# ********************************************************************
# sports_directory = {
#     'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
#     'soccer' : ['Messi', 'Ronaldo', 'Rooney']
# }

# sports_directory['soccer'][0] = 'Andres'
# ***********************************************************************
# z = [ {'x': 10, 'y': 20} ]
# z[0]['y']=30
# print(z)

#***************************************************
# **************************************************
students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]


# # print(students('first_name', 'last_name'))
# iterateDictionary(students) 
# # should output: (it's okay if each key-value pair ends up on 2 separate lines;
# # bonus to get them to appear exactly as below!)
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel



# students = {'first_name'}= 'Michael', 'John', 'Mark', 'KB'
# def iterateDictionary2(some_list):
#     for student in some_list:
#         for key in student:
#             print(student[key])
# #             print(key)

#*******Bonus******
# def iterateDictionary2(some_list):
#     for student in some_list:
#         for key in student:
#             print(key +" - "+ student[key])
           

# iterateDictionary2(students)

# def iterateDictionary(my_list): 
#     for student in my_list:
#         key_value_string =[]
#         for key in student:
#             key_value_string.append(f"{key} - {student}")
#         print(key_value_string)
# iterateDictionary(students)

# ***************************Number 3*******************
# def iterateDictionary2(key,some_list):
#     for student in some_list:
#         print(student[key])
# iterateDictionary2('first_name', students)

#*********************Number3 Last Names*************************
# def iterateDictionary2(key,some_list):
#     for student in some_list:
#         print(student[key])
# iterateDictionary2('last_name', students)

# *******************Number 4*************************

# def dojomo(dictionary1):
#     print('LOCATIONS:',len(dictionary1['locations']))
#     for key in dictionary1['locations']:
#             print( key)
# dojomo(dojo)

# def dojomo(dictionary1):
#     print('INSTRUCTORS:',len(dictionary1['instructors']))
#     for key in dictionary1['instructors']:
#             print( key)
# dojomo(dojo)

dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(some_dict):
    for key in some_dict:
        print(len(some_dict[key]), key,some_dict[key])

printInfo(dojo)

# output:
# 7 LOCATIONS
# San Jose
# Seattle
# Dallas
# Chicago
# Tulsa
# DC
# Burbank
    
# 8 INSTRUCTORS
# Michael
# Amy
# Eduardo
# Josh
# Graham
# Patrick
# Minh
# Devon
