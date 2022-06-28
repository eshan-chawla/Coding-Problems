class Solution:

    def check_start(intervals):
        intervals[0] 

    def merge(intervals):
        def check_start(intervals):
            intervals[0] 
        i=0
        j=1
        intervals.sort(key = check_start(intervals))
        print(intervals)

        # if(len(intervals)==2 and intervals[0][1]>=intervals[1][0] and intervals[0][0]!=intervals[0][1] and intervals[1][0]!=intervals[1][1]):
        #     intervals[0][1] = max(intervals[0][1],intervals[1][1])
        #     intervals[0][0] = min(intervals[0][0],intervals[1][0])
        #     intervals.remove(intervals[1])
        # k = len(intervals)  
        
        # while(i<len(intervals) and j<len(intervals) and k!=2):
        #     if(intervals[i][1]>=intervals[j][0] and intervals[i][0]!=intervals[i][1] and intervals[j][0]!=intervals[j][1]):
        #         intervals[i][1]=max(intervals[i][1],intervals[j][1])
        #         intervals[i][0]=min(intervals[i][0],intervals[j][0])
        #         intervals.remove(intervals[j])
        #     elif(intervals[i][1]<intervals[j][0]):
        #         i+=1
        #         j+=1
    
    
        return intervals
    print(merge([[2,3],[4,5],[6,7],[8,9],[1,10]]))
                