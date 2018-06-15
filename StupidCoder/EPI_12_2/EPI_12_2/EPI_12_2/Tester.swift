//
//  Tester.swift
//  EPI_12_2
//
//  Created by Qingchuan Zhu on 6/15/18.
//  Copyright © 2018 Qingchuan Zhu. All rights reserved.
//

import Foundation

class Tester {
    func runTest()  {
        let testingArray:[Int] = [-14, -10, 2, 108, 108, 243, 285, 285, 285, 401]
        let targetKey:Int = 285 // -13
        let answer:Int = 9 // 1
        
        let uut:Solution = Solution()
        let result = uut.firstEleGT(testingArray, target: targetKey)
        
        assert(result == answer, "Failed for finding first occurrence of \(targetKey)")
        
        print("Passed!!\nFound first occurrence greater than \(targetKey) at index \(result)\n")
    }
}
