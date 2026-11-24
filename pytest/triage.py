def categorise(text):
    text = text.lower()
    if "charged" in text or "refund" in text or "money back" in text:
        return "billing"
    if "parcel" in text or "arrived" in text:
        return "shipping"
    return "other"