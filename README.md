This is a work-in-progress project. 

I've created the functionality to convert audios to text and they're splitted in two process:
1) Check if the extension of the file is ".wav". Because if isn't, a convertion to wav will be needed.
2) Convert the wav file to txt

Now I'm currently working on saving those file in different containers on the Storage Blob and after that I will create an endpoint to send an audio file to be converted to text, indexed by the Vector Database and then we're going to be able to query the content of the audio.

I will provide more info soon.
