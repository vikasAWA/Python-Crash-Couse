from survey import AnonymousSurvey

# Define a question
question = "What is the first language you speak?"

my_survey = AnonymousSurvey(question)
my_survey.show_question()

print("\nEnter q any time you want to quit.\n")
while True:
    response = input("Language: ")
    if response == 'q':
        break
    my_survey.store_response(response)
    
print("\nThank you everyone for all your responses.")
my_survey.show_results()
