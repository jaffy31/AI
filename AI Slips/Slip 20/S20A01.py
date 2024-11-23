class CollegeBot:
    def __init__(self):
        self.college_info = {
            "name": "Poona College",
            "location": "Pune, India",
            "established_year": 2000,
            "programs": ["Computer Science", "Engineering", "Business"],
            "facilities": ["Library", "Sports Complex", "Labs"],
        }

    def get_college_info(self, query):
        query = query.lower()
        if 'name' in query:
            return f"The college name is {self.college_info['name']}."
        elif 'location' in query:
            return f"The college is located in {self.college_info['location']}."
        elif 'established' in query:
            return f"The college was established in {self.college_info['established_year']}."
        elif 'programs' in query:
            return f"The college offers programs in {', '.join(self.college_info['programs'])}."
        elif 'facilities' in query:
            return f"The college provides facilities like {', '.join(self.college_info['facilities'])}."
        else:
            return "I'm sorry, I don't understand that query."

def main():
    college_bot = CollegeBot()

    while True:
        user_query = input("User: ")
        if user_query.lower() == 'exit':
            print("Goodbye!")
            break

        response = college_bot.get_college_info(user_query)
        print(f"College Bot: {response}")

if __name__ == "__main__":
    main()
