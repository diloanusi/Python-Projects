#Wi-Fi Diagnostic Tree
#program that leads a person through the steps of fixing a bad Wi-Fi connection

#welcome message
print("Welcome to Wi-Fi Diagnostics")
print("Reboot the computer and try to connect")
answer = str(input("Did that fix the problem? Yes or No: "))
#set rules depending on yes or no
if(answer == 'No'):
             print("Reboot the router and try to connect")
             answer2 = str(input("Did that fix the problem? Yes or No: "))
             if(answer2 == 'No'):
                          print("Make sure the cables between the router & modem are plugged in firmly")
                          answer3 = str(input("Did that fix the problem? Yes or No: "))
                          if(answer3 == 'No'):
                                       print("Move the router to a new location and try to connect")
                                       answer4 = str(input("Did that fix the problem? Yes or No: "))
                                       if(answer4 == 'No'):
                                                    print("Get a new router")
                                       else:
                                                     print("Great! Have a nice day!")
                          else:
                                       print("Great! Have a nice day!")
                                       
             else:
                          print("Great! Have a nice day!")
                                                                              
else:
             print("Great! Have a nice day!")
             
