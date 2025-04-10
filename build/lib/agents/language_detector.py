################################################################################
# File: aicpa/agents/language_detector.py
################################################################################

LANGUAGES = ["python", "cpp", "torchscript"]

class LanguageDetector:
    """Detects the programming language of a given source or file."""
    def __init__(self):
        pass

    def detect(self, file_path: str)-> str:
       """Return a guessed language from the file path extension"""
       # This is a very naive placeholder detection.
       if file_path.endwith(".py"):
           return "python"
       
       elif file_path.endwith(".cpp"):
           return "cpp"

       elif file_path.endwith(".pt"):
           return "torchscript"

       else:
           return "unknown"


