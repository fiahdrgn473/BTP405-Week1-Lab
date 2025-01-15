def charCount(t):
    from collections import Counter
    try:
        with open(t, 'r') as file:
            text=file.read().replace(" ", "").replace("\n", "")
            return dict(Counter(text))
    except FileNotFoundError:
        print (f"Error: The file '{t} was not found.")
        return {}
    except Exception as e:
        print (f"Error: An error has ocurred '{e}")
        return {}
    
charCount("lab1q1.py")
