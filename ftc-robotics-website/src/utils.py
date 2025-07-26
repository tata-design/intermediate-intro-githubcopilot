def format_text(text):
    return text.strip().capitalize()

def calculate_average(scores):
    if not scores:
        return 0
    return sum(scores) / len(scores)

def validate_email(email):
    import re
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def log_event(event):
    import logging
    logging.basicConfig(filename='app.log', level=logging.INFO)
    logging.info(event)