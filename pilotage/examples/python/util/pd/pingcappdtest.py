from component_util import *


if __name__ == "__main__":
    # get env 
    init()
    
    # ComponentStart
    ComponentStart()
    
    # prepare task
    cmd = "git clone https://github.com/pingcap/pd.git /root/gopath/src/github.com/pingcap/pd"
    execCommand(cmd)
    
    # TaskStart
    TaskStart()
    
    
    os.chdir("/root/gopath/src/github.com/pingcap/pd")
    cmd = "make dev"
    
    # Task exec
    status = execCommand(cmd)
   
    # reesult status
    TaskResult({"status": status,})
    
    # TaskStatus
    TaskStatus({"status":status,})
    
    #ComponentStop
    ComponentStop()

    # wait
    holdWait()
