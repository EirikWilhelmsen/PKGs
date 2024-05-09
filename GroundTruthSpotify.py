

class groundTruthSpotify():
    def __init__(self):
        pass
    def create_statement(self):
        test_data_list = []

        #######################################################################################################################
        subject = "http://example.com/test" 
        predicate = {"value": {"description": "like"}} 
        object = {"value": {"description": "the song Hotel California by Eagles", 
                             "related_entities": ["https://schema.org/artist", "https://musicbrainz.org/artist/f46bd570-5768-462e-b84c-c7c993bbf47e", 
                                                  "https://schema.org/song", "https://musicbrainz.org/recording/c0e9452e-ee38-45a4-857e-ed9cd5e98c7f"]}}
        
        test_data = {
            "subject": subject,
            "predicate": predicate,
            "object": object 
        }
        test_data_list.append(test_data)

        #######################################################################################################################

        subject = "http://example.com/test" 
        predicate = {"value": {"description": "like"}} 
        object = {"value": {"description": "the song Paint It, Black by The Rolling Stones", # Paint It Black
                             "related_entities": ["https://schema.org/artist", "No:URI:found", 
                                                  "https://schema.org/song", "No:URI:found"]}}
        "son'g" "song`g"
        test_data = {
            "subject": subject,
            "predicate": predicate,
            "object": object 
        }
        test_data_list.append(test_data)

        #######################################################################################################################
        
        subject = "http://example.com/test" 
        predicate = {"value": {"description": "like"}} 
        object = {"value": {"description": "the song Fortunate Son by Creedence Clearwater Revival", 
                             "related_entities": ["https://schema.org/artist", "https://musicbrainz.org/artist/109958eb-a335-4c5e-907e-597ff4c6af46", 
                                                  "https://schema.org/song", "https://musicbrainz.org/recording/9e74fbaf-8d5b-40fc-a2c2-955712df69c0"]}}
        
        test_data = {
            "subject": subject,
            "predicate": predicate,
            "object": object 
        }
        test_data_list.append(test_data)

        #######################################################################################################################
        
        subject = "http://example.com/test" 
        predicate = {"value": {"description": "like"}} 
        object = {"value": {"description": "the song Sweet Child O' Mine by Guns N' Roses", # Sweet Child o' Mine
                             "related_entities": ["https://schema.org/artist", "No:URI:found", 
                                                  "https://schema.org/song", "No:URI:found"]}}
        
        test_data = {
            "subject": subject,
            "predicate": predicate,
            "object": object 
        }
        test_data_list.append(test_data)

        #######################################################################################################################
        
        subject = "http://example.com/test" 
        predicate = {"value": {"description": "like"}} 
        object = {"value": {"description": "the song Enter Sandman by Metallica", 
                             "related_entities": ["https://schema.org/artist", "https://musicbrainz.org/artist/65f4f0c5-ef9e-490c-aee3-909e7ae6b2ab", 
                                                  "https://schema.org/song", "https://musicbrainz.org/recording/1eae4668-76ef-424b-9142-ad0fe3392665"]}}
        
        test_data = {
            "subject": subject,
            "predicate": predicate,
            "object": object 
        }
        test_data_list.append(test_data)

        #######################################################################################################################
        
        subject = "http://example.com/test" 
        predicate = {"value": {"description": "like"}} 
        object = {"value": {"description": "the song Seven Nation Army by The White Stripes", 
                             "related_entities": ["https://schema.org/artist", "https://musicbrainz.org/artist/11ae9fbb-f3d7-4a47-936f-4c0a04d3b3b5", 
                                                  "https://schema.org/song", "https://musicbrainz.org/recording/aae0d97b-572e-4598-9b14-977895222794"]}}
        
        test_data = {
            "subject": subject,
            "predicate": predicate,
            "object": object 
        }
        test_data_list.append(test_data)

        #######################################################################################################################
        
        subject = "http://example.com/test" 
        predicate = {"value": {"description": "like"}} 
        object = {"value": {"description": "the song Smells Like Teen Spirit by Nirvana", 
                             "related_entities": ["https://schema.org/artist", "https://musicbrainz.org/artist/5b11f4ce-a62d-471e-81fc-a69a8278c7da", 
                                                  "https://schema.org/song", "https://musicbrainz.org/recording/175088ac-522e-4e91-a84b-8b6ec778e49d"]}}
        
        test_data = {
            "subject": subject,
            "predicate": predicate,
            "object": object 
        }
        test_data_list.append(test_data)

        #######################################################################################################################
        
        subject = "http://example.com/test" 
        predicate = {"value": {"description": "like"}} 
        object = {"value": {"description": "the song Thunderstruck by AC/DC", 
                             "related_entities": ["https://schema.org/artist", "https://musicbrainz.org/artist/66c662b6-6e2f-4930-8610-912e24c63ed1", 
                                                  "https://schema.org/song", "https://musicbrainz.org/recording/5194be29-5fba-4633-820d-7e0994dcd5f7"]}}
        
        test_data = {
            "subject": subject,
            "predicate": predicate,
            "object": object 
        }
        test_data_list.append(test_data)

        #######################################################################################################################
        
        subject = "http://example.com/test" 
        predicate = {"value": {"description": "like"}} 
        object = {"value": {"description": "the song Dream On by Aerosmith", 
                             "related_entities": ["https://schema.org/artist", "https://musicbrainz.org/artist/3d2b98e5-556f-4451-a3ff-c50ea18d57cb", 
                                                  "https://schema.org/song", "https://musicbrainz.org/recording/28ccd1dd-4cbc-4911-9552-2d45e60f662a"]}}
        
        test_data = {
            "subject": subject,
            "predicate": predicate,
            "object": object 
        }
        test_data_list.append(test_data)

        #######################################################################################################################
        
        subject = "http://example.com/test" 
        predicate = {"value": {"description": "like"}} 
        object = {"value": {"description": "the song La Grange (2005 Remaster) by ZZ Top", 
                             "related_entities": ["https://schema.org/artist", "No:URI:found", 
                                                  "https://schema.org/song", "No:URI:found"]}}
        
        test_data = {
            "subject": subject,
            "predicate": predicate,
            "object": object 
        }
        test_data_list.append(test_data)

        #######################################################################################################################
        
        subject = "http://example.com/test" 
        predicate = {"value": {"description": "like"}} 
        object = {"value": {"description": "the song The Color Violet by Tory Lanez", 
                             "related_entities": ["https://schema.org/artist", "https://musicbrainz.org/artist/5b8ec72b-9e39-4a06-a2bf-964166b92a71", 
                                                  "https://schema.org/song", "https://musicbrainz.org/recording/52a0345e-497d-479e-99ca-f869f45dfefc"]}}
        
        test_data = {
            "subject": subject,
            "predicate": predicate,
            "object": object 
        }
        test_data_list.append(test_data)

        #######################################################################################################################
        
        subject = "http://example.com/test" 
        predicate = {"value": {"description": "like"}} 
        object = {"value": {"description": "the song Godspeed by Frank Ocean", 
                             "related_entities": ["https://schema.org/artist", "https://musicbrainz.org/artist/e520459c-dff4-491d-a6e4-c97be35e0044", 
                                                  "https://schema.org/song", "https://musicbrainz.org/recording/6f390fd7-6806-4d0c-aa34-7b748b7a099e"]}}
        
        test_data = {
            "subject": subject,
            "predicate": predicate,
            "object": object 
        }
        test_data_list.append(test_data)

        #######################################################################################################################
        
        subject = "http://example.com/test" 
        predicate = {"value": {"description": "like"}} 
        object = {"value": {"description": "the song Break from Toronto by PARTYNEXTDOOR", # Break From Toronto
                             "related_entities": ["https://schema.org/artist", "No:URI:found", 
                                                  "https://schema.org/song", "No:URI:found"]}}
        
        test_data = {
            "subject": subject,
            "predicate": predicate,
            "object": object 
        }
        test_data_list.append(test_data)

        #######################################################################################################################
        
        subject = "http://example.com/test" 
        predicate = {"value": {"description": "like"}} 
        object = {"value": {"description": "the song Don’t Matter To Me (with Michael Jackson) by Drake, and Michael Jackson", # Don't Matter to Me
                             "related_entities": ["https://schema.org/artist", "No:URI:found", 
                                                  "https://schema.org/artist", "No:URI:found", 
                                                  "https://schema.org/song", "No:URI:found"]}}
        
        test_data = {
            "subject": subject,
            "predicate": predicate,
            "object": object 
        }
        test_data_list.append(test_data)

        #######################################################################################################################
        
        subject = "http://example.com/test" 
        predicate = {"value": {"description": "like"}} 
        object = {"value": {"description": "the song Been Away by Brent Faiyaz", 
                             "related_entities": ["https://schema.org/artist", "https://musicbrainz.org/artist/201412c6-7ced-472b-87a9-9259ec3c07d3", 
                                                  "https://schema.org/song", "https://musicbrainz.org/recording/ca7cff93-3ed3-4e9f-b31f-d76eeecc607c"]}}
        
        test_data = {
            "subject": subject,
            "predicate": predicate,
            "object": object 
        }
        test_data_list.append(test_data)

        #######################################################################################################################
        
        subject = "http://example.com/test" 
        predicate = {"value": {"description": "like"}} 
        object = {"value": {"description": "the song L$D by A$AP Rocky", 
                             "related_entities": ["https://schema.org/artist", "https://musicbrainz.org/artist/25b7b584-d952-4662-a8b9-dd8cdfbfeb64", 
                                                  "https://schema.org/song", "https://musicbrainz.org/recording/5794b69c-fe62-4af4-ae20-188a0583c3dd"]}}
        
        test_data = {
            "subject": subject,
            "predicate": predicate,
            "object": object 
        }
        test_data_list.append(test_data)

        #######################################################################################################################
        
        subject = "http://example.com/test" 
        predicate = {"value": {"description": "like"}} 
        object = {"value": {"description": "the song Lady Of Namek by Tory Lanez",  # Lady of Namek
                             "related_entities": ["https://schema.org/artist", "No:URI:found", 
                                                  "https://schema.org/song", "No:URI:found"]}}
        
        test_data = {
            "subject": subject,
            "predicate": predicate,
            "object": object 
        }
        test_data_list.append(test_data)

        #######################################################################################################################
        
        subject = "http://example.com/test" 
        predicate = {"value": {"description": "like"}} 
        object = {"value": {"description": "the song White Ferrari by Frank Ocean", 
                             "related_entities": ["https://schema.org/artist", "https://musicbrainz.org/artist/e520459c-dff4-491d-a6e4-c97be35e0044", 
                                                  "https://schema.org/song", "https://musicbrainz.org/recording/a1f25623-f56c-4f36-bcce-67488d04e7cc"]}}
        
        test_data = {
            "subject": subject,
            "predicate": predicate,
            "object": object 
        }
        test_data_list.append(test_data)

        #######################################################################################################################
        
        subject = "http://example.com/test" 
        predicate = {"value": {"description": "like"}} 
        object = {"value": {"description": "the song Normal Girl by SZA", 
                             "related_entities": ["https://schema.org/artist", "https://musicbrainz.org/artist/272989c8-5535-492d-a25c-9f58803e027f", 
                                                  "https://schema.org/song", "https://musicbrainz.org/recording/157971d9-ce6c-40b2-99cc-598080965e89"]}}
        
        test_data = {
            "subject": subject,
            "predicate": predicate,
            "object": object 
        }
        test_data_list.append(test_data)

        #######################################################################################################################
        
        subject = "http://example.com/test" 
        predicate = {"value": {"description": "like"}} 
        object = {"value": {"description": "the song Go Flex by Post Malone", 
                             "related_entities": ["https://schema.org/artist", "https://musicbrainz.org/artist/b1e26560-60e5-4236-bbdb-9aa5a8d5ee19", 
                                                  "https://schema.org/song", "https://musicbrainz.org/recording/36a053ce-f660-467c-9e66-d86c17fda6c5"]}}
        
        test_data = {
            "subject": subject,
            "predicate": predicate,
            "object": object 
        }
        test_data_list.append(test_data)

        #######################################################################################################################
        
        subject = "http://example.com/test" 
        predicate = {"value": {"description": "like"}} 
        object = {"value": {"description": "the song I Forgot To Be Your Lover by William Bell", 
                             "related_entities": ["https://schema.org/artist", "https://musicbrainz.org/artist/d9c9cfb7-f751-4fb0-97c0-b3ddd768bc78", 
                                                  "https://schema.org/song", "https://musicbrainz.org/recording/765bad44-e333-4eb7-94e1-beffa0afc6cb"]}}
        
        test_data = {
            "subject": subject,
            "predicate": predicate,
            "object": object 
        }
        test_data_list.append(test_data)

        #######################################################################################################################
        
        subject = "http://example.com/test" 
        predicate = {"value": {"description": "like"}} 
        object = {"value": {"description": "the song Ain’t No Sunshine by Bill Withers", 
                             "related_entities": ["https://schema.org/artist", "https://musicbrainz.org/artist/fd1a2d9d-9bb6-44de-83a3-41560658aba9", 
                                                  "https://schema.org/song", "https://musicbrainz.org/recording/3442b706-8cef-4053-ab3e-dca0283c41dc"]}}
        
        test_data = {
            "subject": subject,
            "predicate": predicate,
            "object": object 
        }
        test_data_list.append(test_data)

        #######################################################################################################################
        
        subject = "http://example.com/test" 
        predicate = {"value": {"description": "like"}} 
        object = {"value": {"description": "the song It’s a Man’s Man’s World by James Brown", 
                             "related_entities": ["https://schema.org/artist", "https://musicbrainz.org/artist/20ff3303-4fe2-4a47-a1b6-291e26aa3438", 
                                                  "https://schema.org/song", "https://musicbrainz.org/recording/cb9e4e4a-f6d3-470b-9f40-f110945165c6"]}}
        
        test_data = {
            "subject": subject,
            "predicate": predicate,
            "object": object 
        }
        test_data_list.append(test_data)

        #######################################################################################################################
        
        subject = "http://example.com/test" 
        predicate = {"value": {"description": "like"}} 
        object = {"value": {"description": "the song Ain't No Mountain High Enough by Marvin Gaye, and Tammi Terrell", 
                             "related_entities": ["https://schema.org/artist", "https://musicbrainz.org/artist/afdb7919-059d-43c1-b668-ba1d265e7e42", 
                                                  "https://schema.org/artist", "https://musicbrainz.org/artist/ce4582b6-aee7-4da1-b841-3c619d4fb5a5", 
                                                  "https://schema.org/song", "https://musicbrainz.org/recording/cbc68a25-c694-4415-bc5a-08d0ae655435"]}}
        
        test_data = {
            "subject": subject,
            "predicate": predicate,
            "object": object 
        }
        test_data_list.append(test_data)

        #######################################################################################################################
        
        subject = "http://example.com/test" 
        predicate = {"value": {"description": "like"}} 
        object = {"value": {"description": "the song Somethin' Stupid by Frank Sinatra, and Nancy Sinatra", 
                             "related_entities": ["https://schema.org/artist", "https://musicbrainz.org/artist/197450cd-0124-4164-b723-3c22dd16494d", 
                                                  "https://schema.org/artist", "https://musicbrainz.org/artist/c2e36518-9c3b-4dcb-82ad-a3fc7fe99c67", 
                                                  "https://schema.org/song", "https://musicbrainz.org/recording/0a13d2e3-530a-499c-9a38-33905829d36c"]}}
        
        test_data = {
            "subject": subject,
            "predicate": predicate,
            "object": object 
        }
        test_data_list.append(test_data)

        #######################################################################################################################
        
        subject = "http://example.com/test" 
        predicate = {"value": {"description": "like"}} 
        object = {"value": {"description": "the song September by Earth, Wind & Fire", 
                             "related_entities": ["https://schema.org/artist", "https://musicbrainz.org/artist/535afeda-2538-435d-9dd1-5e10be586774", 
                                                  "https://schema.org/song", "https://musicbrainz.org/recording/06c82e6b-d0f9-44aa-82e7-1c710e3f0dd5"]}}
        
        test_data = {
            "subject": subject,
            "predicate": predicate,
            "object": object 
        }
        test_data_list.append(test_data)

        #######################################################################################################################
        
        subject = "http://example.com/test" 
        predicate = {"value": {"description": "like"}} 
        object = {"value": {"description": "the song Super Freak by Rick James", 
                             "related_entities": ["https://schema.org/artist", "https://musicbrainz.org/artist/cba9cec2-be8d-41bd-91b4-a1cd7de39b0c", 
                                                  "https://schema.org/song", "https://musicbrainz.org/recording/a192890a-3880-4edb-95b7-9c650eb53aad"]}}
        
        test_data = {
            "subject": subject,
            "predicate": predicate,
            "object": object 
        }
        test_data_list.append(test_data)

        #######################################################################################################################
        
        subject = "http://example.com/test" 
        predicate = {"value": {"description": "like"}} 
        object = {"value": {"description": "the song Lean on Me by Bill Withers", 
                             "related_entities": ["https://schema.org/artist", "https://musicbrainz.org/artist/fd1a2d9d-9bb6-44de-83a3-41560658aba9", 
                                                  "https://schema.org/song", "https://musicbrainz.org/recording/73501326-eec0-4728-9947-f6a1149a4639"]}}
        
        test_data = {
            "subject": subject,
            "predicate": predicate,
            "object": object 
        }
        test_data_list.append(test_data)

        #######################################################################################################################
        
        subject = "http://example.com/test" 
        predicate = {"value": {"description": "like"}} 
        object = {"value": {"description": "the song Baltimore by Nina Simone", 
                             "related_entities": ["https://schema.org/artist", "https://musicbrainz.org/artist/2944824d-4c26-476f-a981-be849081942f", 
                                                  "https://schema.org/song", "https://musicbrainz.org/recording/6d520ea8-30d0-4977-b339-d744d2822fdd"]}}
        
        test_data = {
            "subject": subject,
            "predicate": predicate,
            "object": object 
        }
        test_data_list.append(test_data)

        #######################################################################################################################
        
        subject = "http://example.com/test" 
        predicate = {"value": {"description": "like"}} 
        object = {"value": {"description": "the song Grandma’s Hands by Bill Withers", # Grandma’s Hands
                             "related_entities": ["https://schema.org/artist", "https://musicbrainz.org/artist/fd1a2d9d-9bb6-44de-83a3-41560658aba9", 
                                                  "https://schema.org/song", "https://musicbrainz.org/recording/1ed5d688-5468-4028-b8b2-cd1bab2dbbf0"]}}
        
        test_data = {
            "subject": subject,
            "predicate": predicate,
            "object": object 
        }
        test_data_list.append(test_data)

        #######################################################################################################################
        
        subject = "http://example.com/test" 
        predicate = {"value": {"description": "like"}} 
        object = {"value": {"description": "the song Shook Ones, Pt. II by Mobb Deep", 
                             "related_entities": ["https://schema.org/artist", "https://musicbrainz.org/artist/d75d1f08-bbb8-4eae-9877-399ca9121197", 
                                                  "https://schema.org/song", "https://musicbrainz.org/recording/7f63e3d5-7204-4483-a285-08a8de207c29"]}}
        
        test_data = {
            "subject": subject,
            "predicate": predicate,
            "object": object 
        }
        test_data_list.append(test_data)

        #######################################################################################################################
        
        subject = "http://example.com/test" 
        predicate = {"value": {"description": "like"}} 
        object = {"value": {"description": "the song You Know How We Do It by Ice Cube", 
                             "related_entities": ["https://schema.org/artist", "https://musicbrainz.org/artist/1d11e2a1-4531-4d61-a8c7-7b5c6a608fd2", 
                                                  "https://schema.org/song", "https://musicbrainz.org/recording/5c093e25-5b24-4018-a2d5-872c89ef9966"]}}
        
        test_data = {
            "subject": subject,
            "predicate": predicate,
            "object": object 
        }
        test_data_list.append(test_data)

        #######################################################################################################################
        
        subject = "http://example.com/test" 
        predicate = {"value": {"description": "like"}} 
        object = {"value": {"description": "the song Keep Ya Head Up by 2Pac", 
                             "related_entities": ["https://schema.org/artist", "https://musicbrainz.org/artist/382f1005-e9ab-4684-afd4-0bdae4ee37f2", 
                                                  "https://schema.org/song", "https://musicbrainz.org/recording/c83b35ed-9996-475f-b002-5b746a54cec8"]}}
        
        test_data = {
            "subject": subject,
            "predicate": predicate,
            "object": object 
        }
        test_data_list.append(test_data)

        #######################################################################################################################
        
        subject = "http://example.com/test" 
        predicate = {"value": {"description": "like"}} 
        object = {"value": {"description": "the song Big Poppa - 2005 Remaster by The Notorious B.I.G.", 
                             "related_entities": ["https://schema.org/artist", "No:URI:found", 
                                                  "https://schema.org/song", "No:URI:found"]}}
        
        test_data = {
            "subject": subject,
            "predicate": predicate,
            "object": object 
        }
        test_data_list.append(test_data)

        #######################################################################################################################
        
        subject = "http://example.com/test" 
        predicate = {"value": {"description": "like"}} 
        object = {"value": {"description": "the song Ready or Not by Fugees", 
                             "related_entities": ["https://schema.org/artist", "https://musicbrainz.org/artist/ea321799-9b1d-4e74-a074-a5facf597d82", 
                                                  "https://schema.org/song", "https://musicbrainz.org/recording/67747e92-5d28-4a94-b1f3-0ae0be48afc5"]}}
        
        test_data = {
            "subject": subject,
            "predicate": predicate,
            "object": object 
        }
        test_data_list.append(test_data)

        #######################################################################################################################
        
        subject = "http://example.com/test" 
        predicate = {"value": {"description": "like"}} 
        object = {"value": {"description": "the song N.Y. State of Mind by Nas", 
                             "related_entities": ["https://schema.org/artist", "https://musicbrainz.org/artist/cfbc0924-0035-4d6c-8197-f024653af823", 
                                                  "https://schema.org/song", "https://musicbrainz.org/recording/10379eff-98f9-4d43-9d5c-ae6f045069de"]}}
        
        test_data = {
            "subject": subject,
            "predicate": predicate,
            "object": object 
        }
        test_data_list.append(test_data)

        #######################################################################################################################
        
        subject = "http://example.com/test" 
        predicate = {"value": {"description": "like"}} 
        object = {"value": {"description": "the song Survival of the Fittest by Mobb Deep", 
                             "related_entities": ["https://schema.org/artist", "https://musicbrainz.org/artist/d75d1f08-bbb8-4eae-9877-399ca9121197", 
                                                  "https://schema.org/song", "https://musicbrainz.org/recording/c002e2ac-cfbb-4620-96b7-7d760c5a1e98"]}}
        
        test_data = {
            "subject": subject,
            "predicate": predicate,
            "object": object 
        }
        test_data_list.append(test_data)

        #######################################################################################################################
        
        subject = "http://example.com/test" 
        predicate = {"value": {"description": "like"}} 
        object = {"value": {"description": "the song Work by Gang Starr", 
                             "related_entities": ["https://schema.org/artist", "https://musicbrainz.org/artist/9ef8042a-2528-4f5c-b7c1-5e72b1efe170", 
                                                  "https://schema.org/song", "https://musicbrainz.org/recording/fa183711-699e-4ff8-8355-dc958d7f7954"]}}
        
        test_data = {
            "subject": subject,
            "predicate": predicate,
            "object": object 
        }
        test_data_list.append(test_data)

        #######################################################################################################################
        
        subject = "http://example.com/test" 
        predicate = {"value": {"description": "like"}} 
        object = {"value": {"description": "the song Miami by Will Smith", 
                             "related_entities": ["https://schema.org/artist", "https://musicbrainz.org/artist/5bae7081-64ef-4473-825a-38d310deb14c", 
                                                  "https://schema.org/song", "https://musicbrainz.org/recording/b0b32970-62b1-4a5a-b9d0-30ab998e23e0"]}}
        
        test_data = {
            "subject": subject,
            "predicate": predicate,
            "object": object 
        }
        test_data_list.append(test_data)

        #######################################################################################################################
        
        subject = "http://example.com/test" 
        predicate = {"value": {"description": "like"}} 
        object = {"value": {"description": "the song Hypnotize - 2014 Remaster by The Notorious B.I.G.", 
                             "related_entities": ["https://schema.org/artist", "No:URI:found", 
                                                  "https://schema.org/song", "No:URI:found"]}}
        
        test_data = {
            "subject": subject,
            "predicate": predicate,
            "object": object 
        }
        test_data_list.append(test_data)

        #######################################################################################################################
        
        subject = "http://example.com/test" 
        predicate = {"value": {"description": "like"}} 
        object = {"value": {"description": "the song Starboy by The Weeknd, and Daft Punk", 
                             "related_entities": ["https://schema.org/artist", "https://musicbrainz.org/artist/c8b03190-306c-4120-bb0b-6f2ebfc06ea9", 
                                                  "https://schema.org/artist", "https://musicbrainz.org/artist/056e4f3e-d505-4dad-8ec1-d04f521cbb56", 
                                                  "https://schema.org/song", "https://musicbrainz.org/recording/196f19ab-9c4d-49c7-ac59-9cc70de66845"]}}
        
        test_data = {
            "subject": subject,
            "predicate": predicate,
            "object": object 
        }
        test_data_list.append(test_data)

        #######################################################################################################################
        
        subject = "http://example.com/test" 
        predicate = {"value": {"description": "like"}} 
        object = {"value": {"description": "the song One Dance by Drake, Wizkid, and Kyla", 
                             "related_entities": ["https://schema.org/artist", "https://musicbrainz.org/artist/9fff2f8a-21e6-47de-a2b8-7f449929d43f", 
                                                  "https://schema.org/artist", "https://musicbrainz.org/artist/efc5d365-a448-4e2f-9b5f-4a7c84be725c", 
                                                  "https://schema.org/artist", "https://musicbrainz.org/artist/b1cfbd77-bda6-4de8-a344-eb2f26c4f1ef", 
                                                  "https://schema.org/song", "https://musicbrainz.org/recording/be9e4a6b-3f56-468a-aa61-b1bcb6fc277f"]}}
        
        test_data = {
            "subject": subject,
            "predicate": predicate,
            "object": object 
        }
        test_data_list.append(test_data)

        #######################################################################################################################
        
        subject = "http://example.com/test" 
        predicate = {"value": {"description": "like"}} 
        object = {"value": {"description": "the song Love Yourself by Justin Bieber", 
                             "related_entities": ["https://schema.org/artist", "https://musicbrainz.org/artist/e0140a67-e4d1-4f13-8a01-364355bee46e", 
                                                  "https://schema.org/song", "https://musicbrainz.org/recording/39b2b253-f4d7-446b-81b2-686da38ff2d1"]}}
        
        test_data = {
            "subject": subject,
            "predicate": predicate,
            "object": object 
        }
        test_data_list.append(test_data)

        #######################################################################################################################
        
        subject = "http://example.com/test" 
        predicate = {"value": {"description": "like"}} 
        object = {"value": {"description": "the song Closer by The Chainsmokers, and Halsey", 
                             "related_entities": ["https://schema.org/artist", "https://musicbrainz.org/artist/91a81925-92f9-4fc9-b897-93cf01226282", 
                                                  "https://schema.org/artist", "https://musicbrainz.org/artist/3377f3bb-60fc-4403-aea9-7e800612e060", 
                                                  "https://schema.org/song", "https://musicbrainz.org/recording/c7f73192-a729-43a2-9c60-845271e3d696"]}}
        
        test_data = {
            "subject": subject,
            "predicate": predicate,
            "object": object 
        }
        test_data_list.append(test_data)

        #######################################################################################################################
        
        subject = "http://example.com/test" 
        predicate = {"value": {"description": "like"}} 
        object = {"value": {"description": "the song Hello by Adele", 
                             "related_entities": ["https://schema.org/artist", "https://musicbrainz.org/artist/cc2c9c3c-b7bc-4b8b-84d8-4fbd8779e493", 
                                                  "https://schema.org/song", "https://musicbrainz.org/recording/bd3cd6b8-d0b6-4765-ab58-9b438b760da7"]}}
        
        test_data = {
            "subject": subject,
            "predicate": predicate,
            "object": object 
        }
        test_data_list.append(test_data)

        #######################################################################################################################
        
        subject = "http://example.com/test" 
        predicate = {"value": {"description": "like"}} 
        object = {"value": {"description": "the song Panda by Desiigner", 
                             "related_entities": ["https://schema.org/artist", "https://musicbrainz.org/artist/05b75ee5-98cd-430e-b1ec-ec0f61fdabda", 
                                                  "https://schema.org/song", "https://musicbrainz.org/recording/53bade07-42c0-454f-9a07-4e2cad8cb660"]}}
        
        test_data = {
            "subject": subject,
            "predicate": predicate,
            "object": object 
        }
        test_data_list.append(test_data)

        #######################################################################################################################
        
        subject = "http://example.com/test" 
        predicate = {"value": {"description": "like"}} 
        object = {"value": {"description": "the song Pink + White by Frank Ocean", 
                             "related_entities": ["https://schema.org/artist", "https://musicbrainz.org/artist/e520459c-dff4-491d-a6e4-c97be35e0044", 
                                                  "https://schema.org/song", "https://musicbrainz.org/recording/d90934be-302a-4e0d-a1dd-b94df3421f33"]}}
        
        test_data = {
            "subject": subject,
            "predicate": predicate,
            "object": object 
        }
        test_data_list.append(test_data)

        #######################################################################################################################
        
        subject = "http://example.com/test" 
        predicate = {"value": {"description": "like"}} 
        object = {"value": {"description": "the song Cheap Thrills by Sia, and Sean Paul", # Cheap Thrills
                             "related_entities": ["https://schema.org/artist", "https://musicbrainz.org/artist/2f548675-008d-4332-876c-108b0c7ab9c5", 
                                                  "https://schema.org/artist", "https://musicbrainz.org/artist/c3da3346-2643-48a7-93cd-011f6834b3d7", 
                                                  "https://schema.org/song", "https://musicbrainz.org/recording/8fcdf7b9-6a1c-40c5-aae0-a489dc8898ef"]}}
        
        test_data = {
            "subject": subject,
            "predicate": predicate,
            "object": object 
        }
        test_data_list.append(test_data)

        #######################################################################################################################
        
        subject = "http://example.com/test" 
        predicate = {"value": {"description": "like"}} 
        object = {"value": {"description": "the song Low Life by Future, and The Weeknd", 
                             "related_entities": ["https://schema.org/artist", "https://musicbrainz.org/artist/48262e82-db9f-4a92-b650-dfef979b73", 
                                                  "https://schema.org/artist", "https://musicbrainz.org/artist/c8b03190-306c-4120-bb0b-6f2ebfc06ea9", 
                                                  "https://schema.org/song", "https://musicbrainz.org/recording/1fb6afc2-e6b2-4646-b5d9-497902d09404"]}}
        
        test_data = {
            "subject": subject,
            "predicate": predicate,
            "object": object 
        }
        test_data_list.append(test_data)

        #######################################################################################################################
        
        subject = "http://example.com/test" 
        predicate = {"value": {"description": "like"}} 
        object = {"value": {"description": "the song Work by Rihanna, and Drake", 
                             "related_entities": ["https://schema.org/artist", "https://musicbrainz.org/artist/73e5e69d-3554-40d8-8516-00cb38737a1c", 
                                                  "https://schema.org/artist", "https://musicbrainz.org/artist/9fff2f8a-21e6-47de-a2b8-7f449929d43f", 
                                                  "https://schema.org/song", "https://musicbrainz.org/recording/36c030de-a2d9-4fce-bf89-9581914e4b0a"]}}
        
        test_data = {
            "subject": subject,
            "predicate": predicate,
            "object": object 
        }
        test_data_list.append(test_data)

        #######################################################################################################################
        
        subject = "http://example.com/test" 
        predicate = {"value": {"description": "like"}} 
        object = {"value": {"description": "the song Fast Car by Jonas Blue, and Dakota", 
                             "related_entities": ["https://schema.org/artist", "https://musicbrainz.org/artist/17678771-5799-4017-851a-319f25b6948d", 
                                                  "https://schema.org/artist", "https://musicbrainz.org/artist/3fb5ac5a-1446-4f2a-896f-0630e1405214", 
                                                  "https://schema.org/song", "https://musicbrainz.org/recording/7ca2bdc7-43ab-4a85-9bef-0b7c874323ff"]}}
        
        test_data = {
            "subject": subject,
            "predicate": predicate,
            "object": object 
        }
        test_data_list.append(test_data)

        #######################################################################################################################
        
        subject = "http://example.com/test" 
        predicate = {"value": {"description": "like"}} 
        object = {"value": {"description": "the song Don't Let Me Down by The Chainsmokers, and Daya", 
                             "related_entities": ["https://schema.org/artist", "https://musicbrainz.org/artist/91a81925-92f9-4fc9-b897-93cf01226282", 
                                                  "https://schema.org/artist", "https://musicbrainz.org/artist/9e8a4e92-1598-47d9-80f7-646802abce76", 
                                                  "https://schema.org/song", "https://musicbrainz.org/recording/34b68937-b2ce-4346-b8b0-e08fd95e3a21"]}}
        
        test_data = {
            "subject": subject,
            "predicate": predicate,
            "object": object 
        }
        test_data_list.append(test_data)

        #######################################################################################################################
        
        subject = "http://example.com/test" 
        predicate = {"value": {"description": "like"}} 
        object = {"value": {"description": "the song Thrift Shop by Macklemore & Ryan Lewis", 
                             "related_entities": ["https://schema.org/artist", "https://musicbrainz.org/artist/97b226c8-7140-4da3-91ac-15e62e131a81",
                                                  "https://schema.org/song", "https://musicbrainz.org/recording/84855f43-378a-46d1-b524-a037efe28dc6"]}}
        
        test_data = {
            "subject": subject,
            "predicate": predicate,
            "object": object 
        }
        test_data_list.append(test_data)

        #######################################################################################################################
        
        subject = "http://example.com/test" 
        predicate = {"value": {"description": "like"}} 
        object = {"value": {"description": "the song Dust - feat. Astrid S by CLMD, and Astrid S", 
                             "related_entities": ["https://schema.org/artist", "https://musicbrainz.org/artist/bece0bb8-e39b-4147-98fc-54aa35d6ebf3", 
                                                  "https://schema.org/artist", "https://musicbrainz.org/artist/be389638-e74f-46a9-83d2-91ee3ce1fb0c", 
                                                  "https://schema.org/song", "https://musicbrainz.org/recording/8b3fdf7b-4e42-4b94-bb3b-72ce9cf6032a"]}}
        
        test_data = {
            "subject": subject,
            "predicate": predicate,
            "object": object 
        }
        test_data_list.append(test_data)

        #######################################################################################################################
        
        subject = "http://example.com/test" 
        predicate = {"value": {"description": "like"}} 
        object = {"value": {"description": "the song Who I Wanna Be - Rykkinnfella Remix by Suite 16", 
                             "related_entities": ["https://schema.org/artist", "No:URI:found", 
                                                  "https://schema.org/song", "No:URI:found"]}}
        
        test_data = {
            "subject": subject,
            "predicate": predicate,
            "object": object 
        }
        test_data_list.append(test_data)

        #######################################################################################################################
        
        subject = "http://example.com/test" 
        predicate = {"value": {"description": "like"}} 
        object = {"value": {"description": "the song Our Youth by Sonny Alven, and Emmi", 
                             "related_entities": ["https://schema.org/artist", "https://musicbrainz.org/artist/bd0b73ad-a215-475b-a4d1-cd8114babded", 
                                                  "https://schema.org/artist", "https://musicbrainz.org/artist/685da37b-4f5b-4ec1-8bd2-0688711270f5", 
                                                  "https://schema.org/song", "https://musicbrainz.org/recording/cc5e36fe-cc4d-4c8e-8874-29b1967a6bd2"]}}
        
        test_data = {
            "subject": subject,
            "predicate": predicate,
            "object": object 
        }
        test_data_list.append(test_data)

        #######################################################################################################################
        
        subject = "http://example.com/test" 
        predicate = {"value": {"description": "like"}} 
        object = {"value": {"description": "the song Under Overflaten (Som Marit Larsen) by Karpe", # Karpe Diem
                             "related_entities": ["https://schema.org/artist", "No:URI:found", 
                                                  "https://schema.org/song", "No:URI:found"]}}
        
        test_data = {
            "subject": subject,
            "predicate": predicate,
            "object": object 
        }
        test_data_list.append(test_data)

        #######################################################################################################################
        
        subject = "http://example.com/test" 
        predicate = {"value": {"description": "like"}} 
        object = {"value": {"description": "the song Faded by Alan Walker", 
                             "related_entities": ["https://schema.org/artist", "https://musicbrainz.org/artist/b0e4bc50-3062-4d31-afad-def6a6b7a8e9", 
                                                  "https://schema.org/song", "https://musicbrainz.org/recording/d78a4f92-f8d1-4d8b-8914-39bc3f77bf11"]}}
        
        test_data = {
            "subject": subject,
            "predicate": predicate,
            "object": object 
        }
        test_data_list.append(test_data)

        #######################################################################################################################
        
        subject = "http://example.com/test" 
        predicate = {"value": {"description": "like"}} 
        object = {"value": {"description": "the song Every Breath You Take by The Police", 
                             "related_entities": ["https://schema.org/artist", "https://musicbrainz.org/artist/9e0e2b01-41db-4008-bd8b-988977d6019a",
                                                   "https://schema.org/song", "https://musicbrainz.org/recording/1619e7de-c0dc-4c78-8b25-5dd69d953959"]}}
        
        test_data = {
            "subject": subject,
            "predicate": predicate,
            "object": object 
        }
        test_data_list.append(test_data)

        #######################################################################################################################
        
        subject = "http://example.com/test" 
        predicate = {"value": {"description": "like"}} 
        object = {"value": {"description": "the song Wiggle by Jason Derulo, and Snoop Dogg", 
                             "related_entities": ["https://schema.org/artist", "https://musicbrainz.org/artist/6de0f914-3e60-4418-be3b-42e0feb6eb4d", 
                                                  "https://schema.org/artist", "https://musicbrainz.org/artist/f90e8b26-9e52-4669-a5c9-e28529c47894", 
                                                  "https://schema.org/song", "https://musicbrainz.org/recording/d7ccf1bb-3ca5-44bd-93c5-d46cb2a4244c"]}}
        
        test_data = {
            "subject": subject,
            "predicate": predicate,
            "object": object 
        }
        test_data_list.append(test_data)

        #######################################################################################################################
        
        subject = "http://example.com/test" 
        predicate = {"value": {"description": "like"}} 
        object = {"value": {"description": "the song Beautiful Things by Benson Boone", 
                             "related_entities": ["https://schema.org/artist", "https://musicbrainz.org/artist/62b914a7-d775-4bb4-bb5e-d46e7df115b5",
                                                   "https://schema.org/song", "https://musicbrainz.org/recording/0c76cae1-60b6-4020-befa-9bab4ccb1a83"]}}
        
        test_data = {
            "subject": subject,
            "predicate": predicate,
            "object": object 
        }
        test_data_list.append(test_data)

        #######################################################################################################################
        
        subject = "http://example.com/test" 
        predicate = {"value": {"description": "like"}} 
        object = {"value": {"description": "the song Too Sweet by Hozier", 
                             "related_entities": ["https://schema.org/artist", "https://musicbrainz.org/artist/b4691384-50c3-4afd-9988-51d3ec5db65d", 
                                                  "https://schema.org/song", "https://musicbrainz.org/recording/272be1e2-9599-4b8d-b872-5e879881d103"]}}
        
        test_data = {
            "subject": subject,
            "predicate": predicate,
            "object": object 
        }
        test_data_list.append(test_data)

        #######################################################################################################################
        
        subject = "http://example.com/test" 
        predicate = {"value": {"description": "like"}} 
        object = {"value": {"description": "the song Like That by Future, Metro Boomin, and Kendrick Lamar", 
                             "related_entities": ["https://schema.org/artist", "https://musicbrainz.org/artist/48262e82-db9f-4a92-b650-dfef979b73ec", 
                                                  "https://schema.org/artist", "https://musicbrainz.org/artist/59db3d82-86ea-451f-881f-dffc8ec387c9", 
                                                  "https://schema.org/artist", "https://musicbrainz.org/artist/381086ea-f511-4aba-bdf9-71c753dc5077", 
                                                  "https://schema.org/song", "https://musicbrainz.org/recording/d4133a55-d72a-4ced-9a4d-d8afb4bd2058"]}}
        
        test_data = {
            "subject": subject,
            "predicate": predicate,
            "object": object 
        }
        test_data_list.append(test_data)

        #######################################################################################################################
        
        subject = "http://example.com/test" 
        predicate = {"value": {"description": "like"}} 
        object = {"value": {"description": "the song Lose Control by Teddy Swims", 
                             "related_entities": ["https://schema.org/artist", "https://musicbrainz.org/artist/35feae82-8b2c-4f8f-ae7a-af5662848947", 
                                                  "https://schema.org/song", "https://musicbrainz.org/recording/ff692229-47d4-44b2-9933-d5917a4a8f6d"]}}
        
        test_data = {
            "subject": subject,
            "predicate": predicate,
            "object": object 
        }
        test_data_list.append(test_data)

        #######################################################################################################################
        
        subject = "http://example.com/test" 
        predicate = {"value": {"description": "like"}} 
        object = {"value": {"description": "the song Push Ups by Drake", 
                             "related_entities": ["https://schema.org/artist", "https://musicbrainz.org/artist/9fff2f8a-21e6-47de-a2b8-7f449929d43f", 
                                                  "https://schema.org/song", "https://musicbrainz.org/recording/8bfe5ac6-6b48-4f15-927d-b842c89549a1"]}}
        
        test_data = {
            "subject": subject,
            "predicate": predicate,
            "object": object 
        }
        test_data_list.append(test_data)

        #######################################################################################################################
        
        subject = "http://example.com/test" 
        predicate = {"value": {"description": "like"}} 
        object = {"value": {"description": "the song I Can Fix Him (No Really I Can) by Taylor Swift", 
                             "related_entities": ["https://schema.org/artist", "https://musicbrainz.org/artist/20244d07-534f-4eff-b4d4-930878889970", 
                                                  "https://schema.org/song", "https://musicbrainz.org/recording/051338b7-df5a-4357-bbc9-4fdeded24a9e"]}}
        
        test_data = {
            "subject": subject,
            "predicate": predicate,
            "object": object 
        }
        test_data_list.append(test_data)

        #######################################################################################################################
        
        subject = "http://example.com/test" 
        predicate = {"value": {"description": "like"}} 
        object = {"value": {"description": "the song A Bar Song (Tipsy) by Shaboozey", 
                             "related_entities": ["https://schema.org/artist", "https://musicbrainz.org/artist/0b427dad-1ee5-48f1-aa4b-026680a3338e", 
                                                  "https://schema.org/song", "https://musicbrainz.org/recording/a40b893c-553a-4198-8ca2-d27fc23692c6"]}}
        
        test_data = {
            "subject": subject,
            "predicate": predicate,
            "object": object 
        }
        test_data_list.append(test_data)

        #######################################################################################################################
        
        subject = "http://example.com/test" 
        predicate = {"value": {"description": "like"}} 
        object = {"value": {"description": "the song Lovin On Me by Jack Harlow", # Lovin on Me
                             "related_entities": ["https://schema.org/artist", "No:URI:found", 
                                                  "https://schema.org/song", "No:URI:found"]}}
        
        test_data = {
            "subject": subject,
            "predicate": predicate,
            "object": object 
        }
        test_data_list.append(test_data)

        #######################################################################################################################
        
        subject = "http://example.com/test" 
        predicate = {"value": {"description": "like"}} 
        object = {"value": {"description": "the song Saturn by SZA", 
                             "related_entities": ["https://schema.org/artist", "https://musicbrainz.org/artist/272989c8-5535-492d-a25c-9f58803e027f", 
                                                  "https://schema.org/song", "https://musicbrainz.org/recording/9b6b096f-36d8-4297-b181-ea501c4b41a2"]}}
        
        test_data = {
            "subject": subject,
            "predicate": predicate,
            "object": object 
        }
        test_data_list.append(test_data)

        #######################################################################################################################
        
        subject = "http://example.com/test" 
        predicate = {"value": {"description": "like"}} 
        object = {"value": {"description": "the song we can’t be friends (wait for your love) by Ariana Grande", 
                             "related_entities": ["https://schema.org/artist", "https://musicbrainz.org/artist/f4fdbb4c-e4b7-47a0-b83b-d91bbfcfa387", 
                                                  "https://schema.org/song", "https://musicbrainz.org/recording/b6587011-5a7c-4664-82ad-7a6368f4bd99"]}}
        
        test_data = {
            "subject": subject,
            "predicate": predicate,
            "object": object 
        }
        test_data_list.append(test_data)

        #######################################################################################################################
        
        subject = "http://example.com/test" 
        predicate = {"value": {"description": "like"}} 
        object = {"value": {"description": "the song Stick Season by Noah Kahan", 
                             "related_entities": ["https://schema.org/artist", "https://musicbrainz.org/artist/a2a3f910-b188-43e7-81d0-f1ac2a2f3e12", 
                                                  "https://schema.org/song", "https://musicbrainz.org/recording/8dafee4c-e397-4d19-8f75-e6ae3fb8b601"]}}
        
        test_data = {
            "subject": subject,
            "predicate": predicate,
            "object": object 
        }
        test_data_list.append(test_data)

        #######################################################################################################################
        
        subject = "http://example.com/test" 
        predicate = {"value": {"description": "like"}} 
        object = {"value": {"description": "the song i like the way you kiss me by Artemas", 
                             "related_entities": ["https://schema.org/artist", "https://musicbrainz.org/artist/0211be88-dc0f-4002-a1de-4001bb359d51", 
                                                  "https://schema.org/song", "https://musicbrainz.org/recording/63935ae3-fa46-4663-b83e-2a502318e691"]}}
        
        test_data = {
            "subject": subject,
            "predicate": predicate,
            "object": object 
        }
        test_data_list.append(test_data)

        #######################################################################################################################
        
        subject = "http://example.com/test" 
        predicate = {"value": {"description": "like"}} 
        object = {"value": {"description": "the song I Remember Everything by Zach Bryan, and Kacey Musgraves", # I Remember Everything
                             "related_entities": ["https://schema.org/artist", "https://musicbrainz.org/artist/51e90731-08c0-4f60-89b6-5b78e5844de8", 
                                                  "https://schema.org/artist", "https://musicbrainz.org/artist/d1393ecb-431b-4fde-a6ea-d769f2f040cb", 
                                                  "https://schema.org/song", "https://musicbrainz.org/recording/010e7b4d-9e25-45c6-aaaa-d259f7007e99"]}}
        
        test_data = {
            "subject": subject,
            "predicate": predicate,
            "object": object 
        }
        test_data_list.append(test_data)

        #######################################################################################################################
        
        subject = "http://example.com/test" 
        predicate = {"value": {"description": "like"}} 
        object = {"value": {"description": "the song Cruel Summer by Taylor Swift", 
                             "related_entities": ["https://schema.org/artist", "https://musicbrainz.org/artist/20244d07-534f-4eff-b4d4-930878889970", 
                                                  "https://schema.org/song", "https://musicbrainz.org/recording/6624980c-4eff-444d-9e75-66f756a58ccd"]}}
        
        test_data = {
            "subject": subject,
            "predicate": predicate,
            "object": object 
        }
        test_data_list.append(test_data)

        #######################################################################################################################
        
        subject = "http://example.com/test" 
        predicate = {"value": {"description": "like"}} 
        object = {"value": {"description": "the song Agora Hills by Doja Cat", 
                             "related_entities": ["https://schema.org/artist", "https://musicbrainz.org/artist/5df62a88-cac9-490a-b62c-c7c88f4020f4", 
                                                  "https://schema.org/song", "https://musicbrainz.org/recording/a601e3a7-e52d-477d-a544-4cc3fdd288f1"]}}
        
        test_data = {
            "subject": subject,
            "predicate": predicate,
            "object": object 
        }
        test_data_list.append(test_data)

        #######################################################################################################################
        
        subject = "http://example.com/test" 
        predicate = {"value": {"description": "like"}} 
        object = {"value": {"description": "the song Wanna Be by GloRilla, and Megan Thee Stallion", # Wanna Be
                             "related_entities": ["https://schema.org/artist", "https://musicbrainz.org/artist/2a7ef045-ca10-4cb5-8fe9-1f5d38e84bc2", 
                                                  "https://schema.org/artist", "https://musicbrainz.org/artist/ee27b2d8-648c-4a9d-a68c-e55066959975", 
                                                  "https://schema.org/song", "https://musicbrainz.org/recording/b412ba65-96bd-43d4-bd2c-7f52328fd931"]}}
        
        test_data = {
            "subject": subject,
            "predicate": predicate,
            "object": object 
        }
        test_data_list.append(test_data)

        #######################################################################################################################
        
        subject = "http://example.com/test" 
        predicate = {"value": {"description": "like"}} 
        object = {"value": {"description": "the song End of Beginning by Djo", 
                             "related_entities": ["https://schema.org/artist", "https://musicbrainz.org/artist/dc84c3f5-a44c-4a46-bf41-fd1640e3c99d", 
                                                  "https://schema.org/song", "https://musicbrainz.org/recording/74f3b043-c0b4-4590-8c10-bfc4e3a06fef"]}}
        
        test_data = {
            "subject": subject,
            "predicate": predicate,
            "object": object 
        }
        test_data_list.append(test_data)

        #######################################################################################################################
        
        subject = "http://example.com/test" 
        predicate = {"value": {"description": "like"}} 
        object = {"value": {"description": "the song redrum by 21 Savage", 
                             "related_entities": ["https://schema.org/artist", "https://musicbrainz.org/artist/37b2cb82-ef79-4d46-a184-a549450aa231", 
                                                  "https://schema.org/song", "https://musicbrainz.org/recording/4ff9e97b-f326-440a-a820-943b68f1d938"]}}
        
        test_data = {
            "subject": subject,
            "predicate": predicate,
            "object": object 
        }
        test_data_list.append(test_data)

        #######################################################################################################################
        
        subject = "http://example.com/test" 
        predicate = {"value": {"description": "like"}} 
        object = {"value": {"description": "the song Good Luck, Babe! by Chappell Roan", 
                             "related_entities": ["https://schema.org/artist", "https://musicbrainz.org/artist/56a55378-f155-48de-80a5-d80104221267", 
                                                  "https://schema.org/song", "https://musicbrainz.org/recording/7194cfbb-36e7-48a1-b7aa-8dce21a0785a"]}}
        
        test_data = {
            "subject": subject,
            "predicate": predicate,
            "object": object 
        }
        test_data_list.append(test_data)

        #######################################################################################################################
        
        subject = "http://example.com/test" 
        predicate = {"value": {"description": "like"}} 
        object = {"value": {"description": "the song II MOST WANTED by Beyoncé, and Miley Cyrus", 
                             "related_entities": ["https://schema.org/artist", "https://musicbrainz.org/artist/859d0860-d480-4efd-970c-c05d5f1776b8", 
                                                  "https://schema.org/artist", "https://musicbrainz.org/artist/7e9bd05a-117f-4cce-87bc-e011527a8b18", 
                                                  "https://schema.org/song", "https://musicbrainz.org/recording/f39565d8-ee8d-4cd3-88db-fe246605286c"]}}
        
        test_data = {
            "subject": subject,
            "predicate": predicate,
            "object": object 
        }
        test_data_list.append(test_data)

        #######################################################################################################################
        
        subject = "http://example.com/test" 
        predicate = {"value": {"description": "like"}} 
        object = {"value": {"description": "the song Cry by Benson Boone", 
                             "related_entities": ["https://schema.org/artist", "https://musicbrainz.org/artist/62b914a7-d775-4bb4-bb5e-d46e7df115b5", 
                                                  "https://schema.org/song", "https://musicbrainz.org/recording/900dc2c3-68d8-44dc-9de3-c5ccdb872194"]}}
        
        test_data = {
            "subject": subject,
            "predicate": predicate,
            "object": object 
        }
        test_data_list.append(test_data)

        #######################################################################################################################
        
        subject = "http://example.com/test" 
        predicate = {"value": {"description": "like"}} 
        object = {"value": {"description": "the song Outskirts by Sam Hunt", 
                             "related_entities": ["https://schema.org/artist", "https://musicbrainz.org/artist/b27229bb-5669-4e98-b4ce-0158b2451fe8", 
                                                  "https://schema.org/song", "https://musicbrainz.org/recording/82ae5910-3636-4a36-9ce4-205cd8532ece"]}}
        
        test_data = {
            "subject": subject,
            "predicate": predicate,
            "object": object 
        }
        test_data_list.append(test_data)

        #######################################################################################################################
        
        subject = "http://example.com/test" 
        predicate = {"value": {"description": "like"}} 
        object = {"value": {"description": "the song TÚ NAME by Fuerza Regida", 
                             "related_entities": ["https://schema.org/artist", "https://musicbrainz.org/artist/e665ce26-6ce9-4c42-8f6a-7a361a0ba328", 
                                                  "https://schema.org/song", "https://musicbrainz.org/recording/137b52b4-e203-4b0d-a94e-a9929340bef8"]}}
        
        test_data = {
            "subject": subject,
            "predicate": predicate,
            "object": object 
        }
        test_data_list.append(test_data)

        #######################################################################################################################
        
        subject = "http://example.com/test" 
        predicate = {"value": {"description": "like"}} 
        object = {"value": {"description": "the song We Still Don’t Trust You by Future, Metro Boomin, and The Weeknd", # We Still Don´t Trust You
                             "related_entities": ["https://schema.org/artist", "https://musicbrainz.org/artist/48262e82-db9f-4a92-b650-dfef979b73ec", 
                                                  "https://schema.org/artist", "https://musicbrainz.org/artist/59db3d82-86ea-451f-881f-dffc8ec387c9", 
                                                  "https://schema.org/artist", "https://musicbrainz.org/artist/c8b03190-306c-4120-bb0b-6f2ebfc06ea9", 
                                                  "https://schema.org/song", "https://musicbrainz.org/recording/040c475a-418a-4fc6-ae88-c66b9650577b"]}}
        
        test_data = {
            "subject": subject,
            "predicate": predicate,
            "object": object 
        }
        test_data_list.append(test_data)

        #######################################################################################################################
        
        subject = "http://example.com/test" 
        predicate = {"value": {"description": "like"}} 
        object = {"value": {"description": "the song All The Stars by Kendrick Lamar, and SZA", # All The Stars
                             "related_entities": ["https://schema.org/artist", "https://musicbrainz.org/artist/381086ea-f511-4aba-bdf9-71c753dc5077", 
                                                  "https://schema.org/artist", "https://musicbrainz.org/artist/272989c8-5535-492d-a25c-9f58803e027f", 
                                                  "https://schema.org/song", "https://musicbrainz.org/recording/a0a38516-c9c3-4a05-a2bf-523b6ca219ab"]}}
        
        test_data = {
            "subject": subject,
            "predicate": predicate,
            "object": object 
        }
        test_data_list.append(test_data)

        #######################################################################################################################
        
        subject = "http://example.com/test" 
        predicate = {"value": {"description": "like"}} 
        object = {"value": {"description": "the song In A Sentimental Mood by Duke Ellington, and John Coltrane", 
                             "related_entities": ["https://schema.org/artist", "https://musicbrainz.org/artist/3af06bc4-68ad-4cae-bb7a-7eeeb45e411f", 
                                                  "https://schema.org/artist", "https://musicbrainz.org/artist/b625448e-bf4a-41c3-a421-72ad46cdb831", 
                                                  "https://schema.org/song", "https://musicbrainz.org/recording/41983bf4-23b1-4ece-bdbf-e2733eaac1fe"]}}
        
        test_data = {
            "subject": subject,
            "predicate": predicate,
            "object": object 
        }
        test_data_list.append(test_data)

        #######################################################################################################################
        
        subject = "http://example.com/test" 
        predicate = {"value": {"description": "like"}} 
        object = {"value": {"description": "the song What A Wonderful World by Louis Armstrong", 
                             "related_entities": ["https://schema.org/artist", "https://musicbrainz.org/artist/eea8a864-fcda-4602-9569-38ab446decd6", 
                                                  "https://schema.org/song", "https://musicbrainz.org/recording/3c7d88b5-80e5-48b2-8f16-ae3e1ed3db31"]}}
        
        test_data = {
            "subject": subject,
            "predicate": predicate,
            "object": object 
        }
        test_data_list.append(test_data)

        #######################################################################################################################
        
        subject = "http://example.com/test" 
        predicate = {"value": {"description": "like"}} 
        object = {"value": {"description": "the song Fly Me To The Moon by Frank Sinatra, and Count Basie", 
                             "related_entities": ["https://schema.org/artist", "https://musicbrainz.org/artist/197450cd-0124-4164-b723-3c22dd16494d", 
                                                  "https://schema.org/artist", "No:URI:found", 
                                                  "https://schema.org/song", "https://musicbrainz.org/recording/e038e646-dde6-4d3f-bb10-5f87a3348229"]}}
        
        test_data = {
            "subject": subject,
            "predicate": predicate,
            "object": object 
        }
        test_data_list.append(test_data)

        #######################################################################################################################
        
        subject = "http://example.com/test" 
        predicate = {"value": {"description": "like"}} 
        object = {"value": {"description": "the song The Girl From Ipanema by Stan Getz", 
                             "related_entities": ["https://schema.org/artist", "https://musicbrainz.org/artist/8f2422ab-0ec6-4c92-80c4-afe9622fab32", 
                                                  "https://schema.org/song", "https://musicbrainz.org/recording/271f749c-e7df-4760-8f8b-2a67de17a154"]}}
        
        test_data = {
            "subject": subject,
            "predicate": predicate,
            "object": object 
        }
        test_data_list.append(test_data)

        #######################################################################################################################
        
        subject = "http://example.com/test" 
        predicate = {"value": {"description": "like"}} 
        object = {"value": {"description": "the song Dream A Little Dream Of Me - Single Version by Ella Fitzgerald, and Louis Armstrong", 
                             "related_entities": ["https://schema.org/artist", "https://musicbrainz.org/artist/54799c0e-eb45-4eea-996d-c4d71a63c499", 
                                                  "https://schema.org/artist", "https://musicbrainz.org/artist/eea8a864-fcda-4602-9569-38ab446decd6", 
                                                  "https://schema.org/song", "No:URI:found"]}}
        
        test_data = {
            "subject": subject,
            "predicate": predicate,
            "object": object 
        }
        test_data_list.append(test_data)

        #######################################################################################################################
        
        subject = "http://example.com/test" 
        predicate = {"value": {"description": "like"}} 
        object = {"value": {"description": "the song Danny's Dream by Lars Gullin", 
                             "related_entities": ["https://schema.org/artist", "https://musicbrainz.org/artist/f1a5b44b-bdff-4f8f-b136-2786b3de648e", 
                                                  "https://schema.org/song", "https://musicbrainz.org/recording/4bc11f88-fe77-4781-a952-3853634418e6"]}}
        
        test_data = {
            "subject": subject,
            "predicate": predicate,
            "object": object 
        }
        test_data_list.append(test_data)

        #######################################################################################################################
        
        subject = "http://example.com/test" 
        predicate = {"value": {"description": "like"}} 
        object = {"value": {"description": "the song I’ll Be Seeing You by Billie Holiday", 
                             "related_entities": ["https://schema.org/artist", "https://musicbrainz.org/artist/d59c4cda-11d9-48db-8bfe-b557ee602aed", 
                                                  "https://schema.org/song", "https://musicbrainz.org/recording/9b6a919e-b3cb-44ed-a777-c8fe716880a9"]}}
        
        test_data = {
            "subject": subject,
            "predicate": predicate,
            "object": object 
        }
        test_data_list.append(test_data)

        #######################################################################################################################
        
        subject = "http://example.com/test" 
        predicate = {"value": {"description": "like"}} 
        object = {"value": {"description": "the song La vie en rose - Single Version by Louis Armstrong", 
                             "related_entities": ["https://schema.org/artist", "https://musicbrainz.org/artist/eea8a864-fcda-4602-9569-38ab446decd6", 
                                                  "https://schema.org/song", "No:URI:found"]}}
        
        test_data = {
            "subject": subject,
            "predicate": predicate,
            "object": object 
        }
        test_data_list.append(test_data)

        #######################################################################################################################
        
        subject = "http://example.com/test" 
        predicate = {"value": {"description": "like"}} 
        object = {"value": {"description": "the song My Funny Valentine by Chet Baker", 
                             "related_entities": ["https://schema.org/artist", "https://musicbrainz.org/artist/1ba1d493-7114-45e2-b163-a36d49a0c065", 
                                                  "https://schema.org/song", "https://musicbrainz.org/recording/4619732e-0c23-4c59-abb0-7c401d2c9c7f"]}}
        
        test_data = {
            "subject": subject,
            "predicate": predicate,
            "object": object 
        }
        test_data_list.append(test_data)

        #######################################################################################################################
        
        subject = "http://example.com/test" 
        predicate = {"value": {"description": "like"}} 
        object = {"value": {"description": "the song Elske igjen by Chris Abolade", 
                             "related_entities": ["https://schema.org/artist", "No:URI:found", 
                                                  "https://schema.org/song", "No:URI:found"]}}
        
        test_data = {
            "subject": subject,
            "predicate": predicate,
            "object": object 
        }
        test_data_list.append(test_data)

        #######################################################################################################################
        
        subject = "http://example.com/test" 
        predicate = {"value": {"description": "like"}} 
        object = {"value": {"description": "the song SEX OG BLOMSTER by Chris Abolade", 
                             "related_entities": ["https://schema.org/artist", "No:URI:found", 
                                                  "https://schema.org/song", "No:URI:found"]}}
        
        test_data = {
            "subject": subject,
            "predicate": predicate,
            "object": object 
        }
        test_data_list.append(test_data)

        #######################################################################################################################
        
        subject = "http://example.com/test" 
        predicate = {"value": {"description": "like"}} 
        object = {"value": {"description": "the song Fashion week by Chris Abolade, and Amara", 
                             "related_entities": ["https://schema.org/artist", "https://musicbrainz.org/artist/6a9f069e-bf27-45c8-8237-b92e63d19394", 
                                                  "https://schema.org/artist", "https://musicbrainz.org/artist/62051d1b-50e6-43ce-bf51-6ed96b00e9fc", 
                                                  "https://schema.org/song", "https://musicbrainz.org/recording/ebd98797-716b-46cd-a201-50f14b7549a5"]}}
        
        test_data = {
            "subject": subject,
            "predicate": predicate,
            "object": object 
        }
        test_data_list.append(test_data)

        #######################################################################################################################
        
        subject = "http://example.com/test" 
        predicate = {"value": {"description": "like"}} 
        object = {"value": {"description": "the song Glimmer of Hope by Tevvez", 
                             "related_entities": ["https://schema.org/artist", "https://musicbrainz.org/artist/92ced488-d102-44b5-a3b7-18f9aa67cf66", 
                                                  "https://schema.org/song", "https://musicbrainz.org/recording/88f7465c-e003-418b-8601-1ac6b59f5c35"]}}
        
        test_data = {
            "subject": subject,
            "predicate": predicate,
            "object": object 
        }
        test_data_list.append(test_data)

        #######################################################################################################################
        
        subject = "http://example.com/test" 
        predicate = {"value": {"description": "like"}} 
        object = {"value": {"description": "the song Stronger by Vertile", 
                             "related_entities": ["https://schema.org/artist", "No:URI:found", 
                                                  "https://schema.org/song", "No:URI:found"]}}
        
        test_data = {
            "subject": subject,
            "predicate": predicate,
            "object": object 
        }
        test_data_list.append(test_data)

        #######################################################################################################################
        
        subject = "http://example.com/test" 
        predicate = {"value": {"description": "like"}} 
        object = {"value": {"description": "the song 1-800-273-8255 by Logic, Alessia Cara, and Khalid", 
                             "related_entities": ["https://schema.org/artist", "https://musicbrainz.org/artist/713e751f-3ddb-4b77-b3b1-9e6f2e953ad5", 
                                                  "https://schema.org/artist", "https://musicbrainz.org/artist/97e69730-3791-423b-9770-287261588854", 
                                                  "https://schema.org/artist", "https://musicbrainz.org/artist/28737730-ec70-4da5-89c5-77ac13c5c34d", 
                                                  "https://schema.org/song", "https://musicbrainz.org/recording/ff95390a-ad32-4cc9-b70c-174328e6fdc1"]}}
        
        test_data = {
            "subject": subject,
            "predicate": predicate,
            "object": object 
        }
        test_data_list.append(test_data)

    
        return test_data_list

