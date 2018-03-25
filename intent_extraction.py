from textblob import TextBlob

while True:
    sample_text = input('Enter : ')
    trt = TextBlob(sample_text)

    for i in trt.tags:
        if i[1]=='NN' or i[1]=='VB':
            print(i[0])
        
