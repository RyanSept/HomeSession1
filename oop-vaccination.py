class Vaccination(object):
    '''
    This is the Vaccination class from which vaccination types inherit
    '''
    num_doses = 1
    doses_given = 0
    dates_given = []

    def is_done(self):
        if self.doses_given==num_doses:
            return True
        return False

    def dates_of_vaccination(self):
        if len(self.dates_given)<1::
            return None
        return "The doses were given on the date(s): "+\
                ', '.join(self.dates_given)
    
    def doses_left(self):
        if self.doses_given==self.num_doses:
            return 'All doses have been given'
        return ''+str(self.num_doses-self.doses_given)+' doses left to go.'


        
