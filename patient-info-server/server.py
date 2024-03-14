from flask import Flask, request, jsonify
from dataclasses import dataclass

app = Flask(__name__)

@dataclass
class Patient:
    veteran_status: str
    availability_for_phone_call: str
    cannabis_consumption_per_day: str
    name_on_id: str
    date_of_birth: str
    provincial_health_card_number: str
    issuing_province: str
    gender: str
    email_address: str
    address: str
    phone_number: str
    medical_documents: str
    referral_code: str
    medical_conditions: str
    current_therapy: str
    weight: str
    height: str
    current_doctor: str
    current_medications: str
    known_allergies: str
    schizophrenia_diagnosis: str
    duration_of_cannabis_use: str
    preferred_methods_of_cannabis_consumption: str
    legal_release_acknowledgement: str
    eco_service_agreement: str
    healthcare_practitioner_info: str
    shipping_preferences: str
    how_you_heard_about_service: str
    patient_details: str
    sex_on_health_card: str
    treatment_goals: str
    responsible_adult_info: str
    mailing_address: str
    canadian_veteran_status: str
    indigenous_identity: str
    referral_source: str
    primary_care_provider_info: str
    specialists_info: str
    reason_for_visit: str

@app.route('/submit_form', methods=['POST'])
def handle_form():
    if request.is_json:
        data = request.json
        patient = Patient(**data)
        # Process the patient data or store it as needed
        return jsonify({"message": "Patient data received", "patient": data}), 200
    else:
        return jsonify({"error": "Request must be JSON"}), 400

if __name__ == '__main__':
    app.run(debug=True)
