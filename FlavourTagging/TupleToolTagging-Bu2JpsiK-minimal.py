from Configurables import (DecayTreeTuple,
                           DaVinci,
                           TrackScaleState,
                           CondDB,
                           TaggerMuonTool,
                           CallgrindProfile,
                           BTaggingTool,
                           MessageSvc,
                           )
from Gaudi.Configuration import INFO, DEBUG, WARNING

from DecayTreeTuple.Configuration import *

from FlavourTagging.Tunings import applyTuning

tuple = DecayTreeTuple("TaggingTest")

descriptor_B = "[B+ -> ^(J/psi(1S) -> ^mu+ ^mu-) ^K+]CC"

tuple.Inputs = ['Dimuon/Phys/BetaSBu2JpsiKDetachedLine/Particles']
tuple.Decay = descriptor_B
tuple.addBranches({'Bu': descriptor_B})
tuple.ReFitPVs = True

tuple.ToolList = [
        "TupleToolKinematic",
        "TupleToolPropertime",
        "TupleToolPrimaries",
        "TupleToolPid"
        ]

# Configure TupleToolTagging
tt_tagging = tuple.addTupleTool("TupleToolTagging")
tt_tagging.UseFTfromDST = False
tt_tagging.OutputLevel = INFO
tt_tagging.Verbose = True
btag = tt_tagging.addTool(BTaggingTool, 'MyBTaggingTool')
applyTuning(btag)  # apply default tuning
tt_tagging.TaggingToolName = btag.getFullName()


# DaVinci configuration
DaVinci().TupleFile = "DTT.root"
DaVinci().Simulation = False
DaVinci().UserAlgorithms = [
        tuple,
        ]

DaVinci().EvtMax = 10000

MessageSvc().Format = "% F%60W%S%7W%R%T %0W%M"
