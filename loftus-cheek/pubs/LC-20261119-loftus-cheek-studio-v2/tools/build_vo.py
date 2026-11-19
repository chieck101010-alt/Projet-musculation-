# Assemble la voix off : chaque réplique (découpée aux silences de la prise unique) est placée à sa seconde dans le film.
import subprocess, sys
src = sys.argv[1]; out = sys.argv[2]
# (début dans la prise, fin dans la prise, position dans le film) — prise Achird 19/11
SEGS = [(0.28,1.57,0.25),(2.41,3.66,2.8),(4.35,4.99,4.6),(5.23,6.02,5.45),(6.61,7.55,10.3),(8.09,9.80,10.65),
        (10.24,10.75,16.55),(11.31,11.95,18.15),(12.49,13.50,19.55),(14.03,15.14,20.45),(15.80,16.36,21.5),
        (16.85,18.33,22.3),(18.86,20.73,24.4),(21.15,22.05,25.95)]
parts=[]; labels=[]
for i,(a,b,t) in enumerate(SEGS):
    parts.append(f"[0:a]atrim={a-0.04:.3f}:{b+0.08:.3f},asetpts=PTS-STARTPTS,afade=t=in:d=0.02,afade=t=out:st={b-a+0.06:.3f}:d=0.06,adelay={int(t*1000)}|{int(t*1000)}[s{i}]")
    labels.append(f"[s{i}]")
fc=";".join(parts)+";"+"".join(labels)+f"amix=inputs={len(SEGS)}:normalize=0,apad=whole_dur=28,atrim=0:28,loudnorm=I=-16:TP=-1.5:LRA=11[out]"
subprocess.run(["ffmpeg","-v","error","-y","-i",src,"-filter_complex",fc,"-map","[out]","-ar","48000","-ac","2",out],check=True)
print("ok", out)
