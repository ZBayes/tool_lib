# 处理新文本的一些工具

import re
import nltk
import string

nltk.download('punkt')
nltk.download('stopwords')


class text_clean:

    # Stop words list: 停用词表
    # STOP_WORDS: from NLTK
    STOP_WORDS = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up',
                  'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't", 'won', "won't", 'wouldn', "wouldn't"]
    # STOP_WORDS_MORE: from newly publish paper or internet, more but not that reliable
    STOP_WORDS_MORE = ["'d", "'ll", "'m", "'re", "'s", "'t", "'ve", 'ZT', 'ZZ', 'a', "a's", 'able', 'about', 'above', 'abst', 'accordance', 'according', 'accordingly', 'across', 'act', 'actually', 'added', 'adj', 'adopted', 'affected', 'affecting', 'affects', 'after', 'afterwards', 'again', 'against', 'ah', "ain't", 'all', 'allow', 'allows', 'almost', 'alone', 'along', 'already', 'also', 'although', 'always', 'am', 'among', 'amongst', 'an', 'and', 'announce', 'another', 'any', 'anybody', 'anyhow', 'anymore', 'anyone', 'anything', 'anyway', 'anyways', 'anywhere', 'apart', 'apparently', 'appear', 'appreciate', 'appropriate', 'approximately', 'are', 'area', 'areas', 'aren', "aren't", 'arent', 'arise', 'around', 'as', 'aside', 'ask', 'asked', 'asking',
                       'asks', 'associated', 'at', 'auth', 'available', 'away', 'awfully', 'b', 'back', 'backed', 'backing', 'backs', 'be', 'became', 'because', 'become', 'becomes', 'becoming', 'been', 'before', 'beforehand', 'began', 'begin', 'beginning', 'beginnings', 'begins', 'behind', 'being', 'beings', 'believe', 'below', 'beside', 'besides', 'best', 'better', 'between', 'beyond', 'big', 'biol', 'both', 'brief', 'briefly', 'but', 'by', 'c', "c'mon", "c's", 'ca', 'came', 'can', "can't", 'cannot', 'cant', 'case', 'cases', 'cause', 'causes', 'certain', 'certainly', 'changes', 'clear', 'clearly', 'co', 'com', 'come', 'comes', 'concerning', 'consequently', 'consider', 'considering', 'contain', 'containing', 'contains', 'corresponding', 'could', "couldn't",
                       'couldnt', 'course', 'currently', 'd', 'date', 'definitely', 'describe', 'described', 'despite', 'did', "didn't", 'differ', 'different', 'differently', 'discuss', 'do', 'does', "doesn't", 'doing', "don't", 'done', 'down', 'downed', 'downing', 'downs', 'downwards', 'due', 'during', 'e', 'each', 'early', 'ed', 'edu', 'effect', 'eg', 'eight', 'eighty', 'either', 'else', 'elsewhere', 'end', 'ended', 'ending', 'ends', 'enough', 'entirely', 'especially', 'et', 'et-al', 'etc', 'even', 'evenly', 'ever', 'every', 'everybody', 'everyone', 'everything', 'everywhere', 'ex', 'exactly', 'example', 'except', 'f', 'face', 'faces', 'fact', 'facts', 'far', 'felt', 'few', 'ff', 'fifth', 'find', 'finds', 'first', 'five', 'fix', 'followed', 'following',
                       'follows', 'for', 'former', 'formerly', 'forth', 'found', 'four', 'from', 'full', 'fully', 'further', 'furthered', 'furthering', 'furthermore', 'furthers', 'g', 'gave', 'general', 'generally', 'get', 'gets', 'getting', 'give', 'given', 'gives', 'giving', 'go', 'goes', 'going', 'gone', 'good', 'goods', 'got', 'gotten', 'great', 'greater', 'greatest', 'greetings', 'group', 'grouped', 'grouping', 'groups', 'h', 'had', "hadn't", 'happens', 'hardly', 'has', "hasn't", 'have', "haven't", 'having', 'he', "he's", 'hed', 'hello', 'help', 'hence', 'her', 'here', "here's", 'hereafter', 'hereby', 'herein', 'heres', 'hereupon', 'hers', 'herself', 'hes', 'hi', 'hid', 'high', 'higher', 'highest', 'him', 'himself', 'his', 'hither', 'home', 'hopefully',
                       'how', 'howbeit', 'however', 'hundred', 'i', "i'd", "i'll", "i'm", "i've", 'id', 'ie', 'if', 'ignored', 'im', 'immediate', 'immediately', 'importance', 'important', 'in', 'inasmuch', 'inc', 'include', 'indeed', 'index', 'indicate', 'indicated', 'indicates', 'information', 'inner', 'insofar', 'instead', 'interest', 'interested', 'interesting', 'interests', 'into', 'invention', 'inward', 'is', "isn't", 'it', "it'd", "it'll", "it's", 'itd', 'its', 'itself', 'j', 'just', 'k', 'keep', 'keeps', 'kept', 'keys', 'kg', 'kind', 'km', 'knew', 'know', 'known', 'knows', 'l', 'large', 'largely', 'last', 'lately', 'later', 'latest', 'latter', 'latterly', 'least', 'less', 'lest', 'let', "let's", 'lets', 'like', 'liked', 'likely', 'line', 'little',
                       'long', 'longer', 'longest', 'look', 'looking', 'looks', 'ltd', 'm', 'made', 'mainly', 'make', 'makes', 'making', 'man', 'many', 'may', 'maybe', 'me', 'mean', 'means', 'meantime', 'meanwhile', 'member', 'members', 'men', 'merely', 'mg', 'might', 'million', 'miss', 'ml', 'more', 'moreover', 'most', 'mostly', 'mr', 'mrs', 'much', 'mug', 'must', 'my', 'myself', 'n', "n't", 'na', 'name', 'namely', 'nay', 'nd', 'near', 'nearly', 'necessarily', 'necessary', 'need', 'needed', 'needing', 'needs', 'neither', 'never', 'nevertheless', 'new', 'newer', 'newest', 'next', 'nine', 'ninety', 'no', 'nobody', 'non', 'none', 'nonetheless', 'noone', 'nor', 'normally', 'nos', 'not', 'noted', 'nothing', 'novel', 'now', 'nowhere', 'number', 'numbers', 'o',
                       'obtain', 'obtained', 'obviously', 'of', 'off', 'often', 'oh', 'ok', 'okay', 'old', 'older', 'oldest', 'omitted', 'on', 'once', 'one', 'ones', 'only', 'onto', 'open', 'opened', 'opening', 'opens', 'or', 'ord', 'order', 'ordered', 'ordering', 'orders', 'other', 'others', 'otherwise', 'ought', 'our', 'ours', 'ourselves', 'out', 'outside', 'over', 'overall', 'owing', 'own', 'p', 'page', 'pages', 'part', 'parted', 'particular', 'particularly', 'parting', 'parts', 'past', 'per', 'perhaps', 'place', 'placed', 'places', 'please', 'plus', 'point', 'pointed', 'pointing', 'points', 'poorly', 'possible', 'possibly', 'potentially', 'pp', 'predominantly', 'present', 'presented', 'presenting', 'presents', 'presumably', 'previously', 'primarily',
                       'probably', 'problem', 'problems', 'promptly', 'proud', 'provides', 'put', 'puts', 'q', 'que', 'quickly', 'quite', 'qv', 'r', 'ran', 'rather', 'rd', 're', 'readily', 'really', 'reasonably', 'recent', 'recently', 'ref', 'refs', 'regarding', 'regardless', 'regards', 'related', 'relatively', 'research', 'respectively', 'resulted', 'resulting', 'results', 'right', 'room', 'rooms', 'run', 's', 'said', 'same', 'saw', 'say', 'saying', 'says', 'sec', 'second', 'secondly', 'seconds', 'section', 'see', 'seeing', 'seem', 'seemed', 'seeming', 'seems', 'seen', 'sees', 'self', 'selves', 'sensible', 'sent', 'serious', 'seriously', 'seven', 'several', 'shall', 'she', "she'll", 'shed', 'shes', 'should', "shouldn't", 'show', 'showed', 'showing', 'shown',
                       'showns', 'shows', 'side', 'sides', 'significant', 'significantly', 'similar', 'similarly', 'since', 'six', 'slightly', 'small', 'smaller', 'smallest', 'so', 'some', 'somebody', 'somehow', 'someone', 'somethan', 'something', 'sometime', 'sometimes', 'somewhat', 'somewhere', 'soon', 'sorry', 'specifically', 'specified', 'specify', 'specifying', 'state', 'states', 'still', 'stop', 'strongly', 'sub', 'substantially', 'successfully', 'such', 'sufficiently', 'suggest', 'sup', 'sure', 't', "t's", 'take', 'taken', 'taking', 'tell', 'tends', 'th', 'than', 'thank', 'thanks', 'thanx', 'that', "that'll", "that's", "that've", 'thats', 'the', 'their', 'theirs', 'them', 'themselves', 'then', 'thence', 'there', "there'll", "there's", "there've",
                       'thereafter', 'thereby', 'thered', 'therefore', 'therein', 'thereof', 'therere', 'theres', 'thereto', 'thereupon', 'these', 'they', "they'd", "they'll", "they're", "they've", 'theyd', 'theyre', 'thing', 'things', 'think', 'thinks', 'third', 'this', 'thorough', 'thoroughly', 'those', 'thou', 'though', 'thoughh', 'thought', 'thoughts', 'thousand', 'three', 'throug', 'through', 'throughout', 'thru', 'thus', 'til', 'tip', 'to', 'today', 'together', 'too', 'took', 'toward', 'towards', 'tried', 'tries', 'truly', 'try', 'trying', 'ts', 'turn', 'turned', 'turning', 'turns', 'twice', 'two', 'u', 'un', 'under', 'unfortunately', 'unless', 'unlike', 'unlikely', 'until', 'unto', 'up', 'upon', 'ups', 'us', 'use', 'used', 'useful', 'usefully', 'usefulness',
                       'uses', 'using', 'usually', 'uucp', 'v', 'value', 'various', 'very', 'via', 'viz', 'vol', 'vols', 'vs', 'w', 'want', 'wanted', 'wanting', 'wants', 'was', "wasn't", 'way', 'ways', 'we', "we'd", "we'll", "we're", "we've", 'wed', 'welcome', 'well', 'wells', 'went', 'were', "weren't", 'what', "what'll", "what's", 'whatever', 'whats', 'when', 'whence', 'whenever', 'where', "where's", 'whereafter', 'whereas', 'whereby', 'wherein', 'wheres', 'whereupon', 'wherever', 'whether', 'which', 'while', 'whim', 'whither', 'who', "who'll", "who's", 'whod', 'whoever', 'whole', 'whom', 'whomever', 'whos', 'whose', 'why', 'widely', 'will', 'willing', 'wish', 'with', 'within', 'without', "won't", 'wonder', 'words', 'work', 'worked', 'working', 'works', 'world',
                       'would', "wouldn't", 'www', 'x', 'y', 'year', 'years', 'yes', 'yet', 'you', "you'd", "you'll", "you're", "you've", 'youd', 'young', 'younger', 'youngest', 'your', 'youre', 'yours', 'yourself', 'yourselves', 'z', 'zero', 'zt', 'zz']

    # Words that is abonormal in texts from the internet 异常的一些HTML词
    HTML_WORDS = ['&ldqu', '&rsqu', '&rdqu', '&lsqu', '&p/ts', '&p/as', '&p/nz', '&p###', '&lt;c', '&lt;o', '&gt;#', '&lt;0', '&lt;r', '&p500', '&p.##', '&lt;v', '&gt;=', '&lt;2', '&a.##', '&p&rs', '&p/go', '&gt;.', '&t&rs', '&p/ca', '&gt;s', '&gt;h', '&p/bm', '&q&rs', '&s&rs', '&amp;', '&ps&r', '&prod', '&lt;a', '&lt;x', '&gt;,', '&a?,&', '&gas&', '&i.##', '&lt;e', '&a/ta', '&g.##', '&lt;#', '&i&rs', '&a/mu', '&lt;^', '&dett', '&lt;h', '&lt;u', '&m###', '&lt;g', '&m-co', '&a,&r', '&trad', '&ndas', '&m&rs', '&poun', '&m.##', '&lt;b', '&a/me', '&g&rs', '&deg;', '&a/br', '&mdas', '&gt;e', '&ouml', '&lt;i', '&t.##', '&anti', '&a/si', '&a/fo', '&n&rs', '&lt;p', '&lt;m', '&lt;w', '&lt;k', '&t).#', '&a/fr', '&a/es', '&lt;t', '&d.##', '&lt;1', '&lt;f', '&lt;.', '&eacu', '&aacu',
                  '&atil', '&shop', '&a&rd', '&t###', '&=rel', '&gt;f', '&y:&r', '&lt;n', '&#821', '&#822', '&#823', '&quot', '&m.re', '&a/ma', '&a/ih', '&a/mo', '&#039', '&hell', '&lt;\u200e', '&lt;\x7f', '&gt;*', '&e&rs', '&c.##', '&fbov', '&#x27', '&#xfe', '&acti', '&#39;', '&e.##', '&#10;', '&lt;s', '&lt;7', '&lt;l', '&c."#', '&#038', '&list', '&nain', '&jama', '&dani', '&shan', '&adam', '&name', '&trav', '&mari', '&ephr', '&lt;d', '&gt;o', '&p).#', '&#824', '&a###', '&powe', '&medi', '&gt;7', '&gt;]', '&p/fi', '&midd', '&lt;,', '&cd=1', '&hl=e', '&ct=c', '&gl=u', '&pbul', '&y&rs', '&p,&r', '&e###', '&mode', '&id=e', '&tab=', '&_cvi', '&p/mi', '&p15-', '&p15x', '&e."#', '&d."#', '&s.##', '&o.##', '&t-be', '&fs.#', '&vacc', '&###g', '&thom', '&b/so', '&#835', '&#652', '&#820', '&m)##']

    # Tokenize, 词汇分块
    def tokenize_text(txt):
        sentences = nltk.sent_tokenize(txt)
        word_tokens = [nltk.word_tokenize(
            sentence) for sentence in sentences]
        return word_tokens

    # Delete abnormal words, 删除特殊字符
    def delete_abnormal(sentence, keep_apostrophes=False, delete_html=True):
        # keep_apostrophes:char only or some others is ok, delete_html: isused delete_html
        sentence = sentence.strip()
        if delete_html:
            sentence = text_clean.delete_html(sentence)
        if keep_apostrophes:
            PATTERN = r'[?|$|&|*|%|@|(|)|~]'
            filtered_sentence = re.sub(PATTERN, r' ', sentence)
        else:
            PATTERN = r'[^a-zA-Z0-9 ]'
            filtered_sentence = re.sub(PATTERN, r' ', sentence)
        return filtered_sentence

    # 大小写转换
    def tolower(txt):
        return txt.lower()

    def toupper(txt):
        return txt.upper()

    # Stop words, 删除停用词
    def delete_stopwords(txt, mode=0):
        # mode:1=more, 0=normal
        token = text_clean.tokenize_text(txt)
        if mode == 1:
            stopword_list = text_clean.STOP_WORDS_MORE
        else:
            stopword_list = text_clean.STOP_WORDS
        filtered_tokens = [
            [token_item for token_item in token_sentense if token_item not in stopword_list] for token_sentense in token]
        filtered_txt = " ".join([" ".join(token_sentense)
                                 for token_sentense in filtered_tokens])
        return filtered_txt

    # Stemming, 取词根
    def stemming(txt):
        token = text_clean.tokenize_text(txt)
        stemmer = nltk.stem.SnowballStemmer("english")
        stemmed_tokens = [
            [stemmer.stem(token_item) for token_item in token_sentense] for token_sentense in token]
        stemmed_txt = " ".join([" ".join(token_sentense)
                                for token_sentense in stemmed_tokens])
        return stemmed_txt

    # Delete words that is abonormal in texts from the internet
    # Not recommended for individual use
    # 网络文本异常词提取，建议与delete_abnormal一起使用，不建议单独使用
    def delete_html(txt):
        token = text_clean.tokenize_text(txt)
        stopword_list = text_clean.HTML_WORDS
        filtered_tokens = [
            [token_item for token_item in token_sentense if token_item not in stopword_list] for token_sentense in token]
        filtered_txt = " ".join([" ".join(token_sentense)
                                 for token_sentense in filtered_tokens])
        return filtered_txt

# # UNIT TEST SAMPLE
# text = "brent reaches $80 a barrel after fall in u.s. crude stocks    new york (reuters) - oil futures rose on wednesday, with brent reaching $80 a barrel, after a larger-than-expected drop in u.s. crude inventories and as u.s. sanctions on iran added to concerns over global oil supply.###benchmark brent crude lcoc1 futures rose 68 cents to settle at $79.74 a barrel. the global benchmark earlier reached $80.13 a barrel, its highest level since may 22.###u.s. west texas intermediate (wti) crude clc1 futures  rose $1.12 to settle at $70.37 a barrel, a one-week high.###u.s. crude inventories usoilc=eci fell by 5.3 million barrels in the last week, the u.s. energy information administration said on wednesday. analysts had expected a decrease of 805,000 barrels.###&ldquo;today&rsquo;s crude stock draw of 5.3 million barrels fell far short of the (american petroleum institute&rsquo;s) decline but was significantly larger than the normal draw of around 1 million barrels for this particular week,&rdquo; jim ritterbusch, president of ritterbusch and associates, said in a note.###also supporting prices were supply concerns surrounding u.s. sanctions on iran. since the spring, when the trump administration said it would impose the sanctions, traders have been focusing on the potential impact on global supply. the sanctions will target iran&rsquo;s oil exports from november.###&ldquo;iran is increasingly becoming the preoccupation of the crude market. the last couple of weeks have seen the expected squeeze on iranian crude flows taking shape, with overall outflows down markedly,&rdquo; consultancy jbc energy said.###(graphic: iran oil exports to asia: tmsnrt.rs/2cezade)###russian energy minister alexander novak on wednesday warned of the impact of the u.s. sanctions against iran.###&ldquo;this is a huge uncertainty on the market – how countries, which buy almost 2 million barrels per day (bpd) of iranian oil, will act. the situation should be closely watched, the right decisions should be taken,&rdquo; he said.###novak said global oil markets were &ldquo;fragile&rdquo; due to geopolitical risks and supply disruptions, but added his country could raise output if needed.###the organization of the petroleum exporting countries cut its forecast for oil demand growth in 2019 in its monthly report and said rising challenges in some emerging and developing countries could negatively impact global economic growth. [opec/m]###opec said it expected demand growth of 1.41 million bpd in 2019, a 20,000-bpd downgrade from its previous forecast.###oil traders were also watching the progress of category 4 hurricane florence, which is expected to make landfall on the u.s. east coast by friday.###crude output will not be affected by the massive storm, but the evacuation of more than a million residents, as well as businesses, has prompted a near-term spike in fuel demand."
# print(text)
# print(text_clean.tokenize_text(text))
# print(text_clean.delete_abnormal(text))
# print(text_clean.tolower(text))
# print(text_clean.toupper(text))
# print(text_clean.delete_stopwords(text))
# print(text_clean.stemming(text))
# print(text_clean.delete_html(text))
