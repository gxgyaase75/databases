### Must have MongoDB to use ###
# Imports
from pymongo import MongoClient
from pprint import pprint
import time

# Important Variables and Connection to MongoDB
url = "mongodb+srv://username:password@cluster0.hudohvr.mongodb.net/test"
client = MongoClient(url)
db = client.test
sample = db['Cluster0']
start = time.time()

# Data used in experiment
stdt_info_1 = {
'Name': 'William Coffey',
'Class': '3',
'ID_No': '1'
}
stdt_info_2 = {
'Name': 'Rodney Taylor',
'Class': '8',
'ID_No': '18'
}
stdt_info_3 = {
'Name': 'Kyle Thompson',
'Class': '6',
'ID_No': '22'
}
stdt_info_4 = {
'Name': 'Gabrielle Grant',
'Class': '5',
'ID_No': '30'
}
stdt_info_5 = {
'Name': 'Brandon Bell',
'Class': '3',
'ID_No': '4'
}
stdt_info_6 = {
'Name': 'Andrew Smith',
'Class': '7',
'ID_No': '8'
}
stdt_info_7 = {
'Name': 'Victor Sullivan',
'Class': '1',
'ID_No': '26'
}
stdt_info_8 = {
'Name': 'Kristina Heath',
'Class': '3',
'ID_No': '14'
}
stdt_info_9 = {
'Name': 'Beverly Fuller',
'Class': '7',
'ID_No': '1'
}
stdt_info_10 = {
'Name': 'Charles Juarez',
'Class': '6',
'ID_No': '15'
}

# Inserts data in database
result1 = sample.insert_one(stdt_info_1)
result2 = sample.insert_one(stdt_info_2)
result3 = sample.insert_one(stdt_info_3)
result4 = sample.insert_one(stdt_info_4)
result5 = sample.insert_one(stdt_info_5)
result6 = sample.insert_one(stdt_info_6)
result7 = sample.insert_one(stdt_info_7)
result8 = sample.insert_one(stdt_info_8)
result9 = sample.insert_one(stdt_info_9)
result10 = sample.insert_one(stdt_info_10)

# Updates a student (Rodney in this case)
sample.update_one( 
  {'Class': '8'}, 
  {
    "$set": {
      'Class': '2',
    }
  }
  )

# Deletes a student (Kristina in this case)
sample.delete_one({'Name': 'Kristina Heath'})

# Returns time in milliseconds
end1 = time.time()
print("The time of execution of above program is :",
      (end1 - start) * 10 ** 3 , "ms")

# Finds data in database by name
output1 = sample.find_one({'Name': 'William Coffey'})
output2 = sample.find_one({'Name': 'Rodney Taylor'})
output3 = sample.find_one({'Name': 'Kyle Thompson'})
output4 = sample.find_one({'Name': 'Gabrielle Grant'})
output5 = sample.find_one({'Name': 'Brandon Bell'})
output6 = sample.find_one({'Name': 'Andrew Smith'})
output7 = sample.find_one({'Name': 'Victor Sullivan'})
output8 = sample.find_one({'Name': 'Kristina Heath'})
output9 = sample.find_one({'Name': 'Beverly Fuller'})
output10 = sample.find_one({'Name': 'Charles Juarez'})
# Prints the result from the database; Will print None if not there

pprint(output1)
pprint(output2)
pprint(output3)
pprint(output4)
pprint(output5)
pprint(output6)
pprint(output7)
pprint(output8)
pprint(output9)
pprint(output10) 
# Ends time of printing
end2 = time.time()
print ("The time of execution of the reading is :",
       (end2 - end1) * 10 ** 3, "ms")
