Prompt & Pattern Documentation:

This file records the exact prompts, regex patterns, and chunking logic used in the MinuteMate project for transcription summarization, action item extraction, and reminder/date detection.

1. Transcript Chunking Logic:
Purpose: Split long transcriptions into manageable chunks for summarization.

Chunk Size Limit: 1000 tokens (approx. 750 words)

Chunking Method:
chunks = textwrap.wrap(transcript_text, width=750)

2. Summarization Prompt:
Used in: summarizer.py
Model Used: Offline (manual logic, spaCy & heuristics)

If integrated with a model like OpenAI/HuggingFace, this would be the prompt:

You are a meeting assistant. Summarize the following transcript into a 200-word summary capturing the main discussion points. Preserve clarity, avoid repetition, and use bullet points where helpful.

Transcript:
"""
{{ transcript_chunk }}
"""

Fallback (manual): Extract key sentences with spaCy sentence segmentation and TF-IDF scoring.

3. Action Item Extraction:
 Method: Regex-based pattern matching on entire transcript or summary.

Patterns Used:
ACTION_PATTERNS = [
  r'\b(we|I|you|they)\b.*?\b(will|should|must|need to|plan to|are going to)\b.*?[.!?]',
  r'\b(to be done|task is to|next steps include|follow up on)\b.*?[.!?]',
  r'\b(assign(ed)? to|responsible for)\b.*?[.!?]',
]

Sample Matched Sentences:

"John will send the invoice by Friday."

"We need to finalize the proposal next week."

4. Reminder & Date Extraction:

Regex Patterns Used:
DATE_PATTERNS = [
  r'\b(on )?\d{1,2}(st|nd|rd|th)? [A-Za-z]{3,9}\b',           # 21st July
  r'\b[A-Za-z]{3,9} \d{1,2}(st|nd|rd|th)?\b',                 # July 21
  r'\b(next|this|following) (Monday|Tuesday|Wednesday|...)\b', # next Friday
  r'\b\d{1,2}/\d{1,2}/\d{2,4}\b',                             # 21/07/2025
  r'\b\d{4}-\d{2}-\d{2}\b',                                   # 2025-07-21
]
Date Parsing: dateutil.parser.parse() is used to convert recognized strings into standard datetime formats.

5. Summary Output Structure:

Each meeting summary includes:

summary: A ~200-word bullet or paragraph-style overview

action_items: List of identified actionable tasks

reminders: List of deadlines or events with date/time if parsed

Example JSON:

{
  "summary": "The team discussed...",
  "action_items": [
    "Alice will draft the proposal by Thursday",
    "Bob to set up the follow-up meeting"
  ],
  "reminders": [
    "Proposal submission – 21 July 2025",
    "Team sync – next Monday"
  ]
}

Notes:

1) All prompts and patterns are implemented without LLM APIs.
2) Designed to run completely offline using open-source NLP tools.