import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from src.core.domain_classifier import DomainClassifier

def test_classify_sample_project():
    # Your test logic here
    project_data = {
        "name": "Smart Hospital Management",
        "description": "A platform to automate patient records and scheduling in hospitals.",
        "tags": ["healthcare", "automation", "scheduling"],
        "type": "web app",
        "technologies": ["Python", "Django", "FHIR"],
        "stakeholders": ["patients", "doctors", "administrators"],
        "objectives": ["reduce wait times", "improve record accuracy"],
        "location": "United States",
        "regulatory_context": ["HIPAA"]
    }

    project_data2 = {
    "name": "Remote Health Access for Students",
    "description": "A digital platform enabling students in rural areas to consult with healthcare professionals via video calls, integrated with school attendance systems.",
    "tags": ["telemedicine", "education", "rural", "video conferencing"],
    "type": "Web Application",
    "technologies": ["React", "WebRTC", "AWS", "Node.js"],
    "stakeholders": ["school administrators", "students", "healthcare providers"],
    "objectives": ["improve student health", "reduce absenteeism", "increase healthcare access"],
    "location": "Multiple rural regions",
    "regulatory_context": "HIPAA, FERPA"
}
    project_data3 = {
    "name": "Retail Energy Optimization",
    "description": "An IoT-based system that monitors and optimizes energy usage across multiple retail store locations, using predictive analytics to reduce costs.",
    "tags": ["IoT", "energy efficiency", "retail", "analytics"],
    "type": "IoT Solution",
    "technologies": ["Python", "Raspberry Pi", "Azure IoT", "Power BI"],
    "stakeholders": ["store managers", "energy consultants", "IT department"],
    "objectives": ["reduce energy costs", "improve sustainability metrics"],
    "location": "National retail chain",
    "regulatory_context": "Local energy regulations"
}
    project_data4 = {
    "name": "Decentralized Credential Verification",
    "description": "A blockchain-based platform for verifying professional and academic credentials, targeting both universities and financial institutions.",
    "tags": ["blockchain", "credentials", "verification", "security"],
    "type": "Platform",
    "technologies": ["Ethereum", "Solidity", "React"],
    "stakeholders": ["universities", "banks", "job applicants"],
    "objectives": ["reduce fraud", "streamline verification processes"],
    "location": "Global",
    "regulatory_context": "GDPR, local data privacy laws"
}
    
    project_data5 = {
    "name": "Predictive Supply Chain Insights",
    "description": "A machine learning solution that predicts supply chain disruptions and recommends mitigation strategies for manufacturers and logistics providers.",
    "tags": ["AI", "supply chain", "logistics", "manufacturing"],
    "type": "Analytics Platform",
    "technologies": ["Python", "TensorFlow", "AWS SageMaker"],
    "stakeholders": ["supply chain managers", "logistics companies", "manufacturers"],
    "objectives": ["reduce delays", "optimize inventory"],
    "location": "International",
    "regulatory_context": "Import/export regulations"
}
    
    project_data6 = {
    "name": "Seamless Guest Experience",
    "description": "A mobile app for hotel guests that integrates room controls, concierge services, and instant payment options, including digital wallets and loyalty points.",
    "tags": ["hospitality", "mobile app", "payments", "guest services"],
    "type": "Mobile Application",
    "technologies": ["Flutter", "Stripe API", "IoT"],
    "stakeholders": ["hotel guests", "hotel staff", "payment providers"],
    "objectives": ["improve guest satisfaction", "streamline payments"],
    "location": "Urban hotels",
    "regulatory_context": "PCI DSS, local hospitality regulations"
}
    classifier = DomainClassifier()
    result = classifier.classify(project_data4)
    print(result)

if __name__ == "__main__":
    test_classify_sample_project()