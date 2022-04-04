import requests
hosts = ["www.telkom.co.za","1telkomqa.telkom.co.za","BLV2-FW-PST-WBU29-00.telkom.co.za","www.BLV2-FW-PST-WBU29-00.telkom.co.za","BLV2-FW-SRA-NJ04-00.telkom.co.za","www.BLV2-FW-SRA-NJ04-00.telkom.co.za","CNTRRA02UCEWE01.telkom.co.za","www.CNTRRA02UCEWE01.telkom.co.za","Clevva.telkom.co.za","www.Clevva.telkom.co.za","Connect.telkom.co.za","www.Connect.telkom.co.za","NBSC-FW-SRA-X83-00.telkom.co.za","www.NBSC-FW-SRA-X83-00.telkom.co.za","anniversary.telkom.co.za","www.anniversary.telkom.co.za","api.telkom.co.za","www.api.telkom.co.za","apitest.telkom.co.za","www.apitest.telkom.co.za","apitesttrx.telkom.co.za","www.apitesttrx.telkom.co.za","apitesttrx2.telkom.co.za","www.apitesttrx2.telkom.co.za","apitesttrx3.telkom.co.za","www.apitesttrx3.telkom.co.za","apitrx.telkom.co.za","www.apitrx.telkom.co.za","apitrx2.telkom.co.za","www.apitrx2.telkom.co.za","apitrx3.telkom.co.za","www.apitrx3.telkom.co.za","appdc.telkom.co.za","appdeumfe.telkom.co.za","apps.telkom.co.za","www.apps.telkom.co.za","aslut.telkom.co.za","asmcc.telkom.co.za","autodiscover.telkom.co.za","bcx-telkom.telkom.co.za","www.bcx-telkom.telkom.co.za","bcxad.telkom.co.za","bdrl-eam-papp1.telkom.co.za","www.bdrl-eam-papp1.telkom.co.za","bdrl-eam-papp2.telkom.co.za","www.bdrl-eam-papp2.telkom.co.za","beta-login.telkom.co.za","bim.telkom.co.za","www.bim.telkom.co.za","birthday.telkom.co.za","www.birthday.telkom.co.za","blvmail.telkom.co.za","booking.telkom.co.za","www.booking.telkom.co.za","bookings.telkom.co.za","www.bookings.telkom.co.za","bsd.telkom.co.za","www.bsd.telkom.co.za","business.telkom.co.za","campaigns.telkom.co.za","mail10165.campaigns.telkom.co.za","cas.telkom.co.za","cdih-ep-owsm01.telkom.co.za","www.cdih-ep-owsm01.telkom.co.za","cdih-ep-owsm02.telkom.co.za","www.cdih-ep-owsm02.telkom.co.za","cdihtbs.telkom.co.za","cdlh-ep-app11.telkom.co.za","cdlh-ep-app12.telkom.co.za","cdlh-ep-login03.telkom.co.za","cdlh-ep-login04.telkom.co.za","cdlh-ep-mail01.telkom.co.za","cdlh-ep-mail02.telkom.co.za","cdlh-ep-oif01.telkom.co.za","cdlh-ep-oif02.telkom.co.za","cdlh-ep-search01.telkom.co.za","cdlh-ep-search02.telkom.co.za","cdlh-ep-spwebcache01.telkom.co.za","cdlh-ep-ssoadmin02.telkom.co.za","cdrl-eai-papp1.telkom.co.za","www.cdrl-eai-papp1.telkom.co.za","cdrl-eai-tapp2.telkom.co.za","www.cdrl-eai-tapp2.telkom.co.za","cdsh-ep-admin01.telkom.co.za","cdsh-ep-admin02.telkom.co.za","cdsh-ep-app01.telkom.co.za","cdsh-ep-app02.telkom.co.za","cdsh-ep-app03.telkom.co.za","cdsh-ep-app04.telkom.co.za","cdsh-ep-app05.telkom.co.za","cdsh-ep-app06.telkom.co.za","cdsh-ep-app07.telkom.co.za","cdsh-ep-app09.telkom.co.za","cdsh-ep-app10.telkom.co.za","cdsh-ep-brandlbr.telkom.co.za","cdsh-ep-content01.telkom.co.za","cdsh-ep-content02.telkom.co.za","cdsh-ep-portal01.telkom.co.za","cdsh-ep-portal02.telkom.co.za","cdsh-ep-report01.telkom.co.za","cdsh-ep-report02.telkom.co.za","cdsh-ep-satelitte01.telkom.co.za","cdsh-ep-satelitte02.telkom.co.za","cgate.telkom.co.za","www.cgate.telkom.co.za","cgate03.telkom.co.za","cgate04.telkom.co.za","cgate05.telkom.co.za","cgate06.telkom.co.za","cgate07.telkom.co.za","cgate08.telkom.co.za","chat.telkom.co.za","cixidev.telkom.co.za","www.cixidev.telkom.co.za","cixiprod.telkom.co.za","www.cixiprod.telkom.co.za","cixiqa.telkom.co.za","www.cixiqa.telkom.co.za","cmsweb.telkom.co.za","cnc2105.telkom.co.za","cntrra02-iishfm.telkom.co.za","cntrra20-cas00.telkom.co.za","cntrra20-cas01.telkom.co.za","cntrra20-dns00.telkom.co.za","cntrra20-dns01.telkom.co.za","cntrra20-esa00.telkom.co.za","cntrra20-esa01.telkom.co.za","cntrra20-esa02.telkom.co.za","cntrra20-esa03.telkom.co.za","cntrra20-gtw03.telkom.co.za","cntrra20-gtw04.telkom.co.za","cntrra20-iport-esa-mgt-02.telkom.co.za","cntrra20-mrk-esa00.telkom.co.za","cntrra20-mrk-esa01.telkom.co.za","cntrra20-mrk-esa02.telkom.co.za","cntrra20-mrk-esa03.telkom.co.za","cntrra20-sql05.telkom.co.za","cntrra20-xaswi1.telkom.co.za","collab-edge.telkom.co.za","community.telkom.co.za","community-stage.telkom.co.za","corporate.telkom.co.za","cres.telkom.co.za","ctx.telkom.co.za","www.ctx.telkom.co.za","dappdeumfe.telkom.co.za","dealerapp.telkom.co.za","deals.telkom.co.za","wctb-dsl-dns1.dsl.telkom.co.za","e2k.telkom.co.za","eascntr.telkom.co.za","eastygr.telkom.co.za","ebilling.telkom.co.za","ebpp.telkom.co.za","www.ebpp.telkom.co.za","eb.ebpp.telkom.co.za","www.eb.ebpp.telkom.co.za","ebppeb.telkom.co.za","ebppob.telkom.co.za","www.ebppob.telkom.co.za","ecdev01openserve.telkom.co.za","www.ecdev01openserve.telkom.co.za","connect.ecdev01openserve.telkom.co.za","www.connect.ecdev01openserve.telkom.co.za","webreach.ecdev01openserve.telkom.co.za","www.webreach.ecdev01openserve.telkom.co.za","ecdev03.telkom.co.za","ecdev03apps.telkom.co.za","ecdev03login.telkom.co.za","ecdev3.telkom.co.za","ecdev5.telkom.co.za","eis.telkom.co.za","eis11.telkom.co.za","eis12.telkom.co.za","eis13.telkom.co.za","www.eis13.telkom.co.za","eis21.telkom.co.za","eis22.telkom.co.za","eis23.telkom.co.za","www.eis23.telkom.co.za","eis31.telkom.co.za","eis32.telkom.co.za","email1.telkom.co.za","email2.telkom.co.za","enterprise.telkom.co.za","enterpriseregistration.telkom.co.za","esourcing.telkom.co.za","explore.telkom.co.za","expressway.telkom.co.za","fiori.telkom.co.za","www.fiori.telkom.co.za","fioridev.telkom.co.za","www.fioridev.telkom.co.za","fioriqa.telkom.co.za","www.fioriqa.telkom.co.za","frontapi.telkom.co.za","www.frontapi.telkom.co.za","ftp.telkom.co.za","futurebusiness.telkom.co.za","futurenow.telkom.co.za","gateway.telkom.co.za","gblvusu0003.telkom.co.za","gethelp.telkom.co.za","www.gethelp.telkom.co.za","gis.telkom.co.za","www.hbt.telkom.co.za","ssl-1.hbt.telkom.co.za","www.ssl-1.hbt.telkom.co.za","ssl-2.hbt.telkom.co.za","www.ssl-2.hbt.telkom.co.za","ibm-ssp-dr.telkom.co.za","www.ibm-ssp-dr.telkom.co.za","ibm-ssp-prod.telkom.co.za","www.ibm-ssp-prod.telkom.co.za","ipaccman.telkom.co.za","itdc-ise-psn-02.telkom.co.za","www.itdc-ise-psn-02.telkom.co.za","itdc-ise-psn-04.telkom.co.za","www.itdc-ise-psn-04.telkom.co.za","itslm.telkom.co.za","itsmdev.telkom.co.za","www.itsmdev.telkom.co.za","jag.telkom.co.za","jhbgra22-hesm1.telkom.co.za","jobs.telkom.co.za","www.jobs.telkom.co.za","lit.telkom.co.za","www.lit.telkom.co.za","eds.lit.telkom.co.za","vsc.lit.telkom.co.za","localhost.telkom.co.za","login.telkom.co.za","m.telkom.co.za","media.telkom.co.za","microapi.telkom.co.za","www.microapi.telkom.co.za","msas.telkom.co.za","msp.telkom.co.za","www.msp.telkom.co.za","my.telkom.co.za","myapps.telkom.co.za","www.myapps.telkom.co.za","mydevices.telkom.co.za","nbrl-eai-papp1.telkom.co.za","www.nbrl-eai-papp1.telkom.co.za","nbrl-eai-tapp3.telkom.co.za","www.nbrl-eai-tapp3.telkom.co.za","nbrl-eam-papp1.telkom.co.za","www.nbrl-eam-papp1.telkom.co.za","nbrl-eam-papp2.telkom.co.za","www.nbrl-eam-papp2.telkom.co.za","nbrl-eam-tapp1.telkom.co.za","www.nbrl-eam-tapp1.telkom.co.za","nbrl-eam-tapp2.telkom.co.za","www.nbrl-eam-tapp2.telkom.co.za","nbsc-ise-psn-01.telkom.co.za","www.nbsc-ise-psn-01.telkom.co.za","nbsc-ise-psn-03.telkom.co.za","www.nbsc-ise-psn-03.telkom.co.za","nfs.telkom.co.za","ns1.telkom.co.za","ns2.telkom.co.za","ns3.telkom.co.za","nwdr01-hesm1.telkom.co.za","o365mail.telkom.co.za","o365mailcntr.telkom.co.za","o365mailtygr.telkom.co.za","onnet.telkom.co.za","onnetsecure.telkom.co.za","oo.telkom.co.za","www.oo.telkom.co.za","ooa.telkom.co.za","oob.telkom.co.za","oor.telkom.co.za","openserveqa.telkom.co.za","apps.openshift.telkom.co.za","ota.telkom.co.za","partner.telkom.co.za","payment.telkom.co.za","www.payment.telkom.co.za","pilotmyapps.telkom.co.za","pilotmyoffice.telkom.co.za","pilotpay.telkom.co.za","pilotwifi.telkom.co.za","pledge.telkom.co.za","poc1.telkom.co.za","poc2.telkom.co.za","qit-vwyklm.telkom.co.za","qtts-ws-0001.telkom.co.za","residential.telkom.co.za","rica.telkom.co.za","www.rica.telkom.co.za","salesfulfillment.telkom.co.za","www.salesfulfillment.telkom.co.za","salesfulfillmentpp.telkom.co.za","www.salesfulfillmentpp.telkom.co.za","sapportal.telkom.co.za","www.sapportal.telkom.co.za","sapportaldev.telkom.co.za","www.sapportaldev.telkom.co.za","sapportalqa.telkom.co.za","www.sapportalqa.telkom.co.za","sbg.telkom.co.za","secure.telkom.co.za","secure1.telkom.co.za","secureapp.telkom.co.za","securej.telkom.co.za","securereport.telkom.co.za","selfservice.telkom.co.za","serve.telkom.co.za","www.serve.telkom.co.za","sgis.telkom.co.za","sim.telkom.co.za","sip.telkom.co.za","smb.telkom.co.za","www.smb.telkom.co.za","smbapiportal.telkom.co.za","www.smbapiportal.telkom.co.za","smbmashery.telkom.co.za","www.smbmashery.telkom.co.za","smbpp.telkom.co.za","www.smbpp.telkom.co.za","smbppmashery.telkom.co.za","www.smbppmashery.telkom.co.za","smbuat.telkom.co.za","www.smbuat.telkom.co.za","smbuatapiportal.telkom.co.za","www.smbuatapiportal.telkom.co.za","smbuatmashery.telkom.co.za","www.smbuatmashery.telkom.co.za","smme.telkom.co.za","smtp.telkom.co.za","sponsors.telkom.co.za","srm.telkom.co.za","srmportal.telkom.co.za","sso.telkom.co.za","www.sso.telkom.co.za","ssodev.telkom.co.za","www.ssodev.telkom.co.za","ssoqa.telkom.co.za","www.ssoqa.telkom.co.za","ssp.telkom.co.za","www.ssp.telkom.co.za","static.telkom.co.za","store.telkom.co.za","www.store.telkom.co.za","sts.telkom.co.za","www.sts.telkom.co.za","bsd.sup.telkom.co.za","www.bsd.sup.telkom.co.za","tcen-itx-epapp.telkom.co.za","tcen-itx-epinv.telkom.co.za","tcen-ngw-0001.telkom.co.za","tcen-ngw-0003.telkom.co.za","tcen-ul-0102.telkom.co.za","tcen-ul-0104.telkom.co.za","tcen-vcs-exp.telkom.co.za","tcen-vcs-exp-0000.telkom.co.za","tcen-vcs-exp-0001.telkom.co.za","tcen-ws-easy1a.telkom.co.za","tcen-ws-easy2.telkom.co.za","tcenh058.telkom.co.za","tcenh193.telkom.co.za","tcenxsheb06.telkom.co.za","telkom947cyclechallenge.telkom.co.za","www.telkom947cyclechallenge.telkom.co.za","telkomapps.telkom.co.za","telkomidols.telkom.co.za","www.telkomidols.telkom.co.za","telkomvpn.telkom.co.za","www.telkomvpn.telkom.co.za","testapi.telkom.co.za","www.testapi.telkom.co.za","vpn.telkom.co.za","www.vpn.telkom.co.za","wblv-exp-e-1.telkom.co.za","wblv-ise-psn-01.telkom.co.za","www.wblv-ise-psn-01.telkom.co.za","wblv-ise-psn-02.telkom.co.za","www.wblv-ise-psn-02.telkom.co.za","webmail.telkom.co.za","www.webmail.telkom.co.za","wfm.telkom.co.za","wfm1.telkom.co.za","wifi.telkom.co.za","wifiredirect.telkom.co.za","wms.telkom.co.za","www2.telkom.co.za",""]

for host in hosts:
    try:
        r = requests.get("https://"+ host)
        print("_______________________________________________________________________________________________________________________")
        print("XXXX " + host + "XXX")
        print(r.status_code)
    except:
        pass


