import  Split_Infix2

class CreateTree:

    def __init__(self):
        self.stack = []
        self.tree_list = [""]*31
        
    def Tree(self, left, right, root, test, q):
        Stack_or = []           # Storage operator +
        Stack_and = []          # Storage operator &
        Run = True          
        test = split_expression.check_last(test)
        for i in range(len(test)):

            if( test[i] == "(" ):
                Run = False
                self.stack.append(i)
            elif( test[i] == ")"):
                self.stack.pop()

            if(len(self.stack) == 0):
                Run = True

            if( (test[i] == "!") ):
                if(Run == False):
                    pass
                elif(Run == True):
                    if( root != "!" ):
                        Is_joke = split_expression.check_last(test[i+1:])
                        root = test[i]
                        left = Is_joke
                        right = right
            
            if(Run):
                # find top of root tree
                if(test[i] == "+"):
                    max_position_of_or = i
                    Stack_or.append(max_position_of_or)
                # find top of root tree
                if(test[i] == "&"):
                    max_position_of_and = i
                    Stack_and.append(max_position_of_and)
                # And is Least Significant bit
                # Or is Most Significant bit
                if(len(Stack_and) > 0):
                    root = test[max_position_of_and]
                    left = test[:max_position_of_and]
                    right = test[max_position_of_and+1:]
                    
                if(len(Stack_or) > 0):
                    root = test[max_position_of_or]
                    left = test[:max_position_of_or]
                    right = test[max_position_of_or+1:]

        pl = (2*q)+1
        pr = (2*q)+2

        self.tree_list[q] = root
        self.tree_list[pl] = left
        self.tree_list[pr] = right
        # meter checking value recursive value 
        # Do it Step by Step
        print(f"""{index} == >test:{test}
        left: {left}
        root: {root}
        right: {right}
        {"="*100}""")
    #This Term to Postorder 
        if(len(left) == 1):                # Postfix
            self.tree_list[pl] = left[0]
            if( len(right) > 1):
                self.Tree("", "", "", right, pr)
            else:
                if(right == ""):
                    self.tree_list[pr] = right
                else:
                    self.tree_list[pr] = right[0]
            return self.tree_list
        
        self.Tree("", "", "", left, pl)    # Recursive  

        if( len(right) > 1 ):                # Postfix
            self.Tree("", "", "", right, pr) # Recursive
        else:
            if(right == ""):
                self.tree_list[pr] = right
            else:
                self.tree_list[pr] = right[0]
        
        return self.tree_list
##################################################################33

if( __name__ == "__main__" ):
    Input_sting = open('Expression Tree.txt','r')
    Input = Input_sting.read()
    test_input_strings = Input.split("\n")

    for test,index in zip(test_input_strings, range (len(test_input_strings))):
        split_expression = Split_Infix2.boolean(test)
        Test = CreateTree()
        #print(split_expression)
        print("-"*200)
        result = Test.Tree('','','',split_expression.Split_tree(), 0)
        print(index," ==> ",result)
        print("[]"*100)