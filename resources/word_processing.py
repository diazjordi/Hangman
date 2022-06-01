def create_word_lists(file_path: str):
    wordlists = {}
    words_easy = []
    words_moderate = []
    words_difficult = []
    # read in text file
    if file_path is None:
        with open('resources/words.txt','r') as f:
            lines = f.readline()
            for line in f:
                line = line.rstrip()
                if len(line) <= 4:
                    words_easy.append(line)
                elif 5 <= len(line) <= 8:
                    words_moderate.append(line)
                elif 8 < len(line):
                    words_difficult.append(line)
    elif file_path is not None:
        with open(file_path,'r') as f:
            lines = f.readline()
            for line in f:
                line = line.rstrip()
                if len(line) <= 4:
                    words_easy.append(line)
                elif 5 <= len(line) <= 8:
                    words_moderate.append(line)
                elif 8 < len(line):
                    words_difficult.append(line)
    
    wordlists['easy'] = words_easy
    wordlists['moderate'] = words_moderate
    wordlists['difficult'] = words_difficult
    return wordlists