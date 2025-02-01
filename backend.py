import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import requests
import streamlit as st

# Function to load quiz data 
def load_quiz_data():
    quiz_endpoint = "https://www.jsonkeeper.com/b/LLQT"  
    response = requests.get(quiz_endpoint)
    quiz_data = response.json()
    return pd.json_normalize(quiz_data)

# Function to load quiz submission data
def load_quiz_submission_data():
    quiz_submission_endpoint = "https://api.jsonserve.com/rJvd7g"  
    response = requests.get(quiz_submission_endpoint)
    submission_data = response.json()
    return pd.json_normalize(submission_data)

# Function to load historical quiz data
def load_historical_quiz_data():
    historical_quiz_endpoint = "https://api.jsonserve.com/XgAgFJ"  
    response = requests.get(historical_quiz_endpoint)
    historical_data = response.json()
    return pd.json_normalize(historical_data)

# Function to identify weak areas 
def identify_weak_areas(user_data, threshold=50):
    weak_areas = user_data.groupby('quiz.topic')['score'].mean()  
    weak_areas = weak_areas[weak_areas < threshold]  
    return weak_areas

# Function to identify strength areas 
def identify_strength_areas(user_data, threshold=80):
    strength_areas = user_data.groupby('quiz.topic')['score'].mean()  
    strength_areas = strength_areas[strength_areas > threshold]  
    return strength_areas

# Function to analyze performance trend
def analyze_performance_trend(user_data):
    user_data_sorted = user_data.sort_values(by='quiz_id')  
    user_data_sorted['score_diff'] = user_data_sorted['score'].diff()  
    user_data_sorted = user_data_sorted.dropna(subset=['score_diff']) 
    
    return user_data_sorted[['quiz_id', 'score', 'score_diff']]

# Function to analyze mistakes 
def analyze_mistakes(user_data):
    
    if 'incorrect_answers' in user_data.columns:
        mistakes = user_data[user_data['incorrect_answers'] > 0]  
        mistake_count = mistakes.groupby('quiz.topic')['incorrect_answers'].sum()  
    else:
        mistake_count = pd.Series()  
    return mistake_count

# Function to show average score per topic
def show_average_score_per_topic(user_data):
    avg_score = user_data.groupby('quiz.topic')['score'].mean()  
    st.subheader("Average Score per Topic")
    st.write(avg_score)

# Function to generate recommendations based on weak and strength areas
def generate_recommendations(weak_areas, strength_areas):
    recommendations = []
    
    # Recommendations for weak areas 
    for topic, score in weak_areas.items():
        practice_questions = max(10, 50 - (score / 2))  
        
        recommendations.append({
            'Topic': topic,
            'Suggested Topics': topic,
            'Focus on Difficulty Level': 'Medium',
            'Practice Questions': int(practice_questions)
        })

    # Recommendations 
    for topic, score in strength_areas.items():
        practice_questions = max(5, 20 - (score / 2))  
        
        recommendations.append({
            'Topic': topic,
            'Suggested Topics': topic,
            'Focus on Difficulty Level': 'Easy',
            'Practice Questions': int(practice_questions)
        })
    
    return recommendations

# Function to generate student persona based on score
def generate_student_persona(user_data):
    score = user_data['score'].mean()  
    if score > 90:
        return "High Achiever"
    elif score >= 60:
        return "Competent Learner"
    elif score >= 50:
        return "Struggling Learner"
    else:
        return "At Risk"

# Function to predict NEET rank 
def predict_neet_rank(user_data):
    score = user_data['score'].mean()
    
    if score > 90:
        return 100
    elif score >= 75:
        return 500
    elif score >= 50:
        return 2000
    else:
        return 5000

# Function to visualize weak areas
def visualize_weak_areas(weak_areas):
    if not weak_areas.empty:  
        plt.figure(figsize=(12, 8))
        sns.barplot(x=weak_areas.index, y=weak_areas.values, palette="coolwarm")
        plt.title("Weak Areas (Topics with Low Scores)", fontsize=16)
        plt.xlabel('Topic', fontsize=14)
        plt.ylabel('Average Score', fontsize=14)
        plt.xticks(rotation=45)
        plt.grid(True, linestyle='--', alpha=0.7)
        plt.tight_layout()
        st.pyplot(plt)
        plt.close()
    else:
        st.write("No weak areas found with scores below the threshold.")

# Function to visualize strength areas
def visualize_strength_areas(strength_areas):
    plt.figure(figsize=(12, 8))
    sns.barplot(x=strength_areas.index, y=strength_areas.values, palette="Blues_r")
    plt.title("Strength Areas (Topics with High Scores)", fontsize=16)
    plt.xlabel('Topic', fontsize=14)
    plt.ylabel('Average Score', fontsize=14)
    plt.xticks(rotation=45)
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.tight_layout()
    st.pyplot(plt)
    plt.close()

# Function to visualize performance trend
def visualize_performance_trend(user_data_sorted):
    plt.figure(figsize=(12, 8))
    sns.lineplot(x=user_data_sorted['quiz_id'], y=user_data_sorted['score_diff'], marker='o', color='b')
    plt.title('Score Improvement Over Time', fontsize=16)
    plt.xlabel('Quiz ID', fontsize=14)
    plt.ylabel('Score Difference', fontsize=14)
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.tight_layout()
    st.pyplot(plt)
    plt.close()

# Function to visualize mistakes 
def visualize_mistakes(mistake_count):
    if not mistake_count.empty:  
        plt.figure(figsize=(12, 8))
        sns.barplot(x=mistake_count.index, y=mistake_count.values, palette="viridis")
        plt.title('Mistakes in Topics', fontsize=16)
        plt.xlabel('Topic', fontsize=14)
        plt.ylabel('Number of Mistakes', fontsize=14)
        plt.xticks(rotation=45)
        plt.grid(True, linestyle='--', alpha=0.7)
        plt.tight_layout()
        st.pyplot(plt)
        plt.close()
    else:
        st.write("No mistakes found in the provided data.")

# Function to detect performance gaps
def detect_performance_gaps(user_data, threshold_weak=50, threshold_strong=80):
    weak_areas = identify_weak_areas(user_data, threshold_weak)
    strength_areas = identify_strength_areas(user_data, threshold_strong)
    performance_trend = analyze_performance_trend(user_data)
    mistakes = analyze_mistakes(user_data)

    #Average score per topic
    show_average_score_per_topic(user_data)

    #Results
    if not weak_areas.empty:
        visualize_weak_areas(weak_areas)
    else:
        st.write("No weak areas found with scores below the threshold.")

    visualize_strength_areas(strength_areas)  
    visualize_performance_trend(performance_trend)
    visualize_mistakes(mistakes)

    return weak_areas, strength_areas, performance_trend, mistakes

# Main Streamlit application
def main():
    st.title("Quiz Performance Analysis")

    
    quiz_data = load_quiz_data()
    submission_data = load_quiz_submission_data()
    historical_quiz_df = load_historical_quiz_data()

    # Merge data 
    combined_data = pd.concat([quiz_data, submission_data, historical_quiz_df], ignore_index=True)

    # Show available user_ids for debugging
    st.write("Available User IDs in the data:", combined_data['user_id'].unique())  

    # Input for user_id
    user_id = st.text_input("Please enter your User ID (alphanumeric):", "")

    # Button 
    if st.button("Get Recommendations and Analysis"):
        if user_id:
            
            user_data = combined_data[combined_data['user_id'] == user_id]
            
            if not user_data.empty:
                # Perform analysis 
                weak_areas, strength_areas, performance_trend, mistakes = detect_performance_gaps(user_data)

                #Recommendations with  practice questions
                recommendations = generate_recommendations(weak_areas, strength_areas)
                st.subheader("Recommendations for Improvement")
                for rec in recommendations:
                    st.write(f"**Topic:** {rec['Topic']}, **Suggested Topics:** {rec['Suggested Topics']}, **Focus on Difficulty Level:** {rec['Focus on Difficulty Level']}, **Practice Questions:** {rec['Practice Questions']}")

                #Student persona
                persona = generate_student_persona(user_data)
                st.subheader("Student Persona")
                st.write(f"You are classified as a: **{persona}**")

                # Predicting NEET rank
                predicted_rank = predict_neet_rank(user_data)
                st.subheader("Predicted NEET Rank")
                st.write(f"Your predicted NEET rank is: **{predicted_rank}**")
            else:
                st.warning(f"No data found for User ID: {user_id}")
        else:
            st.info("Please enter a valid User ID.")

if __name__ == "__main__":
    main()
