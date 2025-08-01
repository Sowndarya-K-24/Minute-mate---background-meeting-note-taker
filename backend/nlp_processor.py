import spacy, re

nlp = spacy.load("en_core_web_sm")

def process_transcript(text):
    summary = summarize(text)
    actions = extract_actions(text)
    reminders = extract_dates(text)
    return summary, actions, reminders

def summarize(text):
    doc = nlp(text)
    sents = list(doc.sents)
    return ' '.join([str(s) for s in sents[:8]])  # ~200 words

def extract_actions(text):
    return re.findall(r"\b(?:will|need to|should)\b.*?[\.]", text, flags=re.IGNORECASE)

def extract_dates(text):
    doc = nlp(text)
    return [ent.text for ent in doc.ents if ent.label_ == "DATE"]