from collect_data import CollectData
from analysis import StudentAnalyzer
from store_data import JsonData


if __name__ == "__main__":
    
    data, file_name = CollectData().run()
    
    if data is not None:
		
        analysis_json, successful_json, failed_jso = StudentAnalyzer(data).run()
		
        JsonData(file_name, analysis_json, successful_json, failed_jso).export()
        
    else:
        print ("No Data")

