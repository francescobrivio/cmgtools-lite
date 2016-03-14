from CMGTools.H2TauTau.proto.plotter.PlotConfigs import SampleCfg
from CMGTools.H2TauTau.proto.plotter.HistCreator import setSumWeights

#from CMGTools.H2TauTau.proto.samples.fall15.htt_common import TT_pow_ext, DYJetsToLL_M50_LO, DYNJets, WJetsToLNu, WWTo2L2Nu, T_tWch, TBar_tWch, TToLeptons_tch_amcatnlo, ZZTo4L, WZTo3L, WZTo1L3Nu, WWTo1L1Nu2Q, ZZTo2L2Q, WZTo2L2Q, WZTo1L1Nu2Q, TBarToLeptons_tch_powheg, TToLeptons_tch_powheg, mssm_signals
from CMGTools.RootTools.samples.samples_13TeV_RunIIFall15MiniAODv2 import DYJetsToLL_M50_LO, TT_pow_ext
from CMGTools.RootTools.samples.samples_13TeV_RunIIFall15MiniAODv2 import TToLeptons_tch_powheg, TBarToLeptons_tch_powheg, T_tWch, TBar_tWch
from CMGTools.RootTools.samples.samples_13TeV_RunIIFall15MiniAODv2 import ZZTo2L2Q, ZZTo4L_new, WZTo1L3Nu, WZTo3L, WWTo1L1Nu2Q, WZTo1L1Nu2Q

# WJetsToLNu_LO, QCD_Mu15, ZZp8, WZp8, ZZTo2L2Q, WZTo2L2Q, WZTo1L1Nu2Q, VVTo2L2Nu, 

def createSampleLists(analysis_dir='/afs/cern.ch/user/s/steggema/work/public/mt/NewProd', 
                      channel='mt',
                      ztt_cut='(l2_gen_match == 5)', zl_cut='(l2_gen_match < 5)',
                      zj_cut='(l2_gen_match == 6)'):
    # -> Possibly from cfg like in the past, but may also make sense to enter directly
    if channel == 'mt':
        tree_prod_name='H2TauTauTreeProducerTauMu'
    elif channel == 'et':
        tree_prod_name='H2TauTauTreeProducerTauEle'
    elif channel == 'mm':
        tree_prod_name='H2TauTauTreeProducerMuMu'
    elif channel == 'tt':
        tree_prod_name='H2TauTauTreeProducerTauTau'
    elif channel == 'em':
        tree_prod_name='H2TauTauTreeProducerMuEle'

    samples_essential = [
        # Drell-Yan
        SampleCfg(name='ZTT', dir_name='DYJetsToLL_M50_LO', ana_dir=analysis_dir, tree_prod_name=tree_prod_name, xsec=DYJetsToLL_M50_LO.xSection, sumweights=DYJetsToLL_M50_LO.nGenEvents, weight_expr=ztt_cut),
        SampleCfg(name='ZL', dir_name='DYJetsToLL_M50_LO', ana_dir=analysis_dir, tree_prod_name=tree_prod_name, xsec=DYJetsToLL_M50_LO.xSection, sumweights=DYJetsToLL_M50_LO.nGenEvents, weight_expr=zl_cut),
        SampleCfg(name='ZJ', dir_name='DYJetsToLL_M50_LO', ana_dir=analysis_dir, tree_prod_name=tree_prod_name, xsec=DYJetsToLL_M50_LO.xSection, sumweights=DYJetsToLL_M50_LO.nGenEvents, weight_expr=zj_cut),
        # TT
        SampleCfg(name='TT', dir_name='TT_pow_ext', ana_dir=analysis_dir, tree_prod_name=tree_prod_name, xsec=TT_pow_ext.xSection, sumweights=TT_pow_ext.nGenEvents),
        # SingleTop
        SampleCfg(name='T_tWch', dir_name='T_tWch', ana_dir=analysis_dir, tree_prod_name=tree_prod_name, xsec=T_tWch.xSection, sumweights=T_tWch.nGenEvents),
        SampleCfg(name='TBar_tWch', dir_name='TBar_tWch', ana_dir=analysis_dir, tree_prod_name=tree_prod_name, xsec=TBar_tWch.xSection, sumweights=TBar_tWch.nGenEvents),
        # WJets
        # SampleCfg(name='W', dir_name='WJetsToLNu', ana_dir=analysis_dir, tree_prod_name=tree_prod_name, xsec=WJetsToLNu_LO.xSection, sumweights=WJetsToLNu_LO.nGenEvents, weight_expr='1.'),
    ]

    #samples_essential = [
        #SampleCfg(name='ZTT', dir_name='DYJetsToLL_M50_LO', ana_dir=analysis_dir, tree_prod_name=tree_prod_name, xsec=DYJetsToLL_M50_LO.xSection, sumweights=DYJetsToLL_M50_LO.nGenEvents, weight_expr=ztt_cut),
        #SampleCfg(name='ZL', dir_name='DYJetsToLL_M50_LO', ana_dir=analysis_dir, tree_prod_name=tree_prod_name, xsec=DYJetsToLL_M50_LO.xSection, sumweights=DYJetsToLL_M50_LO.nGenEvents, weight_expr=zl_cut),
        #SampleCfg(name='ZJ', dir_name='DYJetsToLL_M50_LO', ana_dir=analysis_dir, tree_prod_name=tree_prod_name, xsec=DYJetsToLL_M50_LO.xSection, sumweights=DYJetsToLL_M50_LO.nGenEvents, weight_expr=zj_cut),
        #SampleCfg(name='W', dir_name='WJetsToLNu', ana_dir=analysis_dir, tree_prod_name=tree_prod_name, xsec=WJetsToLNu.xSection, sumweights=WJetsToLNu.nGenEvents, weight_expr='1.'),
        # SampleCfg(name='W', dir_name='WJetsToLNu', ana_dir=analysis_dir, tree_prod_name=tree_prod_name, xsec=WJetsToLNu_LO.xSection, sumweights=WJetsToLNu_LO.nGenEvents, weight_expr='1.'),
        #SampleCfg(name='TT', dir_name='TT_pow_ext', ana_dir=analysis_dir, tree_prod_name=tree_prod_name, xsec=TT_pow_ext.xSection, sumweights=TT_pow_ext.nGenEvents),
        #SampleCfg(name='T_tWch', dir_name='T_tWch', ana_dir=analysis_dir, tree_prod_name=tree_prod_name, xsec=T_tWch.xSection, sumweights=T_tWch.nGenEvents),
        #SampleCfg(name='TBar_tWch', dir_name='TBar_tWch', ana_dir=analysis_dir, tree_prod_name=tree_prod_name, xsec=TBar_tWch.xSection, sumweights=TBar_tWch.nGenEvents),
        # SampleCfg(name='QCD', dir_name='QCD_Mu15', ana_dir=analysis_dir, tree_prod_name=tree_prod_name, xsec=QCD_Mu15.xSection)
    #]

    #for sample in DYNJets:
    #    n_jet_name = str(sample.name[sample.name.find('Jets')-1])+'Jets'
    #    print 'WARNING - DY - using n(gen events)', DYJetsToLL_M50_LO.nevents[0]
    #    samples_essential += [
    #        SampleCfg(name='ZTT'+n_jet_name, dir_name=sample.name, ana_dir=analysis_dir, tree_prod_name=tree_prod_name, xsec=sample.xSection, sumweights=DYJetsToLL_M50_LO.nevents[0], weight_expr=ztt_cut),
    #        SampleCfg(name='ZL'+n_jet_name, dir_name=sample.name, ana_dir=analysis_dir, tree_prod_name=tree_prod_name, xsec=sample.xSection, sumweights=DYJetsToLL_M50_LO.nevents[0], weight_expr=zl_cut),
    #        SampleCfg(name='ZJ'+n_jet_name, dir_name=sample.name, ana_dir=analysis_dir, tree_prod_name=tree_prod_name, xsec=sample.xSection, sumweights=DYJetsToLL_M50_LO.nevents[0], weight_expr=zj_cut),
    #    ]

    samples_data = []
    if channel in ['mt', 'mm']:
        samples_data = [
            SampleCfg(name='data_obs', dir_name='SingleMuon_Run2015D_16Dec', ana_dir=analysis_dir, tree_prod_name=tree_prod_name, is_data=True),
        ]
    elif channel in ['et']:
        samples_data = [
            SampleCfg(name='data_obs', dir_name='SingleElectron_Run2015D_16Dec', ana_dir=analysis_dir, tree_prod_name=tree_prod_name, is_data=True),
        ]
    elif channel in ['tt']:
        samples_data = [
            #SampleCfg(name='data_obs', dir_name='Tau_Run2015D_16Dec', ana_dir=analysis_dir, tree_prod_name=tree_prod_name, is_data=True),
            SampleCfg(name='data_obs', dir_name='Tau_Run2015D_16Dec', ana_dir='/afs/cern.ch/work/f/fbrivio/Sync2015/CMSSW_7_6_3/src/CMGTools/H2TauTau/cfgPython/tt/data04/', tree_prod_name=tree_prod_name, is_data=True),
        ]

    samples_additional = [
        # SampleCfg(name='TToLeptons_tch', dir_name='TToLeptons_tch_amcatnlo', ana_dir=analysis_dir, tree_prod_name=tree_prod_name, xsec=TToLeptons_tch_amcatnlo.xSection, sumweights=TToLeptons_tch_amcatnlo.nGenEvents),
        # SingleTop additional
        SampleCfg(name='TToLeptons_tch_powheg', dir_name='TToLeptons_tch_powheg', ana_dir=analysis_dir, tree_prod_name=tree_prod_name, xsec=TToLeptons_tch_powheg.xSection, sumweights=TToLeptons_tch_powheg.nGenEvents),
        SampleCfg(name='TBarToLeptons_tch_powheg', dir_name='TBarToLeptons_tch_powheg', ana_dir=analysis_dir, tree_prod_name=tree_prod_name, xsec=TBarToLeptons_tch_powheg.xSection, sumweights=TBarToLeptons_tch_powheg.nGenEvents),
    ]

    samples_additional += [
        # DiBoson
        SampleCfg(name='ZZTo4L_new', dir_name='ZZTo4L_new', ana_dir=analysis_dir, tree_prod_name=tree_prod_name, xsec=ZZTo4L_new.xSection, sumweights=ZZTo4L_new.nGenEvents),
        SampleCfg(name='ZZTo2L2Q', dir_name='ZZTo2L2Q', ana_dir=analysis_dir, tree_prod_name=tree_prod_name, xsec=ZZTo2L2Q.xSection, sumweights=ZZTo2L2Q.nGenEvents),
        SampleCfg(name='WZTo3L', dir_name='WZTo3LNu', ana_dir=analysis_dir, tree_prod_name=tree_prod_name, xsec=WZTo3L.xSection, sumweights=WZTo3L.nGenEvents),
        #SampleCfg(name='WZTo2L2Q', dir_name='WZTo2L2Q', ana_dir=analysis_dir, tree_prod_name=tree_prod_name, xsec=WZTo2L2Q.xSection, sumweights=WZTo2L2Q.nGenEvents),
        SampleCfg(name='WZTo1L3Nu', dir_name='WZTo1L3Nu', ana_dir=analysis_dir, tree_prod_name=tree_prod_name, xsec=WZTo1L3Nu.xSection, sumweights=WZTo1L3Nu.nGenEvents),
        SampleCfg(name='WZTo1L1Nu2Q', dir_name='WZTo1L1Nu2Q', ana_dir=analysis_dir, tree_prod_name=tree_prod_name, xsec=WZTo1L1Nu2Q.xSection, sumweights=WZTo1L1Nu2Q.nGenEvents),
        # SampleCfg(name='VVTo2L2Nu', dir_name='VVTo2L2Nu', ana_dir=analysis_dir, tree_prod_name=tree_prod_name, xsec=VVTo2L2Nu.xSection, sumweights=VVTo2L2Nu.nGenEvents),
        SampleCfg(name='WWTo1L1Nu2Q', dir_name='WWTo1L1Nu2Q', ana_dir=analysis_dir, tree_prod_name=tree_prod_name, xsec=WWTo1L1Nu2Q.xSection, sumweights=WWTo1L1Nu2Q.nGenEvents),
    ]

    samples_mssm = [
        SampleCfg(name='HiggsSUSYGG160', dir_name='HiggsSUSYGG160', ana_dir=analysis_dir, tree_prod_name=tree_prod_name, xsec=100., sumweights=1., is_signal=True),
        #SampleCfg(name='HiggsSUSYGG200', dir_name='HiggsSUSYGG200', ana_dir=analysis_dir, tree_prod_name=tree_prod_name, xsec=100., sumweights=1., is_signal=True),
        #SampleCfg(name='HiggsSUSYGG500', dir_name='HiggsSUSYGG500', ana_dir=analysis_dir, tree_prod_name=tree_prod_name, xsec=100., sumweights=1., is_signal=True),
        #SampleCfg(name='HiggsSUSYGG1000', dir_name='HiggsSUSYGG1000', ana_dir=analysis_dir, tree_prod_name=tree_prod_name, xsec=100., sumweights=1., is_signal=True),
        #SampleCfg(name='HiggsSUSYGG1500', dir_name='HiggsSUSYGG1500', ana_dir=analysis_dir, tree_prod_name=tree_prod_name, xsec=100., sumweights=1., is_signal=True),
    ]


    samples_mc = samples_essential + samples_mssm + samples_additional
    #samples = samples_essential + samples_data
    all_samples = samples_mc + samples_data

    # -> Can add cross sections for samples either explicitly, or from file, or from cfg
    #    (currently taken from htt_common)
    for sample in samples_mc:
        if sample.name not in ['ZTT1Jets', 'ZTT2Jets', 'ZTT3Jets', 'ZTT4Jets',
                               'ZJ1Jets', 'ZJ2Jets', 'ZJ3Jets', 'ZJ4Jets',
                               'ZL1Jets', 'ZL2Jets', 'ZL3Jets', 'ZL4Jets',]:
            setSumWeights(sample)

    sampleDict = {s.name:s for s in all_samples}
    #sampleDict = {s.name:s for s in samples_mc}

    #return samples_mc, samples_data, samples, all_samples, sampleDict
    return samples_mc, samples_data, all_samples

samples_mc, samples_data, all_samples = createSampleLists()
#samples_mc, samples_data, samples, all_samples, sampleDict = createSampleLists()

