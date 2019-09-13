#Dictionaries3

dictionary = {
  "Name": 'Daliah',
  "Age" : 26 ,
  "Year" : 1993,
  "Graduate_Year" : 2018,
  "Career": "Computer"  
    }
print('My Dictionary is  : ',dictionary)

#Copy a Dictionary
Copy_dictionary = dictionary.copy()
print('\nCopy of Dictionary: ',dictionary)

#Nested Dictionaries
Trainers = {
     'First': {'Name':'Daliah', "Course" : 'CIT' , 'Time_Job' : 'Full Part'},
     'Second': {'Name':'Redna', "Course" : 'Networking' , 'Time_Job' : 'Full Part'},
     'Third': {'Name':'Ather', "Course" : 'Business' , 'Time_Job' : 'half Part'},
     'Forth': {'Name':'Suha', "Course" : 'Entering' , 'Time_Job' : 'half Part'}       }
print('\nTrainers information: ',Trainers)

#Constructor
Constructor = dict(Company="Alkhaleej" ,Business="Training" )
print('\nConstructor: ',Constructor)
