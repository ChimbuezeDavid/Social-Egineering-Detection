# predict.py
from pipeline import predict_email

def main():
    print("="*50)
    print("Social Engineering Detection System")
    print("="*50)
    
    email = input("\nPaste the email content to analyze:\n> ")
    
    if not email.strip():
        print("Error: Email content cannot be empty.")
        return
        
    print("\nAnalyzing...\n")
    result = predict_email(email)
    
    print(f"Verdict:     {result['verdict']}")
    print(f"Probability: {result['probability']}")
    print(f"Confidence:  {result['confidence']}")
    
    if result['zero_day_warning']:
        print("⚠️ Warning:  Zero-Day Scam Pattern Detected!")
        
    print(f"Reasons:     {result['explanation']}")
    print("="*50)

if __name__ == "__main__":
    main()
