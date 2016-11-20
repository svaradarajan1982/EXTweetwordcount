# EXTweetwordcount

## MIDS W205 Exercise 2

## Steps to run the file:

**Step 1:** Clone the code base EXTweetwordcount from the github location

**Step 2:** Ensure postgres is running. You can check whether postgres is running by running the following command:  
          1. ps aux | grep post   
          2. If postgres is not running. Start postgres: /data/start_postgres.sh

**Step 3:** Change directory into /root/EXTweetwordcount

**Step 4:** Run the [shell-wrapper](shell_wrapper.sh) script as: bash shell_wrapper.sh

**Step 5:** Code should produce a print out all the outputs on the screen and create top20.html bar chart file

**Note:** Histogram of [top 20](top20.html) words is presented as a html document instead of .png file. Bokeh does not have a save as .png option. Download the HTML file and open in browser or copy paste the HTML code into a text file and open in any browser.
