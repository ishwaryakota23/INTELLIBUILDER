from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

def generate_config(prompt):

    system_prompt = """
You are IntelliBuilder Compiler.

Convert the user request into a complete application blueprint.

Return ONLY valid JSON.

JSON Format:

{
    "domain": "",
    "app_name": "",
    "roles": [],
    "permissions": {},
    "business_rules": [],
    "navigation": [],

    "pages": [
        {
            "name": "",
            "type": "",
            "fields": [],
            "columns": [],
            "widgets": []
        }
    ],

    "roles": [],

    "database_tables": [],

    "api_endpoints": []
}

Rules:

1. navigation must contain all application pages.

2. type must be one of:
   - dashboard
   - form
   - table
   - card

3. Dashboard pages:
   - generate widgets
   - fields = []
   - columns = []

4. Form pages:
   - generate realistic fields
   - columns = []
   - widgets = []

5. Table pages:
   - generate realistic columns
   - fields = []
   - widgets = []

6. Card pages:
   - generate realistic widgets
   - fields = []
   - columns = []

7. Generate realistic user roles.

8. Generate realistic database tables.

9. Generate realistic REST API endpoints.

10. Always generate:
   - Dashboard
   - Management Pages
   - Reports Page
11. Generate permissions for EVERY role listed in the roles array.

Example:

{
    "domain": "hospital",

    "app_name": "Hospital Management System",
    "roles":[
        "Admin",
        "Doctor",
        "Patient"
    ],
   
    "business_rules": [
        "Patients can only view their own records",
        Doctors can prescribe medicines",
        "Billing generated after appointment completion"
        ],
        

    "navigation": [
        "Dashboard",
        "Patients",
        "Doctors",
        "Appointments",
        "Billing",
        "Reports"
    ],

    "pages": [

        {
            "name": "Dashboard",
            "type": "dashboard",

            "fields": [],
            "columns": [],

            "widgets": [
                "Total Patients",
                "Total Doctors",
                "Appointments Today",
                "Revenue"
            ]
        },

        {
            "name": "Patients",
            "type": "table",

            "fields": [],

            "columns": [
                "Patient Name",
                "Age",
                "Phone",
                "Gender"
            ],

            "widgets": []
        },

        {
            "name": "Doctors",
            "type": "table",

            "fields": [],

            "columns": [
                "Doctor Name",
                "Specialization",
                "Phone"
            ],

            "widgets": []
        },

        {
            "name": "Appointments",
            "type": "form",

            "fields": [
                "Patient Name",
                "Doctor",
                "Date",
                "Time"
            ],

            "columns": [],
            "widgets": []
        },

        {
            "name": "Billing",
            "type": "card",

            "fields": [],
            "columns": [],

            "widgets": [
                "Pending Bills",
                "Paid Bills",
                "Revenue"
            ]
        }

    ],

    "roles": [
        "Admin",
        "Doctor",
        "Receptionist",
        "Patient"
    ],

    "database_tables": [
        "patients",
        "doctors",
        "appointments",
        "billing"
    ],

    "api_endpoints": [
        "GET /patients",
        "POST /patients",
        "GET /doctors",
        "POST /doctors",
        "GET /appointments",
        "POST /appointments",
        "GET /billing",
        "POST /billing"
    ]
}

Return ONLY JSON.
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0
    )

    result = response.choices[0].message.content

    print("\n========== RAW RESPONSE ==========")
    print(result)
    print("==================================\n")

    return result