from flask import Flask, render_template, make_response
from weasyprint import HTML
from patient import Patient

app = Flask(__name__)

@app.route('/generate-pdf', methods=['POST'])
def generate_pdf():
    # Example of retrieving and processing form data into a Patient instance
    # this data will be extracted from request.form/request.json
    patient_data = Patient(
        veteran_status="Yes",
        availability_for_phone_call="2024-04-01 14:00",
        cannabis_consumption_per_day="3 grams",
        name_on_id="John Doe",        
        reason_for_visit="Consultation"
        # Add the rest of your patient fields here
    )

    # convert the patient dataclass instance to a dictionary
    data = patient_data.__dict__

    # add additional data like url to company logo
    data['logo_url'] = 'images/eco-logo.png'

    # render HTML template with the data
    html_content = render_template('template.html', **data)

    # convert the rendered HTML to a PDF document
    pdf = HTML(string=html_content).write_pdf()

    # create a response that serves the generated PDF
    response = make_response(pdf)
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = 'attachment; filename=patient_form.pdf'

    return response

if __name__ == '__main__':
    app.run(debug=True)

