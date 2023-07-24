def select(command):
    
    selected = []
    
    for i in range(len(command)):
        if command[i] == 'FROM':
            frompos = i
            
    for i in range(1, frompos):
        selected.append(command[i])
        
    file = command[frompos + 1]
                
    f = open(file + ".txt", "r")
    contents = f.readlines()
    
    for i in range(len(contents)): 
        contents[i] = contents[i].split()
    
    columnlist = []
    
    for i in range(len(contents[0])):
        attribute = contents[0][i]
        
        if attribute in selected:
            columnlist.append(i)
            
    if selected == ['*']:
        for i in range(len(contents[0])):
            columnlist.append(i)
            
    for i in range(len(contents)):
        out = ''
        
        for j in columnlist:
            out += contents[i][j]
            out += ' '
            
        print(out)
        
    f.close()
   
   
def insert(command):
    
    for i in range(len(command)):
        command[i] = command[i].replace('(', '').replace(')', '')
        
    if command[3] == 'VALUES':
        file = command[2]
        f = open(file + '.txt', "a")
        string = ''
        
        for i in command[4:]:
            string += i
            string += ' '
            
        f.write('\n' + string)
        f.close()
        
    else:
        print("Error in syntax")
   
   
def update(command):
    
    if command[2] != 'SET' or command[6] != "WHERE":
        print("Error in syntax")
        
    else:
        file = command[1]
        f = open(file + '.txt', "r")
        contents = f.readlines()
        
        condition = command[7].replace('=', ' ').split()
        
        for i in range(len(contents)):
            contents[i] = contents[i].split()
            
        for i in range(len(contents[0])):
            if contents[0][i] == command[3]:
                attribute_number = i
                print(attribute_number)
                
            if contents[0][i] == condition[0]:
                condition_attribute = i
                print(condition_attribute)
                
        for i in range(len(contents)):
            if str(condition[1]) == str(contents[i][condition_attribute]):
                contents[i][attribute_number] = command[5]
                
        f.close()
        
        f = open(file + '.txt', "w")
        f.truncate()
        f.close()
        
        f = open(file + '.txt', "a")
        
        for i in contents:
            line = ''
            
            for j in i:
                line += j
                line += ' '
                
            print(line)
            f.write(line + '\n')
            
        f.close()
   
   
def main():
    
    command = input("Enter SQL command: ").replace(',', '').split()
    print()
    
    if command[0] == 'SELECT': 
        select(command)
        
    elif command[0:2] == ['INSERT', 'INTO']:
        insert(command)
    
    elif command[0] == 'UPDATE':
        update(command)
        
        
if __name__ == "__main__":
    main()
    