class Sorts:
    """
    CLass of sorting algorithms
    Author: Okley Julio Andreotti Papafio
    """
    def __init__(self,array):
        self.array = array
    #Swap function to swap elements in an array
    def swap(self, j, i):
        tmp = self.array[j]
        self.array[j] = self.array[i]
        self.array[i] = tmp
    ## Insertion sort function
    ## Complexity O(N)2
    def insertion_sort(self):
        i = 1
        for i in range(len(self.array)):
            j = i-1
            while j>=0:
                if self.array[i]<self.array[j]:
                    self.swap(i,j)
                    i = i-1
                j= j-1
      """
    Selection Sort Function
    Complexity: O(N)2
    In Place Algorithm
    Stable Algorithm
    """
    def selection_sort(self):
        for i in range(len(self.array)):
            curr_min = self.array[i]
            curr_in = i
            j = i+1
            while j< len(self.array):
                if curr_min> self.array[j]:
                    curr_in = j
                    curr_min =self.array[j]
                j=j+1
            self.swap(curr_in,i)
    def outting(self):
        print(self.array)



newthing = Sorts([3,4,6,78,43,54,12,34,56,78,90,12,1300,233,424,789,5,567,12,34,2,1,0,7,65,3342,567,2346,78,54,3,45,75,32,12,21,15,76,42])
newthing.insertion_sort()
newthing.outting()
