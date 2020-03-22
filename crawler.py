from bs4 import BeautifulSoup
import requests
import json
courses_data = {}

def get_dep_links():
	url = 'https://ssb-prod.ec.middlebury.edu/PNTR/saturn_midd.course_catalog_utlq.catalog_page_by_dept?p_term=202020'
	source = requests.get(url).text
	soup = BeautifulSoup(source, 'lxml')
	
	lis = soup.find_all('li') #find all li tags
	department_links = {}
	for li in lis:
		link = li.a.get('href')
		department_links[li.a.text] = 'https://ssb-prod.ec.middlebury.edu/PNTR/' + link
	return department_links


def get_courses(source, department):

	soup = BeautifulSoup(source, 'lxml')

	trs = soup.find_all('tr')
	for i in range(2, len(trs)-1):	#iterate through all appropriate lines on the page
		tds = trs[i].find_all('td')
		if tds[0].find('a') != None:	#if not a second line of the previous course
			CRN = tds[0].a.text

			#create a key-value binding of the course
			#key: CRN, value: empty
			courses_data[CRN] = {}

			#fill in the values of this course
			courses_data[CRN]["CRN"] = CRN
			courses_data[CRN]["Department"] = department
			courses_data[CRN]["Course_code"] = tds[2].text
			courses_data[CRN]["CW"] = tds[4].text
			courses_data[CRN]["Seats_avail"] = tds[6].text
			courses_data[CRN]["Reserved_incoming"] = tds[8].text
			courses_data[CRN]["Course_title"] = tds[14].text
			courses_data[CRN]["Room"] = tds[22].text
			courses_data[CRN]["Instructor"] = tds[24].text

			#time is tricky so I'm extracting it separately
			courses_data[CRN]["Days"] = tds[16].text
			courses_data[CRN]["Time"] = {
				"M": (tds[18].text,tds[20].text) if 'M'in courses_data[CRN]["Days"] else "No Class",
				"T": (tds[18].text,tds[20].text) if 'T'in courses_data[CRN]["Days"] else "No Class",
				"W": (tds[18].text,tds[20].text) if 'W'in courses_data[CRN]["Days"] else "No Class",
				"R": (tds[18].text,tds[20].text) if 'R'in courses_data[CRN]["Days"] else "No Class",
				"F": (tds[18].text,tds[20].text) if 'F'in courses_data[CRN]["Days"] else "No Class"
			}
			
				

		elif trs[i-1].find('a') != None:	# it is the second row of the previous course
			CRN = trs[i-1].find('td').a.text
			courses_data[CRN]["Days"] += trs[i].find_all('td')[16].text
			courses_data[CRN]["Time"] = {
				"M": (tds[18].text,tds[20].text) if 'M'in tds[16].text else courses_data[CRN]["Time"]['M'],
				"T": (tds[18].text,tds[20].text) if 'T'in tds[16].text else courses_data[CRN]["Time"]['T'],
				"W": (tds[18].text,tds[20].text) if 'W'in tds[16].text else courses_data[CRN]["Time"]['W'],
				"R": (tds[18].text,tds[20].text) if 'R'in tds[16].text else courses_data[CRN]["Time"]['R'],
				"F": (tds[18].text,tds[20].text) if 'F'in tds[16].text else courses_data[CRN]["Time"]['F']
			}

		else:	#it is the third row
			CRN = trs[i-2].find('td').a.text
			courses_data[CRN]["Days"] += trs[i].find_all('td')[16].text
			courses_data[CRN]["Time"] = {
				"M": (tds[18].text,tds[20].text) if 'M'in tds[16].text else courses_data[CRN]["Time"]['M'],
				"T": (tds[18].text,tds[20].text) if 'T'in tds[16].text else courses_data[CRN]["Time"]['T'],
				"W": (tds[18].text,tds[20].text) if 'W'in tds[16].text else courses_data[CRN]["Time"]['W'],
				"R": (tds[18].text,tds[20].text) if 'R'in tds[16].text else courses_data[CRN]["Time"]['R'],
				"F": (tds[18].text,tds[20].text) if 'F'in tds[16].text else courses_data[CRN]["Time"]['F']
			}




if __name__ == '__main__':
	#1. get links of all departments
	dep_links = get_dep_links()


	#2. click on all departments 
	#	and get all classes on the department page
	i=0
	for department in dep_links:
		url = dep_links[department]
		source = requests.get(url).text
		get_courses(source, department)
		i+=1
		print(str(i) + '/58	' + department + ' finished')
	
	
	#3. save all data to courses_data.json
	with open('courses_data.json', 'w') as f:
		json.dump(courses_data, f, indent=4)


	print("HOORAY!\nNow you have all the info of all Midd courses.\nThe crawler is exhausted...")

