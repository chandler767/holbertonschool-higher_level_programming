//
//  ViewController.swift
//  TapperProject
//
//  Copyright © 2016 Chandler Mayo. All rights reserved.
//

import UIKit

class ViewController: UIViewController {

   
    @IBOutlet weak var image_tapper: UIImageView!
    @IBOutlet weak var button_play: UIButton!
    @IBOutlet weak var textfield_number: UITextField!
    @IBOutlet weak var button_coin: UIButton!
    @IBOutlet weak var label_taps: UILabel!
    
    var taps_requested:Int = 0
    var taps_done :Int =  0

    
    func initGame(){ // The init view
        label_taps.hidden = false
        button_coin.hidden = false
        taps_done =  0
        label_taps.text = "0 Taps"
        image_tapper.hidden = true
        button_play.hidden = true
        textfield_number.hidden = true
    }
    
    
    func resetGame(){ // Game view
        label_taps.hidden = true
        button_coin.hidden = true
        taps_requested = 0
        textfield_number.text = ""
        image_tapper.hidden = false
        button_play.hidden = false
        textfield_number.hidden = false
    }
    
    @IBAction func clickPlayButton(sender: UIButton) { // called when the button button_play is touch up inside
    
        let num = Int(textfield_number?.text ?? "")
        
        if num != nil {
            if num >= 0 {
            print("Let's do "+String(num)+" taps")
                taps_requested = num!
                initGame() // Starts game with entered number of taps
            }
        }
        
    }
 
    @IBAction func clickCoinButton(sender: UIButton) { //  called when the button coin is touch up inside
    
       if taps_done >= taps_requested{
             resetGame() // Resets the game
        }
        taps_done += 1
        label_taps.text = String(taps_done)+" taps" // Otherwise updates the count ot taps
        print("Tap!")

    }
    override func viewDidLoad() {
        super.viewDidLoad()
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
    }
 }

