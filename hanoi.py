
import time

"""
# The towers of Hanoi 2.0
def print_state():
    print(f'A:{state["A"]} B:{state["B"]} C:{state["C"]}')


def change_state(source, destination):
    source_len_last_index = 0
    # state[destination].append(state[source][source_len_last_index])
    # state[source].pop(source_len_last_index)
    # print_state()
    destination_len_last_index = 0
    if len(state[source]) == 0:
        return False
    else:
        source_len_last_index = len(state[source])-1
        if len(state[destination]) > 0:
            destination_len_last_index = len(state[destination])-1
            if state[source][source_len_last_index]>state[destination][destination_len_last_index]:
                return False
            else:
                pass
        else:
            pass
        state[destination].append(state[source][source_len_last_index])
        state[source].pop(source_len_last_index)
        print_state()
        return True


  
def hanoi(n, source, auxiliary, destination):
    time.sleep(0.2)
    

    source_len = len(state[source])
    destination_len = len(state[destination])
    auxiliary_len = len(state[auxiliary])
    all_len = source_len + destination_len + auxiliary_len

    source_last_value =all_len +1 if source_len==0 else state[source][source_len-1]
    auxiliary_last_value =all_len +1 if auxiliary_len==0 else state[auxiliary][auxiliary_len-1]
    destination_last_value=all_len +1 if destination_len==0 else state[destination][destination_len-1]

    # print(f'Last higher val: {source}={source_last_value} {auxiliary}={auxiliary_last_value} {destination}={destination_last_value}')


    # if n==1:
    #     # print ("Move disk 1 from source",source,"to destination",destination)
    #     change_state(source , destination)
    #     print('Completed')
    #     return True
    # hanoi(n-1, source, auxiliary, destination)
    # # print ("Move disk",n,"from source",source,"to destination",destination)
    # change_state(source , destination)
    # hanoi(n-1, auxiliary, destination, source)
    
         





    if destination == "C" and all_len == len(state[destination]):
        print('Completed!')
        return True 
    elif len(state["A"])==1 and len(state["C"])==0 :
        print('step 0')
        change_state(source , destination)
        hanoi(all_len, source, auxiliary, destination)



    elif  change_state(source , auxiliary):
        # print('step 1')
        hanoi(all_len, source, auxiliary, destination)

    elif  change_state(source , destination):
        # print('step 2')
        hanoi(all_len, source, auxiliary, destination)
        
    elif  change_state(auxiliary , destination):
        # print('step 3')
        hanoi(all_len, source, auxiliary, destination)
    
    # elif  change_state(destination,source) and destination == "A":
    #     # print('step 3')
    #     change_state(destination,source)
    #     hanoi(all_len, destination, auxiliary, source)
    
    else:
        print(' ')
        print(' ---deciding...')
        print(' ')
        if destination == "A":
            pass
        else:
            change_state(destination,source)
            hanoi(all_len, destination, auxiliary, source)

        ####Works until 4 disks!
        # if destination == "C":
        #     if auxiliary_len==2:
        #         print('moving..')
        #         change_state(auxiliary , source)
        #     print('A is destiny now')
        #     hanoi(all_len, destination, auxiliary, source)
    
        # else:
        #     if auxiliary_len<2:
        #         print('moving..')
        #         change_state(auxiliary , source)
        #     print('C is destiny now')
        #     hanoi(all_len, destination, auxiliary, source)


        # if auxiliary_len==1:
        #     if destination == "C":
        #         print('simon')
        #         hanoi(all_len, destination, auxiliary, source)
        #     else:
        #         print('simont')
        #         change_state(auxiliary , source)
        #         hanoi(all_len, destination, auxiliary, source)
        # else:
        #     print('passxd')
        #     change_state(auxiliary , source)
        #     hanoi(all_len, destination, auxiliary, source)

        # if auxiliary_len==1 and destination == "C":
        #     if change_state(auxiliary , destination):
        #         print('simon')
        #         hanoi(all_len, destination, auxiliary, source)
        #     else:
        #         print('simont')
        #         hanoi(all_len, destination, auxiliary, source)
        # else:
        #     print('passxd')
        #     change_state(auxiliary , source)
        #     hanoi(all_len, destination, auxiliary, source)


        # print(f'Asi esta C = {state["C"]}')
        # if auxiliary_len>1 and not state['C']:
        #     change_state(auxiliary , 'C')
        #     hanoi(all_len, destination, auxiliary, source)
        # else:
        #     hanoi(all_len, destination, auxiliary, source)


        # # if source_last_value > auxiliary_last_value and auxiliary_last_value > destination_last_value:
        # if state['C']:
        #     hanoi(all_len, destination, auxiliary, source)
        # else:
        #     if auxiliary_len>1:
        #         if source == 'A' and auxiliary_last_value<source_last_value:
        #             change_state(auxiliary , source)
        #         hanoi(all_len, destination, auxiliary, source)
        #     else:
        #         change_state(auxiliary , 'C')
        #         hanoi(all_len, destination, auxiliary, source)


        # if auxiliary_len==1:
        #     if state['C']:
        #         print('TURN AROUND!')
        #         if state['C'][len(state['C'])-1]>auxiliary_last_value:
        #             change_state(auxiliary , 'C')
        #         hanoi(all_len, destination, auxiliary, source)
        #     else:
        #         print('moving and... TURN AROUND!!')
        #         change_state(auxiliary , 'C')
        #         hanoi(all_len, destination, auxiliary, source)
        # else:
        #     if state['A']:
        #         print('TURN AROUNDaa!')
        #         hanoi(all_len, destination, auxiliary, source)
        #     else:
        #         print('movingaa and... TURN AROUNDaaa!!')
        #         change_state(auxiliary , 'A')
        #         hanoi(all_len, destination, auxiliary, source)
            # print('a veer.. TURN AROUND')
            # hanoi(all_len, destination, auxiliary, source)
            

        # if len(state['A'])>1:
        #     if auxiliary_len>1:
        #         print('hola aqui')
        #         print('TURNING THIS SHIIIII x3!!')
        #         hanoi(all_len, destination, auxiliary, source)
        #         return 'aqui'
        #     else:
        #         print('TURNING THIS SHIIIII AGAAAAIN')
        #         change_state(auxiliary , 'C')
        #         hanoi(all_len, destination, auxiliary, source)
        #         return 'jiji'
        # else:
        #     if auxiliary_len>1:
        #         print('TURNING THIS SHIIIII x4!!')
        #         change_state(auxiliary , 'A')
        #         hanoi(all_len, destination, auxiliary, source)
        #     else:
        #         print('TURNING THIS SHIIIII')
        #         hanoi(all_len, destination, auxiliary, source)
        # return ''
    # return False


state = {
    # "A": [6,5,4,3,2,1],
    # "A": [5,4,3,2,1],
    # "A": [4,3,2,1],
    "A": [3,2,1],
    # "A": [2,1],
    # "A": [1],
    "B": [],
    "C": []
}

#to compare

compList = {
    "A: [4, 3, 2, 1] B: [] C: []",
    "A: [4, 3, 2] B: [1] C: []",
    "A: [4, 3] B: [1] C: [2]",
    "A: [4, 3] B: [] C: [2, 1]",
    "A: [4] B: [3] C: [2, 1]",
    "A: [4, 1] B: [3] C: [2]",
    "A: [4, 1] B: [3, 2] C: []",
    "A: [4] B: [3, 2, 1] C: []",
    "A: [] B: [3, 2, 1] C: [4]",
    "A: [] B: [3, 2] C: [4, 1]",
    "A: [2] B: [3] C: [4, 1]",
    "A: [2, 1] B: [3] C: [4]",
    "A: [2, 1] B: [] C: [4, 3]",
    "A: [2] B: [1] C: [4, 3]",
    "A: [] B: [1] C: [4, 3, 2]",
    "A: [] B: [] C: [4, 3, 2, 1]",
}

print('Starting...')
print_state()
hanoi(len(state["A"]), "A", "B", "C")


"""







tower = {
    "A": [6,5,4,3,2,1],
    # "A": [5,4,3,2,1],
    # "A": [4,3,2,1],
    # "A": [3,2,1],
    # "A": [2,1],
    # "A": [1],
    "B": [],
    "C": []
}

def moveTower(source, destination):
    source_last_index = len(tower[source])-1
    tower[destination].append(tower[source][source_last_index])
    tower[source].pop()


# Recursive Python function to solve the tower of hanoi
 
def TowerOfHanoi(n , source, auxiliary, destination):
    print(tower)
    if n==1:
        # print ("Move disk 1 from source",source,"to destination",destination)
        moveTower(source,destination)
        return
    TowerOfHanoi(n-1, source, destination, auxiliary)
    # print ("Move disk",n,"from source",source,"to destination",destination)
    moveTower(source,destination)
    TowerOfHanoi(n-1, auxiliary, source, destination)
    

# def TowerOfHanoi(n , source, destination, auxiliary):
#     if n==1:
#         print ("Move disk 1 from source",source,"to destination",destination)
#         moveTower(source,destination)
#         print(tower)

#         return
#     TowerOfHanoi(n-1, source, auxiliary, destination)
#     print ("Move disk",n,"from source",source,"to destination",destination)
#     moveTower(source,destination)
#     print(tower)
#     TowerOfHanoi(n-1, auxiliary, destination, source)
         
# Driver code
n = len(tower["A"])
TowerOfHanoi(n,'A','B', 'C')
print(tower)
# A, C, B are the name of rods
 
# Contributed By Dilip Jain
