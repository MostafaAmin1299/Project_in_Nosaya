import json
import os

class JsonData:
    def __init__(self, filename, analysis, success, failed):
        self.filename = os.path.splitext(os.path.basename(filename))[0]
        self.analysis = analysis
        self.success = success
        self.failed = failed

    def export(self):
        with open(f"MyData/analysis_to_{self.filename}.json", "w", encoding="utf-8") as f:
            json.dump(self.analysis, f, ensure_ascii=False, indent=4)

        with open(f"MyData/successful_students_to_{self.filename}.json", "w", encoding="utf-8") as f:
            json.dump(self.success, f, ensure_ascii=False, indent=4)

        with open(f"MyData/failed_students_to_{self.filename}.json", "w", encoding="utf-8") as f:
            json.dump(self.failed, f, ensure_ascii=False, indent=4)

        print("The JSON files have been created successfully.")
