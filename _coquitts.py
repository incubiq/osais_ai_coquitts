
##
##      Entry of the AI_PING prog
##
##          - parse args
##          - do ping (ie nothing, only copy an image to prove full way round works)
##

from ai.runai import fnRun

##
##      ENTRY POINTS
##

## WARMUP Data
def getWarmupData(_id):
    try:
        import time
        from werkzeug.datastructures import MultiDict
        ts=int(time.time())
        sample_args = MultiDict([
            ('-u', 'test_user'),
            ('-uid', str(ts)),
            ('-t', _id),
            ('-cycle', '0'),
            ('-p', 'a test message'),
            ('-o', 'warmup.wav'),
            ('-filename', 'warmup.wav')
        ])
        return sample_args
    except:
        print("Could not call warm up!\r\n")
        return None

## Run Warmup
def runWarmup(_id, fn_osais_runWarmup): 
    _args=getWarmupData(_id)
    fn_osais_runWarmup(fnRun, _args)

## Run AI
def runAI(_args, fn_osais_runAI): 
    fn_osais_runAI(fnRun, _args)

