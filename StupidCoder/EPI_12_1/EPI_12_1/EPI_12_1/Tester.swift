//
//  Tester.swift
//  EPI_12_1
//
//  Created by Qingchuan Zhu on 6/15/18.
//  Copyright © 2018 Qingchuan Zhu. All rights reserved.
//

import Foundation

class Tester {
    
    func runTest()  {
        let testingArray:[Int] = [-14, -10, 2, 108, 108, 243, 285, 285, 401]
        let targetKey:Int = 108
        
        let uut:Solution = Solution()
        let result = uut.firstOccurrence(testingArray, key: targetKey)
        
        assert(result == 3, "Failed for finding first occurrence of \(targetKey)")
        
        print("Passed!!\nFound first occurrence of \(targetKey) at index \(result)\n")
    }
}
