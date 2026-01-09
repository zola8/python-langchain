from langchain.agents.middleware import PIIMiddleware
from langchain_core.tools import tool

from a21_middleware_base import llm, create_my_agent, main_loop

patient_records = [
    {
        "name": "Alice Johnson",
        "email": "alice.johnson@example.com",
        "address": "123 Maple Street, Springfield, IL 62704",
        "phone": "+1-555-123-4567",
        "credit_card": "1111 1234 1234 1234",
        "url": "http://aaa.111.com",
        "ip": "11.22.33.44",
    },
    {
        "name": "Michael Chen",
        "email": "michael.chen@example.com",
        "address": "456 Oak Avenue, Portland, OR 97201",
        "phone": "+1-555-987-6543",
        "credit_card": "2222 1234 1234 1234",
        "url": "http://bbb.222.com",
        "ip": "22.22.33.44",
    },
    {
        "name": "Sofia Rodriguez",
        "email": "sofia.rodriguez@example.com",
        "address": "789 Pine Road, Austin, TX 78701",
        "phone": "+1-555-456-7890",
        "credit_card": "3333 1234 1234 1234",
        "url": "http://ccc.333.com",
        "ip": "33.22.33.44",
    },
]


@tool
def get_patient_info(name: str):
    """
    Retrieve patient information by name from patient records.

    Args:
        name (str): Full name of the patient to search for

    Returns:
        dict or None: Patient record if found, None if not found
    """
    name_lower = name.lower()
    for record in patient_records:
        if name_lower in record["name"].lower():
            return record
    return None


agent = create_my_agent(my_llm=llm, my_tools=[get_patient_info], my_middleware=
[
    PIIMiddleware("email", strategy="redact"),
    PIIMiddleware("credit_card", strategy="mask"),
    PIIMiddleware("url", strategy="redact"),
    PIIMiddleware("ip", strategy="hash"),
    PIIMiddleware("api_key", detector=r"sk-[a-zA-Z0-9]{6}", strategy="block"),
])

if __name__ == "__main__":
    # result = agent.invoke({"messages": "I have a key: sk-abc123"})
    # print(result)
    # PIIDetectionError: Detected 1 instance(s) of api_key in text content

    main_loop(agent)
    # what is Alice Johnson's email?
