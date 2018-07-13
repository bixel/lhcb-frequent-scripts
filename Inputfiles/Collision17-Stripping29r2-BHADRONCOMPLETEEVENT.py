#-- GAUDI jobOptions generated on Wed Jul  4 10:02:11 2018
#-- Contains event types : 
#--   90000000 - 25 files - 1033859 events - 97.59 GBytes


#--  Extra information about the data processing phases:


#--  Processing Pass Step-133315 

#--  StepId : 133315 
#--  StepName : Stripping29r2-Merging-DV-v42r7p2-AppConfig-v3r353-LZMA4-Compression 
#--  ApplicationName : DaVinci 
#--  ApplicationVersion : v42r7p2 
#--  OptionFiles : $APPCONFIGOPTS/Merging/DV-Stripping-Merging.py;$APPCONFIGOPTS/Persistency/Compression-LZMA-4.py 
#--  DDDB : dddb-20170721-3 
#--  CONDDB : cond-20170724 
#--  ExtraPackages : AppConfig.v3r353;SQLDDDB.v7r10 
#--  Visible : N 

from Configurables import DaVinci, CondDB

DaVinci().DataType = '2017'
DaVinci().InputType = 'DST'
CondDB().Tags['DDDB'] = 'dddb-20170721-3'

from Gaudi.Configuration import * 
from GaudiConf import IOHelper
IOHelper('ROOT').inputFiles([
    'PFN:root://f01-081-129-e.gridka.de:1094/pnfs/gridka.de/lhcb/LHCb/Collision17/BHADRONCOMPLETEEVENT.DST/00071671/0000/00071671_00000361_1.bhadroncompleteevent.dst',
    'PFN:root://f01-081-129-e.gridka.de:1094/pnfs/gridka.de/lhcb/LHCb/Collision17/BHADRONCOMPLETEEVENT.DST/00071671/0000/00071671_00000377_1.bhadroncompleteevent.dst',
    'PFN:root://f01-080-123-e.gridka.de:1094/pnfs/gridka.de/lhcb/LHCb/Collision17/BHADRONCOMPLETEEVENT.DST/00071671/0000/00071671_00000390_1.bhadroncompleteevent.dst',
    'PFN:root://f01-080-123-e.gridka.de:1094/pnfs/gridka.de/lhcb/LHCb/Collision17/BHADRONCOMPLETEEVENT.DST/00071671/0000/00071671_00000401_1.bhadroncompleteevent.dst',
    'PFN:root://f01-081-129-e.gridka.de:1094/pnfs/gridka.de/lhcb/LHCb/Collision17/BHADRONCOMPLETEEVENT.DST/00071671/0000/00071671_00003360_1.bhadroncompleteevent.dst',
    'PFN:root://ccdcacli265.in2p3.fr:1094/pnfs/in2p3.fr/data/lhcb/LHCb/Collision17/BHADRONCOMPLETEEVENT.DST/00071671/0000/00071671_00001724_1.bhadroncompleteevent.dst',
    'PFN:root://ccdcacli264.in2p3.fr:1094/pnfs/in2p3.fr/data/lhcb/LHCb/Collision17/BHADRONCOMPLETEEVENT.DST/00071671/0000/00071671_00001850_1.bhadroncompleteevent.dst',
    'PFN:root://ccdcacli265.in2p3.fr:1094/pnfs/in2p3.fr/data/lhcb/LHCb/Collision17/BHADRONCOMPLETEEVENT.DST/00071671/0000/00071671_00003360_1.bhadroncompleteevent.dst',
    'PFN:root://bohr3226.tier2.hep.manchester.ac.uk:1094//dpm/tier2.hep.manchester.ac.uk/home/lhcb/lhcb/LHCb/Collision17/BHADRONCOMPLETEEVENT.DST/00071671/0000/00071671_00000232_1.bhadroncompleteevent.dst',
    'PFN:root://bohr3226.tier2.hep.manchester.ac.uk:1094//dpm/tier2.hep.manchester.ac.uk/home/lhcb/lhcb/LHCb/Collision17/BHADRONCOMPLETEEVENT.DST/00071671/0000/00071671_00000274_1.bhadroncompleteevent.dst',
    'PFN:root://bohr3226.tier2.hep.manchester.ac.uk:1094//dpm/tier2.hep.manchester.ac.uk/home/lhcb/lhcb/LHCb/Collision17/BHADRONCOMPLETEEVENT.DST/00071671/0000/00071671_00000292_1.bhadroncompleteevent.dst',
    'PFN:root://bohr3226.tier2.hep.manchester.ac.uk:1094//dpm/tier2.hep.manchester.ac.uk/home/lhcb/lhcb/LHCb/Collision17/BHADRONCOMPLETEEVENT.DST/00071671/0000/00071671_00000316_1.bhadroncompleteevent.dst',
    'PFN:root://bohr3226.tier2.hep.manchester.ac.uk:1094//dpm/tier2.hep.manchester.ac.uk/home/lhcb/lhcb/LHCb/Collision17/BHADRONCOMPLETEEVENT.DST/00071671/0000/00071671_00000336_1.bhadroncompleteevent.dst',
    'PFN:root://bohr3226.tier2.hep.manchester.ac.uk:1094//dpm/tier2.hep.manchester.ac.uk/home/lhcb/lhcb/LHCb/Collision17/BHADRONCOMPLETEEVENT.DST/00071671/0000/00071671_00000361_1.bhadroncompleteevent.dst',
    'PFN:root://bohr3226.tier2.hep.manchester.ac.uk:1094//dpm/tier2.hep.manchester.ac.uk/home/lhcb/lhcb/LHCb/Collision17/BHADRONCOMPLETEEVENT.DST/00071671/0000/00071671_00000401_1.bhadroncompleteevent.dst',
    'PFN:root://bohr3226.tier2.hep.manchester.ac.uk:1094//dpm/tier2.hep.manchester.ac.uk/home/lhcb/lhcb/LHCb/Collision17/BHADRONCOMPLETEEVENT.DST/00071671/0000/00071671_00001724_1.bhadroncompleteevent.dst',
    'PFN:root://gfe02.grid.hep.ph.ic.ac.uk:1094/pnfs/hep.ph.ic.ac.uk/data/lhcb/LHCb/Collision17/BHADRONCOMPLETEEVENT.DST/00071671/0000/00071671_00000377_1.bhadroncompleteevent.dst',
    'PFN:root://gfe02.grid.hep.ph.ic.ac.uk:1094/pnfs/hep.ph.ic.ac.uk/data/lhcb/LHCb/Collision17/BHADRONCOMPLETEEVENT.DST/00071671/0000/00071671_00001850_1.bhadroncompleteevent.dst',
], clear=True)
