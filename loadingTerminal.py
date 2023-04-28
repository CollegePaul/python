import time, sys
def loading():
    print ("Loading...")
    for i in range(0, 100):
        time.sleep(0.01)
        sys.stdout.write(u"\u001b[1000D" + str(i + 1) + "%")
        sys.stdout.flush()
    print()


def progress():
    print ("Progress...")
    for i in range(0, 25):
        time.sleep(0.02)
        width = (i + 1)
        #barwidth = "".join("#" for i in range(width))
        #blank = "".join(" " for i in range(25-width))     
        # bar = "[" + barwidth + blank + "]"

        bar = "[" + "#" * width + " " * (25 - width) + "]"   
        sys.stdout.write(u"\u001b[1000D" +  bar)
        sys.stdout.flush()
    print
    
import  random
def progress_multiple(count):
    all_progress = [0] * count
    sys.stdout.write("\n" * count) # Make sure we have space to draw the bars
    while any(x < 25 for x in all_progress):
        time.sleep(0.01)
        # Randomly increment one of our progress values
        unfinished = [(i, v) for (i, v) in enumerate(all_progress) if v < 25]
        index, _ = random.choice(unfinished)
        all_progress[index] += 1
        
        # Draw the progress bars
        sys.stdout.write(u"\u001b[1000D") # Move left
        sys.stdout.write(u"\u001b[" + str(count) + "A") # Move up
        for progress in all_progress: 
            width = progress
            print ("[" + "#" * width + " " * (25 - width) + "]")


#loading()
#progress()
progress_multiple(4)