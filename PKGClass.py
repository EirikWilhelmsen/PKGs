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
    
    def compute_precision_recall(self, ground_truth_data, test_data, test_type):
        """sumary_line
        
        Keyword arguments:
        groud_truth_data -- dataset with list of expected output
        test_data -- dataset with list of actual output
        Return: 
        precision -- precision TP / (TP + FP),
        recall -- recall TP / (TP + FN), 
        F_measure -- F1 score 2 * (precision * recall) / (precision + recall)
        """
        
        true_positives = 0
        false_positives = 0
        false_negatives = 0

        print(f"Test type: {test_type}")

        if test_type == "Related_entities":
            for test_item in test_data:
                match_found = False
                for ground_truth_item in ground_truth_data:
                    if (test_item["object"]["value"]["related_entities"] == ground_truth_item["object"]["value"]["related_entities"]):
                        true_positives += 1
                        match_found = True
                        break
                if not match_found:
                    print("FP: ", test_item["object"]["value"]["related_entities"])
                    false_positives += 1

            false_negatives = len(ground_truth_data) - true_positives
        
        elif test_type == "Description":
            for test_item in test_data:
                match_found = False
                for ground_truth_item in ground_truth_data:
                    if (test_item["object"]["value"]["description"] == ground_truth_item["object"]["value"]["description"]):
                        # test_item["predicate"] = ground_truth_item["predicate"] and 
                        true_positives += 1
                        match_found = True
                        break
                if not match_found:
                    print("FP: ", test_item["object"]["value"]["description"])
                    false_positives += 1
            false_negatives = len(ground_truth_data) - true_positives
        
        elif test_type == "song_URI":
            for test_item in test_data:
                match_found = False
                for ground_truth_item in ground_truth_data:
                    if (test_item["object"]["value"]["related_entities"][-1] == ground_truth_item["object"]["value"]["related_entities"][-1]):
                        true_positives += 1
                        match_found = True
                        break
                if not match_found:
                    print("FP: ", test_item["object"]["value"]["related_entities"][-1])
                    false_positives += 1
            false_negatives = len(ground_truth_data) - true_positives
        
        
        precision = true_positives / (true_positives + false_positives) if (true_positives + false_positives) > 0 else 0
        recall = true_positives / (true_positives + false_negatives) if (true_positives + false_negatives) > 0 else 0
        F_measure = 2 * (precision * recall) / (precision + recall) if (precision + recall) > 0 else 0

        print("-------------------------------------------")
        print(f"Precision and recall for : {test_type}")
        print("Precision:", precision)
        print("Recall:", recall)
        print("F-measure:", F_measure)
        print("-------------------------------------------")


SPARQLQuery = str

class URI(str):
    def __new__(cls, *args, **kwargs):
        """Creates a new URI."""
        assert match(args[0], rule="IRI"), f"Invalid URI: {args[0]}"
        return super().__new__(cls, *args, **kwargs)
        