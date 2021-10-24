def colorsurvey():
    colors = ["red", "green", "blue", "purple"]
    # List of color
    like = []
    # Empty list for like
    dislike = []
    # Empty list for dislike
    for i in range(len(colors)):  # For loop in colors list
        while True:
            try:
                a = input("Do you like " + colors[i] + "?")
                if a == "Yes" or a == "yes" or a == "y" or a == "Y":
                    like.append(colors[i])  # store like color
                    break

                elif a == "No" or a == "no" or a == "N" or a == "n":
                    dislike.append(colors[i])  # store dislike color
                    break

                else:
                    print("Sorry, please answer with Yes or No.")

            except ValueError:
                continue

    if not like:
        print("You don't like all colors")

    elif not dislike:
        print("You like all colors")

    else:
        toStr1 = ' '.join(like)
        toStr2 = ' '.join(dislike)
        print("You like " + toStr1 + " but you don't like " + toStr2)
        # Survey result

colorsurvey()

# # input age
# while True:
#   try:
#     age = int(input("Enter age: "))
#     if age>18 and age<51:
#       print("Age entered successfully...")
#       break;
#     else:
#       print("Age should be >18 and <51...")
#   except ValueError:
#     print("Provide an integer value...")
#     continue
#
# # input gender
# while True:
#   try:
#     gender = input("Enter gender: ")
#     if gender == "Male" or gender == "Female":
#       print("Gender entered successfully...")
#       break;
#     else:
#       print("Gender should be either Male or Female")
#   except:
#     continue
#
# # print age and gender
# print("Age is:", age)
# print("Gender is:", gender)
