# Banker Algorithm

def sefety_algorithm(avilable, allocation_matrix, need_matrix, number_of_processe, calm_allocation, calm_need):
    print("-----------------------Safety Algorithm------------------------")
    work=[]
    for item in avilable:
        work.append(item)

    finish=[]
    for i in range(number_of_processe):
        finish.append(False)
    
    sefe_processes=[]

    count=0

    while count < number_of_processe:
        found=False

        for i in range(number_of_processe):
            if finish[i] == False:

                can_execute=True
                for j in range(calm_need):
                    if need_matrix[i][j] > work[j]:
                        can_execute = False
                        break

                if can_execute == True:
                    for j in range(calm_allocation):
                        work[j] = work[j] + allocation_matrix[i][j]
            
                    process_name="p" + str(i)
                    sefe_processes.append(process_name)
                    finish[i]=True
                    count+=1
                    found=True

                    print(f"Process {process_name} executed. Work: {work}")

        if found == False:
            print("processes not found")
            break


    print("------------------------------- Result --------------------------------")
    if len(sefe_processes) == number_of_processe:
        print("System is SAFE")
        print("Safe Sequence:")
        for preocess in sefe_processes:
             print(preocess , end=" -> ")
        print("End")
        
    else:
        print("System is UNSAFE")
        print("DEAD LOCK")

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

number_of_processe=int(input("How many your processe? :"))


avilable=[]
n=3
while len(avilable) < n :
    try:
        value=int(input("Enter the number of value : "))
        avilable.append(value)
    except ValueError:
        print("please enter the number")
        
while True:
    print("-----------------------Alloacation Matrix------------------------")
    rows_allocation=number_of_processe
    calm_allocation=int(input("Enter the number of calm : "))

    allocation_matrix=[]

    for i in range(rows_allocation):
        row=[]
        for j in range(calm_allocation):
            data=int(input(f"Enter [{i}][{j}] : "))
            row.append(data)
        allocation_matrix.append(row)
    
    for r in allocation_matrix:
        print(r)

    print("-----------------------Max Matrix------------------------")   
    rows_max=number_of_processe
    calm_max=int(input("Enter the number of calm : "))

    max_matrix=[]
    for i in range(rows_max):
        row_max=[]
        for j in range(calm_max):
            data_max=int(input(f"Enter [{i}][{j}] : "))
            row_max.append(data_max)
        max_matrix.append(row_max)   

    for i in max_matrix:
        print(i)


    print("-----------------------need Matrix------------------------")

    rows_need=number_of_processe
    calm_need=int(input("Enter the number of calm : "))

    need_matrix = []
    for i in range(rows_need):
       row_need=[]
       for j in range(calm_need):
           row_need.append(max_matrix[i][j] - allocation_matrix[i][j])
       need_matrix.append(row_need)

    for i in need_matrix:
        print(i)
    break

sefety_algorithm(avilable, allocation_matrix, need_matrix, number_of_processe, calm_allocation, calm_need)