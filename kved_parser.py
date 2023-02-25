"""
KVED
"""
import json

def read_file():
    """
    function for read file
    """
    with open('kved.json', 'r', encoding='utf-8') as file_to_parse:
        return json.load(file_to_parse)

def parse_kved(class_code):
    """
    This functiom searching all informstion about classCode in Kved
    >>> parse_kved('62.01')

    """
    data = read_file()
    for sections in data['sections']:
        for elements in sections:
            for division in elements['divisions']:
                for group in division['groups']:
                    for classes in group['classes']:
                        if classes['classCode'] == class_code:
                            result = {"name" : classes['className'],
                                    "type" : "class", 
                                    "parent": {"name" : group['groupName'],
                                    "type" : "group", 
                                    "num_children" : len(group['classes']),
                                    "parent" : {"name" :
                                    division['divisionName'],
                                    "type" : "division",
                                    "num_children" : len(division['groups']),
                                    "parent" : {"name" :
                                    elements['sectionName'],
                                    "type" : "section",
                                    "num_children" : len(elements['divisions'])}
                            }}} 
                            with open('kved_results.json', 'w',
                            encoding='utf-8') as file:
                                json.dump(result, file, ensure_ascii=False,
                                indent = 4)
                            return None

if __name__ == "__main__":
    import doctest
    print(doctest.testmod())

