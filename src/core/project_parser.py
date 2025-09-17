#imports



class ProjectParser:
    def __init__(self,project):
        self.project = project
        #create a project parsing agent
    #have a function that checks and converts the type of the project to a string:
    """if the file is a json file, convert it to a string by checking the file extension and reading a file
       if the file is a pdf file, convert it to a txt file and then read the txt file into a string
       if the file is a txt file, read it into a string. 
       if the file is a dictionary, combine the values into a string. 
       if the file is a string, return the string
    """
    #have a function that infers the name of the project frome the project string
    """
    there would be an agent that would be able to infer the name of the project from the project string and return it as a string
    """
    #have a function that infers the project description from the project string
    """
    there would be an agent that would be able to infer the project description from the project string and return it as a string
    """
    #have a function that infers the rest of the values of the dictionary from the project string.
    """
    the agent should be able to return a dictionary with values for the following keys and values:
    Industries: ind1, ind2,.., indn
    Tags: tag1, tag2,..., tagn
    Project Type: pt1, pt2,..., ptn
    Technologies Used: tech1, tech2,..., techn
    Stakeholders: st1, st2,..,stn
    Objectives: obj1, obj2,..,objn
    Location: loc1, loc2,...,locn
    Regulatory Context: reg1, reg2,...,regn

    the value for each key should be a string of values separated by commas and if the agent cannot infer a value then the value should be an empty string
    """

    #final dictionary preparation function
    """
    In this function we add the values of the name and description to the dictionary
    then we loop through the keys of the dictionary. If the value is not an empty string we convert the string to a list of strings   
    if the value is an empty string then we remove the key from the dictionary.
    """
    