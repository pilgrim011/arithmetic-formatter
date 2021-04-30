import re #import regex
import operator
ops = { "+": operator.add, "-": operator.sub }


def arithmetic_arranger(problems, x=False):
    stringified = ",".join(problems)
    isnumonly = re.search("[^\d\s\+\-,]+", stringified)
    numlen = re.findall(r'\b\d+\b', stringified)
    #handle errors
    
    if len(problems) >5:
        return "Error: Too many problems."
    
    elif stringified.find("*") != -1 or stringified.find("/") != -1:
        return "Error: Operator must be '+' or '-'."
    elif isnumonly != None:
        return "Error: Numbers must only contain digits."
    for num in numlen:
        if len(num)>4:
            return "Error: Numbers cannot be more than four digits."
        
    else:   splitter = re.compile(r"[\s|,]").split(stringified)
        #group all first operators, operands and second operators
    first_num = [splitter[item] for item in range(0, len(splitter), 3)]
    plusminus = [splitter[item] for item in range(1, len(splitter), 3)]
    sec_num = [splitter[item] for item in range(2, len(splitter), 3)]
    
    lineone = ""
    linetwo=""
    linethree=""
    result = ""
    final =""

    for (a, b,c) in zip(first_num, plusminus, sec_num):
            
        if len(c) > len(a) and len(c)-len(a)>=2:
            lineone += (" "*(len(c)+1) + a + "    ")
            linetwo += ((b.rjust(len(b)) + " " + c.rjust(len(c)) + "    "))
            linethree += "-" * (2+len(c)) + "    "
            threenospace = "-" * (2+len(c))
            all = str(a) + str(b) + str(c)
            
            result += str(eval(all))
            final +=  " " * ((len(threenospace) - len(str(eval(all))))) + str(eval(all)) + "    "

        elif len(c) > len(a) and len(c)-len(a)==1 and len(a)==1:
            lineone += (" "*(len(c)+1) + a + "    ")
            linetwo += ((b.rjust(len(b)) + " " + c.rjust(len(c)) + "    "))
            linethree += "-" * (2+len(c)) + "    "
            threenospace = "-" * (2+len(c))
            all = str(a) + str(b) + str(c)
            
            result += str(eval(all))
            final +=  " " * ((len(threenospace) - len(str(eval(all))))) + str(eval(all)) + "    "
            
        elif len(c) > len(a) and len(c)-len(a)==1 and len(a)==2:
            lineone += (" "*(len(c)) + a + "    ")
            linetwo += ((b.rjust(len(b)) + " " + c.rjust(len(c)) + "    "))
            linethree += "-" * (2+len(c)) + "    "
            threenospace = "-" * (2+len(c))
            all = str(a) + str(b) + str(c)
            
            result += str(eval(all))
            final +=  " " * ((len(threenospace) - len(str(eval(all))))) + str(eval(all)) + "    "
            
        elif len(c)<len(a) and len(a)-len(c) == 3:
            lineone += ("  " + a.rjust(len(a)) + "    ")
            linetwo += ((b.rjust(len(b)) + " "*len(a) + c.rjust(len(c)) + "    "))
            linethree += "-" * (2+len(a)) + "    "
            threenospace = "-" * (1+len(a))
            all = str(a) + str(b) + str(c)
            
            result += str(eval(all))
            final +=  " " * ((len(threenospace) - len(str(eval(all))))) + str(eval(all)) + "    "
            
        elif len(c)<len(a) and len(a)-len(c) == 2 and len(c)==2:
            lineone += ("  " + a.rjust(len(a)) + "    ")
            linetwo += ((b.rjust(len(b)) + " "*(len(a)-1) + c.rjust(len(c)) + "    "))
            linethree += "-" * (2+len(a)) + "    "
            threenospace = "-" * (1+len(a))
            all = str(a) + str(b) + str(c)
            print(str(eval(all)))
            result += str(eval(all))
            final +=  " " * ((len(threenospace) - len(str(eval(all))))) + str(eval(all)) + "    "
        elif len(c)<len(a) and len(a)-len(c) == 2 and len(c)==1:
            lineone += ("  " + a.rjust(len(a)) + "    ")
            linetwo += ((b.rjust(len(b)) + " "*(len(a)) + c.rjust(len(c)) + "    "))
            linethree += "-" * (2+len(a)) + "    "
            threenospace = "-" * (2+len(a))
            all = str(a) + str(b) + str(c)
            print(str(eval(all)))
            result += str(eval(all))
            final +=  " " * ((len(threenospace) - len(str(eval(all))))) + str(eval(all)) + "    "                
            
        elif len(c)<len(a) and len(a)-len(c) == 1:
            lineone += ("  " + a.rjust(len(a)) + "    ")
            linetwo += ((b.rjust(len(b)) + "  " + c.rjust(len(c)) + "    "))
            linethree += "-" * (2+len(a)) + "    "
            threenospace = "-" * (2+len(a))
            all = str(a) + str(b) + str(c)
            
            result += str(eval(all))
            final +=  " " * ((len(threenospace) - len(str(eval(all))))) + str(eval(all)) + "    "
            
        elif len(a) == len(c):
            lineone += "  " + a.rjust(len(a)) + "    "
            linetwo += ((b.rjust(len(b)) + " " + c.rjust(len(c)) + "    "))
            linethree += "-" * (2+len(a)) + "    "
            threenospace = "-" * (2+len(a))
            all = str(a) + str(b) + str(c)
            
            result += str(eval(all))
            final +=  " " * ((len(threenospace) - len(str(eval(all))))) + str(eval(all)) + "    "
        
    if x != True:
        arranged_problems = lineone.rstrip() + "\n" + linetwo.rstrip() + "\n" + linethree.rstrip()
        return arranged_problems
    elif x == True:
        arranged_problems = lineone.rstrip() + "\n" + linetwo.rstrip() + "\n" + linethree.rstrip() + "\n" + final.rstrip()
        return arranged_problems
        
arithmetic_arranger(["34 + 44", "3801 - 4442", "454 + 443", "1 + 4"])