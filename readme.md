#### Quiz Performance Analysis Web App
Overview
Welcome to the Quiz Performance Analysis Web App! This web app allows users to analyze their quiz performance across multiple topics, identify areas of strength and weakness, track their progress over time, and receive personalized recommendations to improve their scores.

The app uses data from quizzes that users have taken and visualizes important metrics such as weak and strong areas, the number of mistakes in each topic, and trends in performance over time. Users can input their unique User ID to get tailored insights into their learning journey, helping them focus on areas that need improvement.

Features
Weak Area Detection: Automatically identifies which topics need more attention based on your average quiz scores.
Strength Area Detection: Highlights the topics you’re excelling in to help you maintain your strengths.
Performance Trends: Shows how your performance is improving or declining over time.
Mistake Analysis: Identifies common mistakes in different topics, helping you focus on the areas with the most room for improvement.
Personalized Recommendations: Gives tailored practice questions based on your weaknesses (more practice for weaker topics and fewer questions for stronger ones).
Student Persona & NEET Rank Prediction: Based on your quiz performance, you’ll get a persona (High Achiever, Competent Learner, etc.) and a predicted NEET rank.
Project Setup
Follow these steps to get the project up and running locally on your machine.

Prerequisites-


Python 3.6+
pip (Python’s package installer)
Installation
Clone the repository:

Terminal-
git clone https://github.com/kartikeyYadav19/Quiz-Performance-Analysis-Web-App.git
Navigate to the project folder:

Terminal-
cd quiz-performance-analysis
Create and activate a virtual environment:

Terminal-
python -m venv venv
venv\Scripts\activate

Terminal-
python3 -m venv venv
source venv/bin/activate
Install the required dependencies: Once the virtual environment is activated, install the necessary Python libraries with:

Terminal-
pip install -r requirements.txt
Running the App
To start the app, simply run:

Terminal-
streamlit run backend.py
This will open the app in your default web browser.

Accessing the Data
The app uses publicly available quiz data and user submission data. You don’t need to worry about uploading any personal data — the app will load the data directly from the provided API endpoints.

Once the app is running, you’ll be prompted to enter your User ID. This is the unique identifier for your quiz data. After inputting your ID, the app will display various analyses and visualizations to help you understand your performance.

Project Approach
The main goal of this project was to help users make sense of their quiz data, so we focused on creating clear, actionable insights.

Data Processing: We first load the quiz data from three main sources:

Quiz Data: Contains the scores for each quiz.
Submission Data: Includes information about the specific questions answered in each quiz.
Historical Data: Tracks the performance over time to analyze trends and improvements.
Weak and Strong Areas: The app automatically detects weak areas (topics where you scored below a certain threshold) and strong areas (topics where you excelled). We also make sure to suggest more practice for the topics that need improvement while maintaining focus on your strengths.

Performance Trends: By analyzing the quiz scores over time, the app visualizes your progress. Whether you're improving or struggling in certain areas, the trend chart helps you see the bigger picture.

Mistakes Analysis: By tracking the number of mistakes made in each topic, we give you a clear indication of where you are making the most errors. This helps you prioritize practice in those topics to avoid repeating mistakes.

Recommendations: Based on the analysis of weak and strong areas, the app generates personalized practice recommendations. For weaker topics, you’ll get more questions to practice, and for stronger topics, the app suggests fewer questions.

Student Persona & Rank Prediction: The app generates a persona based on your average score and gives an estimated NEET rank, which serves as an additional metric for tracking your progress.


## Visualizations
For Analyzing and giving summary , I have taken the student performance with user id ="YcDFSO4ZukTJnnFMgRNVwZTE4j42".

Here are some key visualizations from the analysis:

### Weak Areas Visualization
![Weak Areas](Screenshots\Weak_Area.png)
### Strength Areas Visualization
![Strength Areas](Screenshots\Strength_Area.png)

### Improvemnts Trend Visualization
![Performance Trend](Screenshots\Improvement.png)

### Mistakes Analysis Visualization
![Mistakes Analysis](Screenshots\Mistakes_By_Topics.png)
Okay, let's make this sound a bit more human and less like a robot wrote it:

#### Insights Summary:

Looking at this student's performance, a few things jump out.  He is  been tagged as a "Competent Learner," which is a good starting point, and his predicted NEET rank is around 2000.  That gives us something to aim for, right?

It's clear that He has got a good handle on some areas, especially "Human Health and Disease" and "Body Fluids and Circulation."  Those scores are pretty solid, so they definitely have a good foundation there.  It's like they get the big picture stuff.

But, like everyone, there are some spots where he is struggling a bit. "Human Reproduction" seems to be a real stumbling block – high number of mistakes, low scores, the whole nine yards.  "Respiration and Gas Exchange" and "Principles of Inheritance and Variation" are also a bit shaky.  It makes you wonder if he is  getting tripped up on the details or if the core concepts just aren't clicking yet.  Even though "Body Fluids and Circulation" shows up as a strength, it's interesting that the system is recommending some easy practice questions.  Maybe it's just a case of needing a quick refresher to keep things fresh.

Looking at how his scores have changed over time is going to be really important.  If we see an upward trend, that's awesome – it means he is learning and improving.  If not, we need to figure out why and adjust the study plan.  For example, if he is  making a lot of mistakes in "Body Fluids and Circulation" at first but then got better, it means he can overcome their difficulties.

The recommendations are.  Hitting those weaker areas – "Human Reproduction," "Respiration," and "Genetics" – with medium-difficulty questions makes sense.  That's where they need the most work.  And keeping up with the stronger areas with some easy questions is a smart move too.

Overall, this student has real potential.  With some focused effort on those tricky topics and a good study strategy, they could definitely boost that NEET rank. It's all about understanding where he is struggling and giving him the right tools to succeed.

If you'd like to contribute to this project, feel free to fork the repository, make your changes, and create a pull request. Contributions are welcome, whether it’s fixing bugs, improving documentation, or adding new features!
### Here is the video of the working of the code and the result it gives-[Recording](Screenshots\Recording.mp4)
[Mail](yadavkartikey1901@gmail.com)