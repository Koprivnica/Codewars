VOWELS = "aeiou"

def find_solutions(words):
    word_dict = {}
    result = []
    for word in words:
        for i, char in enumerate(word):
            if char in VOWELS:
                temp_word = word[:i] + "_" + word[i+1:]
                word_dict[temp_word] = word_dict.get(temp_word, 0) + 1
    
    for key, value in word_dict.items():
        temp_list = []
        if value == 5:
            for char in "aeiou":
                temp_word = key.replace("_", char)
                temp_list.append(temp_word)
            result.append(temp_list)
    
    return sorted(result)


word = ['eumahohi', 'qioega', 'uofekegan', 'wucadu', 'moaub', 'zezouei', 'reqecoeiv', 'vorotaaiuo', 'moaib', 'tonezei', 'tudobaoojo', 'qukooagaai', 'puoiropo', 'pueiropo', 'eilamuooq', 'fojegaoee', 'iibine', 'puairopo', 'suxidin', 'aeuaa', 'eijifouib', 'aioec', 'roaoqoyeco', 'tacuviq', 'iifiq', 'riyoqapoho', 'uequqoaixu', 'wucada', 'qioegu', 'culeqay', 'fojegauee', 'aesejuk', 'jaiiniqu', 'reqecooiv', 'xioeta', 'lomaminoe', 'eilamuioq', 'luleiap', 'fojegaeee', 'jaeiniqu', 'ougecu', 'wusaiet', 'lumaminoe', 'eioug', 'qioegi', 'puiiropo', 'iijifouib', 'loleiap', 'suxidon', 'zanud', 'bedifediu', 'gibueoye', 'cajooucoyu', 'duzesahew', 'tonezee', 'uequqoeixu', 'ooiaxuq', 'rouoqoyeco', 'tacaviq', 'wucadi', 'qioege', 'rioezoein', 'wucado', 'moaab', 'laleiap', 'aumahohi', 'uioec', 'zivuougiru', 'tiiiwurile', 'roooqoyeco', 'jeiafara', 'tiaiwurile', 'moaeb', 'cajoeucoyu', 'tudobaooje', 'eiaug', 'jauiniqu', 'suxiden', 'roeoqoyeco', 'vorotaaiio', 'xiueta', 'zinud', 'xieeta', 'iioec', 'nicenanuqi', 'iumahohi', 'zunud', 'eesejuk', 'culeqiy', 'eilamueoq', 'ooiaxaq', 'oesejuk', 'xiiidew', 'zenud', 'eioec', 'oigecu', 'riyoqapohe', 'vorotaaioo', 'culeqey', 'qukoeagaai', 'eilamuuoq', 'riyoqapoha', 'heeileeomo', 'culeqoy', 'uofoauuoqo', 'eieug', 'gibuuoye', 'aibine', 'leleiap', 'tieiwurile', 'reqecoaiv', 'uibine', 'eofoauuoqo', 'zamie', 'wusaoet', 'taceviq', 'qukouagaai', 'tiuiwurile', 'fojegaiee', 'zonud', 'qioego', 'duzesohew', 'gibuooye', 'taciviq', 'zezooei', 'roioqoyeco', 'oifiq', 'zivuougeru', 'duzesihew', 'xioidew', 'tudobaooja', 'oeuaa', 'ueuaa', 'moaob', 'suxidan', 'zivuougaru']

print(find_solutions(word))
                