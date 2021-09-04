from  tokenization import dict_models
import numpy as np
import nltk
import re


replaces = {
    'hello':'xin chào','hi':'chào','hey':'chào','my':'tôi tên','is':'là','thank':'cảm ơn','thanks':'cảm ơn',
    'Thank you':'cảm ơn','Bye':'Tạm biệt', 'See you later':'hẹn gặp lại bạn sau', 'Goodbye':'tạm biệt',
    'name':'tên','product':'sản phẩm','email_address':'địa chỉ email','phone_number':'số điện thoại',
    'òa': 'oà', 'óa': 'oá', 'ỏa': 'oả', 'õa': 'oã', 'ọa': 'oạ', 'òe': 'oè', 'óe': 'oé','ỏe': 'oẻ',
    'õe': 'oẽ', 'ọe': 'oẹ', 'ùy': 'uỳ', 'úy': 'uý', 'ủy': 'uỷ', 'ũy': 'uỹ','ụy': 'uỵ', 'uả': 'ủa',
    'ả': 'ả', 'ố': 'ố', 'u´': 'ố','ỗ': 'ỗ', 'ồ': 'ồ', 'ổ': 'ổ', 'ấ': 'ấ', 'ẫ': 'ẫ', 'ẩ': 'ẩ',
    'ầ': 'ầ', 'ỏ': 'ỏ', 'ề': 'ề','ễ': 'ễ', 'ắ': 'ắ', 'ủ': 'ủ', 'ế': 'ế', 'ở': 'ở', 'ỉ': 'ỉ',
    'ẻ': 'ẻ', 'àk': u' à ','aˋ': 'à', 'iˋ': 'ì', 'ă´': 'ắ','ử': 'ử', 'e˜': 'ẽ', 'y˜': 'ỹ', 'a´': 'á',
    'okey': ' ok ', 'ôkê': ' ok ', 'oki': ' ok ', ' oke ':  ' ok ',' okay':' ok ','okê':' ok ','êu':'chào',
    ' tks ': u' cám ơn ', 'thks': u' cám ơn ', 'thanks': u' cám ơn ', 'ths': u' cám ơn ', 'thank': u' cám ơn ',
    'kg ': u' không ','not': u' không ', u' kg ': u' không ', '"k ': u' không ',' kh ':u' không ','kô':u' không ',
    'hok':u' không ',' kp ': u' không phải ',u' kô ': u' không ', '"ko ': u' không ', u' ko ': u' không ', 
    u' k ': u' không ', 'khong': u' không ', u' hok ': u' không ', ' vs ': u' với ', 'wa': ' quá ', 
    'wá': u' quá', 'j': u' gì ', '“': ' ',' sz ': u' cỡ ', 'size': u' cỡ ', u' đx ': u' được ', 
    'dk': u' được ', 'dc': u' được ', 'đk': u' được ','đc': u' được ','authentic': u' chuẩn chính hãng ',
    u' aut ': u' chuẩn chính hãng ', u' auth ': u' chuẩn chính hãng ', 'thick': u' thích ', 'store': u' cửa hàng ',
    'shop': u' cửa hàng ', 'sp': u' sản phẩm ', 'gud': u' tốt ','god': u' tốt ','wel done':' tốt ', 
    'good': u' tốt ', 'gút': u' tốt ','sấu': u' xấu ','gut': u' tốt ', u' tot ': u' tốt ', u' nice ': u' tốt ', 
    'perfect': 'rất tốt', 'bt': u' bình thường ','time': u' thời gian ', 'qá': u' quá ', u' ship ': u' giao hàng ', 
    u' m ': u' mình ', u' mik ': u' mình ','ể': 'ể', 'quality': 'chất lượng','chat':' chất ', 
    'excelent': 'hoàn hảo', 'bad': 'tệ','fresh': ' tươi ','sad': ' tệ ','date': u' hạn sử dụng ', 
    'hsd': u' hạn sử dụng ','quickly': u' nhanh ', 'quick': u' nhanh ','fast': u' nhanh ',
    'delivery': u' giao hàng ',u' síp ': u' giao hàng ','beautiful': u' đẹp tuyệt vời ', u' tl ': u' trả lời ',
    u' r ': u' rồi ', u' shopE ': u' cửa hàng ',u' order ': u' đặt hàng ','chất lg': u' chất lượng ',
    u' sd ': u' sử dụng ',u' dt ': u' điện thoại ',u' nt ': u' nhắn tin ',u' tl ': u' trả lời ',u' sài ': u' xài ',
    u'bjo':u' bao giờ ','thik': u' thích ',u' sop ': u' cửa hàng ', ' fb ': ' facebook ', ' face ': ' facebook ', 
    ' very ': u' rất ',u'quả ng ':u' quảng  ','dep': u' đẹp ',u' xau ': u' xấu ','delicious': u' ngon ', 
    u'hàg': u' hàng ', u'qủa': u' quả ','iu': u' yêu ','fake': u' giả mạo ', 'trl': 'trả lời',
    ' tao ':' tôi ',' mày ':' bạn ',' đk ':' được ',' ss ':' samsung ',' ip ':' iphone ',' ip12 ':' iphone 12 ',
    ' ip11 ':' iphone 11 ',' ipx ':' iphone x ',' ip8 ':' iphone 8 ',' ip7 ':' iphone 7 ',' ip6s ':' iphone 6s ',
    ' ip6 ':' iphone 6 ',' ip5 ':' iphone 5 ',' ip5s ':' iphone 5s ',' ip4 ':' iphone 4 ',' ip4s ':' iphone 4s '
}

def process_data(text):
    for i, j in replaces.items():
        text = text.replace(i,j)
    #text = re.sub(r'(.)\1+', r'\1', text)
    text = re.sub(r"\s+", " ", str(text))
    return text
    


def tokenizes(sentence):
    lm_tokenizer = dict_models.LongMatchingTokenizer()
    tokens = lm_tokenizer.tokenize(sentence)

    return tokens

# a = tokenizes("bên bạn")
# print(a)
def bag_of_words(tokenized_sentence, words):
    sentence_words = [word.lower() for word in tokenized_sentence]
    bag = np.zeros(len(words), dtype=np.float32)
    for idx, w in enumerate(words):
        if w in sentence_words: 
            bag[idx] = 1
    return bag
