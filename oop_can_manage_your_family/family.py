import os.path
import datetime
import json

''' class Person '''
class Person():
    
    EYES_COLORS = ["Blue", "Green", "Brown"]
    GENRES = ["Female", "Male"]

    def __init__(self, id, first_name, date_of_birth, genre, eyes_color):
        
        if type(id) is not int or id < 0:
            raise Exception("id is not an integer")
        if type(first_name) is not str:
            raise Exception("string is not a string")
        if (all(isinstance(item, int) for item in date_of_birth)) and (1<= date_of_birth[0] <= 12) and (1<= date_of_birth[1] <= 31) and (date_of_birth[2]>0) :
            pass
        else:
            raise Exception("date_of_birth is not a valid date")
        if (genre not in self.GENRES) or (type(genre) is not str):
            raise Exception("genre is not valid")
        if (eyes_color not in self.EYES_COLORS) or (type(eyes_color) is not str):
            raise Exception("eyes_color is not valid")
        
        self.__id = id
        self.__first_name = first_name
        self.last_name=''
        self.__date_of_birth = date_of_birth
        self.__genre = genre;
        self.__eyes_color = eyes_color         
        self.children = []
        self.is_married_to = 0
        
    def __str__(self):
        ''' First name + last name'''
        return self.__first_name+" "+self.last_name

    def is_male(self):
        ''' True if male, false if not'''
        return True if self.__genre == "Male" else False

    def age(self):
        '''current age from 5/20/16'''
        getbday = datetime.date(self.__date_of_birth[2],self.__date_of_birth[0],self.__date_of_birth[1])
        return ((datetime.date(2016,05,20))-getbday).days/365

    def __gt__(self,other):
        return self.age() > other.age()

    def __lt__(self, other):
        return self.age() < other.age()

    def __ge__(self, other):
        return self.age() >= other.age()
         
    def __le__(self, other):
        return self.age() <= other.age()

    def __eq__(self, other):
        return self.age() == other.age()
        
    def get_id(self):
        ''' Id '''
        return self.__id
        
    def get_eyes_color(self):
        ''' eye color '''
        return self.__eyes_color
    
    def get_genre(self):
        ''' genre'''
        return self.__genre

    def get_date_of_birth(self):
        ''' birthday '''
        return self.__date_of_birth
        
    def get_first_name(self):
        ''' first name '''
        return self.__first_name

    def getname(self):
        return self.__class__.__name__


    def json(self):
        '''create a dict to store person from json'''
        dict ={
            'first_name': self.__first_name,
            'last_name' : self.last_name,
            'id' : self.__id,
            'date_of_birth' : self.__date_of_birth,
            'genre' : self.__genre,
            'eyes_color' : self.__eyes_color,
            'is_married_to' : self.is_married_to,
            'kind' : self.getname(),
            'children' : self.children
        }
        return dict

    def load_from_json(self,json):
        ''' as long as json is json load into person '''
        if type(json) is not dict:
            raise Exception("json is not valid")
        self.kind = str(json['kind'])
        self.__first_name = str(json['first_name'])
        self.last_name = str(json['last_name'])
        self.__id = json['id']
        self.__date_of_birth = json['date_of_birth']
        self.__genre = str(json['genre'])
        self.__eyes_color = str(json['eyes_color'])
        self.is_married_to=json['is_married_to']
        self.children =json['children']

class Baby(Person):

    def __init__(self, id, first_name, date_of_birth, genre, eyes_color):
        Person.__init__(self, id, first_name, date_of_birth, genre, eyes_color)
        

    '''true if serson is a teen or an adult'''
    def can_run(self):
        return True if (self.getname()== 'Teenager') or (self.getname()== 'Adult') else False 

    '''true if they are baby of senior'''
    def need_help(self):
         return True if (self.getname()== 'Baby') or (self.getname()== 'Senior') else False 


    '''true if they are baby or teen'''
    def is_young(self):
         return True if (self.getname()== 'Baby') or (self.getname()== 'Teenager') else False 


    '''true if an adult or a senior'''
    def can_vote(self):
         return True if (self.getname()== 'Adult') or (self.getname()== 'Senior') else False 

    ''' true if an adult or a senior '''
    def can_be_married(self):
         return True if (self.getname()== 'Adult') or (self.getname()== 'Senior') else False 

    '''return True if is_married_to is different of 0'''
    def is_married(self):
        return True if self.is_married_to != 0 else False

    '''changes is_married to 0 for two people'''
    def divorce(self, p):
        self.is_married_to = 0
        p.is_married_to = 0

    '''if both can be married than set is_married to 0 and ser is_married_to to id of other person'''
    def just_married_with(self, p):
        if((not self.can_be_married()) or (not p.can_be_married())):
            raise Exception("Can't be married")
        if (self.is_married_to != 0) or (p.is_married_to !=0):
            raise Exception("Already married")           
        self.is_married_to = p.get_id()
        p.is_married_to=self.get_id()
        if(self.get_genre == 'Female'):
            self.last_name = p.last_name
        else:
            p.last_name = self.last_name

    '''true if an adult'''
    def can_have_child(self):
        return True if (self.getname()== 'Adult') else False

    '''if both can have baby then create baby with ids from parents'''
    def has_child_with(self, p, id, first_name, date_of_birth, genre, eyes_color):
        if (p is None) or ((p.kind != 'Adult') and (p.kind !='Senior')):
            raise Exception("p is not an Adult of Senior")
        if (not p.can_have_child()) or(not self.can_have_child()):
            raise Exception("Can't have baby")        
        b = Baby(id,first_name,date_of_birth,genre,eyes_color)
        p.children.append(id)
        self.children.append(id)       
        return b

    '''add id of parent if can have child'''
    def adopt_child(self, c):
       if (not self.can_have_child()):
            raise Exception("Can't adopt child")
       self.children.append(c.get_id())
        

class Adult(Person):

    def __init__(self, id, first_name, date_of_birth, genre, eyes_color):
        Person.__init__(self, id, first_name, date_of_birth, genre, eyes_color)
        
    '''true if serson is a teen or an adult'''
    def can_run(self):
        return True if (self.getname()== 'Teenager') or (self.getname()== 'Adult') else False 

    '''true if they are baby of senior'''
    def need_help(self):
         return True if (self.getname()== 'Baby') or (self.getname()== 'Senior') else False 

    '''true if they are baby or teen'''
    def is_young(self):
         return True if (self.getname()== 'Baby') or (self.getname()== 'Teenager') else False 

    '''true if an adult or a senior'''
    def can_vote(self):
         return True if (self.getname()== 'Adult') or (self.getname()== 'Senior') else False 

    ''' true if an adult or a senior '''
    def can_be_married(self):
         return True if (self.getname()== 'Adult') or (self.getname()== 'Senior') else False 

    '''return True if is_married_to is different of 0'''
    def is_married(self):
        return True if self.is_married_to != 0 else False

    '''changes is_married to 0 for two people'''
    def divorce(self, p):
        self.is_married_to = 0
        p.is_married_to = 0

    '''if both can be married than set is_married to 0 and ser is_married_to to id of other person'''
    def just_married_with(self, p):
        if (self.is_married_to != 0)  or (p.is_married_to !=0):
            raise Exception("Already married")           
        if((not self.can_be_married()) or  (not p.can_be_married())):
            raise Exception("Can't be married")
        self.is_married_to = p.get_id()
        p.is_married_to = self.get_id()
        if(self.get_genre == 'Female'):
            self.last_name = p.last_name
        else:
            p.last_name = self.last_name

    '''true if an adult'''
    def can_have_child(self):
        return True if (self.getname()== 'Adult') else False

    '''if both can have baby then create baby with ids from parents'''
    def has_child_with(self, p, id, first_name, date_of_birth, genre, eyes_color):
        if (p is None) or ((p.kind != 'Adult') and (p.kind !='Senior')):
            raise Exception("p is not an Adult of Senior")
        if (not p.can_have_child()) or(not self.can_have_child()):
            raise Exception("Can't have baby")        
        b = Baby(id,first_name,date_of_birth,genre,eyes_color)
        p.children.append(id)
        self.children.append(id)      
        return b

 
    '''add id of parent if can have child'''
    def adopt_child(self, c):
       if (not self.can_have_child()):
            raise Exception("Can't adopt child")
       self.children.append(c.get_id())

class Teenager(Person):

    def __init__(self, id, first_name, date_of_birth, genre, eyes_color):
        Person.__init__(self, id, first_name, date_of_birth, genre, eyes_color)
        
    
    '''true if serson is a teen or an adult'''
    def can_run(self):
        return True if (self.getname()== 'Teenager') or (self.getname()== 'Adult') else False 

    '''true if they are baby of senior'''
    def need_help(self):
         return True if (self.getname()== 'Baby') or (self.getname()== 'Senior') else False 


    '''true if they are baby or teen'''
    def is_young(self):
         return True if (self.getname()== 'Baby') or (self.getname()== 'Teenager') else False 


    '''true if an adult or a senior'''
    def can_vote(self):
         return True if (self.getname()== 'Adult') or (self.getname()== 'Senior') else False 

    ''' true if an adult or a senior '''
    def can_be_married(self):
         return True if (self.getname()== 'Adult') or (self.getname()== 'Senior') else False 

    '''if is_married = 0 then false otherwise true'''
    def is_married(self):
        return True if self.is_married_to != 0 else False

    '''changes is_married to 0 for two people'''
    def divorce(self, p):
        self.is_married_to = 0
        p.is_married_to = 0


    '''if both can be married than set is_married to 0 and ser is_married_to to id of other person'''
    def just_married_with(self, p):
        if (self.is_married_to != 0)  or (p.is_married_to !=0):
            raise Exception("Already married")           
        if(not(self.can_be_married()) or (not  p.can_be_married())):
            raise Exception("Can't be married")
        self.is_married_to = p.get_id()
        p.is_married_to = self.get_id()
        if(self.get_genre == 'Female'):
            self.last_name = p.last_name
        else:
            p.last_name = self.last_name

    '''true if an adult'''
    def can_have_child(self):
        return True if (self.getname()== 'Adult') else False

    '''if both can have baby then create baby with ids from parents'''
    def has_child_with(self, p, id, first_name, date_of_birth, genre, eyes_color):
        if (p is None) or ((p.kind != 'Adult') and (p.kind !='Senior')):
            raise Exception("p is not an Adult of Senior")
        if (not p.can_have_child()) or(not self.can_have_child()):
            raise Exception("Can't have baby")        
        b = Baby(id,first_name,date_of_birth,genre,eyes_color)
        p.children.append(id)
        self.children.append(id)       
        return b

 
    '''add id of parent if can have child'''
    def adopt_child(self, c):
       if (not self.can_have_child()):
            raise Exception("Can't adopt child")
       self.children.append(c.get_id())

class Senior(Person):

    def __init__(self, id, first_name, date_of_birth, genre, eyes_color):
        Person.__init__(self, id, first_name, date_of_birth, genre, eyes_color)
       
    '''true if serson is a teen or an adult'''
    def can_run(self):
        return True if (self.getname()== 'Teenager') or (self.getname()== 'Adult') else False 

    '''true if they are baby of senior'''
    def need_help(self):
         return True if (self.getname()== 'Baby') or (self.getname()== 'Senior') else False 

    '''true if they are baby or teen'''
    def is_young(self):
         return True if (self.getname()== 'Baby') or (self.getname()== 'Teenager') else False 

    '''true if an adult or a senior'''
    def can_vote(self):
         return True if (self.getname()== 'Adult') or (self.getname()== 'Senior') else False 

    ''' true if an adult or a senior '''
    def can_be_married(self):
         return True if (self.getname()== 'Adult') or (self.getname()== 'Senior') else False 

    '''return True if is_married_to is different of 0'''
    def is_married(self):
        return True if self.is_married_to != 0 else False

    '''changes is_married to 0 for two people'''
    def divorce(self, p):
        self.is_married_to = 0
        p.is_married_to = 0

    '''if both can be married than set is_married to 0 and ser is_married_to to id of other person'''
    def just_married_with(self, p):
        if (self.is_married_to != 0)  or (p.is_married_to !=0):
            raise Exception("Already married")           
        if(not self.can_be_married()) or  (not p.can_be_married()):
            raise Exception("Can't be married")
        self.is_married_to = p.get_id()
        p.is_married_to = self.get_id()
        if(self.get_genre == 'Female'):
            self.last_name = p.last_name
        else:
            p.last_name = self.last_name

    '''true if an adult'''
    def can_have_child(self):
        return True if (self.getname()== 'Adult') else False

    '''if both can have baby then create baby with ids from parents'''
    def has_child_with(self, p, id, first_name, date_of_birth, genre, eyes_color):
        if (p is None) or ((p.kind != 'Adult') and (p.kind !='Senior')):
            raise Exception("p is not an Adult of Senior")
        if (not p.can_have_child()) or(not self.can_have_child()):
            raise Exception("Can't have baby")        
        b = Baby(id,first_name,date_of_birth,genre,eyes_color)
        p.children.append(id)
        self.children.append(id)       
        return b

    '''add id of parent if can have child'''
    def adopt_child(self, c):
       if (not self.can_have_child()):
            raise Exception("Can't adopt child")
       self.children.append(c.get_id())

def save_to_file(list, filename):
    with open(filename,'w') as outfile:
        list_of_jsonstrings = []
        for person in list:
            list_of_jsonstrings.append(person.json())
        outfile.write(json.dumps(list_of_jsonstrings,indent=2))


def load_from_file(filename):
    if type(filename) is not str or (not os.path.isfile(filename)) :
        Exception("filename is not valid or doesn't exist")
    else:
        with open(filename) as datafile:
            data = json.load(datafile)
            Persons = []
            for d in data:
                if d['kind'] == 'Adult':
                    p = Adult(0,'',[12,12,12],"Male","Blue")
                if d['kind'] == 'Baby':
                    p = Baby(0,'',[12,12,12],"Male","Blue")
                if d['kind'] == 'Senior':
                    p = Senior(0,'',[12,12,12],"Male","Blue")
                if d['kind'] == 'Teenager':
                    p = Teenager(0,'',[12,12,12],"Male","Blue")                
                p.load_from_json(d)
                Persons.append(p)                
            return Persons
