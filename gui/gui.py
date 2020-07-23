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
