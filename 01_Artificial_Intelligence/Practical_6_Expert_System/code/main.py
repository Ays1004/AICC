# ============================================================
# AI Practical 6 : Rule-based Expert System
#   Medical diagnosis (Hospitals and medical facilities)
# ============================================================
# Problem statement (handout):
# Implement any one of the following expert systems:
#   I.   Information management
#   II.  Hospitals and medical facilities
#   III. Help desk management
#   IV.  Employee performance evaluation
#   V.   Stock market trading
#   VI.  Airline scheduling and cargo schedules
#
# This is a simple rule-based / forward-chaining expert system:
#   knowledge base + inference engine (if-then rules) + user interface.
#
# Based on the SPPU TE Comp Content repository (KSKA Git).
# Fix: the "memory" question is now worded so that YES means the
# symptom is present (the original question was inverted).
# ============================================================


def knowledge():
    # Knowledge base: symptom -> disease
    return {
        "sneezes": "Cold",
        "temperature": "Fever",
        "weakness": "Iron Deficiency",
        "forgets": "Alzheimer's",
        "cough": "Covid-19",
        "paleness": "Flu",
    }


def ask(q):
    while True:
        a = input(f"{q} [Yes/No]\t").strip().lower()
        if a in ["yes", "no"]:
            return a == "yes"
        print("Please answer in Yes or No.\n")


def questions_list():
    return {
        "sneezes": "Are you sneezing frequently?",
        "temperature": "Do you have a high temperature?",
        "weakness": "Are you feeling weak in your legs and arms?",
        "forgets": "Do you forget things often?",
        "cough": "Do you have a cough or sore throat?",
        "paleness": "Does your skin look pale?",
    }


def doctor():
    print("*" * 30, "\nWelcome to Doctor Smith's!", "*" * 30)
    know = knowledge()
    questions = questions_list()

    symptoms = {}
    for s, q in questions.items():
        symptoms[s] = ask(q)

    # Inference engine: collect every disease whose symptom is present.
    diagnosis = []
    for sym in know:
        if symptoms[sym]:
            diagnosis.append(know[sym])

    print("\n\nYour Diagnosis is:\n")
    if diagnosis:
        for d in diagnosis:
            print("-", d)
    else:
        print("- No matching disease found. Please consult a doctor.")


if __name__ == "__main__":
    doctor()
