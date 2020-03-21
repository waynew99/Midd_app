import json
from datetime import datetime


#print("Current Time =", current_time)


launch_guide = "type in the option# to use the function: \n 1. Course Search - display the course details listed on bannerweb \n 2. Classroom availability check \n "

def pretty_print(course):
	print("Course name: ", course.[course_code],
		  "\nCRN:			", course.[CNR])
	

def course_search():
	f = open("example_courses.json")
	courses = json.load(f)
	given = input("\nenter the course you would like to search: ")
	for i in courses:
		if given.lower() in i.lower() or given.lower() in courses[i]["course_title"].lower():
			print(type(courses[i]))
			pretty_print(courses[i])

def room_search():
	f = open("example_courses.json")
	courses = json.load(f)

	given = input("\nPlease enter the room you would like to search: e.g. 'MBH104'\n")
	for i in courses:
			if check_room_occupied(courses[i]):
				print("\nThe classroom is currently occupied:(\n" + courses[i]["course_code"] + ": " + courses[i]["course_title"] + ", until " + courses[i]["end"] + '\n')
				return
	print("\nThe room is empty:D\n")
	#next = next_course(given)
	#print("The next class starts at" + next["start"] + ". It's " + next["course_code"] + ": " + next["course_title"])

def check_room_occupied(given_course):
	now = datetime.now()
	tt = now.timetuple()
	#print('weekday: ', tt[6])	#6 is the day of the week, 0mon
	#print('current time: ', tt[3], tt[4])	#3hour, 4minute

	days = ['M','T','W','R','F','S']
	if days[tt[6]] in given_course["days"]:
		# if day of the week matches
		current_hour = tt[3]
		current_minute = tt[4]
		c_start_h = int(given_course["start"][0:2])
		c_start_m = int(given_course["start"][3:5])
		c_end_h = int(given_course["end"][0:2])
		c_end_m = int(given_course["end"][3:5])

		current_time = current_hour * 60 + current_minute
		c_start_time = c_start_h * 60 + c_start_m
		c_end_time = c_end_h * 60 + c_end_m

		if 'PM' in given_course["start"]:
			c_start_time += 720
		if 'PM' in given_course["end"]:
			c_end_time += 720

		if c_start_time < current_time and current_time < c_end_time:
			return True
		else:
			return False



if __name__ == '__main__':
	func = input(launch_guide)
	
	if (func == "1"):
		course_search()
	elif (func == "2"):
		room_search()
	else:
		print("Irregular input\n" + launch_guide)