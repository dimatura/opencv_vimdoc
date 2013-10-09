
import path
import re
import collections
import pprint

tags_fnames = collections.defaultdict(lambda: list())
p = path.path('.')
for f in p.files('*.txt'):
    lines = f.lines()
    for ix,ln in enumerate(lines):
        #match = re.search('p(\d+)_t(\d+)_r(\d+)', line)
        matches = re.findall('\*([:\_\-\w]+)\*', ln)
        for match in matches:
            #print match.group(1)
            #tags_fnames[match.group(1)].append(str(f))
            tags_fnames[match].append([f, ix+1])

tags_fnames = dict(tags_fnames)
#pprint.pprint(tags_fnames)
dupe_tags_fnames = {}
for k,v in tags_fnames.items():
    if len(v) > 1:
        dupe_tags_fnames[k] = v

"""
# just process opencv ones
for k,v in dupe_tags_fnames.items():
    # to delete
    #if len(v)==2:
        #ix1, ix2 = v[0][1], v[1][1]
        #fname1, fname2 = v[0][0], v[1][0]
        #if ix2-ix1==3 and fname1==fname2:
            #fnametmp = fname1+'.2'
            #lines = fname1.lines()
            ##print lines[ix2-1], lines[ix1-1]
            #lines[ix2-1] = '\n'
            #with open(fnametmp, 'w') as f:
                #f.writelines(lines)
            #fnametmp.rename(fname1)

    # to show
    #for fname, ln_ix in v:
        #if not fname.basename().startswith('cv-'): continue
        #lines = fname.lines()
        #ln = lines[ln_ix-1]
        #print ln.strip(), fname, ln_ix
"""

#pprint.pprint(dupe_tags_fnames)
for k,v in dupe_tags_fnames.items():
    if v[0][0].basename().startswith('csound'):
        print k, v
