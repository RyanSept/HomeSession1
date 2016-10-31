# OOP
Andela Object Oriented Programming Learning Outcome

The program **oop-vaccination.py**  helps keep track of vaccinations done on infants. Vaccinations can be hard to keep track of, ending up in either duplicates or omissions of a vaccination. It keeps track of all the vaccination doses for a particular vaccination that have been given and the dates they were given. 

  

>  **`Vaccination`**   class
> This is the main class that all vaccination types eg. Polio, TB. BCG extend. It offers the following methods:
> 
> method **`is_done_vaccinating`**
> >This method checks if all the vaccination doses for a particular vaccine have been given.
> 
>  method **`dates_of_vaccination`**
>  >This returns a message displaying all dates vaccinations were given.
>
>method   **`doses_left`**
>>Returns the remaining doses to be given
>
>method   **`record_vaccinate`**
>
>>To be called when a vaccination is given out to an infant. It records the day's date and increments the count of the total dosages given so far. Returns a message if all dosages have been given out.


----------
These examples can give further guidance.

**`Polio`** class extends **`Vaccination`**

For Polio vaccination.

**`BCG`** class extends **`Vaccination`**

For Tuberculosis vaccination.

