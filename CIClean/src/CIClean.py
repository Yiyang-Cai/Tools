import os,sys
import time
import datetime
import shutil

class Env:
    InvCI = "InvCI"
    Automation = "Automation"
    BuildLog = 'BuildLog'
    PDB = 'PDB'
    QDiff = 'QDiff'

class ConfigValue:
    InvCIUrl = "\\\\invci-package.ecs.ads.autodesk.com\\InvCI\\"
    AutomationUrl = "\\\\invci-package.ecs.ads.autodesk.com\\InvCI_Automation_Results\\"
    BuildLogUrl = "\\\\invci-package.ecs.ads.autodesk.com\\InvCI_BuildLog\\Jenkins\\"
    PDBUrl = "\\\\invci-package.ecs.ads.autodesk.com\\InvCI_PDB\\Jenkins\\"
    QDiffUrl = "\\\\invci-package.ecs.ads.autodesk.com\\QDiff\\Jenkins\\"

class Clean:
    
    def __init__(self,env):
        self.env=env
        self.serverHost=""
        self.grade=0
        self.TransferEnv(env)

    def TransferEnv(self,env):
        self.env=env
        if(env==Env.InvCI):
            self.serverHost=ConfigValue.InvCIUrl
            self.grade=2
        elif(env==Env.Automation):
            self.serverHost=ConfigValue.AutomationUrl
            self.grade=1
        elif(env==Env.BuildLog):
            self.serverHost=ConfigValue.BuildLogUrl
            self.grade=1
        elif(env==Env.PDB):
            self.serverHost=ConfigValue.PDBUrl
            self.grade=1
        elif(env==Env.QDiff):
            self.serverHost=ConfigValue.QDiffUrl
            self.grade=1
            
    def CleanCI(self):
        if (self.grade == 1):
            f = list(os.listdir(self.serverHost))
            for i in range(len(f)):
                filedate = os.path.getmtime(self.serverHost+f[i])
                time1 = datetime.datetime.fromtimestamp(filedate).strftime('%Y-%m-%d')
                date1 = time.time()
                num1 =(date1 - filedate)/60/60/24
                if num1 >= 30:
                    try:
                        if os.path.isdir(self.serverHost + f[i]):
                            print("%s : %s : %s"%(self.env, f[i], time1)+" cleaning...")
                            shutil.rmtree(self.serverHost + f[i])
                            print("done")
                        else:
                            print("%s : %s : %s"%(self.env, f[i], time1)+" cleaning...")
                            os.remove(self.serverHost + f[i])
                            print("done")
                    except Exception as e:
                        print(e)

        elif (self.grade == 2):
            g = list(os.listdir(self.serverHost))
            Excludelist = ['CC_Packages_x64',]
            g = [item for item in g if item not in Excludelist]
            for j in range(len(g)):
                if os.path.isdir(self.serverHost+g[j]):
                    f = list(os.listdir(self.serverHost+g[j]))
                    for i in range(len(f)):
                        filedate = os.path.getmtime(self.serverHost+g[j]+'\\'+f[i])
                        time1 = datetime.datetime.fromtimestamp(filedate).strftime('%Y-%m-%d')
                        date1 = time.time()
                        num1 =(date1 - filedate)/60/60/24
                        if num1 >= 30:
                            try:
                                if os.path.isdir(self.serverHost+g[j]+'\\'+f[i]):
                                    print("%s : %s/%s : %s"%(self.env, g[j], f[i], time1)+" cleaning...")
                                    shutil.rmtree(self.serverHost + f[i])
                                    print("done")
                                else:
                                    print("%s : %s/%s : %s"%(self.env, g[j], f[i], time1)+" cleaning...")
                                    os.remove(self.serverHost + f[i])
                                    print("done")
                            except Exception as e:
                                print(e)

if __name__ == "__main__":
    url = ['InvCI','Automation','BuildLog','PDB','QDiff']
    try:
        if(sys.argv[1]=='All'):
            for i in range(len(url)):
                cleaner = Clean(url[i])
                cleaner.CleanCI()
            print('clean end')
        elif(sys.argv[1] in url):
            cleaner=Clean(sys.argv[1])
            cleaner.CleanCI()
            print('clean end')
        else:
            print('error input')
    except Exception as error:
        print(error)
