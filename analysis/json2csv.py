import json
with open('data.json') as data_file:    
    data = json.load(data_file)

resFile = open("data.csv","w")
resFile.write("user,question,value,end_value,datetime,is_question_startTime,is_question_endTime,start_value,userPlatform,questionset,questionNumber\n")
for obj in data:
	resFile.write(str(obj['user'])+","+str(obj['question'])+","+str(obj['value'])+","+str(obj['end_value'])+","+str(obj['datetime'])+","+str(obj['is_question_startTime'])+","+str(obj['is_question_endTime'])+","+str(obj['start_value'])+","+str(obj['userPlatform'])+","+str(obj['questionset'])+","+str(obj['questionNumber'])+"\n")