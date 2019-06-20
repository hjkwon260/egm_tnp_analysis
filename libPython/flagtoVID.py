def flagtoVID( flag ):
	vid_name = ''
	if flag == 'passingVeto94XV2':       		vid_name = 'cutBasedElectronID-Fall17-94X-V2-veto'
	if flag == 'passingLoose94XV2':      		vid_name = 'cutBasedElectronID-Fall17-94X-V2-loose'
	if flag == 'passingMedium94XV2':     		vid_name = 'cutBasedElectronID-Fall17-94X-V2-medium'
	if flag == 'passingTight94XV2':      		vid_name = 'cutBasedElectronID-Fall17-94X-V2-tight'
	if flag == 'passingMVA94Xwp80isoV2': 		vid_name = 'mvaEleID-Fall17-iso-V2-wp80'
	if flag == 'passingMVA94Xwp90isoV2': 		vid_name = 'mvaEleID-Fall17-iso-V2-wp90'
	if flag == 'passingMVA94Xwp80noisoV2':      vid_name = 'mvaEleID-Fall17-noIso-V2-wp80'												
	if flag == 'passingMVA94Xwp90noisoV2':      vid_name = 'mvaEleID-Fall17-noIso-V2-wp90'		

	if flag == 'passingVeto94X':       		    vid_name = 'cutBasedElectronID-Fall17-94X-V1-veto'
	if flag == 'passingLoose94X':      		    vid_name = 'cutBasedElectronID-Fall17-94X-V1-loose'
	if flag == 'passingMedium94X':     		    vid_name = 'cutBasedElectronID-Fall17-94X-V1-medium'
	if flag == 'passingTight94X':      		    vid_name = 'cutBasedElectronID-Fall17-94X-V1-tight'
	if flag == 'passingMVA94Xwp80iso': 		    vid_name = 'mvaEleID-Fall17-iso-V1-wp80'
	if flag == 'passingMVA94Xwp90iso': 		    vid_name = 'mvaEleID-Fall17-iso-V1-wp90'
	if flag == 'passingMVA94Xwp80noiso':        vid_name = 'mvaEleID-Fall17-noIso-V1-wp80'												
	if flag == 'passingMVA94Xwp90noiso':        vid_name = 'mvaEleID-Fall17-noIso-V1-wp90'	

	if flag == 'passingVeto80X':       		    vid_name = 'cutBasedElectronID-Summer16-80X-V1-veto'
	if flag == 'passingLoose80X':      		    vid_name = 'cutBasedElectronID-Summer16-80X-V1-loose'
	if flag == 'passingMedium80X':     		    vid_name = 'cutBasedElectronID-Summer16-80X-V1-medium'
	if flag == 'passingTight80X':      		    vid_name = 'cutBasedElectronID-Summer16-80X-V1-tight'
	if flag == 'passingMVA80Xwp80': 		    vid_name = 'mvaEleID-Spring16-GeneralPurpose-V1-wp80'
	if flag == 'passingMVA80Xwp90': 		    vid_name = 'mvaEleID-Spring16-GeneralPurpose-V1-wp90'									


	return vid_name