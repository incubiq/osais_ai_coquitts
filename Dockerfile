##
##      To build the AI_COQUITTS docker image
##

FROM yeepeekoo/public:ai_coqui_


## keep ai in its directory
RUN mkdir -p ./ai
RUN chown -R root:root ./ai
COPY ./ai/datasets ./ai/datasets
COPY ./ai/recipes ./ai/recipes
COPY ./ai/TTS ./ai/TTS
COPY ./ai/runai.py ./ai/runai.py

# copy OSAIS mapping into AI
COPY ./coquitts.json .
COPY ./_coquitts.py .

# overload config with those default settings
ENV ENGINE=coquitts

# run as a server
CMD ["uvicorn", "main_fastapi:app", "--host", "0.0.0.0", "--port", "5502"]
