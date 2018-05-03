def build_weights(channel, Type):

    common_weight = "*(1.0)"

    ##This is the section where you define the weights => one can make this auxilary, to build proper weights per channel
    if channel is 'signal':
        if Type is 'data':
            common_weight = "*(1.0)"
        else:
            common_weight = "*sf_pu*sf_tt*normalizedWeight*sf_lepID*sf_lepIso*sf_lepTrack*sf_ewkV*sf_metTrig"
                
    elif channel is 'Zmm':
        if Type is 'data':
            common_weight = "*(1.0)"
        else:
            common_weight = "*sf_pu*sf_tt*normalizedWeight*sf_lepID*sf_lepIso*sf_lepTrack*sf_ewkV*sf_metTrigZmm"
                
    elif channel is 'Wmn':
        if Type is 'data':
            common_weight = "*(1.0)"
        else:
            common_weight = "*sf_pu*sf_tt*normalizedWeight*sf_lepID*sf_lepIso*sf_lepTrack*sf_ewkV*sf_metTrig"                         
            
    elif channel is 'Wen':
        if Type is 'data':
            common_weight = "*(1.0)"
        else:
            common_weight = "*sf_pu*sf_tt*normalizedWeight*sf_lepID*sf_lepIso*sf_lepTrack*sf_ewkV*sf_eleTrig"
                
    elif channel is 'Zee':
        if Type is 'data':
            common_weight = "*(1.0)"                                
        else:
            common_weight = "*sf_pu*sf_tt*normalizedWeight*sf_lepID*sf_lepIso*sf_lepTrack*sf_ewkV*sf_eleTrig"

    return common_weight

def build_selection(selection):

    selections = ['signal','Zmm','Wmn','gjets','Zee','Wen']
    
    snippets = {
        
        'presel' :['jet1Pt>100 && fabs(jet1Eta)<2.4 && jet1IsTight==1 && nTau==0 && jetNMBtags==0',selections],

        #filters and triggers
        'metFilter' :[ 'metFilter==1',selections],

        'signal'             : ['pfmet>250   && dphipfmet>0.5 && nLooseLep==0    && nLoosePhoton==0 && fabs(calomet-pfmet)/pfmet<0.5','signal'], 
        'singlemuon'         : ['pfUWmag>250 && dphipfUW>0.5  && nLoosePhoton==0 && nLooseLep==1    && looseLep1IsTight==1 && abs(looseLep1PdgId)==13 && fabs(calomet-pfmet)/pfUWmag<0.5 && mT<160','Wmn'],
        'singleelectron'     : ['pfUWmag>250 && dphipfUW>0.5  && nLoosePhoton==0 && nLooseLep==1    && looseLep1IsTight==1 && abs(looseLep1PdgId)==11 && fabs(calomet-pfmet)/pfUWmag<0.5 && mT<160 && pfmet>50','Wen'],

        }
    
    selectionString = ''
    for cut in snippets:
        if selection in snippets[cut][1]: 
            selectionString += snippets[cut][0]+'&&'
            

    selectionString+=" 1.0"
    return selectionString


