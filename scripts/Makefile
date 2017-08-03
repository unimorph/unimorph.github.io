all: index.html schema.html contact.html publications.html software.html

index.html:
	#python generate_table.py ../data-content.html ../data-orig.html
	python generate_page.py ../data-orig.html ../index-orig.html ../index.html

schema.html:
	python generate_page.py ../schema-orig.html ../index-orig.html ../schema.html


contact.html:
	python generate_page.py ../contact-orig.html ../index-orig.html ../contact.html

software.html:
	python generate_page.py ../software-orig.html ../index-orig.html ../software.html

publications.html:
	python generate_page.py ../publications-orig.html ../index-orig.html ../publications.html	
