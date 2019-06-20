import zipfile
print """


                 mdddm        mdhys
                   hsssyh  mddhssss                  ddm              dm
                  hssssymmmm  hsssh                  hyyhm           myyhm
                 dssssh      msssym                 hyyyyd          mhyyyh
               mysssd      myssym                 dyyyym           hyyyd
               ysssd      myssym myyhdm    mdh   myyyhm   mmdh    hyyym   mmmdm mddmm
 m            msssm      dssyh  mysyhmmm  dyyd  myyyh  mmddyyy   dyyhm  mmmhyydmhhhdmmm    dhhdm
   dddddmmm  myssd     myssydd myssh     mysym  hyyhm     dyyd  myyyd     myyhdhyhm       hhhhd
    mddhyyyyyyssyddddhysssssss hssy      hsyd  dyyyh     myyhm mhyyhm     hyydhyhd      mhhhhm
         mmmdssyhhhhhhhdddysshmysym     hysh  myyyym    myyym  hyyyd     dyyddyyd      mhhhhm
            mssm         hssymdssd    mhssh   hyyyh    dyyyd  dyyhh    mhyyh dyh     mdhhhhm
            msy         dssym dsym   mysyh   dyydym   dyyyd   yydhd   mhyyh  hyh    dhdhhhd
            msh       mhssyd  msym  dysyd    yyddy   hyyhm   dyh ym  mhyhd   dyh   dhmdhhh    m
         m   yh      mhssym    hshdhyyd     msy dymdhyhm     hym hdmhyhd     mhhmmdd dhhh mmdm
        dm   md     dyssy       dhhdm       mym  dhhdm       hh  mdhdm        mdddm mhhhddmm
       mh         mhssyd                     d               d                    mm dhhh
       hd        dysshm                                                        mddm mhhhd
      msm      mysshm                                                       mdhhd  mhhhd
      msm    mhsshm                                                        dhhhhdddhhdm
       dhhhdm                                                               mmmmmmmmm



  mmmmmmmmmm                                ddddd                                      ms+m         
 y++++++++++dmy++s                       do+++++++d                                    +++h         
hhddddddy+s  ds+sd                      som    s+sm                                    o++h         
       doy     mm          m           so             mm  mdm     mddmm          mm    o++d  mmm    
  mhhhhoh     hsoh  myoodhooosh       hoo           hsoohsoooh hssddhoosh     hyoooosm oooyhyooos   
 mdmhosyyyd   yooh  hooodmdyoooh      soom          dooohmdym yssh   hooo   hsh  dssh  oooh  dosy   
   dsy        yssd  msss    yssy      ysss          msss       dyyyyyssss  yssd        ssshmhssd    
  hsh         yssd  msssm   msy       msssyd        msss      hsm    hsss  sssym       sssh dsssh   
 hyyyyyyyyyym hyyy  yyyyyhmmhd         myyyyyhdddhd myyyh    hyyyhmmmyyyyh myyyyyddddm yyyh  myyyymm
dhhhhhhyyyhm  dyhm  myyydddm             mdhyyyhd    hyd      mhyyyhd hyhm   dhyyyhm   dyhd    hyhm 
                    dyyy                                                                            
                     hhhdm                                                                          
                     mdd                 


  
----------------------------------------------------------------------------------
----------------------------------------------------------------------------------

      
                                    
 """
def extract(zFile,passwd):
    try:
        zFile.extractall(pwd=passwd)
        print "[+]Password is %s"%passwd
        return
    except:
        print "[-]Password %s is not correct"%passwd


file=str(raw_input("[*]Enter the zip file path: "))
zfile=zipfile.ZipFile(file)
dictionary=str(raw_input("[*]Enter the dictionary: "))
passFile = open(dictionary)
for line in passFile.readlines():
    passwd = line.strip('\n')
    extract(zfile,passwd)
