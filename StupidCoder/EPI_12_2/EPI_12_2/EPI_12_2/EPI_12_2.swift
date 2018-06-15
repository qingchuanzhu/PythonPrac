//
//  EPI_12_2.swift
//  EPI_12_2
//
//  Created by Qingchuan Zhu on 6/15/18.
//  Copyright © 2018 Qingchuan Zhu. All rights reserved.
//

import Foundation

class Solution {
    func firstEleGT(_ array:[Int], target:Int) -> Int {
        var index:Int = -1
        
        var low = 0
        var high = array.count - 1
        
        while low <= high {
            let mid = low + (high - low) / 2
            if array[mid] > target {
                high = mid - 1
                index = mid
            } else {
                low = mid + 1
            }
        }
        return index
    }
}
