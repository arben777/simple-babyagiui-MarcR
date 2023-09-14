# config.py
# This is a dictionary where keys are investor names and values are lists of example prompts for that investor.
investor_specific_prompts = {
    "Marc Randolph": {
        "objectives": ["Launch a rare books subscription aiming for 10,000 subscribers in year one.", "Start an indie film streaming service, targeting 20 filmmaker collaborations in 6 months.", " Develop a podcast platform with exclusive content across genres."],
        "tasks": ["Negotiate with book dealers for a 50-box pilot with at least one first edition.", "Connect with 10 indie filmmakers for potential partnerships.", "Study top 5 podcast genres and list potential podcasters for the platform."]
    },
    "InvestorB": {
        "objectives": ["Objective 1 for InvestorB", "Objective 2 for InvestorB", "Objective 3 for InvestorB"],
        "tasks": ["Task 1 for InvestorB", "Task 2 for InvestorB", "Task 3 for InvestorB"]
    },
    # Add more investors and their specific tasks as needed
}
# Default investor - change this before sending to a specific investor.
DEFAULT_INVESTOR = "Marc Randolph"