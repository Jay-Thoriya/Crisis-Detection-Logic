"""
pseudo code : - 


// List of urgent keywords
urgent_keywords = ["emergency", "crisis", "urgent", "danger", "self-harm", "suicidal"]

// Function to analyze messages for urgent keywords
function analyzeMessage(message):
    score = 0
    
    // Check for urgent keywords in the message
    for keyword in urgent_keywords:
        if keyword in message:
            score += 10  // Increase score for each keyword found

    // Additional criteria to increase urgency
    if message.contains("I need help immediately"):
        score += 20
        
    if message.length > 200:  // Longer messages might indicate more distress
        score += 5
        
    return score


// Function to determine if staff should be alerted
function shouldAlertStaff(urgencyScore):
    if urgencyScore >= 15:
        return true  // Alert staff
    else:
        return false  // No alert


// Example function for appointment scheduling
function scheduleAppointment(patientInfo):
    if patientInfo is valid:
        // Code to schedule an appointment
        return "Appointment scheduled."
    else:
        return "Invalid patient information."


// Main execution
messages = getPatientMessages()
for message in messages:
    urgencyScore = analyzeMessage(message)
    if shouldAlertStaff(urgencyScore):
        alertHumanStaff(message)  // Notify human staff about the urgent message
    else:
        processNormalMessage(message)  // Routine handling


"""

# List of urgent keywords
urgent_keywords = ["emergency", "crisis", "urgent", "danger", "self-harm", "suicidal"]

# Function to analyze messages for urgent keywords
def analyze_message(message):
    score = 0

    # Check for urgent keywords in the message
    for keyword in urgent_keywords:
        if keyword in message:
            score += 10  # Increase score for each keyword found

    # Additional criteria to increase urgency
    if "I need help immediately" in message:
        score += 20

    if len(message) > 200:  # Longer messages might indicate more distress
        score += 5

    return score

# Function to determine if staff should be alerted
def should_alert_staff(urgency_score):
    return urgency_score >= 15  # Alert staff if the score is 15 or higher

# Example function for appointment scheduling
def schedule_appointment(patient_info):
    if patient_info:  # Assuming patient_info validity is determined here
        # Code to schedule an appointment
        return "Appointment scheduled."
    else:
        return "Invalid patient information."

# Main execution
def main():
    messages = get_patient_messages()  # Function to fetch patient messages
    for message in messages:
        urgency_score = analyze_message(message)
        if should_alert_staff(urgency_score):
            alert_human_staff(message)  # Notify human staff about the urgent message
        else:
            process_normal_message(message)  # Routine handling

# Example placeholder functions
def get_patient_messages():
    # Replace with actual logic to fetch patient messages
    return ["This is a test message.", "I need help immediately. It's an emergency."]

def alert_human_staff(message):
    print(f"Alerting staff: {message}")

def process_normal_message(message):
    print(f"Processing message normally: {message}")

# Run the main execution
if __name__ == "__main__":
    main()
