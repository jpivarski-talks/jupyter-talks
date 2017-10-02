#!/usr/bin/env python
import os, sys
import time

import ROOT
ROOT.PyConfig.IgnoreCommandLineOptions = True
from importlib import import_module
from PhysicsTools.NanoAODTools.postprocessing.framework.postprocessor import PostProcessor

from PhysicsTools.NanoAODTools.postprocessing.examples.mhtProducer import *
p=PostProcessor(".", ["/home/pivarski/storage/data/nano-TTLHE-2017-09-04-uncompressed.root"], "Jet_pt>150", "keep_and_drop.txt", [mht()], compression="ZLIB:0", friend=True)

startTime = time.time()
p.run()
print("time: {0}".format(time.time() - startTime))
