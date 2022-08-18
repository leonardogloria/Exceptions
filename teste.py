def remove_dots(word):
    word2 = ''
    inicio = 0
    for i in range(0, len(word)):
        if i != word.find('.', inicio):
            word2 = word2 + word[i]
        else:
            inicio = i+1

        print("i = {}\n, proximo ponto {}\n, letra {}, palavra {}".format(i,word.find('.',inicio), word[i], word2 ) )
    return word2

if __name__ == "__main__":
    print(remove_dots('a.b.c'))