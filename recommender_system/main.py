import import_data.functions as id
import convert_answers.functions as ca
import random

if __name__ == "__main__":
    questions = ["periode", "temperatuur", "budget", "zon"]
    answers = ["zomer", "warm", "hoog", "ja"]
    ca.check_qa(questions, answers)

    properties, qa = id.read_google_sheets()

    ## FIGURE OUT WHICH PERIOD (IF ASKED)
    try:
        period = answers[questions.index("periode")]
        period = [period]
        period.append("")
    except:
        period = ["zomer", "winter", "herfst", "lente", ""]

    relevant_properties = properties[properties["period"].isin(period)]

    ## TEMPERATURE SUBSET
    countries = ca.subset_based_on_temperature(relevant_properties, questions, answers)
    relevant_properties = relevant_properties[relevant_properties["country"].isin(countries)]

    ## SUN SUBSET
    countries = ca.subset_based_on_sun(relevant_properties, questions, answers)
    relevant_properties = relevant_properties[relevant_properties["country"].isin(countries)]

    ## BUDGET SUBSET
    countries = ca.subset_based_on_budget(relevant_properties, questions, answers)
    relevant_properties = relevant_properties[relevant_properties["country"].isin(countries)]

    ## MEANS OF TRANSPORT SUBSET
    countries = ca.subset_based_on_transport(relevant_properties, questions, answers)
    relevant_properties = relevant_properties[relevant_properties["country"].isin(countries)]

    print(countries)

    recommended_country = random.choice(countries)

    print(recommended_country)