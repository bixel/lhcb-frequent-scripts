from Configurables import DaVinci

from StrippingConf.Configuration import StrippingConf, StrippingStream
from StrippingSettings.Utils import strippingConfiguration
from StrippingArchive.Utils import buildStreams
from StrippingArchive import strippingArchive

from DSTWriters.Configuration import (SelDSTWriter,
                                      stripDSTStreamConf,
                                      stripDSTElements,
                                      )

myLine = 'StrippingBetaSBu2JpsiKDetachedLine'

stripping = 'Stripping29r2'
config = strippingConfiguration(stripping)
archive = strippingArchive(stripping)
streams = buildStreams(stripping=config, archive=archive)

# Select my line

MyStream = StrippingStream('MyStream')

for stream in streams:
    for line in stream.lines:
        if line.name() == myLine:
            MyStream.appendLines([line])

# Configure Stripping
from Configurables import ProcStatusCheck
filterBadEvents = ProcStatusCheck()

sc = StrippingConf(Streams=[MyStream],
                   MaxCandidates=2000,
                   AcceptBadEvents=False,
                   BadEventSelection=filterBadEvents,
                   HDRLocation='NonexistingPlaceholder',
                   )

#
# Configuration of SelDSTWriter
#
SelDSTWriterElements = {
        'default': stripDSTElements(),
        }


SelDSTWriterConf = {
        'default': stripDSTStreamConf(),
        }

dstWriter = SelDSTWriter("MyDSTWriter",
                         StreamConf=SelDSTWriterConf,
                         OutputFileSuffix='TAGGING',
                         SelectionSequences=sc.activeStreams())

# DaVinci Config
DaVinci().appendToMainSequence([
    sc.sequence(),
    dstWriter.sequence(),
    ])
