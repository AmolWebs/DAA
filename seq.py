#Job sequencing
def jobScheduling(jobs):

    # Convert jobs in descending order of profit by bubble sort
    jobs.sort(key=lambda x: x[2], reverse=True)

    # To Identify maximum deadline by comparison
    maxi = jobs[0][1] 
    for job in jobs:
        if job[1] > maxi:
            maxi = job[1]
    
    # Initialize the slot array with -1
    slot = []   
    for i in range(maxi + 1):
        slot.append(-1)

    # Arrangement of jobs with considering maximum deadline and identify the maximum profit and no. of jobs .
    countJobs = 0
    jobProfit = 0
    jobs_done = []
    for i in range(len(jobs)):
        for j in range(jobs[i][1], 0, -1):
            if slot[j] == -1:
                slot[j] = i
                countJobs += 1
                jobs_done.append(jobs[i][0])
                jobProfit += jobs[i][2]
                break

    return countJobs, jobProfit, jobs_done

# jobs = [(1, 4, 20), (2, 1, 10), (3, 2, 40), (4, 2, 30)]
jobs = [(1, 4, 20), (2, 5, 60), (3, 6, 70), (4, 6, 65),(5, 4, 25), (6, 2,80), (7, 2, 10), (8, 2, 22)]
jo = []
count, profit, jo = jobScheduling(jobs)
print("Class: TECSD  Rollno: 39")
print("Name: Kotkar Rahul Pramod")
print(count,profit)
print(jo)