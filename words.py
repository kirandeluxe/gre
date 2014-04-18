'''
Created on Apr 17, 2014

@author: kiran
'''

from os  import listdir

from collections import defaultdict
import re
import Tkinter

d = {}
r = defaultdict(list)

def scan():
    for fileName in listdir("./files"):
        for line in open('./files/' + fileName).readlines():
            m = re.search(r'\s', line)
            if(m == None):
                continue
            word = line[0:m.start(0)]
            meaning = line[len(word) + 1:-1].lower()
            d[word] = meaning
            meaning = re.sub(r'[\\/,\.\(\);]', ' ', meaning)
            tokens = [ x for x in meaning.split(' ')
                       if not x in set(['to', ''
                       , 'the'
                       , 'in'
                       , 'and'
                       , 'or'
                       , 'to'
                       , 'a'
                       , 'of'
                       , 'that'
                       , 'by'
                       , 'for'
                       , 'where'
                       , 'with'
                       , 'is'
                       , 'are'
                       , 'etc'
                       , 'as'
                       , 'were'
                       , 'was'
                       , 'would'
                       , 'should'
                       , 'eg'
                       ])
                      ]
            for token in tokens:
                (r[token]).append(word)
            pass
    
    
    
def test():
    print ' '.join(r['use'])
    

def gui():
    top = Tkinter.Tk()
    
    top.geometry('500x600')
    
    label = Tkinter.Label(top, text="Enter Text and press enter")
    label.pack(side=Tkinter.TOP, fill=Tkinter.X)
    
    frame = Tkinter.Frame(top)
    
    scroll = Tkinter.Scrollbar(frame)
    scroll.pack(side=Tkinter.RIGHT, fill=Tkinter.Y, expand=Tkinter.YES)
    listbox = Tkinter.Listbox(frame, height=31, width=80, yscrollcommand=scroll.set)
    listbox.pack(side=Tkinter.RIGHT, fill=Tkinter.BOTH, expand=Tkinter.YES)
    scroll.config(command=listbox.yview)
    
    frame.pack(side=Tkinter.TOP, fill=Tkinter.BOTH, expand=Tkinter.YES)
    
    
    text = Tkinter.Entry(top, name="text1")
    text.bind('<Return>', lambda e: fill(text, listbox))
    text.pack(side=Tkinter.TOP, fill=Tkinter.BOTH)
    
    Tkinter.mainloop()
  
  
def fill(textInput, listBox):
    listBox.delete(0, Tkinter.END)
    text = textInput.get().lower()
    words = set()
    for word in re.split(r'\s', text):
        words = words.union(set(r[word]))
    
    for word in words:
        listBox.insert(Tkinter.END, word + " : " + d[word])
    
   

if __name__ == '__main__':
    scan()
    gui()
