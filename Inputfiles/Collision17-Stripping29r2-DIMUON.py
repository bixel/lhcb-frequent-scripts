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
    'PFN:root://eoslhcb.cern.ch//eos/lhcb/grid/prod/lhcb/LHCb/Collision17/DIMUON.DST/00071700/0000/00071700_00000046_1.dimuon.dst',
    'PFN:root://eoslhcb.cern.ch//eos/lhcb/grid/prod/lhcb/LHCb/Collision17/DIMUON.DST/00071700/0000/00071700_00000080_1.dimuon.dst',
    'PFN:root://eoslhcb.cern.ch//eos/lhcb/grid/prod/lhcb/LHCb/Collision17/DIMUON.DST/00071700/0000/00071700_00000130_1.dimuon.dst',
    'PFN:root://eoslhcb.cern.ch//eos/lhcb/grid/prod/lhcb/LHCb/Collision17/DIMUON.DST/00071700/0000/00071700_00000462_1.dimuon.dst',
    'PFN:root://eoslhcb.cern.ch//eos/lhcb/grid/prod/lhcb/LHCb/Collision17/DIMUON.DST/00071700/0000/00071700_00000546_1.dimuon.dst',
    'PFN:root://eoslhcb.cern.ch//eos/lhcb/grid/prod/lhcb/LHCb/Collision17/DIMUON.DST/00071700/0000/00071700_00000707_1.dimuon.dst',
    'PFN:root://eoslhcb.cern.ch//eos/lhcb/grid/prod/lhcb/LHCb/Collision17/DIMUON.DST/00071700/0000/00071700_00000893_1.dimuon.dst',
    'PFN:root://eoslhcb.cern.ch//eos/lhcb/grid/prod/lhcb/LHCb/Collision17/DIMUON.DST/00071700/0000/00071700_00000969_1.dimuon.dst',
    'PFN:root://eoslhcb.cern.ch//eos/lhcb/grid/prod/lhcb/LHCb/Collision17/DIMUON.DST/00071700/0000/00071700_00001115_1.dimuon.dst',
    'PFN:root://eoslhcb.cern.ch//eos/lhcb/grid/prod/lhcb/LHCb/Collision17/DIMUON.DST/00071700/0000/00071700_00001238_1.dimuon.dst',
], clear=True)
