### This code do Change Input string to Split infix
### and in we find no active Parentheses and we will cut it

### Maintenance 20/8/2020 Change name: Class , Def , variable

class Split_Infix:
    def __init__(self, og):
        self.og = og
        self.stack = ""
        self.operator = "+ & ! - /"
        self.storage = []               # Storage is cut check_last
        self.operator_list = []
        self.operate = []               # Store input string
        self.operate_unique = []        # Store input string are not same
        self.ouput_list = []            # output of This class

    def Split_tree(self):
        Str = self.og       # This is solution of input

        for i, j in zip(Str, range(len(Str))):  # i is str of input, j is length of input
            if(i == "("):                  
                self.ouput_list.append(i)  #add ( in output
                pass

            elif(i in self.operator or i == ")"): 
                if(i != ")"):                       # if i check is ) add that in Output_list
                    self.operator_list.append(i)    # if i check is operator add that in Operator_List

                if(len(self.stack) != 0):               # if Stack have str will add them in Output_list
                    self.operate.append(self.stack)             
                    self.ouput_list.append(self.stack)           

                    if( self.stack not in self.operate_unique):
                        self.operate_unique.append(self.stack)   #Create another List then isn't same str for do Top of Turth table

                self.ouput_list.append(i)               # Other that will add them to Output_list

                self.stack = "" 
            
            else:
                self.stack += i                         # Combine Operate
                if( len(Str) == j+1 and len(self.stack) != 0 ): # Check If it the last Operate
                    self.operate.append(self.stack)
                    self.ouput_list.append(self.stack)

                    if( self.stack not in self.operate_unique):
                        self.operate_unique.append(self.stack)

        return self.ouput_list

    def Check_last(self, test):                 # This def to subtract the outermost parenthesis of the equation
        for i in range(len(test)):              
            if(test[i] == "("):
                self.storage.append([test[i], i])

            elif(test[i] == ")"):
                position_ = self.storage.pop()
                range_bracket = i - position_[1]
                if(range_bracket == len(test)-1):
                    return test[1:-1]

        return test 

    def Get_operator(self):
        return self.operator_list

    def Get_operate(self):
        return self.operate

    def Get_original_list(self):
        return self.ouput_list
        
#################################################################################################################################

if( __name__ == "__main__" ):
    Input_sting = open('Expression Tree.txt','r')
    Input = Input_sting.read()
    test_input_strings = Input.split("\n")

    for test in test_input_strings:
        Testing = Split_Infix(test)
        print("Splite tree",test,"==>",Testing.Split_tree(),'\n')
        print("Out of Parentheses",test,"==>",Testing.Check_last(test),'\n')
        print("="*100)