func is_palindrome(s: String) -> (Bool) {
	let reversestring = String(s.characters.reverse())
	if (reversestring == s) {
		return(true)
	} else {
		return(false)
	}
}