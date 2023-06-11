#User function Template for python3

class Solution:
    #Function to sort the array using bubble sort algorithm.
    def bubbleSort(self,arr, n):
        k=0
        for i in range(n):
            for j in range(1,n-k):
                # print(i,j,n-k-1,arr)
                if arr[j-1] > arr[j]:
                    arr[j-1],arr[j]=arr[j],arr[j-1]
            k+=1
        # code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3



if __name__=='__main__':
    n = 5
    arr = [3,1,4,9,7]
    ob = Solution()
    ob.bubbleSort(arr, n)
    for i in arr:
        print(i,end=' ')
    print()

# } Driver Code Ends