#    Copyright 2018, by Andreas Brandner

#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at

#    http://www.apache.org/licenses/LICENSE-2.0

#    Unless required by applicdemoable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.

import subprocess

class SyntaxNetElement:
    def __init__(self, id, form, upos, xpos, lemma="", feats="", head="", deprel="", deps="", misc=""):
        self.id = id
        self.form = form
        self.lemma = lemma
        self.upos = upos
        self.xpos = xpos
        self.feats = feats
        self.head = head
        self.deprel = deprel
        self.deps = deps
        self.misc = misc

    def pos_tags(self):
        print "Form: " +self.form+ " UPOS Tag: " +self.upos+ " XPOS Tag: " +self.xpos


sentence = "I'm sorry Dave, I'm afraid I can't do that"
result = subprocess.Popen(["echo \"" + sentence + "\" | ./demo-conll.sh 2>/dev/null"], shell=True, stdout=subprocess.PIPE).stdout.read()
lines = [line.replace("\t", " ") for line in result.splitlines()]
tokens = []

for line in lines:
    annos = line.split(" ")
    if(len(annos) > 1):
        tokens.append(SyntaxNetElement(annos[0], annos[1], annos[3], annos[4], annos[2], annos[5], annos[6], annos[7], annos[8], annos[9]))

for token in tokens:
    token.pos_tags()
