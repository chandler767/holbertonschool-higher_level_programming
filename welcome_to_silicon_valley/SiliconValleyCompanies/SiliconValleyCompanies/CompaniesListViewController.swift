//
//  CompaniesListViewController.swift
//  SiliconValleyCompanies
//


import UIKit

class CompaniesListViewController: UITableViewController {

    var companiesList: [String] = TechCompaniesHelper.getTechCompanies()
    
    override func viewDidLoad() {
        super.viewDidLoad()
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
    }

    // MARK: - Table view data source

    override func numberOfSectionsInTableView(tableView: UITableView) -> Int {
        return 1
    }

    override func tableView(tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        return self.companiesList.count
    }

    override func tableView(tableView: UITableView, cellForRowAtIndexPath indexPath: NSIndexPath) -> UITableViewCell {
        let cell = tableView.dequeueReusableCellWithIdentifier("CompanyCell", forIndexPath: indexPath)
        cell.textLabel?.text = companiesList[indexPath.row]
        if companiesList[indexPath.row] == "Holberton" {
            cell.detailTextLabel?.text = "I love studying at Holberton" // "I love studying" if the company name is "Holberton" otherwise, "I love working"
        } else {
            cell.detailTextLabel?.text = "I love working at " + companiesList[indexPath.row]
        }
        return cell
    }

   

}
