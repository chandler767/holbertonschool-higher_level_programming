func longest_word(text: String) -> (String) {
        
var word = ""
var longestWord = ""
var length = 0
var max = 0

for character in my_text.characters {
    if character == " " {
        if length > max {
            max = length
            longestWord = word
        }
        word = ""
        length = 0
    } else {
        word += "\(character)"
        length+=1
    }
}

return(longestWord)
}
