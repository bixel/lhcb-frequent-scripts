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

ntuple = DecayTreeTuple("TaggingTest")

descriptor_B = "[B0 -> ^(J/psi(1S) -> ^mu+ ^mu-) ^(K*(892)0 -> ^K+ ^pi-)]CC"

ntuple.Inputs = ['Dimuon/Phys/BetaSBd2JpsiKstarDetachedLine/Particles']
ntuple.Decay = descriptor_B
ntuple.addBranches({'B0': descriptor_B})
ntuple.ReFitPVs = True

ntuple.ToolList = [
    "TupleToolKinematic",
    "TupleToolPropertime",
    "TupleToolPrimaries",
    "TupleToolPid"
]

# Configure TupleToolTagging
tt_tagging = ntuple.addTupleTool("TupleToolTagging")
tt_tagging.UseFTfromDST = False
tt_tagging.OutputLevel = INFO
tt_tagging.Verbose = True
btag = tt_tagging.addTool(BTaggingTool, 'MyBTaggingTool')
applyTuning(btag, tuning_version="Summer2019Optimisation_v1_Run2")  # apply most recent tuning
#applyTuning(btag)   # apply default tuning
tt_tagging.TaggingToolName = btag.getFullName()
tt_tagging.AddTagPartsInfo = True

# DaVinci configuration
DaVinci().TupleFile = "DTT.root"
DaVinci().DataType = "2017"
DaVinci().Simulation = False
DaVinci().UserAlgorithms = [ ntuple ]

DaVinci().EvtMax = 50000 

MessageSvc().Format = "% F%60W%S%7W%R%T %0W%M"
