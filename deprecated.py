import re


# extract title, director, and year from cineteca info
def extract_info(inner_texts):
    info_list = []

    for text in inner_texts:
        # Regular expression to find title, year, and director
        pattern = r'\((.*), Dir.: (.*), .*, (.*), .*\)'

        # Find matches
        matches = re.match(pattern, text)

        if matches:
            # Get title, director and year
            title = matches.group(1)
            director = matches.group(2)
            year = matches.group(3)

            # Add the information to the list
            info_list.append({
                'title': title,
                'director': director,
                'year': year
            })
    return info_list
