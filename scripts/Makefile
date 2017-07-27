all: index.html data.html contact.html publications.html software.html

data.html:
	#python generate_table.py ../data-content.html ../data-orig.html
	python generate_page.py ../data-orig.html ../index-orig.html ../data.html

index.html:
	python generate_page.py ../project.html ../index-orig.html ../index.html


contact.html:
	python generate_page.py ../contact-orig.html ../index-orig.html ../contact.html

software.html:
	python generate_page.py ../software-orig.html ../index-orig.html ../software.html

publications.html:
	python generate_page.py ../publications-orig.html ../index-orig.html ../publications.html	
