# Northrop Grumman Code Triton Challenge
# TritonSmart
This was done as part of the above codeathon over 18 Hours. We won the **third** place in this competition.
### Inspiration
Having worked as a Teaching Assistant for a number of courses, our team (Ramkishore, Srinivas, Lenord, Sriram and Joe) thought about utilizing the huge amout of data gathered during the quarter for each course. By data we mean the marks obtained for sections like Calibration Quizes, Class Participation, Attendance, Assignments, Midterms and Final, etc. We can also utilize the details logged by the student for spending time on Assingments, Individual Study, Discussion Sessions, Office Hours and Lab Hours.

### What it does
The system learns the characteristics of each student and each course from the data fed into it. Based on that it predicts the student's progress or recommends to the student how much amount of extra work needs to be put in based on a few metrics to achieve an expected grade for a course.
For example, if the student expects A+ in a course CSE XXX, then the systems, runs the model, fits to the student's characteristics and then gives the output as:

1. You need to put in 50% more effort for assignments
2. You need to put in 43% more effort for midterms

and so on.

The system also tells the user, what grade he might get based on his current performance. This is achieved through clustering of the past data for that course.

### How we built it
We cleaned the data to get necessary features for the clustering models. The backend was a Flask server from Python and the frontend was Vanilla JS with google charts for Visualization.

### Challenges we ran into
We did not have any real data that we could have used directly. So we had to generate data on our with proper distribution to get the correct data.

### Accomplishments that we are proud of
We did not have any prior preparations or idea before the hackathon. We came together at the Hackathon, discussed a lot of ideas, picked this idea, worked overnight to get it implemented. We also bagged the third prize. 

### What's next for TritonSmart
Take it to the next level by putting it into real time use.