def sum_of_target(arr,target):
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i] + arr[j] == target:
                print([i,j])
                break
        # else:
        #     print("No match found")
        #     break
sum_of_target([1,2,3,4,5],4)