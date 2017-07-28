# a > b
#
# a >= b
#
# a >= 18  and  day == 3
#
# a >= 18  or  day != 3
#
# a<bug
# a<=bug
# a>=18 or day==3
#
# a<=18 and day !=3
def grade(score):
    if score >= 90:
        return "A"
    else:
        if score >= 80:
            return "B"
        else:
            if score >= 70:
                return "C"
            else:
                if score >= 60:
                    return "D"
                else:
                    return "F"
def main():
    score = 83
    print( "Score:", str(score), "Grade:", grade(score))

if __name__ == "__main__":
    main()
