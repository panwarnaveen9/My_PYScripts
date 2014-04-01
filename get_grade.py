#!/usr/bin/python
import urllib
import urllib2
import re

my_dict = {}
grades = ["A", "A-", "B", "B-", "C", "C-", "D", "D-", "F" ]

roll_no = int(input('Enter Roll Number - '))
htmls = []
htmls.append("<HTML><HEAD><TITLE>Grade Details</TITLE><style>h3 {text-align:center}</style></HEAD><BODY bgcolor='#EFEAD1'><br />")

for grade in grades:
	url = 'https://isas.iiit.ac.in/grade/course.php'
	values = {'rno' : roll_no, 'grade' : grade }
	data = urllib.urlencode(values)
	req = urllib2.Request(url)
	response = urllib2.urlopen(req,data)
	the_page = response.read()
#	f = open('template_downloaded','r')
#	the_page = f.read()
	
	result = re.search('<th>(.*?)</th>.*?<th>(.*?)</th>.*?<th>(.*?)</th>(.*)</table>',the_page)
	kk = result.group(4)
	if(kk!=""):
		result1 = re.search('<td>(.*?)</td>.*?<td>(.*?)</td>.*?<td>(.*?)</td>(.*)</tr>', kk)
		if(grade == "A"):
			my_dict[result.group(1)] = result1.group(1)
			htmls.append("<h3>" + result.group(1) + " - " + result1.group(1) + "</h3>")
			my_dict[result.group(2)] = result1.group(2)
			htmls.append("<h3>" + result.group(2) + " - " + result1.group(2) + "</h3>")
			htmls.append("<br /><table align=center border=2 cellpadding=0 cellspacing=0><tr><th>Grade</th><th>Courses</th></tr>")
		if(result1.end()>=3):
			my_dict[grade] = result1.group(3)
			htmls.append("<tr><td>" + grade + "</td><td>")
			htmls.append(result1.group(3) + "</td></tr>")
		
htmls.append("</table></BODY></HTML>")

write_f = open('result.html','w')
for i in htmls:
	write_f.write(i)
	write_f.write("\n")
write_f.close()

#print my_dict
