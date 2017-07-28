def course_grader(test_scores):
    bool="pass"
    sum=0
    for i in test_scores:
        sum+=i
        if i<50:
            bool="fail"
    aveg=sum/len(test_scores)
    if aveg>=70 and bool=="pass":
        return("pass")
    else:
        return("fail")

def main():
    print(course_grader([100,75,45]))     # "fail"
    print(course_grader([100,70,85]))     # "pass"
    print(course_grader([80,60,60]))      # "fail"
    print(course_grader([80,80,90,30,80]))  # "fail"
    print(course_grader([70,70,70,70,70]))  # "pass"

if __name__ == "__main__":
    main()






# //////////////////////////////////////////



import math
def isprime(n):
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    max = n**0.5+1
    i = 3
    while i <= max:
        if n % i == 0:
            return False
        i+=2
    return True

print(isprime(5))
