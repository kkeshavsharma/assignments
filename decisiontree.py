
print("hello welcome to the last activity of day")

def want_to_desc():
  input("explain what happened?: ")
  while True:
    desc_input = input("and how will you figure this problem out?: ")
    if desc_input.lower() in ("ok", "", "done", "idk", "i don't know", "0"):
      print("don't bypass, think of valid reasoning.")
      continue
    else:
      print("Great, you just figured out your problem, tommorow figure out with your GOAL!")
      break

def get_distracted():
  while True:
    try:
        print("NO WORRIES! let figure out why you get distracted?")
        dis_input = int(input('''choose one:
        1. scrolling reels on phone.
        2. talking with someone.
        3. got an urgent work, and didn't return on goal.
        4. want to explain in my own words.

        Think and choose number between 1 to 4: '''))
        if dis_input == 1:
          print("tommorow try not to touch your phone until you reach your goal or sub goal")
          break
        elif dis_input == 2:
          print("Talking can be stress brusting but try to contorl if its getting you down, tommorow speak less work hard.")
          break
        elif dis_input == 3:
          temp_dis_input = input("was the work more import then GOAL? yes/no: ")
          if temp_dis_input.lower() in ("y", "yes", "1", "yeah!"):
            print("then its ok, make it done tommorow")
          elif temp_dis_input.lower() in ("n", "no", "0", "nah!"):
            print("getting distracted from unnecessary work can kill your productivity, tommorow set priority for every task.")
          break
        elif dis_input == 4:
            want_to_desc()
            print("JUST REMEMBER THIS, DONT GET DISTRACTED TOMMOROW!")
            break
        else:
            print("OOPS! look like you choose invalid option, PLEASE CHOOSE NUMBER 1 TO 4")
            continue
    except ValueError:
            print("Invalid input! Please enter a NUMBER (1-5).")
            continue

def get_failed():
  while True:
    try:
        temp_inp = int(input('''lets figure it out?
              1. get distracted.
              2. plan was not good.
              3. less understanding about topics.
              4. failed in any other part.
              5. want to explain in my own words.
              
              Think and choose number between 1 to 5: '''))
              
        if temp_inp == 1:
          get_distracted()
          print("LEARN controling on yourself. don't get DISTRACTED")
          break
        elif temp_inp == 2:
          planning()
          print("PLAN your day, EVERYDAY")
          break
        elif temp_inp == 3:
          print("we cant make things DONE with half knowledge, LEARN MORE today and try again tommorow")
          break
        elif temp_inp == 4:
          print("FAILED? then TRY AGAIN and FAIL AGAIN... repeat until you get it!!")
          break
        elif temp_inp == 5:
          want_to_desc()
          print("NOW LETS MAKE IT DONE TOMMOROW")
          break
        else:
          print("OOPS! look like you choose invalid option, PLEASE CHOOSE NUMBER 1 TO 4")
          continue
    except ValueError:
        print("Invalid input! Please enter a NUMBER (1-5).")
        continue

def planning():
  while True:
    try:
        plan_input = int(input('''why you failed with your plan or its execution?
        1. get Distracted with anything.
        2. it was so hard to execute that i quit.
        3. my plan was a failure or not fit to achive goal.
        4. want to explain in my own words.
        
        Think and choose number between 1 to 4: '''))

        if plan_input == 1:
          get_distracted()
          print("NO DISTRACTION IN PLANNING AND EXECUTING, TRY TO HOLD YOURSELF")
          break
        elif plan_input == 2:
          print("COMPLEX and NEW problems can be hard to understand, try to break it in SMALLER CHUNKS and then make it tommorow.")
          break
        elif plan_input == 3:
          print("LEARN from the MISTAKES you found in your plan today, MODIFY it and make it done Tommorow")
          break
        elif plan_input == 4:
          want_to_desc()
          print("NOW YOU GOT IT!!")
          break
        else: 
          print("OOPS! look like you choose invalid option, PLEASE CHOOSE NUMBER 1 TO 4")
          continue
    except ValueError:
          print("Invalid input! Please enter a NUMBER (1-5).")
          continue

def lack_energy():
 while True:
    try:
      le_input = int(input('''why are'nt you energetic?
      1. used phone late night.
      2. didnt sleep till late night.
      3. over eating make me sleepy.
      4. some urgent work make me tired.
      5. want to explain in my own words.
      
      Think and choose number between 1 to 5: '''))
      if le_input in (1, 2, 3): 
        print("Be deciplined and take care of your sleep shedule and diet to stay healthy. and keep phone AWAY at night")
        break
      elif le_input == 4:
        temp_le_input = input("was the work more import then GOAL? yes/no: ")
        if temp_le_input.lower() in ("y", "yes", "1", "yeah!"):
          print("then its ok, have some rest tonight and make it done tommorow")
        elif temp_le_input.lower() in ("n", "no", "0", "nah!"):
          print("getting distracted from unnecessary work can kill your productivity, tommorow set priority for every task.")
        break
      elif le_input == 5:
          want_to_desc()
          print("JUST REMEMBER THIS, DONT GET TIRED TOMMOROW!")
          break
      else:
          print("OOPS! look like you choose invalid option, PLEASE CHOOSE NUMBER 1 TO 5")
          continue
    except ValueError:   
        print("Invalid input! Please enter a NUMBER (1-5).")
        continue




def main():
  while True:
    try:
            print("its all about you, so dont lie to your self")
            print("what do you think? was your day productive?")

            MainInput = int(input('''1. YES, i was'nt distracted at all and completed my goal for day.
        2. MOSTLY YES, i was productive and managed to complete/Almost Complete goal, but got distracted.
        3. MOSTLY NO, i wasnt working good, but i know i can do better
        4. NO, i was Distracted whole day and did'nt worked at all.

        ''' ))

            if MainInput == 1:
                print("great to listen you are happy with your progess, and reached GOAL!.")
                print("CAN YOU EXPLAIN WHY YOU THINK SO")
                input1 = int(input('''1. Completed my GOAL!, and Did'nt get distracted.
        2. did something very productive, and happy about it.
        3. solved a big problem, and Enhanced experince.

        Think and choose number between 1 to 3: '''))

                if input1 in (1, 2, 3) :
                  print("great, can you do it better then this?")
                  input_a = input("yes/no: ")
                  if input_a.lower() in ("y", "yes", "1", "yeah!"):
                      print("OK THEN PUSH HARDER TOMMOROW")
                  elif input_a.lower() in ("n", "no", "0", "nah!"):
                      print("Great, Keep it UP!")
                else:
                      print("OOPS! look like you choose invalid option, PLEASE CHOOSE NUMBER 1 TO 3")
                break      

            elif MainInput == 2:
                print("good atleast you manage to GOAL! and knowing where you lacking, even if just for short time")
                print("CAN YOU EXPLAIN WHY YOU WERE DISTRACTED? for your better tommorow")
                input2 = int(input('''1. get distracted by phone, call, talkative colleague, etc.
                2. Achived the GOAL but still feeling incomplete.
                3. execution was not good, just worked anyhow.
                4. wasn't prouctive at work cause feeling less energetic.
                5. want to explain it in my own words.

                Think and choose number between 1 to 5: '''))

                if input2 == 1:
                  get_distracted()
                  print("YOU CAN DO IT")
                elif input2 in (2, 3):
                  temp_input2 = input("can you do it better then this? yes/no: ")
                  if temp_input2.lower() in ("y", "yes", "1", "yeah!"):
                    print("then DO IT TOMMOROW!")
                  elif temp_input2.lower() in ("n", "no", "0", "nah!"):
                    print("DON'T OVERTHINK YOU DID WELL!")
                elif input2 == 4:
                  lack_energy()
                  print("YOU CAN DO IT")
                elif input2 == 5:
                  want_to_desc()
                  print("JUST REMEMBER THIS, MAKE YOUR TOMMOROW BETTER!")
                else:
                  print("OOPS! look like you choose invalid option, PLEASE CHOOSE NUMBER 1 TO 5")
                break


            elif MainInput == 3:
                print("very good to know that you are willing to do better and accepting reality")
                input3 = int(input('''CHOOSE OPTION TO MAKE YOUR TOMMOROW BETTER
                1. get distracted by phone, call, talkative colleague, etc.
                2. didnt executed my plan.
                3. wasn't able to complete goal.
                4. wasn't prouctive at work cause feeling less energetic.
                5. wasn't not in good state of mind/ having some personal issue.
                6. want to explain it in my own words.

                Think and choose number between 1 to 6: '''))
                if input3 == 1:
                  get_distracted()
                  print("NOW YOU FIGURED THIS OUT, NOT RUIN YOUR DAY AGAIN TOMMOROW")
                elif input3 == 2:
                  planning()
                  print("planning is very important, it make your tommorow better")
                elif input3 == 3:
                  get_failed()
                  print("NOW MAKE IT HAPPEN TOMMOROW")
                elif input3 == 4:
                  lack_energy()
                  print("Don't be irresponseable man, make the best out of you")
                elif input3 == 5:
                  print("life goes unpridictable and hard sometimes so, have some rest and calm your mind. try to be efficient tommorow ALL THE BEST.")
                elif input3 == 6:
                  want_to_desc()
                  print("NOW YOU GOT WHAT WAS HOLDING YOU BACK, NOT LET IT BE SAME TOMMOROW")
                else:
                  print("OOPS! look like you choose invalid option, PLEASE CHOOSE NUMBER 1 TO 6")
                  
                break


            elif MainInput == 4:
                print("its look like it was a TOUGH DAY. lets try to figure it out.")
                input4 = int(input('''CHOOSE OPTION TO MAKE YOUR TOMMOROW BETTER, WHAT MAKE YOU FEEL NO PRODUCTIVE TODAY
                1. get distracted by phone, call, talkative colleague, etc.
                2. didnt even planned or executed my day.
                3. tried to do my work but get failed and distracted.
                4. wasn't prouctive at work cause feeling less energetic.
                5. wasn't not in good state of mind/ having some personal issue.
                6. want to explain it in my own words.

                Think and choose number between 1 to 6: '''))
                if input4 == 1:
                  get_distracted()
                  print("NOW YOU FIGURED THIS OUT, NOT RUIN YOUR DAY AGAIN TOMMOROW")
                elif input4 == 2:
                  temp_inp = input("did you even plan your day? yes/no: ")
                  if temp_inp.lower() in ("n", "no", "0", "nah!"):
                    print("first plan your day and COME BACK tommorow")
                  elif temp_inp.lower() in ("y", "yes", "1", "yeah!"):
                    planning()
                    print("planning is very important, it make your tommorow better")
                elif input4 == 3:
                  get_failed()
                  print("NOW MAKE IT HAPPEN TOMMOROW")
                elif input4 == 4:
                  lack_energy()
                  print("Don't be irresponseable man, make the best out of you")
                elif input4 == 5:
                  print("life goes unpridictable and hard sometimes so, have some rest and calm your mind. try to be efficient tommorow ALL THE BEST.")
                elif input4 == 6:
                  want_to_desc()
                  print("NOW YOU GOT WHAT WAS HOLDING YOU BACK, NOT LET IT BE SAME TOMMOROW")
                else:
                  print("OOPS! look like you choose invalid option, PLEASE CHOOSE NUMBER 1 TO 6")
                break
            else:
              print("OOPS! look like you choose invalid option, PLEASE CHOOSE NUMBER 1 TO 4")
              continue
    except ValueError:
      print("Invalid input! Please enter a NUMBER (1-6).")
      continue

main()
print("this small activity will help you increase productivity,and track your record")
print("SO COME BACK STRONGER TOMMOROW")