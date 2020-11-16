
import csv

DIVS = ""
FUNCTS = ""

with open('./resources.csv', newline='') as csvfile:

	resourceReader = csv.reader(csvfile, delimiter=',')

	counter = 0
	year = ''
	yearCompare = ''
	for row in resourceReader:
		# print(row)
		if counter > 0:
			postDate = row[0]
			year = postDate.split('-')[0]
			description = row[1]
			identifier = row[2]

			if year != yearCompare:
				NEW_YEAR_STRING = "\n\n\n**********\n\n{year}\n\n**********\n\n\n".format(year=year)
				FUNCTS += NEW_YEAR_STRING
				DIVS += NEW_YEAR_STRING
				yearCompare = year

			FUNCTS += 'compareDate("{postDate}");\n'.format(postDate=postDate)

			DIVS += '''<div class="container" style="display: none;" id="{postDate}">\n'''.format(postDate=postDate, description=description, identifier=identifier)
			DIVS += '''<h4 data-toggle="collapse" data-target="#{postDate}_collapse">{description} (posted: {postDate})</h4>\n'''.format(postDate=postDate, description=description, identifier=identifier)
			DIVS += '''<div id="{postDate}_collapse" class="collapse"><iframe width="560" height="315" src="https://www.youtube.com/embed/{identifier}&t=15" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>\n'''.format(postDate=postDate, description=description, identifier=identifier)
			DIVS += '''<p>{description} (posted: {postDate})</p>\n</div></div>\n'''.format(postDate=postDate, description=description, identifier=identifier)
		counter+=1


print(FUNCTS)
print(DIVS)