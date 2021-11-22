This is the FAST API Demo Project I created one afternoon.

It's Pretty great and really simple to use. 

To get started download the project then run a couple of commands. 

First lets install all the needed requirements using pip (or pip3) and the requirements.txt file. This will download everything that is needed to run this project.

```bash
pip install -r requirements.txt
```

After all the libraries have been installed.

Next Run the start server call.

```bash
uvicorn demo_fast_api:app --reload
```

```bash
INFO:     Will watch for changes in these directories: ['{path-to-python-based-prjects}/FastApiDemo']
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)  
INFO:     Started reloader process [31587] using statreload
INFO:     Started server process [31589]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

Now is it Running locally at the link above 
http://127.0.0.1:8000 just click the link, and you will see

### DONE.  
<img src="https://github.com/adfleshner/FastApiDemo/blob/master/images/you_did_a_thing.png"
	 style="object-fit:cover;
            width:578px;
            height:332px;
            border: solid 1px #CCC"/>

Cool You have it running.

### Next Steps
If you have Postman install open it. if you don't you can download it here. <a href="https://www.postman.com/downloads/">PostMan Download</a>

After you have downloaded and opened postman. Go to File > Import > and find calls.json in the postman folder inside of this project.

This will give you the 4 commands that I added to this project.

### Swagger
So one of the best parts about FastApi is that it supports swagger out of the box.

Simply go to http://127.0.0.1:8000/docs to see the swagger docs.
