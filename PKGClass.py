import requests
from datetime import datetime
from rfc3987 import match

API_URL = "https://rel.cs.ru.nl/api"

class PKGFunctions:
    """sumary_line
    Class for the Spotify and Netflix functions
    """
    

    def __init__(self):
        """sumary_line
        init for PKGFunctions
        """
        
        self.temp_song = []
        pass
    
        
    def get_REL_api_response(self, example_string):
        """sumary_line
        
        Keyword arguments:
        example_string -- input text
        Return: response.json() -- dictionary with REL API response
        """
        
        response = requests.get(API_URL)
        
        if response.status_code == 200:
            response = requests.post(
                API_URL, json={"text": example_string, "spans": []}
            )
            return response.json()
        else:
            return {"error": response.status_code}
        
          
       
    
    def process_entity_linking_response(self, NER_response, input_text):
        """sumary_line
        
        Keyword arguments:
        NER_response -- dictionary with NER response
        input_text -- input text
        Return: 
        output_text -- input text with found entities marked
        """
        
        
        entity_dict = {}
        for entity in NER_response:
            start_index, end_index = entity[:2]
            entity_dict[(start_index, end_index)] = (entity[2], entity[3], entity[6])
        string_index = 0
        output_array = []
        count = 0
        
        for item in entity_dict.items():
            start = item[0][0]
            end = item[0][1] + start
            entity = input_text[start:end]
            output_array.append(input_text[string_index:start])
            
            if entity:
                text = f"<{item[1][2]}> {entity} </{item[1][2]}>"
                output_array.append(text)
                count += 1         
            string_index = end
            if count == len(entity_dict):
                output_array.append(input_text[string_index:]) 

        output_text = ''.join(output_array)
        return(output_text)
    
    def compute_precision_recall(self, ground_truth_data, test_data):
        """sumary_line
        
        Keyword arguments:
        groud_truth_data -- dataset with list of expected output
        test_data -- dataset with list of actual output
        Return: 
        precision -- precision TP / (TP + FP),
        recall -- recall TP / (TP + FN), 
        F_measure -- F1 score 2 * (precision * recall) / (precision + recall)
        """
        print(len(ground_truth_data), len(test_data))
        
        true_positives = 0
        false_positives = 0
        false_negatives = 0

        for test_item in test_data:
            match_found = False
            for ground_truth_item in ground_truth_data:
                if (test_item["object"] == ground_truth_item["object"]):
                    print("Match found\n")
                    true_positives += 1
                    match_found = True
                    break

            if not match_found:
                false_positives += 1

        false_negatives = len(ground_truth_data) - true_positives
        
        print(f"True positives: {true_positives}, False positives: {false_positives}, False negatives: {false_negatives}")

        precision = true_positives / (true_positives + false_positives) if (true_positives + false_positives) > 0 else 0
        recall = true_positives / (true_positives + false_negatives) if (true_positives + false_negatives) > 0 else 0
        F_measure = 2 * (precision * recall) / (precision + recall) if (precision + recall) > 0 else 0
        print(f"Precision: {precision}, Recall: {recall}, F-measure: {F_measure}")

        return precision, recall, F_measure


SPARQLQuery = str

class URI(str):
    def __new__(cls, *args, **kwargs):
        """Creates a new URI."""
        assert match(args[0], rule="IRI"), f"Invalid URI: {args[0]}"
        return super().__new__(cls, *args, **kwargs)
        