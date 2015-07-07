import json
from datetime import datetime


correctAnswerMap = {
	"horizontal_slider_1":25,
	"horizontal_slider_2":12.5,
	"horizontal_slider_3":37.5,
	"horizontal_slider_4":62.5,
	"horizontal_slider_5":75,
	"horizontal_slider_6":87.5,
	"horizontal_slider_7":100,
	"line_shape_1":18,
	"line_shape_2":9,
	"line_shape_3":27,
	"line_shape_4":45,
	"line_shape_5":54,
	"line_shape_6":63,
	"line_shape_7":72,
	"hor_curve_1":30,
	"hor_curve_2":15,
	"hor_curve_3":45,
	"hor_curve_4":75,
	"hor_curve_5":90,
	"hor_curve_6":105,
	"hor_curve_7":120,
	"square_area_1":20,
	"square_area_2":10,
	"square_area_3":30,
	"square_area_4":50,
	"square_area_5":60,
	"square_area_6":70,
	"square_area_7":80,
	"circle_area_1":20,
	"circle_area_2":10,
	"circle_area_3":30,
	"circle_area_4":50,
	"circle_area_5":60,
	"circle_area_6":70,
	"circle_area_7":80,
	"horizontal_direction_1":250,
	"horizontal_direction_2":125,
	"horizontal_direction_3":375,
	"horizontal_direction_4":625,
	"horizontal_direction_5":750,
	"horizontal_direction_6":875,
	"horizontal_direction_7":850,
	"angle_1":7.5,
	"angle_2":3.75,
	"angle_3":11.25,
	"angle_4":18.75,
	"angle_5":22.5,
	"angle_6":26.25,
	"angle_7":30,
	"height_1":50,
	"height_2":25,
	"height_3":75,
	"height_4":125,
	"height_5":150,
	"height_6":175,
	"height_7":200,
	"width_1":100,
	"width_2":50,
	"width_3":150,
	"width_4":250,
	"width_5":300,
	"width_6":350,
	"width_7":400,
	"texture_1":20,
	"texture_2":10,
	"texture_3":30,
	"texture_4":50,
	"texture_5":60,
	"texture_6":70,
	"texture_7":80,
	"vertical_slider_1":25,
	"vertical_slider_2":12.5,
	"vertical_slider_3":37.5,
	"vertical_slider_4":62.5,
	"vertical_slider_5":75,
	"vertical_slider_6":87.5,
	"vertical_slider_7":100,
	"vertical_direction_1":100,
	"vertical_direction_2":50,
	"vertical_direction_3":150,
	"vertical_direction_4":250,
	"vertical_direction_5":300,
	"vertical_direction_6":350,
	"vertical_direction_7":400
}



optFile = open("res.txt","w")
json_data=open('data.json')
data = json.load(json_data)
json_data.close()

#getting all users:
allUsers = []
for obj in data:
	if obj['user'] not in allUsers:
		allUsers.append(str(obj['user']))
#-----------------
#getting filtered users:
userTrueCounts = {}
filteredUsers = []
for user in allUsers:
	userTrueCounts[user] = 0

for user in allUsers:
	for obj in data:
		if obj['user']==user:
			if obj['is_question_endTime']=="true":
				userTrueCounts[user] += 1

for user in userTrueCounts.keys():
	if userTrueCounts[user]==84:
		filteredUsers.append(user)


optFile.write("Total users in logs : " + str(len(allUsers))+"\n")
optFile.write("All users : " + str(allUsers)+"\n")
optFile.write("Filtered users in logs : " + str(len(filteredUsers))+"\n")
optFile.write("Filtered users : " + str(filteredUsers)+"\n")
#-----------------
#getting all questions
lineShapeQuestionList = []
questionList = []


for obj in data:
	if obj['question'] not in questionList:
		questionList.append(str(obj['question']))
"""
for obj in data:
	if ("line_shape" in obj['question']) or ("hor_curve" in obj['question']):
		if obj['question'] not in lineShapeQuestionList:
			lineShapeQuestionList.append(str(obj['question']))

for obj in data:
	if obj['question'] not in questionList:
		if ("line_shape" not in obj['question']) and ("hor_curve" not in obj['question']):
			questionList.append(str(obj['question']))		
"""

#print lineShapeQuestionList
#print questionList
questionValueMap = {}
questionTimeMap = {}
totalQuestionTimeMap = {}
for question in questionList:
	questionValueMap[question] = 0
	questionTimeMap[question] = []
	totalQuestionTimeMap[question] = []

for question in lineShapeQuestionList:
	questionTimeMap[question] = []
	totalQuestionTimeMap[question] = []

#-----------------
#average values for each question (except line shape)
numberOfUsers = len(filteredUsers)
if numberOfUsers > 0 :
	for question in questionList:
		for obj in data:		
			if obj['question'] == question:
				if obj['end_value'] == "true":
					questionValueMap[question] += float(obj['value'])

	for question in questionValueMap.keys():
		questionValueMap[question] = questionValueMap[question]/numberOfUsers


	optFile.write("------------------\n")
	optFile.write("End_values by user\n")
	optFile.write("------------------\n")
	userEndValueMap = {}
	for user in filteredUsers:
		userEndValueMap[user] = []

	for user in filteredUsers:
		for obj in data:
			if obj['user']==user:
				if obj['end_value']=="true":
					userEndValueMap[user].append((str(obj['question']),str(obj['value'])))

	for user in userEndValueMap.keys():
		optFile.write("---\n")
		optFile.write(user+"\n")
		optFile.write("---\n")
		for entry in userEndValueMap[user]:
			optFile.write(entry[0] + " : " + entry[1]+"\n")

	optFile.write("------------------\n")
	optFile.write("End_value errors by user\n")
	optFile.write("------------------\n")	
	for user in userEndValueMap.keys():
		optFile.write("---\n")
		optFile.write(user+"\n")
		optFile.write("---\n")
		for entry in userEndValueMap[user]:
			#error = (float(entry[1])-(float(correctAnswerMap[entry[0]]))/float(correctAnswerMap[entry[0]]))*100.0
			error = ((float(entry[1])-(float(correctAnswerMap[entry[0]])))/float(correctAnswerMap[entry[0]]))*100.0
			#print float(entry[1])-(float(correctAnswerMap[entry[0]]))
			#print float(correctAnswerMap[entry[0]])
			#print ((float(entry[1])-(float(correctAnswerMap[entry[0]])))/float(correctAnswerMap[entry[0]]))*100.0
			#print "-------"
			"""
			if error<0.0:
				error *= -1
			"""
			optFile.write(entry[0] + " : " + str(error)  +"\n")

	optFile.write("------------------\n")
	optFile.write("Average end_values\n")
	optFile.write("------------------\n")
	for question in questionValueMap.keys():
		optFile.write(str(question) + " : " + str(questionValueMap[question])+"\n")

	averageEndValueErrorMap = {
		"vertical_curve":[],
		"horizontal_curve":[],
		"height":[],
		"width":[],
		"circle_area":[],
		"horizontal_distance":[],
		"texture":[],
		"slider":[],
		"angle":[],
		"square_area":[],
		"vertical_distance":[],
		"vertical_slider":[]
	}
	optFile.write("------------------\n")
	optFile.write("Average end_value errors\n")
	optFile.write("------------------\n")
	x = 1
	for question in questionValueMap.keys():
		#error = ((float(correctAnswerMap[question])-float(questionValueMap[question]))/float(correctAnswerMap[question]))*100.0		
		error = ((float(questionValueMap[question])-(float(correctAnswerMap[question])))/float(correctAnswerMap[question]))*100.0
		"""
		if error<0.0:
			error *= -1
		"""
		print x, question,error
		x+=1
		if "line_shape" in question:			
			averageEndValueErrorMap["vertical_curve"].append(error)
		elif "hor_curve" in question:
			averageEndValueErrorMap["horizontal_curve"].append(error)
		elif "height_" in question:
			averageEndValueErrorMap["height"].append(error)
		elif "width_" in question:
			averageEndValueErrorMap["width"].append(error)
		elif "texture_" in question:
			averageEndValueErrorMap["texture"].append(error)
		elif "horizontal_slider_" in question:
			averageEndValueErrorMap["slider"].append(error)
		elif "vertical_slider_" in question:
			averageEndValueErrorMap["vertical_slider"].append(error)
		elif "square_area_" in question:
			averageEndValueErrorMap["square_area"].append(error)
		elif "circle_area_" in question:
			averageEndValueErrorMap["circle_area"].append(error)
		elif "horizontal_direction_" in question:
			averageEndValueErrorMap["horizontal_distance"].append(error)
		elif "vertical_direction_" in question:
			averageEndValueErrorMap["vertical_distance"].append(error)
		elif "angle_" in question:
			averageEndValueErrorMap["angle"].append(error)
		optFile.write(str(question) + " : " + str(error)+"\n")

	#-----------------
	#total and average time taken for each question

	for user in filteredUsers:
		for question in questionTimeMap.keys():
			for obj in data:
				if obj['question'] == question and obj['user'] == user:
					if obj['start_value'] == "true":
						epoch = datetime.fromtimestamp(0)
						curTime = datetime.strptime(str(obj['datetime']), "%H:%M:%S:%f")
						curSecondsFromEpoch = (curTime - epoch).total_seconds()
						questionTimeMap[question].append([user,curSecondsFromEpoch])
					if obj['end_value'] == "true":
						for i in range(0,len(questionTimeMap[question])):
							if questionTimeMap[question][i][0]==user:
								epoch = datetime.fromtimestamp(0)
								curTime = datetime.strptime(str(obj['datetime']), "%H:%M:%S:%f")
								curSecondsFromEpoch = (curTime - epoch).total_seconds()
								diff = curSecondsFromEpoch - questionTimeMap[question][i][1]
								if diff<0:
									diff *= -1
								questionTimeMap[question][i] = [user,diff]

	for user in filteredUsers:
		for question in totalQuestionTimeMap.keys():
			#print question
			for obj in data:
				if obj['question'] == question and obj['user'] == user:
					if obj['is_question_startTime'] == "true":
						epoch = datetime.fromtimestamp(0)
						curTime = datetime.strptime(str(obj['datetime']), "%H:%M:%S:%f")
						curSecondsFromEpoch = (curTime - epoch).total_seconds()
						totalQuestionTimeMap[question].append([user,curSecondsFromEpoch])
					if obj['is_question_endTime'] == "true":
						for i in range(0,len(totalQuestionTimeMap[question])):
							if totalQuestionTimeMap[question][i][0]==user:
								epoch = datetime.fromtimestamp(0)
								curTime = datetime.strptime(str(obj['datetime']), "%H:%M:%S:%f")
								curSecondsFromEpoch = (curTime - epoch).total_seconds()
								diff = curSecondsFromEpoch - totalQuestionTimeMap[question][i][1]
								#print question,diff
								if diff<0:
									diff *= -1
								totalQuestionTimeMap[question][i] = [user,diff]
					
	optFile.write("------------------\n")
	optFile.write("Interaction Time stats by question and user\n")
	optFile.write("------------------\n")
	temp = 0
	for user in filteredUsers:
		optFile.write("------\n")
		optFile.write(user+"\n")
		optFile.write("------\n")
		temp = 0
		for question in questionTimeMap.keys():
			for entry in questionTimeMap[question]:
				if entry[0]==user:
					optFile.write(str(question) + " : " + str(entry[1])	+" sec.\n")
					temp += entry[1]
		optFile.write("Total number of seconds user "+ user +" actually interacted with elements : " + str(temp) +" sec.\n")

	optFile.write("------------------\n")
	optFile.write("Average interaction time per question\n")
	optFile.write("------------------\n")
	for question in questionTimeMap.keys():
		total = 0.0
		for entry in questionTimeMap[question]:
			total+=entry[1]
		optFile.write(str(question)+" : "+str(total/numberOfUsers) +" sec.\n")

	optFile.write("------------------\n")
	optFile.write("Average interaction time taken for study\n")
	optFile.write("------------------\n")
	total = 0.0
	for question in questionTimeMap.keys():	
		for entry in questionTimeMap[question]:
			total+=entry[1]
	optFile.write(str(total/numberOfUsers)+" sec.\n")

	optFile.write("------------------\n")
	optFile.write("Total question time stats by question and user\n")
	optFile.write("------------------\n")
	for user in filteredUsers:
		optFile.write("------\n")
		optFile.write(user+"\n")
		optFile.write("------\n")
		temp = 0
		for question in totalQuestionTimeMap.keys():
			for entry in totalQuestionTimeMap[question]:
				if entry[0]==user:
					optFile.write(str(question) + " : " + str(entry[1])	+" sec.\n")
					temp += entry[1]
		optFile.write("Total number of seconds user "+ user +" spent on study : " + str(temp) +" sec.\n")

	optFile.write("------------------\n")
	optFile.write("Average total time taken for study\n")
	optFile.write("------------------\n")
	total = 0.0
	for question in totalQuestionTimeMap.keys():	
		for entry in totalQuestionTimeMap[question]:
			total+=entry[1]
	optFile.write(str(total/numberOfUsers)+" sec.\n")

	optFile.write("------------------\n")
	optFile.write("Average errors by encoding\n")
	optFile.write("------------------\n")	
	for question in averageEndValueErrorMap.keys():
		"""
		print "-----"
		print question
		print averageEndValueErrorMap[question]
		print "-----"
		"""
		optFile.write(question + " : " + str(sum(averageEndValueErrorMap[question])/len(averageEndValueErrorMap[question])) +"\n")

else:
	print "zero users"
"""
myTime1 = "12:22:1:30"
dt = datetime.strptime(myTime1, "%H:%M:%S:%f")
epoch = datetime.fromtimestamp(0)
curDt = (dt - epoch).total_seconds()
myTime2 = "12:25:9:358"
dt = datetime.strptime(myTime2, "%H:%M:%S:%f")
newDt = (dt - epoch).total_seconds()
optFile.write newDt-curDt
"""