
from pyscipopt import Model, Heur, SCIP_RESULT, SCIP_PARAMSETTING, SCIP_HEURTIMING, SCIP_LPSOLSTAT

class MyRoundingHeur(Heur):







    def heurexec(self, heurtiming, nodeinfeasible):
        
        # if(self.model.getLPSolstat() != SCIP_LPSOLSTAT.OPTIMAL):
        #     return {"result": SCIP_RESULT.DIDNOTRUN}
        
        # if ( self.model.isGE(self.model.getLPObjVal(), self.model.getCutoffbound()) ):
        #     return {"result":SCIP_RESULT.DIDNOTRUN}

        lpcands, lpcandssol, lpcadsfrac, nlpcands, npriolpcands, nfracimplvars = self.model.getLPBranchCands()

        nfrac = nlpcands

        # if (nfrac == 0):
        #     return {"result":SCIP_RESULT.DIDNOTRUN}


        lprows = self.model.getLPRowsData()
        nlprows = len(lprows)



        # nviolrows = 0
        # activities = [0 for i in range(nlprows)]
        # violrowpos = [-2 for i in range(nlprows)]
        # violrows = []
        # for r in range(nlprows):

        #     row = lprows[r]
        #     assert row.getLPPos() == r, "row number doesn't match"

        #     if(not row.isLocal()):
        #         activities[r] = self.model.getRowActivity(row)
        #         if( self.model.isFeasLT(activities[r], row.getLhs()) or self.model.isFeasGT(activities[r], row.getRhs())):
        #             violrows.append(row)
        #             violrowpos[r] = nviolrows
        #             nviolrows = nviolrows + 1
        #         else:
        #             violrowpos[r] = -1
            
        #     sol = self.model.createSol()
        
        sol = self.model.createSol()
        print("sol bf:",sol)
        self.model.linkLPSol(sol)
        print("sol af:",sol)



        print("solstat",self.model.getLPSolstat())
        print("cut:",self.model.getCutoffbound())
        print("nlpcands:",nlpcands)
        print("nlprows:", nlprows)
        print("lt:",self.model.isFeasLT(1.0,2.0))
        print("gt:",self.model.isFeasGT(2.0,1.0))


        return {"result": SCIP_RESULT.DIDNOTRUN}





    def help1(self):
        pass

    def help2(self):
        pass    

if __name__ == "__main__":
    import pyscipopt

    # 创建SCIP实例
    model = Model("Rounding_Heuristic_Example")
    filename = "acc-tight2.mps"
    print(filename)
    abs_filepath = "/home/yyzhou/MIPLIB_data/data/"+filename
    model.readProblem(abs_filepath)
    

    # 设置参数
    model.setPresolve(pyscipopt.SCIP_PARAMSETTING.OFF)  # 关闭预处理
    # model.setHeuristics(pyscipopt.SCIP_PARAMSETTING.OFF)
    # model.setSeparating(pyscipopt.SCIP_PARAMSETTING.OFF)  # 关闭分离算法
    # model.setIntParam('limits/solutions', 1)  # 限制求解器找到的解的数量为1个

    # 引入heuristics
    heuristic = MyRoundingHeur()
    model.includeHeur(heuristic, "PyHeur", "custom heuristic implemented in python", "Y", timingmask=SCIP_HEURTIMING.DURINGLPLOOP)

    # 求解最终解
    model.optimize()

    print(model.getPrimalDualIntegral())