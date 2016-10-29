import datetime
class Vaccination(object):
    '''
    This is the Vaccination class from which is the parent of all vaccination
    types
    '''
    max_doses = 0
    doses_given = 0
    def __init__(self):
        self.dates_given = []

    #checks if all vaccinations have been given
    def is_done_vaccinating(self):
        if self.doses_given==self.max_doses:
            return True
        return False
    #returns the dates of vaccination
    def dates_of_vaccination(self):
        if len(self.dates_given)<1:
            return 0
        return "The doses were given on the date(s): "+\
                ', '.join(self.dates_given)
    
    def doses_left(self):
        if self.doses_given==self.max_doses:
            return 'All doses have been given'
        return ''+str(self.max_doses-self.doses_given)+' dose(s) left to go.'
    
    def to_vaccinate(self,age):
        pass
    
    def record_vaccinate(self,age):
        if self.to_vaccinate(age):
            self.doses_given+=1
            date = datetime.date.today().isoformat() 
            self.dates_given.append(date)
        elif self.is_done_vaccinating():
            return self.doses_left()

#Examples
class Polio(Vaccination):
    max_doses = 4
    def to_vaccinate(self,age):
        '''takes age in months'''
        if age>=2 and age<=72 and self.doses_given<self.max_doses:
            return True
        return False

class DPT(Polio):
    '''Diphtheria,Pertussis and Whooping Cough vaccine'''
    max_doses = 5
    #has same age range as polio

class BCG(Vaccination):
    '''Tuberculosis Vaccine'''
    max_doses = 1
    def to_vaccinate(self,age):
        '''takes age in months'''
        if age>=0 and self.doses_given<self.max_doses:
            return True
        return False


    

                                
