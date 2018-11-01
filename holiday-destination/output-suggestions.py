import json
import os
import random
import settings as stt

def create_possible_suggestions(questions, answers, countries, country_information):
    suggestion_list = countries
    for i in range(0, len(questions)):
        countries = [item.get("country") for item in country_information if answers[i] in item[questions[i]]]
        suggestion_list = list(set(suggestion_list) & set(countries))
    return suggestion_list


def recommend_single_country(countries):
    return random.choice(countries)

def write_output_as_json(recommendation, filename):
    cwd = os.getcwd()
    with open(cwd + '/' + filename, 'w') as outfile:
        json.dump(recommendation, outfile)

questions_list = ["Avontuurlijk of ontspannen?",
                  "Welke periode?",
                  "Budget?",
                  "Moet het warm zijn?"]

answers_list = ["Avontuurlijk",
                "Winter",
                "Oneindig",
                "Nee"]


def main():
    suggestions = create_possible_suggestions(questions=questions_list, answers=answers_list,
                                              countries=stt.list_of_countries,
                                              country_information=stt.list_of_dicts_country_information)
    recommendation = recommend_single_country(suggestions)
    print(recommendation)

    filename = 'output_ruby.json'
    write_output_as_json(recommendation, filename)

if __name__ == "__main__":
    main()

def write_output_as_json(recommendation, filename):
    cwd = os.getcwd()
    with open(cwd + '/' + filename, 'w') as outfile:
        json.dump(recommendation, outfile)
