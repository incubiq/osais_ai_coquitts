##
##      To build the AI_COQUITTS docker image
##

FROM yeepeekoo/public:ai_coqui_


## keep ai in its directory
RUN mkdir -p ./ai
RUN chown -R root:root ./ai

# copy only the models we use...
RUN mkdir -p ./ai/datasets
COPY ./ai/datasets/tts_models--multilingual--multi-dataset--your_tts ./ai/datasets/tts_models--multilingual--multi-dataset--your_tts

COPY ./ai/recipes ./ai/recipes
COPY ./ai/TTS ./ai/TTS
COPY ./ai/runai.py ./ai/runai.py

# push again the base files
COPY ./_temp/main_fastapi.py .
COPY ./_temp/main_flask.py .
COPY ./_temp/main_common.py .
COPY ./_temp/osais_debug.py .
COPY ./_temp/osais.json .

# copy AI specifics
COPY ./coquitts.json .
COPY ./_coquitts.py .
COPY ./_input/warmup.wav ./_input/warmup.wav

# overload config with those default settings
ENV ENGINE=coquitts

# run as a server
CMD ["uvicorn", "main_fastapi:app", "--host", "0.0.0.0", "--port", "5502"]
