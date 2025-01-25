def check_voting_eligibility(age, nationality):
    """
    Check if a person is eligible to vote.
    The person must be:
    1. A citizen of Uganda, Tanzania, or Kenya.
    2. Above 18 years of age.
    """
    eligible_countries = ["Uganda", "Tanzania", "Kenya"]
    if age >= 18 and nationality in eligible_countries:
        return "You are eligible to vote."
    else:
        return "You are not eligible to vote."

try:
    age = int(input("Enter your age: "))
    nationality = input("Enter your nationality: ").strip().capitalize()
    result = check_voting_eligibility(age, nationality)
    print(result)

except ValueError:
    print("Invalid input! Please enter a valid number for age.")
