class boolean:
    def __init__(self, Og):
        self.Og = Og
        self.Stack = ""
        self.Operator = "+ & ! - /"
        self.Storage = []
        self.Operator_List = []
        self.Operate = []
        self.Operate_unique = []
        self.Ouput_list = []

    def Split_tree(self):
        Str = self.Og       # This is solution of input

        for i, j in zip(Str, range(len(Str))):  # i is str of input, j is length of input
            if(i == "("):                  
                self.Ouput_list.append(i)  #add ( in output
                pass

            elif(i in self.Operator or i == ")"): 
                if(i != ")"):                       # if i check is ) add that in Output_list
                    self.Operator_List.append(i)    # if i check is operator add that in Operator_List

                if(len(self.Stack) != 0):               # if Stack have str will add them in Output_list
                    self.Operate.append(self.Stack)             
                    self.Ouput_list.append(self.Stack)           

                    if( self.Stack not in self.Operate_unique):
                        self.Operate_unique.append(self.Stack)   #Create another List then isn't same str for do Top of Turth table

                self.Ouput_list.append(i)               # Other that will add them to Output_list

                self.Stack = "" 
            
            else:
                self.Stack += i 
                if( len(Str) == j+1 and len(self.Stack) != 0 ):
                    self.Operate.append(self.Stack)
                    self.Ouput_list.append(self.Stack)

                    if( self.Stack not in self.Operate_unique):
                        self.Operate_unique.append(self.Stack)

        return self.Ouput_list

    def check_last(self, test):
        for i in range(len(test)):
            if(test[i] == "("):
                self.Storage.append([test[i], i])

            elif(test[i] == ")"):
                position_ = self.Storage.pop()
                range_bracket = i - position_[1]
                if(range_bracket == len(test)-1):
                    return test[1:-1]

        return test 

    def get_operator(self):
        return self.Operator_List

    def get_operate(self):
        return self.Operate

    def get_original_list(self):
        return self.Ouput_list
        
#################################################################################################################################

if( __name__ == "__main__" ):
    Input_sting = open('Expression Tree.txt','r')
    Input = Input_sting.read()
    test_input_strings = Input.split("\n")

    for test in test_input_strings:
        Testing = boolean(test)
        print("Splite tree",test,"==>",Testing.Split_tree(),'\n')
        print("Out of Parentheses",test,"==>",Testing.check_last(test),'\n')
        print("="*100)