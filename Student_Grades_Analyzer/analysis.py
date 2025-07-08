class StudentAnalyzer:
    def __init__(self, data):
        self.data = data
        self.analysis_json = {}
        self.successful_json = {}
        self.failed_json = {}


    def analyze(self):
        if self.data is not None:
            
            self.analysis_json = {
				"AVG": float(self.data["Student Grade"].mean()),
				"MAX": int(self.data["Student Grade"].max()),
				"MIN": int(self.data["Student Grade"].min())
			}


            successful_students = self.data[self.data["Student Grade"] > 60]
            self.successful_json = dict(
                zip(successful_students["Student Name"], successful_students["Student Grade"])
            )

            failed_students = self.data[self.data["Student Grade"] < 60]
            self.failed_json = dict(
                zip(failed_students["Student Name"], failed_students["Student Grade"])
            )
        else:
            print("No Data")


    def run(self):
        self.analyze()
        
        print("Analyze the data Done")
        
        return self.analysis_json, self.successful_json, self.failed_json

