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

    classifier = DomainClassifier()
    result = classifier.classify(project_data)
    print(result)

if __name__ == "__main__":
    test_classify_sample_project()