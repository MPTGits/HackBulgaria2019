
class SingleVariable:
    
    def __init__(self,str_variable):
        self.str_variable=str_variable

    def variable_derive(self):
        if len(self.str_variable)==1 and self.str_variable.isdigit():
            return '0'
        if len(self.str_variable)==1:
            return '1'
        if len(self.str_variable)==3 and self.str_variable[0].isdigit():
            return self.str_variable[0]
        calculation=int(self.str_variable[0])*int(self.str_variable[len(self.str_variable)-1])
        if (int(self.str_variable[len(self.str_variable)-1]))-1==1:
            return str(calculation)+self.str_variable[1:len(self.str_variable)-2]
        return str(calculation)+self.str_variable[1:len(self.str_variable)-1]+str(int(self.str_variable[len(self.str_variable)-1])-1)
    
    @property
    def variable(self):
        return self.str_variable


class Polynom:

    def __init__(self,poly_str):
        self.poly_list=poly_str

    def polynom_derive(self):
        variable_list=self.poly_list.split('+')
        derived_list=[]
        for variable in variable_list:
            eachVariable=SingleVariable(variable)
            if variable.isdigit() and len(variable_list)!=1:
                continue
            derived_list.append(eachVariable.variable_derive())
        return '+'.join(derived_list)



    @property 
    def polynom(self):
        return self.poly_list

import sys

def main():
   str_polynom = sys.argv[1]
   polynom=Polynom(str_polynom)
   print(polynom.polynom_derive())

if __name__=='__main__':
    main()