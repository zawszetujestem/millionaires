class Gui:
    @staticmethod
    def welcome(name):
        print(f"Welcome in Millionaires. Only ten questions left to win million, {name}.")

    @staticmethod
    def show_dashboard(question_no, guaranteed_levels, current_money):
        for item in range (1, 11):
            if item in guaranteed_levels:
                print(f"{'-' * 5}Guaranteed money.{'-' * 5}")
            print(f"{'---> ' if question_no == item else ''}{item}. {current_money[item - 1]} PLN")

    @staticmethod
    def show_question(question, answers):
        answers_letter = ['A', 'B', 'C', 'D']
        print(f"Question: {question}")
        print('-' * 30)
        for idx, item in enumerate(answers_letter):
            print(f"{item}. {answers[idx]}")
            print('-' * 30)

    @staticmethod
    def player_options():
        return input("""What you want to do:
        1. Final answer
        2. Get lifeline
        3. End game
        """)

    @staticmethod
    def get_player_answer():
        return input("Choose your answer [A, B, C, D]: \n")

    @staticmethod
    def get_user_lifeline(lifelines, lifelines_done):
        lifelines_list = lifelines
        for idx, lifeline in enumerate(lifelines_list):
            if lifeline not in lifelines_done:
                lifelines_list.append(f"{idx}. {lifeline}")
        lifeline_text = '\n'.join(lifelines_list)
        return input(f"Choose lifelines: \n {lifeline_text}")

    @staticmethod
    def play_again():
        return input("Do you want to play again? [Y/N] \n")

    @staticmethod
    def show_result(score):
        print(f"You win {score}. Congrats! Game over.")
