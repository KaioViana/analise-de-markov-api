def formatText(text):
    import re
    

    text = text.strip()
    text = text.replace('\n', ' ')
    text = text.replace('\t', '')
    text = re.sub(r'(http\S*|@\S*|;|#\S*)', '', text)
    text = re.sub(
                    r'[(\U0001F600-\U0001F92F|\U0001F300-\U0001F5FF|\U0001F680-\U0001F6FF|\U0001F190-\U0001F1FF|\U00002702-\U000027B0|\U0001F926-\U0001FA9F|\u200d|\u2640-\u2642|\u2600-\u2B55|\u23cf|\u23e9|\u231a|\ufe0f)]*',
                    '',
                    text
                )
    text = re.sub(' +', ' ', text)
    return text