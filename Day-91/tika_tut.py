
# import parser object from tike 
from tika import parser   
import tika
tika.initVM()
from tika import parser
  
# opening pdf file 
parsed_pdf = parser.from_file("Day-91\consumer kavita vs ida.docx") 
  
# saving content of pdf 
# you can also bring text only, by parsed_pdf['text']  
# parsed_pdf['content'] returns string  
data = parsed_pdf['content'] 
# Printing of content  
print(data)  
  
# # Gtts ##

from gtts import gTTS
tts = gTTS(data)  
tts.save('Day-91/hello.mp3')
