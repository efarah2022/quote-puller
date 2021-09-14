def extract_empty(lines) : 
    for line in lines : 
        if line == "" :
            lines.remove(line)
    return lines

def index_authors(lines) :
    author_indices = []
    for i in range(0, len(lines)) : 
        if (lines[i])[0:2] == "--" : 
            author_indices.append(i)
    return author_indices

def get_quotes(file) : 
    with open(file, 'r') as q:
        lines = q.readlines()
        lines = extract_empty(lines)
        author_indices = index_authors(lines)
        curQuote = ""
        quotes = {}
        for i in range(0, len(lines)) : 
            if i not in author_indices : 
                curQuote += lines[i].strip() + " "
            else : 
                curAuthor = lines[i][2:].strip()
                if curAuthor not in quotes:
                    quotes[curAuthor] = []
                quotes[curAuthor].append(curQuote)
                curQuote = ""
        return quotes