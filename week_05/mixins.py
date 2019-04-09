import json
import xml.etree.ElementTree as ET

class Jsonable:
    
    def to_json(self,indent=4):
        return 'dict:'+'\n'+json.dumps(self.__dict__,indent=4) + '\n'+'type:'+str(self.__class__.__name__)


    @classmethod
    def from_json(self,json_string):
        return json.loads(json_string)


class Xmlable:
    
    def to_xml(self):
        return ET.dump(self.__dict__)

    @classmethod
    def from_xml(xml_string):
        pass

class Corgi(Jsonable,Xmlable):
    
    def __init__(self,name='',types=''):
        self.name=name
        self.types=types
    
    def __str__(self):
        return str(self.__dict__)

    def __repr__(self):
        return str(self)

    def __eq__(self,other):
        return str(self)==str(other)

dogz=Corgi("Scotty",'Welsh')
corgz=Corgi('Jannet','idk other types')
smth=dogz.from_json(json.dumps(dogz.__dict__))
print(smth)
print(dogz)
print(smth==dogz)
#XML documenetation was too confusing,leaving this for a bit later
#print(dogz.from_json(str(corgz.__dict__)))
#print(dogz.to_xml())