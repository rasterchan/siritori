import sys
import tkinter as tk

#==
# tkinter設定
#==
root = tk.Tk()
root.title('しりとりをしよう')
root.geometry("600x600")

label = tk.Label(root, text="ぼくとしりとりをしよう。つぎのもじをにゅうりょくしてね。", bg='pink', fg='brown')
label.place(x=50,y=10)
label.pack

#now_word = tk.Label(root, text="いまのもじは+word+")
In_word = tk.Entry(root,width=50)
In_word.place(x=50,y=40)
word_list=[]

#==
#コンピューターの初期ワードリスト
#==
com_list = ['あいすくりーむ','いちご','えのぐ','おにぎり',\
    'かき','きつね','くりーむ','けむし','こま','さとう','しいたけ','すし',\
    'たい','ちーず','つみき','てがみ','とまと','なす','にわとり','ねこ','のり',\
    ]

def answer():
    for words in com_list:
        if word_list[-1][-1] == words[0]:
            print(word_list)
            word_list.append(words)
            label['text'] = 'ぼくのこたえは、　' +words+ '　。きみのばんだよ'
            print(word_list)
        

def check1():
    Get_word = In_word.get()
    if Get_word != '':
        word = str(Get_word)
        return word
    else:
        label['text'] = 'もじがにゅうりょくされていないよ'
        raise ValueError('文字入力なし')
 
def check2(strj):
    """
    check2: 入力がひらがなかカタカナのいずれかであるかを判定する関数
    """
    hiragana = "ぁあぃいぅうぇえぉおかがきぎくぐけげこごさざし\
        じすずせぜそぞただちぢっつづてでとどなにぬねのはばぱひびぴふぶ\
        ぷへべぺほぼぽまみむめもゃやゅゆょよらりるれろゎわゐゑをん"
    katakana = "ァアィイゥウェエォオカガキギクグケゲコゴサザシジ\
        スズセゼソゾタダチヂッツヅテデトドナニヌネノハバパヒビピフ\
        ブプヘベペホボポマミムメモャヤュユョヨラリルレロヮワヰヱヲンヴ"
    return all([chr in hiragana or chr in katakana for chr in strj])

def main(word):
    """
    しりとりに合う文字列かどうかの判定
    - check1: 入力が空白ではないか関数
    - check2: 入力がひらがなかカタカナのいずれかであるかを判定する関数
    """
    word=check1()
    if check2(word):
        #最初のワードの場合
        if word_list==[]:
            word_list.append(word)
        #最初の文字とリストの最後の文字が一致する場合
        elif word[0] == word_list[-1][-1]:
            for words in word_list:
                if words == word:
                    label["text"] = "重複するワードがあります"
                    raise ValueError("重複ワードあり")
            word_list.append(word)
        else:
            label["text"] = "入力された文字が正しくありません"
            raise ValueError("不正文字入力")
        print(word_list)
        answer()

Button = tk.Button(root, text='しりとり')
Button.bind("<Button-1>", main)
Button.place(x=50,y=100)

root.mainloop()