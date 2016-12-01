#!/usr/bin/env python
import csv
import io

def get_cast(row):
    cast = { 0: "all", 1: "singer", 2: "bass", 3: "drums" }
    cs   = ( row['cast_all'], row['cast_singer'], row['cast_bass'], row['cast_drumms'] )

    for idx, val in enumerate(cs):
        if('X' == val):
            yield cast[idx]
            break
        elif(3 == idx):
            yield "none"

def get_framing(row):
    yield row['framing']

def get_styling(row):

    rid = row['styling']

    if(rid == ""):
        yield "none"
    else:
        yield rid

def cons_line(d):
    return "    " + '"id": ' + '"' + d + '"' + "\n"

def make_obj(d):
    s = "{" + "\n"

    for l in d:
        s += cons_line(l)

    s += "}" + "\n"

    return s

def make_cue(s, e, obj):
    s_p = s.split(':')
    e_p = e.split(':')

    ss = ":".join(s_p[0:3]) + "." + s_p[3] + "0"
    ee = ":".join(e_p[0:3]) + "." + e_p[3] + "0"

    cue  = "cue\n"
    cue +=  ss + ' --> ' + ee + '\n'
    cue += obj

    return cue

def parse_csv(fn, f):
    with open(fn, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            obj = make_obj(f( row ))
            yield make_cue(row['time_in'], row['time_out'], obj)

def write_vtt(fn, ls):
    with io.open(fn, 'wb') as f:
        f.write("WEBVTT\n\n")

        for l in ls:
            f.write(l + "\n")

def cast():
    return parse_csv('files/framing_cast_styling.csv', get_cast)

def framing():
    return parse_csv('files/framing_cast_styling.csv', get_framing)

def styling():
    return parse_csv('files/framing_cast_styling.csv', get_styling)

write_vtt("files/out/cast.vtt", cast())
write_vtt("files/out/editing.vtt", framing())
write_vtt("files/out/styling.vtt", styling())
