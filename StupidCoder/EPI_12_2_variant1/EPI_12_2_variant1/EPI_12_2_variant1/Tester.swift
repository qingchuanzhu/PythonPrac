//
//  Tester.swift
//  EPI_12_2_variant1
//
//  Created by Qingchuan Zhu on 6/15/18.
//  Copyright © 2018 Qingchuan Zhu. All rights reserved.
//

import Foundation

class Tester {
    func runTest()  {
        let testingArray:[Int] = [1, 2, 2, 4, 4, 4, 7, 11, 11, 13]
        let targetKey:Int = 4
        let answer:(Int, Int) = (3,5)
        
        let uut:Solution = Solution()
        let result:(L:Int, U:Int) = uut.intervalEncloseK(testingArray, target: targetKey)
        
        assert(result == answer, "Failed for finding first occurrence of \(targetKey)")
        
        print("Passed!!\nFound interval of target key \(targetKey) between \(result.L) and \(result.U)\n")
    }
}
