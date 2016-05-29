//
//  TechCompaniesHelper.swift
//  SiliconValleyCompanies
//

import Foundation

class TechCompaniesHelper { // Returns a list of companies
    static var companies:[String] = ["Holberton", "Linkedin", "Docker", "Google", "Yahoo", "Apple"]
    static func getTechCompanies() -> [String] {
        return companies
    }
}