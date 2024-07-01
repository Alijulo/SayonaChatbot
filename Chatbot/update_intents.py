import json

# Read the existing JSON file
filename = 'intents.json'
with open(filename, 'r') as file:
    data = json.load(file)

print(data)

# Add a new question and response
new_question = ["What factors affect loan approval?","What is the interest rate on personal loans"]
new_response = ["Loan approval depends on factors such as credit score, income stability, debt-to-income ratio, and collateral (if applicable). A good credit history increases your chances of approval.",
"Interest rates vary based on the loan type, amount, and your creditworthiness. Check our website or contact our customer service for current rates."]
new_tag = "custom_questions"  # Specify the appropriate tag

# Find the intent with the specified tag
dict={
    "tag":new_tag,
    "patterns":new_question,
    "responses":new_response
}

data['intents'].append(dict)

# Write the updated data back to the file
with open(filename, 'w') as file:
    json.dump(data, file, indent=2)

print(f"Added: {new_question} -> {new_response} (Tag: {new_tag})")
