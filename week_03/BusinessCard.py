import json
import sys

#Pretty bruthe force I know :D

def html_creator(filename):
    file_json_data=open(filename,'r')
    json_data=json.load(file_json_data)
    file_json_data.close()
    generated_htmls=[]
    for k,people in json_data.items():
        for person in people:
            generated_htmls.append(person['first_name']+'.html')

            person_html=open(person['first_name']+'.html','w+')
            person_html.write('<!DOCTYPE html>\n<html>\n<head>\n\t<title>'+person['first_name']+' '+person['last_name']+'</title>')
            person_html.write('\n\t<link rel="stylesheet" type="text/css" href="styles.css">\n</head>\n<body>')
            person_html.write('\n\t<div class="business-card '+person['gender']+'">\n\t\t<h1 class="full-name">'+person['first_name']+' ' +person['last_name']+'</h1>')
            person_html.write('\n\t\t<img class="avatar" src="avatars/'+person['first_name'].lower()+'.png">\n\t\t<div class="base-info">')
        
            for k,v in person.items():
                if type(v)!=list and k!='avatar' and k!='last_name' and k!='first_name':
                    person_html.write('\n\t\t\t<p>'+str(k)+':'+str(v)+'</p>')
        
            person_html.write('\n\t\t</div>\n\t\t<div class="interests">\n\t\t\t<h2>Interests:</h2>\n\t\t\t<ul>')
        
            for interest in person['interests']:
                person_html.write('\n\t\t\t\t <li>'+interest+'</li>')
        
            person_html.write('\n\t\t\t</ul>\n\t\t</div>\n\t\t<div class="skills">\n\t\t\t\t<h2>Skills:</h2>\n\t\t\t\t<ul>')

            for skill in person['skills']:
                person_html.write('\n\t\t\t\t <li>'+skill['name']+'-'+str(skill['level'])+'</li>')

            person_html.write('\n\t\t\t</ul>\n\t\t</div>\n\t</div>\n</body>\n</html>')

            person_html.close()
    return generated_htmls


def main(filename):
    print(html_creator(filename))

if __name__ == '__main__':
    filename = sys.argv[1]
    main(filename)