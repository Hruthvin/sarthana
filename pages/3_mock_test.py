import streamlit as st
import random

# Pre-defined sets of questions for each topic
questions_db = {
    "Indian Economy": [
        ("What is the GDP growth rate of India?", ["A. 6%", "B. 6.5%", "C. 7%", "D. 7.5%"], "C"),
        ("Which organization regulates the Indian money market?", ["A. RBI", "B. SEBI", "C. NABARD", "D. IRDA"], "A"),
        ('What does GDP stand for?', ['Gross Domestic Product', 'Gross Development Policy', 'General Domestic Product'], 'a'),
        ("Which sector contributes the most to India's GDP?", ['Agriculture', 'Industry', 'Services'], 'c'),
        ('What is core inflation?', ['Inflation excluding food and fuel prices', 'Inflation including only fuel prices', 'Inflation based on wholesale prices'], 'a'),
        ('Who formulates the fiscal policy in India?', ['RBI', 'SEBI', 'Ministry of Finance'], 'c'),
        ('When was NITI Aayog established?', ['2010', '2015', '2020', '2005'], 'b'),
        ('What is the main objective of the "Make in India" initiative?', ['Boost manufacturing', 'Increase agricultural output', 'Promote foreign investment'], 'a'),
        ('The concept of Five-Year Plans in India was adopted from?', ['USA', 'Soviet Union', 'Germany'], 'b'),
        ('The main tool of monetary policy is?', ['Taxation', 'Public expenditure', 'Repo rate'], 'c'),
        ('Which scheme is associated with skill development?', ['PMAY', 'Skill India', 'Make in India'], 'b'),
        ('Where is the headquarters of the World Bank located?', ['New York', 'Washington D.C.', 'Geneva'], 'b'),
        ('WTO deals with?', ['Monetary policies', 'Trade regulations', 'Defense agreements'], 'b'),
        ('Inflation is defined as?', ['Increase in unemployment', 'Fall in production', 'Sustained increase in general price levels'], 'c'),
        ('What is the primary sector of the economy?', ['Agriculture', 'Industry', 'Services'], 'a'),
        ('What does PMAY stand for?', ['Pradhan Mantri Awas Yojana', 'Pradhan Mantri Adarsh Yojana', 'Public Management Awas Yojana'], 'a'),
        ('What is the main objective of "Digital India"?', ['Boost manufacturing', 'Increase internet connectivity', 'Promote agriculture'], 'b'),
        ('When was GST introduced in India?', ['2017', '2015', '2019'], 'a'),
        ('Which institution manages monetary policy in India?', ['RBI', 'SEBI', 'NITI Aayog'], 'a'),
        ('The Green Revolution primarily focused on which sector?', ['Agriculture', 'Industry', 'Services'], 'a'),
        ('What is the main goal of Atmanirbhar Bharat?', ['Self-reliance', 'Increase exports', 'Improve foreign trade'], 'a'),
        ('Which is an example of indirect tax?', ['Income tax', 'GST', 'Corporate tax'], 'b'),
        ('What does FDI stand for?', ['Foreign Direct Investment', 'Financial Domestic Investment', 'Foreign Digital Investment'], 'a'),
        ('Which body is responsible for the monetary policy in India?', ['RBI', 'SEBI', 'Finance Ministry'], 'a'),
        ('What is the purpose of the Pradhan Mantri Krishi Sinchayee Yojana?', ['Improve irrigation', 'Subsidize seeds', 'Offer crop insurance'], 'a'),
        ('Which Indian state is known as the "Rice Bowl of India"?', ['Punjab', 'West Bengal', 'Andhra Pradesh'], 'c'),
        ('What is the main objective of MGNREGA?', ['Employment generation', 'Skill development', 'Urban development'], 'a'),
        ("When was the Planning Commission of India established?", ["A. 1947", "B. 1950", "C. 1955", "D. 1957"], "B")
    ],
    "Indian Polity and Governance": [
        ("Who is the Chief Justice of India?", ["A. CJI Deepak Mishra", "B. CJI Sharad Arvind Bobde", "C. CJI Ranjan Gogoi", "D. CJI U.U. Lalit"], "B"),
        ("The Constitution of India was adopted on?", ["A. 26 January 1950", "B. 15 August 1947", "C. 1 January 1950", "D. 26 December 1949"], "A"),
        ("Which part of the Indian Constitution deals with the Fundamental Rights?",  ["A) Part III", "B) Part IV", "C) Part II", "D) Part V"], "A"),
        ("What does the Preamble of the Constitution begin with?",  ["A) Sovereignty", "B) We the People", "C) Justice", "D) None"], "B"),
        ("Which part of the Indian Constitution deals with the Fundamental Rights?", ["A) Part III", "B) Part IV", "C) Part II", "D) Part V"], "A"),
        ("What does the Preamble of the Constitution begin with?",  ["A) Sovereignty", "B) We the People", "C) Justice", "D) None"], "B"),
        ("Which part of the Indian Constitution deals with the Fundamental Rights?", 
         ["A) Part III", "B) Part IV", "C) Part II", "D) Part V"], "A"),
        ("What does the Preamble of the Constitution begin with?", 
         ["A) Sovereignty", "B) We the People", "C) Justice", "D) None"], "B"),
        ("Which part of the Indian Constitution deals with the Fundamental Rights?", 
         ["A) Part III", "B) Part IV", "C) Part II", "D) Part V"], "A"),
        ("What does the Preamble of the Constitution begin with?", 
         ["A) Sovereignty", "B) We the People", "C) Justice", "D) None"], "B"),
        ("Which part of the Indian Constitution deals with the Fundamental Rights?", 
         ["A) Part III", "B) Part IV", "C) Part II", "D) Part V"], "A"),
        ("What does the Preamble of the Constitution begin with?", 
         ["A) Sovereignty", "B) We the People", "C) Justice", "D) None"], "B"),
        ("Which part of the Indian Constitution deals with the Fundamental Rights?", 
         ["A) Part III", "B) Part IV", "C) Part II", "D) Part V"], "A"),
        ("What does the Preamble of the Constitution begin with?", 
         ["A) Sovereignty", "B) We the People", "C) Justice", "D) None"], "B"),
        ("Which part of the Indian Constitution deals with the Fundamental Rights?", 
         ["A) Part III", "B) Part IV", "C) Part II", "D) Part V"], "A"),
        ("What does the Preamble of the Constitution begin with?", 
         ["A) Sovereignty", "B) We the People", "C) Justice", "D) None"], "B"),
        ("Which part of the Indian Constitution deals with the Fundamental Rights?", 
         ["A) Part III", "B) Part IV", "C) Part II", "D) Part V"], "A"),
        ("What does the Preamble of the Constitution begin with?", 
         ["A) Sovereignty", "B) We the People", "C) Justice", "D) None"], "B"),
        ("Which part of the Indian Constitution deals with the Fundamental Rights?", 
         ["A) Part III", "B) Part IV", "C) Part II", "D) Part V"], "A"),
        ("What does the Preamble of the Constitution begin with?", 
         ["A) Sovereignty", "B) We the People", "C) Justice", "D) None"], "B"),
        ("Which part of the Indian Constitution deals with the Fundamental Rights?", 
         ["A) Part III", "B) Part IV", "C) Part II", "D) Part V"], "A"),
        ("What does the Preamble of the Constitution begin with?", 
         ["A) Sovereignty", "B) We the People", "C) Justice", "D) None"], "B"),
        ("Which part of the Indian Constitution deals with the Fundamental Rights?", 
         ["A) Part III", "B) Part IV", "C) Part II", "D) Part V"], "A"),
        ("What does the Preamble of the Constitution begin with?", ["A) Sovereignty", "B) We the People", "C) Justice", "D) None"], "B"),
        ("Who is the first President of India?", ["A. Dr. Rajendra Prasad", "B. Dr. Zakir Husain", "C. Dr. V. V. Giri", "D. Dr. Abdul Kalam"], "A")
    ],
     "Geography": [
        ("What is the innermost layer of the Earth called?", 
         ["Mantle", "Core", "Crust", "Lithosphere"], "b"),
        ("Which river is known as the 'Sorrow of Bihar'?", 
         ["Ganga", "Kosi", "Yamuna", "Brahmaputra"], "b"),
        ("What is the largest ocean on Earth?", 
         ["Indian Ocean", "Atlantic Ocean", "Pacific Ocean", "Arctic Ocean"], "c"),
        ("Which is the highest mountain peak in the world?", 
         ["K2", "Kangchenjunga", "Everest", "Makalu"], "c"),
        ("Which continent is known as the 'Dark Continent'?", 
         ["Asia", "South America", "Africa", "Australia"], "c"),
        ("Which desert is the largest in the world?", 
         ["Sahara", "Gobi", "Atacama", "Thar"], "a"),
        ("What is the capital city of Australia?", 
         ["Sydney", "Melbourne", "Canberra", "Perth"], "c"),
        ("Which planet is known as the 'Blue Planet'?", 
         ["Mars", "Earth", "Neptune", "Uranus"], "b"),
        ("What is the main source of energy for the Earth's climate system?", 
         ["Volcanoes", "The Moon", "The Sun", "The Core"], "c"),
        ("Which country has the largest population in the world?", 
         ["India", "USA", "China", "Indonesia"], "c"),
        # Add 90 more questions below following the same format...
    ],
    "Current Affairs": [
        ("Who is the current President of India?", 
         ["Ram Nath Kovind", "Droupadi Murmu", "Pranab Mukherjee", "A. P. J. Abdul Kalam"], "b"),
        ("Which country hosted the G20 summit in 2023?", 
         ["Indonesia", "India", "Saudi Arabia", "Italy"], "b"),
        ("Which bill aims to replace the colonial-era IPC in India?", 
         ["Bharatiya Nyaya Sanhita Bill", "Lokpal Bill", "GST Bill", "Farm Bills"], "a"),
        ("What is the main objective of the Digital India initiative?", 
         ["Increase digital literacy", "Strengthen digital infrastructure", 
          "Provide government services digitally", "All of the above"], "d"),
        ("Who won the Nobel Peace Prize in 2023?", 
         ["Maria Ressa", "Abiy Ahmed", "Narges Mohammadi", "Greta Thunberg"], "c"),
        ("Which Indian actor received an Oscar in 2023?", 
         ["Shah Rukh Khan", "Allu Arjun", "Deepika Padukone", "None"], "d"),
        ("India's rank in the Human Development Index 2023 is:", 
         ["129", "132", "135", "140"], "b"),
        ("Which organization publishes the Ease of Doing Business Report?", 
         ["World Bank", "IMF", "WTO", "UNDP"], "a"),
        ("Which city is known as the Silicon Valley of India?", 
         ["Mumbai", "Bangalore", "Hyderabad", "Chennai"], "b"),
        ("What is the main goal of the 'Atmanirbhar Bharat' initiative?", 
         ["Self-reliance", "Increase exports", "Improve foreign trade", "Promote FDI"], "a"),
         
        # ... Continue adding questions here from the Word file ...
    ],
    "History": [
        ("The Civil Disobedience Movement was launched in India in response to which British action?", ["The Rowlatt Act", "The Quit India Movement", "The Partition of Bengal", "The Simon Commission"], "A"),
        ("Which event marked the beginning of the First War of Indian Independence in 1857?", 
         ["The Revolt at Meerut", "The Revolt at Delhi", "The Revolt at Kanpur", "The Revolt at Jhansi"], "B"),
        ("Who was the founder of the 'Indian National Congress'?", 
         ["A.O. Hume", "Dadabhai Naoroji", "Swaraj Party", "Mahatma Gandhi"], "A"),
        ("The 'Quit India Movement' was launched in India in which year?", ["1942", "1930", "1920", "1950"], "A"),
        ("The 'Civil Disobedience Movement' was called off after:", 
         ["a) Jallianwala Bagh massacre", "b) Chauri Chaura incident", "c) Gandhi-Irwin Pact", "d) Salt Satyagraha"], "b"),
        ("The 'Simon Commission' was formed in 1927 under the leadership of:", 
         ["a) Lord Irwin", "b) Sir John Simon", "c) Lord Minto", "d) Lord Curzon"], "b"),
        ("The 'Khilafat Movement' was led by:", 
         ["a) Maulana Abul Kalam Azad", "b) Muhammad Ali and Shaukat Ali", "c) Syed Ahmed Khan", "d) M.K. Gandhi"], "b"),
        ("The 'Quit India Movement' was launched in:", 
         ["a) 1930", "b) 1940", "c) 1942", "d) 1947"], "c"),
        ("The 'Lucknow Pact' was signed between:", 
         ["a) Congress and British", "b) Congress and Muslim League", "c) Congress and Marathas", "d) Hindu Mahasabha and Muslim League"], "b"),
        ("The 'Indian National Congress' adopted the 'Purna Swaraj' resolution in the year:", 
         ["a) 1929", "b) 1930", "c) 1942", "d) 1919"], "a"),
        ("The 'Jallianwala Bagh Massacre' occurred in:", 
         ["a) 1915", "b) 1919", "c) 1921", "d) 1923"], "b"),
        ("The 'Poona Pact' was an agreement between:", 
         ["a) Congress and British", "b) Mahatma Gandhi and Dr. B.R. Ambedkar", "c) Congress and Muslim League", "d) Congress and Sikh leaders"], "b"),
        ("The 'Salt March' led by Mahatma Gandhi started from:", 
         ["a) Sabarmati", "b) Allahabad", "c) Dandi", "d) New Delhi"], "a"),
        ("The 'Battle of Saragarhi' was fought in:", 
         ["a) 1857", "b) 1897", "c) 1860", "d) 1914"], "b"),
        ("The 'Brahmo Samaj' was responsible for the abolition of:", 
         ["a) Sati", "b) Untouchability", "c) Child marriage", "d) Dowry"], "a"),
        ("The 'First All India Muslim League' conference was held in:", 
         ["a) 1885", "b) 1906", "c) 1913", "d) 1930"], "b"),
        ("The 'Battle of Plassey' in 1757 was fought between:", 
         ["a) Marathas and British", "b) Mughals and British", "c) Siraj-ud-Daula and British", "d) Sikhs and Mughals"], "c"),
        ("The 'Indian National Congress' split into two factions in the year:", 
         ["a) 1905", "b) 1916", "c) 1907", "d) 1919"], "c"),
        ("The 'Indian Famine Code' was introduced in:", 
         ["a) 1837", "b) 1868", "c) 1878", "d) 1901"], "c"),
        ("The 'Battle of Saragarhi' was fought between:", 
         ["a) British and Sikhs", "b) British and Pathans", "c) Marathas and British", "d) Rajputs and Mughals"], "a"),
        ("The 'Indian Councils Act of 1861' allowed for:", 
         ["a) Establishment of separate electorates", "b) Introduction of elected members in councils", "c) Creation of a legislative council in India", "d) Introduction of reforms for independence"], "c"),
        ("The 'Home Rule Movement' was led by:", 
         ["a) Bipin Chandra Pal", "b) Annie Besant and Bal Gangadhar Tilak", "c) Subhas Chandra Bose", "d) Jawaharlal Nehru"], "b"),
        ("The 'Montagu-Chelmsford Reforms' were implemented in:", 
         ["a) 1909", "b) 1919", "c) 1935", "d) 1940"], "b"),
        ("The 'Gandhi-Irwin Pact' was signed in:", 
         ["a) 1931", "b) 1929", "c) 1930", "d) 1940"], "a"),
        ("The 'Salt March' of 1930 began from:", 
         ["a) Sabarmati Ashram", "b) Dandi", "c) Delhi", "d) Calcutta"], "a"),
        ("The 'Simon Commission' was formed to:", 
         ["a) Implement constitutional reforms in India", "b) Examine the constitutional progress in India", "c) Create a separate Pakistan", "d) Assess British control over India"], "b"),
        ("The 'Moplah Rebellion' of 1921 took place in:", 
         ["a) Kerala", "b) Tamil Nadu", "c) Maharashtra", "d) Uttar Pradesh"], "a"),
        ("The 'Salt Satyagraha' took place in:", 
         ["a) Gujarat", "b) Bengal", "c) Maharashtra", "d) Tamil Nadu"], "a"),
    ]
}

# Function to display the quiz questions
def mock_test():
    st.write("### Mock Test - Choose the correct answer for each question")

    # Get topics from the database
    topics = list(questions_db.keys())

    # Randomly select 5 questions from each topic
    selected_questions = {}
    for topic in topics:
        selected_questions[topic] = random.sample(questions_db[topic], 5)

    user_answers = {}

    # Loop through each selected question and present it
    for idx, (topic, questions) in enumerate(selected_questions.items(), 1):
        st.write(f"### {topic} Questions")
        for i, (question, options, correct_answer) in enumerate(questions, 1):
            selected_option = st.radio(f"Q{i}: {question}", options, key=f"{topic}_radio_{i}")
            
            # Save user answer
            user_answers[f"{topic}_{i}"] = {
                'question': question,
                'options': options,
                'selected_option': selected_option,
                'correct_answer': correct_answer
            }

    # Submit button
    if st.button("Submit Quiz"):
        score = 0
        st.write("### Results")

        # Evaluate answers
        for idx, answer in user_answers.items():
            topic, question_num = idx.split('_')
            st.write(f"**{question_num}: {answer['question']}**")
            st.write(f"Your Answer: {answer['selected_option']}")
            st.write(f"Correct Answer: {answer['correct_answer']}")
            
            # Check if the answer is correct
            if answer['selected_option'] == answer['correct_answer']:
                score += 1
            st.write("---")
        
        st.write(f"Your Score: {score}/{len(selected_questions[topic])}")

if __name__ == "__main__":
    mock_test()
