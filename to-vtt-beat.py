#!/usr/bin/env python
import csv
import io

def get_timing(row):
    yield row['time']

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

    print(s_p)
    print(e_p)

    ss = ":".join(s_p[0:3]) + "." + s_p[3] + "0"
    ee = ":".join(e_p[0:3]) + "." + e_p[3] + "0"

    print(ss)
    print(ee)

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

def beat(f):
    return parse_list(f, get_timing)

write_vtt("files/out/pulse.vtt", beat("files/kick.csv"))
write_vtt("files/out/beat.vtt", beat("files/snare.csv"))
