
##
##      COQUITTS AI
##

## https://github.com/coqui-ai/tts
## https://colab.research.google.com/drive/1NC4eQJFvVEqD8L4Rd8CVK25_Z-ypaBHD?usp=sharing#scrollTo=6LWsNd3_M3MP

import sys
sys.path.insert(0, './ai/TTS')
sys.path.insert(0, './ai')

import os
import argparse
import torch
import time
from TTS.api import TTS

MODEL_MULTILINGUAL="tts_models/multilingual/multi-dataset/your_tts"
mainTTS = TTS(model_name=MODEL_MULTILINGUAL, progress_bar=False, gpu=True)

# Running a multi-speaker and multi-lingual model
def _test(): 
    # List available 🐸TTS models and choose the first one
    model_name = TTS.list_models()[0]
    # Init TTS
    tts = TTS(model_name)

    # Run TTS
    fileDir = os.path.dirname(os.path.abspath(__file__))
    _inputDir=os.path.abspath(os.path.join(fileDir, '../_input')) 
    _inputFile=os.path.join(_inputDir, "eric.wav") 
    _outputDir=os.path.abspath(os.path.join(fileDir, '../_output')) 

    # ❗ Since this model is multi-speaker and multi-lingual, we must set the target speaker and the language
    wav = tts.tts("This is a test! This is also a test!!", speaker=tts.speakers[0], language=tts.languages[0])
    _outputFile=os.path.join(_outputDir, "output0.wav") 
    tts.tts_to_file(text="Hello world!", speaker=tts.speakers[0], language=tts.languages[0], file_path=_outputFile)

    # Running a single speaker model

    # Init TTS with the target model name
    #tts = TTS(model_name="tts_models/de/thorsten/tacotron2-DDC", progress_bar=False, gpu=False)
    #tts.tts_to_file(text="Ich bin eine Testnachricht.", file_path="output2.wav")

    # Example voice cloning with YourTTS in English, French and Portuguese

    #tts = TTS(model_name="tts_models/en/vctk/vits", progress_bar=False, gpu=True)

    tts = TTS(model_name="tts_models/multilingual/multi-dataset/your_tts", progress_bar=False, gpu=True)
    _outputFile=os.path.join(_outputDir, "output3.wav") 
    tts.tts_to_file("This is voice cloning.", speaker_wav=_inputFile, language="en", file_path=_outputFile)
    _outputFile=os.path.join(_outputDir, "output4.wav") 
    tts.tts_to_file("C'est le clonage de la voix.", speaker_wav=_inputFile, language="fr-fr", file_path=_outputFile)

    _outputFile=os.path.join(_outputDir, "output5.wav") 
    tts.tts_to_file("Frédéric, j'ai eu Marriotte au téléphone. Ils gardent l'argent!", 
                    speaker_wav=_inputFile, language="fr-fr", 
                    file_path=_outputFile, 
                    emotion="Happy",
                    speed=1.6)

    _outputFile=os.path.join(_outputDir, "output6.wav") 
    tts.tts_to_file("C'est le clonage de la voix.", speaker_wav=_inputFile, language="fr-fr", file_path=_outputFile, emotion="Happy", speed=0.9)


    # Example voice conversion converting speaker of the `source_wav` to the speaker of the `target_wav`
    # tts = TTS(model_name="voice_conversion_models/multilingual/vctk/freevc24", progress_bar=False, gpu=True)
    # _outputFile=os.path.join(_outputDir, "output7.wav") 
    #tts.voice_conversion_to_file(source_wav=_inputFile, target_wav="my/target.wav", file_path=_outputDir)

    # Example voice cloning by a single speaker TTS model combining with the voice conversion model. This way, you can
    # clone voices by using any model in 🐸TTS.

    # tts = TTS("tts_models/de/thorsten/tacotron2-DDC")
    # _outputFile=os.path.join(_outputDir, "output8.wav") 
    # tts.tts_with_vc_to_file("Wie sage ich auf Italienisch, dass ich dich liebe?", speaker_wav=_inputFile, file_path=_outputFile)

    # Example text to speech using [🐸Coqui Studio](https://coqui.ai) models.

    # You can use all of your available speakers in the studio.
    # [🐸Coqui Studio](https://coqui.ai) API token is required. You can get it from the [account page](https://coqui.ai/account).
    # You should set the `COQUI_STUDIO_TOKEN` environment variable to use the API token.

    # If you have a valid API token set you will see the studio speakers as separate models in the list.
    # The name format is coqui_studio/en/<studio_speaker_name>/coqui_studio
    models = TTS().list_models()
    # Init TTS with the target studio speaker
    # tts = TTS(model_name="coqui_studio/en/Torcull Diarmuid/coqui_studio", progress_bar=False, gpu=False)

    # Run TTS
    # _outputFile=os.path.join(_outputDir, "output9.wav") 
    # tts.tts_to_file(text="This is a test.", file_path=_outputDir)
    # Run TTS with emotion and speed control
    # _outputFile=os.path.join(_outputDir, "output10.wav") 
    # tts.tts_to_file(text="This is a test.", file_path=_outputDir, emotion="Happy", speed=1.5)


    #Example text to speech using **Fairseq models in ~1100 languages** 🤯.

    #For these models use the following name format: `tts_models/<lang-iso_code>/fairseq/vits`.
    #You can find the list of language ISO codes [here](https://dl.fbaipublicfiles.com/mms/tts/all-tts-languages.html) and learn about the Fairseq models [here](https://github.com/facebookresearch/fairseq/tree/main/examples/mms).

    # TTS with on the fly voice conversion
    api = TTS("tts_models/deu/fairseq/vits")
    _outputFile=os.path.join(_outputDir, "output11.wav") 
    api.tts_with_vc_to_file("Wie sage ich auf Italienisch, dass ich dich liebe?", speaker_wav=_inputFile, file_path=_outputFile)

def fnRun(_args): 
    # Create the parser
    vq_parser = argparse.ArgumentParser(description='Voice file generation with Coqui TTS')

    # OSAIS arguments
    vq_parser.add_argument("-odir", "--outdir", type=str, help="Output directory", default="../_output/", dest='outdir')
    vq_parser.add_argument("-idir", "--indir", type=str, help="input directory", default="../_input/", dest='indir')

    # Add the arguments
    vq_parser.add_argument("-filename","--voice", type=str, help="Input for voice cloning", default=None, dest='voice')
    vq_parser.add_argument("-p",    "--prompts", type=str, help="Text prompts", default=None, dest='prompts')
    vq_parser.add_argument("-intl",  "--intl", type=str, help="Language code", default="en", dest='intl')
    vq_parser.add_argument("-speed",  "--speed", type=float, help="Playback speed", default=1, dest='speed')
    vq_parser.add_argument("-model",  "--model", type=str, help="TTS model to use", default=MODEL_MULTILINGUAL, dest='model')
    vq_parser.add_argument("-o",    "--output", type=str, help="Output filename", default="output.wav", dest='output')


    # Execute the parse_args() method
    try:
        args = vq_parser.parse_args(_args)
        print(args)

        fileDir = os.path.dirname(os.path.abspath(__file__))
        _inputDir=os.path.abspath(os.path.join(fileDir, "../_input/")) 
        _outputDir=os.path.abspath(os.path.join(fileDir, "../_output/")) 

        if args.voice==None or args.voice=="null":
            mainTTS.tts_to_file(args.prompts, speaker=mainTTS.speakers[0], language=args.intl, file_path=os.path.join(_outputDir,args.output), speed=args.speed)
        else : 
            mainTTS.tts_to_file(args.prompts, speaker_wav=os.path.join(_inputDir, args.voice), language=args.intl, file_path=os.path.join(_outputDir,args.output), speed=args.speed)

    except Exception as err:
        print("\r\nCRITICAL ERROR!!!")
        raise err
