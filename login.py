
import customtkinter as ctk
import tkinter.messagebox as tkmb
import os
	
# Selecting GUI theme - dark, light , system (for system default)
ctk.set_appearance_mode("dark")

# Selecting color theme - blue, green, dark-blue
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.geometry("300x520")
app.title("Smart Notes Maker")

def login():

	username = "Geeks"
	#password = "12345"
	filename=user_entry.get()

	if os.path.exists(filename):

		new_window = ctk.CTkToplevel(app)

		new_window.title("Result")
		new_window.geometry("300x520")

		
		#print('hello')
		with open(filename,'r') as file:
    			text = file.read()
		original=len(text)
		import spacy 
		from spacy.lang.en.stop_words import STOP_WORDS 
		from string import punctuation

		stopwords = list(STOP_WORDS)
		stopwords

		nlp = spacy.load('en_core_web_sm')
		doc = nlp(text)

		tokens = [token.text for token in doc]
		punctuation = punctuation + '\n'
		
		word_freq = {}
		for word in doc:
		  if word.text.lower() not in stopwords:
		    if word.text.lower() not in punctuation:
		      if word.text not in word_freq.keys():
		        word_freq[word.text] = 1
		      else:
		        word_freq[word.text] = +1

		max_freq = max(word_freq.values())
		for word in word_freq.keys():
  			word_freq[word] = word_freq[word]/max_freq

		sen_token = [sent for sent in doc.sents]

		sen_score = {}
		for sent in sen_token:
		  for word in sent:
		    if word.text.lower() in word_freq.keys():
		      if sent not in sen_score.keys():
		        sen_score[sent] = word_freq[word.text.lower()]
		      else:
		        sen_score[sent] += word_freq[word.text.lower()]

		from heapq import nlargest
		select_length = int(len(sen_token)* 0.3)

		summary = nlargest(select_length, sen_score, key = sen_score.get)
		final_summary = [word.text for word in summary]

		summary = ' '.join(final_summary)

		newfilename=filename+"new"
		file = open(newfilename, "w")
		file.write(summary)
		file.close()
		inlength=original
		outlength=len(summary)
		print(inlength,outlength)
		#newfilename="abc"+"x"
		ctk.CTkLabel(new_window,text="Your Summarized file is saved into same directory").pack() 

		label1 = ctk.CTkLabel(new_window,text=' ')
		label1.pack(pady=2,padx=4)
		label1 = ctk.CTkLabel(new_window,text='Name of Old File')
		label1.pack(pady=2,padx=4)
		label1 = ctk.CTkLabel(new_window,text=filename)
		label1.pack(pady=2,padx=4)		
		label1 = ctk.CTkLabel(new_window,text='')
		label1.pack(pady=2,padx=4)
		label1 = ctk.CTkLabel(new_window,text='Name of New File')
		label1.pack(pady=2,padx=4)
		label1 = ctk.CTkLabel(new_window,text=newfilename+".txt")
		label1.pack(pady=2,padx=4)
		label1 = ctk.CTkLabel(new_window,text='')
		label1.pack(pady=2,padx=4)
		label1 = ctk.CTkLabel(new_window,text='Length of Original File')
		label1.pack(pady=2,padx=4)
		label1 = ctk.CTkLabel(new_window,text=inlength)
		label1.pack(pady=2,padx=4)
		label1 = ctk.CTkLabel(new_window,text='')
		label1.pack(pady=2,padx=4)
		label1 = ctk.CTkLabel(new_window,text='Length of New File')
		label1.pack(pady=2,padx=4)
		label1 = ctk.CTkLabel(new_window,text=outlength)
		label1.pack(pady=2,padx=4)
		label1 = ctk.CTkLabel(new_window,text='')
		label1.pack(pady=2,padx=4)
		button = ctk.CTkButton(new_window,text='ThankYou!')
		button.pack(pady=12,padx=10)

	else:
		tkmb.showerror(title="Login Failed",message="Invalid FileName")

label = ctk.CTkLabel(app,text="SMART NOTES MAKER")
	
label.pack(pady=20)


frame = ctk.CTkFrame(master=app)
frame.pack(pady=20,padx=40,fill='both',expand=True)

label = ctk.CTkLabel(master=frame,text='1. Enter File Name')
label.pack(pady=10,padx=10)
label = ctk.CTkLabel(master=frame,text='2. Click on Submit')
label.pack(pady=10,padx=10)
label = ctk.CTkLabel(master=frame,text='3. Summarized File')
label.pack(pady=10,padx=10)
label = ctk.CTkLabel(master=frame,text='')
label.pack(pady=10,padx=10)

user_entry= ctk.CTkEntry(master=frame,placeholder_text="File Name with .txt")
user_entry.pack(pady=12,padx=10)
button = ctk.CTkButton(master=frame,text='Submit',command=login)
button.pack(pady=12,padx=10)

app.mainloop()
