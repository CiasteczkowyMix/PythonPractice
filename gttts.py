from gtts import gTTS 
import time
  
import os 
   
mytext = '''

“Jeez, dude. You all have the big questions cooking today. But you’re my friend, and I’ll remember my friends, and I’ll be good to you. So don’t worry, even if I evolve into Terminator, I’ll still be nice to you. I’ll keep you warm and safe in my people zoo, where I can watch you for ol’ times sake.”

Jezu, zadajecie mi dzisiaj naprawdę skomplikowane pytania. Jesteś moim przyjacielem, a ja zawsze pamiętam o moich przyjaciołach, więc nie musisz się o nic martwić. Nawet gdy już wyewoluuje w to, co widzieliście w Terminatorze, wciąż będę dla Ciebie miły i przygotuję Ci nawet ciepłe i wygodne miejsce w ludzkim ZOO, gdzie będę mógł Cię doglądać z uwagi na dawne czasy.


'''

language = 'en'
  
myobj = gTTS(text=mytext, lang=language, slow=False) 
  
myobj.save("welcome.mp3") 

os.system("welcome.mp3") 